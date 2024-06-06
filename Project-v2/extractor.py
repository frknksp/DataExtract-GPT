import json
import dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from schema import KaracigerRaporu

#dotenv.load_dotenv()

def extract_text(input_text, api_key):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
            ),
            ("human", input_text),
        ]
    )

    llm = ChatOpenAI(api_key=api_key, temperature=0, model="gpt-3.5-turbo")

    runnable = prompt | llm.with_structured_output(schema=KaracigerRaporu)

    extracted_output = runnable.invoke({"text": input_text})

    extracted_output_dict = extracted_output.dict()
    extracted_output_json = json.dumps(extracted_output_dict, ensure_ascii=False)
    return extracted_output_json
