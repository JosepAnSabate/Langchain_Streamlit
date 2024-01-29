from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv


load_dotenv()

def generate_name(company_type, feelings):
    llm = OpenAI(temperature=0.7, model='gpt-3.5-turbo-instruct')

    prompt_template = PromptTemplate(
        input_variables=["company_type", 'feelings'],
        template = "My company is a {company_type}\
                and I want you to convey these ideas or emotions:\
                {feelings}. Suggest me 5 names for this company."
    )

    name_chain = LLMChain(llm=llm, 
                          prompt=prompt_template,
                          output_key="company_name" )

    response = name_chain({
        'company_type': company_type,
        'feelings': feelings
        })

    return response

if __name__ == '__main__':
    print(generate_name("wine cellar", 'happiness, joy, love'))