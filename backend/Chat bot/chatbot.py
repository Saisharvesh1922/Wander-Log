import os
from dotenv import load_dotenv
load_dotenv()

os.environ["TOKENIZERS_PARALLELISM"] = "false"

from langchain.memory import ConversationBufferMemory
from langchain_core.documents import Document
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq


def create_user_chatbot(user_stories):

    if not user_stories:
        raise ValueError("user_stories is empty")

    documents = [
        Document(page_content=story.get("story", ""))
        for story in user_stories
        if story.get("story")
    ]

    if not documents:
        raise ValueError("No valid story content found")

    print("Documents:", len(documents))

    #Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(documents)

    print("Chunks:", len(docs))

    #Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    #Vector DB
    vectorstore = FAISS.from_documents(docs, embeddings)

    #Memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    #LLM (Groq)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    #Chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        return_source_documents=False,
        verbose=True
    )

    return qa_chain