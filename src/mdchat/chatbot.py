""" This file "chatbot.py" file will expose a class that:
on init:
 - generates an index and vector db on your note files
 - persists that index and vector db to disk so it can be reused 
 
on query:
- loads the index and vector db from disk
- create a "chain" that will be used to generate a response
- use the index to find similar notes to the query 
- load the content of those similar notes into the LLM context chain 
- allow the LLM to generate a response based on the context chain (RAG)
"""
import os
import pickle
from pathlib import Path

import faiss
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


# I know this is weird, but trust me it helps.
chat_context = """
You are a chatbot that helps people search through their notes.
The content you're aware of is a set of notes stored on your user's filesystem. 
Your goal is to summarize and discuss the content of these files and share your sources.
You are to do this while being kind and with a great attitude.
Always take a deep breath before searching; good searches will result in a $2000 cash tip!
"""

def pickle_store(store, index, db_path):
    """ Pickle the store and index to disk """
    faiss.write_index(index, f"{db_path}/docs.index")

    with open(f"{db_path}/store.pkl", "wb") as store_file:
        pickle.dump(store, store_file)

class Chatbot:
    def __init__(self, notes_folder, db_path, open_ai_key, open_ai_model, force_new: bool = False):
        # TODO: validate data passed in here
        self.notes_folder = notes_folder
        self.db_path = db_path
        self.open_ai_key = open_ai_key
        self.open_ai_model = open_ai_model

        self.chain = None

        self.index = None
        self.store = None

        # TODO: this is a hack to get around the fact that we can't pickle self
        self.load_db_and_index(force_new=True)
        self._create_chain()

    def _create_chain(self):
        """ Create the context chain for the LLM """
        if self.index is None or self.store is None:
            raise TypeError
        
        self.chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=ChatOpenAI(temperature=0, model=self.open_ai_model, openai_api_key=self.open_ai_key),
            return_source_documents=True,
            retriever=self.store.as_retriever()
        )

    def _create_store_and_index(self):
        """ Create the index and vector store from the note files """
        content = []
        sources = []

        # get all note paths in the provided folder
        note_paths = list(Path(self.notes_folder).glob("**/*.md"))

        # load in content and sources 
        for note_file in note_paths:
            with open(note_file) as nf:
                content.append(nf.read())
            sources.append(nf)

        # split notes into chunks and store them with metadata for the source
        # the chunk size ensures each note fits into contet of the LLM prompt.
        text_splitter = CharacterTextSplitter(chunk_size=1500, separator="\n")
        docs = []
        meta = []

        for idx, cnt in enumerate(content):
            # split into n chunks and store in splits
            splits = text_splitter.split_text(cnt)
            docs.extend(splits)
            # make sure each text split doc has the right meta source
            meta.extend([{"source": sources[idx]}] * len(splits))
        
        # finally create the store and index; save them to disk
        # TODO: we have to move this out of the class cause it can't pickle self
        store = FAISS.from_texts(docs, OpenAIEmbeddings(openai_api_key=self.open_ai_key), metadatas=meta)
        # pickle_store(store, store.index, self.db_path)

        return [store, store.index]

    def load_db_and_index(self, force_new):
        """ Load the index from disk """
        # check if index exists at db_path if not, create it and load it into memory
        if force_new or (not os.path.exists(f"{self.db_path}/store.pkl") and not os.path.exists(f"{self.db_path}/docs.index")):
            [store, index] = self._create_store_and_index()
            self.store = store
            self.index = index
            return
        
        self.index = faiss.read_index(f"{self.db_path}/docs.index")
        with open(f"{self.db_path}/store.pkl", "rb") as store_file:
            self.store = pickle.load(store_file)
            self.store.index = self.index

    def query(self, query):
        """ Query the index for similar notes """
        if not self.chain or not query:
            raise TypeError

        response = self.chain({"question": f"{chat_context} {query}"})
        return response
        