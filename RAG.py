# from langchain_groq import Groq
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.messages import HumanMessage, AIMessage
# from langchain_core.output_parsers import StrOutputParser
# from PyPDF2 import PdfReader
# from langchain_openai import OpenAIEmbeddings
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import Chroma
# from langchain.chains.combine_documents.stuff import StuffDocumentsChain
# from langchain.chains.llm import LLMChain
# from langchain_core.prompts import PromptTemplate

# # Step 1: Load the PDF
# loader = PyPDFLoader("Credit-Card-Policy.pdf")
# documents = loader.load()

# # Step 2: Split into chunks
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(documents)

# # Step 3: Create embeddings and store in a vectorstore
# embeddings = OpenAIEmbeddings()
# db = Chroma.from_documents(texts, embeddings)

# # Step 4: Initialize the LLM (Groq Llama 3) - Do this *once* at module level
# llm = Groq(model_name="llama-3.3-70b-versatile")  # Or the correct model name

# template = """Use the following pieces of context to answer the question at the end.
# If you don't know the answer, just say that you don't know, don't try to make up an answer.

# {context}

# Question: {question}
# Helpful Answer:"""
# QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# def load_chain(llm, prompt = QA_CHAIN_PROMPT):
#     llm_chain = LLMChain(llm=llm, prompt=prompt)
#     combine_documents_chain = StuffDocumentsChain(
#         llm_chain=llm_chain, document_variable_name="context"
#     )
#     return combine_documents_chain

# def get_rag_response(user_question): # Modified
#     # Step 4: Retrieve relevant documents from the vector store
#     docs = db.similarity_search(user_question) #Basic similarity search

#     chain = load_chain(llm)
#     result = chain.run(input_documents=docs, question=user_question)
#     return result

# if __name__ == "__main__":
#     # Test the RAG pipeline
#     user_question = "What is the interest rate?"
#     rag_response = get_rag_response(user_question)
#     print(f"User Question: {user_question}")
#     print(f"RAG Response: {rag_response}")
