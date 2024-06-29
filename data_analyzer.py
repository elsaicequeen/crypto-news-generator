import os
import requests
from dotenv import load_dotenv
from alchemy import Alchemy
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain import OpenAI

load_dotenv()

alchemy_api_key = os.getenv("ALCHEMY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize Alchemy instance
alchemy_instance = Alchemy(api_key=alchemy_api_key)

def get_blockchain_data():
    # Fetch blockchain data (you can add more API calls here)
    block_number = alchemy_instance.core.get_block_number()
    return block_number

def analyze_blockchain_data():
    block_number = get_blockchain_data()
    analysis_result = f"Current block number is {block_number}"
    return analysis_result

# Example usage of LangChain for more sophisticated analysis
def generate_langchain_analysis(data):
    template = """
    Analyze the following blockchain data:
    {data}

    Provide detailed insights.
    """
    prompt = PromptTemplate(input_variables=["data"], template=template)
    llm = OpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"data": data})

if __name__ == "__main__":
    analysis_result = analyze_blockchain_data()
    detailed_analysis = generate_langchain_analysis(analysis_result)
    print(detailed_analysis)
