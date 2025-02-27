import os
from langchain_openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

sys_prompt = """
Voici des documents pertinents pour la question suivante. Veuillez répondre à la question en utilisant les informations fournies dans les documents.

Documents: {documents}

Question: {query_text}

"""

def query_llm(documents, query_text):
    llm = OpenAI(
        api_key=os.getenv('API_KEY'),
        base_url=os.getenv('BASE_URL'),
        model=os.getenv('MODEL')
    )

    result = llm.invoke(sys_prompt.format(documents=documents['documents'], query_text=query_text))
    return(result)

