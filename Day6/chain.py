import prompt
from model import create_create_groq
def generate_poem(topic):
    '''
    Function to generate a poem

    Args:
        topic(str): The topic of the poem

    Returns:

        response.content(str)
    '''
    prompt_template = prompt.poem_generator_prompt_from_hub()
    llm = create_create_groq()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic":topic})  
    llm = create_create_groq()
    response = llm.invoke(topic)
    return response.content