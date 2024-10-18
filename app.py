from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings,custom_retrieval_qa

from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
# from langchain.llms import CTransformers
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone


from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
INDEX_NAME = os.environ.get('INDEX_NAME')


embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

#Loading the index
vectorstore=PineconeVectorStore.from_existing_index(INDEX_NAME, embeddings)


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

llm_model=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                model_type="llama",
                config={'max_new_tokens':512,
                        'temperature':0.8})



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=custom_retrieval_qa(input,vectorstore,llm_model,PROMPT)
    # result = "hello"
    print("Response : ", result)
    return str(result)


if __name__ == '__main__':
    app.run(debug= True)

