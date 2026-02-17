import fitz 
import os 
from dotenv import load_dotenv

from groq import Groq 


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def extract_text_from_pdf(uploaded_file):
    '''
    Extracts text from pdf file.
    
    :param uploaded_file: Path to the pdf 

    Returns: 
        str: The extracted text.
    '''

    doc = fitz.open(stream=uploaded_file.read(),
                    filetype='pdf')
    
    text = ""

    for page in doc:
        text += page.get_text()

    return text
    
def ask_groq(prompt,max_tokens=1000):
    '''
    Sends a prompt to groq api and returns response 
    :param prompt: The prompt to send Groq API
    :param max_tokens: Description

    Returns:
        str: The response from Groq API
    '''

    client = Groq()
    completion = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[{
            "role":"user",
            "content":prompt
        }],
        temperature=0,
        max_tokens=max_tokens
    )

    return completion.choices[0].message.content

