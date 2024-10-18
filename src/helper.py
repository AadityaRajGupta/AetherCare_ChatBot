from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# Extract data from the PDF
def load_pdf(data):
    loader = DirectoryLoader(data,
                                glob="*.pdf",
                                loader_cls=PyPDFLoader)
    
    documents = loader.load()
    return documents

# Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks


# Using all-MiniLM-L6-v2 model for embedding text.

# download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

# Custom Retrieval QA function that retrieves relevant documents and generates an answer.
def custom_retrieval_qa(query, vectorstore, llm_model,PROMPT, k=3):

    results = vectorstore.similarity_search(query, k=k) 
    context = "\n".join([result.page_content for result in results])
    formatted_prompt = PROMPT.format(context=context, question=query)
    answer = llm_model(formatted_prompt)

    return answer

