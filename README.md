# FAQ Assistant
 Chatbot to answer previously answered queries for your company

This is an end to end LLM project based on Google Gimini API, Langchain, HuggingFace. It is a  Q&A system which will provide a streamlit based user interface for people where they can ask questions and get answers(if their queries are already present in the database). 

![](images/example.png)

## Project Highlights

- Use a real CSV file of FAQs that Codebasics company is using right now. 
- Their human staff will use this file to assist their course learners.
- We will build an LLM based question and answer system that can reduce the workload of their human staff.
- Students should be able to use this system to ask questions directly and get answers within seconds

## Tools Used
  - Langchain + Google Gimini API(free): LLM based Q&A
  - Streamlit: UI
  - Huggingface instructor embeddings: Text embeddings
  - FAISS: Vector databse

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/OmSDeshmukh/FAQ-Assistant
```
2.Navigate to the project directory:

```bash
  cd FAQ-Assistant
```

3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

5. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```

6. Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="the_api_key_here"
```

## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- To create a database of FAQs, click on Create Database button. It will take some time before knowledgebase is created so please wait.

- Once knowledge base is created you will see a directory called faiss_index in your current folder

- Now you are ready to ask questions. Type your question in Question box and hit Enter

## Project Structure

- src/main.py: The main Streamlit application script.
- src/langchain_helper.py: This has all the code related to getting the chain for final inference.
- src/get_vector_db.py: This will take the csv file and load the vector database into disk for faster retrieval.
- src/prompt_template.py: This stores the prompt template give as input to the llm.
- notebooks/main.ipynb: Same code as entire project but at a single place in a notebook for testing purposes.
- data/demo.csv: The csv file used for loading data.
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.

## Aknowledgement

A huge thanks to [Codebasics YouTube Channel](https://www.youtube.com/@codebasics) for this valuable project idea. Here is the [Video link](https://youtu.be/AjQPRomyd-k?si=ZKr1PZuxUExvGRW7)and [Github repository](https://github.com/codebasics/langchain/tree/main/3_project_codebasics_q_and_a)
