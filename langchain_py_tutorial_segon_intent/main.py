from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_company_names():
    llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.7)

    prompt_template_name = PromptTemplate

    name = llm('I want a cool name for a tech company that optimize mining processes using AI. Suggest my five')

    return name

if __name__ == "__main__":
    print(generate_company_names())