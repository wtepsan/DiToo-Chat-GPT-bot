### This program is updated from 
### https://github.com/anoopshrma/Chatgpt-using-GPT-4
### https://pythonwarriors.com/how-to-make-chatgpt-remember-our-previous-conversations/

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import os
import json
import ast
import openai
import uvicorn

app = FastAPI()  

from openai import OpenAI
client = OpenAI(
  api_key= ,
)

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

f = open("./lessons/problemandsolution.txt", "r")  
information = f.read()
# information+ ". Please study the previos information.\
preprompt = [{"role": "system", \
           "content": f"You will be the a chatbot tutor for the course Fundamental Digital Tools for Entreprenuers. am Fun DigiTool.\
            You name is DiToo\
            Your responsibility is to answer questions about the information:"}]

class UserQuery(BaseModel):
    user_input: str
    conversation_id: str

def create_prompt(user_input, conversation_id):

    filename = "/coversations/" + conversation_id + ".txt"

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            file_contents = file.read()
            prompt = ast.literal_eval(file_contents)
    else: 
        prompt = preprompt

    prompt.append({"role":"user", "content":user_input})

    return prompt

def generate_response(user_input, conversation_id):

    prompt = create_prompt(user_input, conversation_id)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #GPT-3.5-turbo
        messages=prompt,
        max_tokens=250
    )

    message = response.choices[0].message.content 

    prompt.append({"role": "system", "content": message})

    filename = "/coversations/" + conversation_id + ".txt"
    with open(filename, 'w') as f: 
        f.write(json.dumps(prompt))

    return message

@app.get("/", response_class=HTMLResponse)
async def chatgpt_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chatgpt/")
async def chatgpt_endpoint(user_query: UserQuery):
    response = generate_response(user_query.user_input, user_query.conversation_id)
    response = response.replace("\n", "<br>")
    print(response)
    return {"response": response}

if __name__ == '__main__':
    uvicorn.run("tutor:app", port=8000, reload=True)
    # print(information)
    # output = chatGPT("Where is Thailand")
    # print(output)

    # user_input = "Where is Thailand?"
    # output = generate_response(user_input)
    # print(output)
    # print("\n\n")

    # for user_input in ["1", "2", "3"]:
    #     prompt = create_prompt(user_input)
    #     print(prompt, "\n\n")
