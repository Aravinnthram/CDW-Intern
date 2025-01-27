import prompt
from model import create_create_groq

def generate_quiz(topic, difficulty):
    '''
    Function to generate a quiz

    Args:
        topic (str): The topic for the quiz
        difficulty (str): The difficulty level (Easy, Medium, Hard)

    Returns:
        response.content (str): The generated quiz
    '''
    prompt_template = prompt.quiz_generator_prompt()
    llm = create_create_groq()

    chain = prompt_template | llm

    response = chain.invoke({
        "topic": topic,
        "difficulty": difficulty
    })

    return response.content
