from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()

def generate_company_names(company_type, values):
    llm = OpenAI(
        model='gpt-3.5-turbo-instruct', 
        temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables = ['company_type', 'values'],
        template = """I want a cool name for a company that 
                    works with {company_type}, and represent our values: 
                    {values}.
                    Suggest my five"""
    ) 
    
    name_chain = LLMChain(
        llm=llm, 
        prompt=prompt_template_name,
        output_key='company_name' # output key
        )
    
    response = name_chain({'company_type':company_type, 'values':values})

    return response


# test of agent, run with command line: python langchain_helper.py
# agents are used to run multiple chains in parallel, in this case
# we are useing wikipedia and llm-math tools 
def langchain_agent():
    llm = OpenAI(
        model='gpt-3.5-turbo-instruct', 
        temperature=0.5)
    
    tools = load_tools(['wikipedia', 
                        'llm-math'], llm=llm)
    
    agent = initialize_agent(
        tools, 
        llm,
        # agent type, in this case we are using a zero shot agent
        # that can be used to run multiple chains in parallel
        # with different prompts
        agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

    result = agent.run(
        """Tell me the median numbers of years between all the
        declarations of independence of Catalunya."""
    )

    print(result)
        

if __name__ == "__main__":
    #print(generate_company_names('AI', 'transparency, ethics, privacy'))
    print(langchain_agent())

