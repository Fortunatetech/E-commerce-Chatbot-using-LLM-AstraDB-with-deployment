from langchain_astradb import AstraDBVectorStore
#from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
from src.data_preprocessing import data_preprocessing

load_dotenv()

#OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = "AIzaSyDi6pgyhOai6zPHFuDoklgem9DiW7CEhFQ"
ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def data_ingestion(status):
    vstore = AstraDBVectorStore(
            embedding=embedding,
            collection_name="EcommerceChatBot",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
    
    storage=status
    
    if storage==None:
        docs=data_preprocessing()
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, inserted_ids
           

   