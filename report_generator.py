import os
from dotenv import load_dotenv
import openai
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
openai.api_key = openai_api_key

def generate_report(prompt):
    llm = OpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run()

if __name__ == "__main__":
    prompt = """
    Generate a detailed report based on the following blockchain analysis:
    {analysis}

    Provide insights and future predictions.
    """
    analysis_result = "Sample blockchain analysis data."  # Replace with real data
    report = generate_report(prompt.format(analysis=analysis_result))
    print(report)
