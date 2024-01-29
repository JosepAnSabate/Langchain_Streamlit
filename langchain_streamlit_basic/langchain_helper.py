from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7, model='gpt-3.5-turbo-instruct')

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template = "Suggest me five cool names for my {animal_type}, it is {pet_color} in color."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, 
                          output_key='pet_name')

    response = name_chain({'animal_type': animal_type, 'pet_color':pet_color})

    return response

def lanching_agent():
    llm = OpenAI(temperature=0.7)

    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose= True
    )

    result = agent.run('What is the average age of a dog? Multiply the average age by 3.')
    print(result)

if __name__ == "__main__":
    #print(generate_pet_name('cat'))
    lanching_agent()