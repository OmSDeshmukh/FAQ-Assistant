import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from prompt_template import prompt_template
from get_vector_db import get_vector__db
load_dotenv()


def get_chain(db_path):
    # loading the llm model
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ['GOOGLE_API_KEY'],temperature = 0.1)
    
    # using the intructor emebeddings to convert the data in the csv file into vector embeddings
    instructor_embeddings = HuggingFaceInstructEmbeddings(
    query_instruction="Represent the query for retrieval: ")
    
    # #  Loading a vector database to store the embeddings
    # vectordb = FAISS.from_documents(documents=data,
    #                              embedding=instructor_embeddings)
    
    # loading the vector database into the memory
    vectordb = FAISS.load_local(db_path,instructor_embeddings)
    
    # setting up a retriever to retrieve from the vector database
    retriever = vectordb.as_retriever(score_threshold = 0.7)
    
    # creating a prompt template using an existing prompt structure
    # so that the llm answers according to the context(which is the database here)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain_type_kwargs = {"prompt": prompt}
    
    # Loading the final pipeline(chain) for complete process which includes
    # converting the input query to vector
    # then loading similar queries from the database
    # then quering the llm to answer based on the loaded similar queries
    chain = RetrievalQA.from_chain_type(llm=llm,
                            chain_type="stuff",
                            retriever=retriever,
                            input_key="query",
                            return_source_documents=True,
                            chain_type_kwargs=chain_type_kwargs)
    
    return chain