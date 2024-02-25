from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import os
from langchain_community.embeddings import HuggingFaceInstructEmbeddings


# loads the csv file into the vector database
# and stores it locally in a folder so that we don't have to use it again and again
def get_vector__db(csv_file_path):
    # loading the CSV file
    loader = CSVLoader(csv_file_path,source_column = 'prompt')
    data = loader.load()
    
    instructor_embeddings = HuggingFaceInstructEmbeddings(
    query_instruction="Represent the query for retrieval: ")
    
    #  Loading a vector database to store the embeddings
    vectordb = FAISS.from_documents(documents=data,
                                 embedding=instructor_embeddings)
    
    # Saving it locally so that we don't have to load it again and again
    db_path = os.path.split(csv_file_path)[0]+'/vector_db'
    vectordb.save_local(db_path)
    return db_path