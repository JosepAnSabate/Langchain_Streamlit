from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv


load_dotenv()

def generate_law_res(country, text):
    llm = OpenAI(temperature=0.7, model='gpt-3.5-turbo-instruct')

    prompt_template = PromptTemplate(
        input_variables=["country", "text"],
        template = "Respond as a lawyer from {country} to the following question: {text}?"
    )

    res_chain = LLMChain(llm=llm, 
                          prompt=prompt_template)#,
                          #output_key="company_name" )

    response = res_chain({
        'country': country,
        'text': text
        })
    return response

# for executing this file for testing purposes
if __name__ == '__main__':
    print(generate_law_res("Spain", "Is legal to steal?"))