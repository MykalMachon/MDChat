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
from notechat import config

class Chatbot:
    def __init__(self):
        self.index = None
        self.vector_db = None
        self.chain = None

        self.load_index()
        self.load_vector_db()

    def _create_index_and_vector_db(self):
        """ Create the index from the note files """
        pass

    def load_index(self):
        """ Load the index from disk """
        pass

    def load_vector_db(self):
        """ Load the vector db from disk """
        pass

    def query(self, query):
        """ Query the index for similar notes """