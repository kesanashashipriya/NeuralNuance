# from langchain_groq import Groq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# llm = Groq(model_name="llama-3.3-70b-versatile") # Or the correct Llama 3 model name if different
# prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
# chain.invoke({"topic": "ice cream"})
