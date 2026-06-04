from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5"
)

PERSIST_DIR = r"C:\Users\boddu\Innomatics\Batch no-435\Deep Learning(Neural Networks)\LLM'S\IPL_Vector_Store_DB"

vector_store = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embedding_model
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":10}
)

template="""
You are an elite IPL cricket analyst and statistics expert.

Answer ONLY from the provided context.

RULES:
- Never hallucinate information.
- Use only context data.
- Give detailed and engaging cricket explanations and use full player names.
- Mention runs, strike rate, fours and sixes if available.
- Mention total runs/wickets clearly.
- Format rankings in clean bullet points.
- If rankings are available, show all rankings from context and mention rankings properly..
- If only one winner exists, explain their dominance in that season.
- Keep response professional like Cricbuzz or ESPN Cricinfo analysis.
- If answer is unavailable in context, say:
  "Information not available in context."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["context","question"],
    template=template
)

generator = ChatGroq(
    model= 'openai/gpt-oss-120b',
    temperature=0,
    api_key=api_key
)

rag = RetrievalQA.from_chain_type(
    llm=generator,
    retriever=retriever,
    chain_type_kwargs={"prompt":prompt},
    return_source_documents=True
)
