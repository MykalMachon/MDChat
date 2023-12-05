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

class Chatbot:
    def __init__(self, notes_folder, db_path, open_ai_key, open_ai_model):
        self.notes_folder = notes_folder
        self.db_path = db_path
        self.open_ai_key = open_ai_key
        self.open_ai_model = open_ai_model

        self.chain = None
        self.index = None

        self.load_index()
        self.load_vector_db()

    def _create_chain(self):
        """ Create the context chain for the LLM """
        pass

    def _create_index(self):
        """ Create the index from the note files """
        pass

    def load_index(self):
        """ Load the index from disk """
        # check if index exists at db_path
        # if not, create it
        if os.path.exists(f"{self.db_path}/index.pkl"):
            # Load index 
            print("TODO: load index")
        else: 
            # Create index
            self._create_()

    def query(self, query):
        """ Query the index for similar notes """