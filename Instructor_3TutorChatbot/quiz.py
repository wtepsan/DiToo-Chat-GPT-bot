### This program is updated from 
### https://github.com/anoopshrma/Chatgpt-using-GPT-4
### https://pythonwarriors.com/how-to-make-chatgpt-remember-our-previous-conversations/

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from datetime import datetime

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

q = open("./lessons/problemandsolution_questions.txt", "r")  
questions = q.read()

c = open("./lessons/problemandsolution.txt", "r") 
contents = c.read()

#print(contents)

genquestion = [{"role": "user",
                "content": f"random one question from the list of questions: {questions}."}]

def generate_question():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #GPT-3.5-turbo
        messages=genquestion,
        max_tokens=250
    )
    question = response.choices[0].message.content 
    return  question

def answer_feedback(question, answer):
    prompt = [{'role':'user', 
               'content': f"Study the following content:{contents}. Base on what you study, if I answer {answer} to the question {question}. How much score out of 10 I will get and why?"}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #GPT-3.5-turbo
        messages=prompt,
        max_tokens=250
    )

    feedback = response.choices[0].message.content 
    return feedback


def generate_response(user_input):
    prompt = [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", #GPT-3.5-turbo
        messages=prompt,
        max_tokens=250
    )
    message = response.choices[0].message.content 
    return message

def read_last_line_simple(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1] if lines else None
    return last_line


#### FAST API APP ####
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("inputname.html", {"request": request})

@app.post("/quiz", response_class=HTMLResponse)
async def get_chatbot_interface(request: Request, name: str = Form(...)):
    current_datetime = datetime.now()
    conversation_ID = name+"_"+current_datetime.strftime('%Y%m%d%H%M%S')
    conversation_file = "./conversations/Q_"+conversation_ID+".txt"
    initial_question = generate_question()

    with open(conversation_file, 'a') as file:
        file.write(initial_question.replace("\n", " "))  

    return templates.TemplateResponse("questions.html", {"request": request, "conversation_ID":conversation_ID, "initial_question": initial_question})

class UserQuery(BaseModel):
    user_input: str 
    conversation_ID: str

@app.post("/evaluate")
async def chatgpt_endpoint(user_query: UserQuery):

    conversation_ID = user_query.conversation_ID
    conversation_file = "./conversations/Q_"+conversation_ID+".txt"
    question = read_last_line_simple(conversation_file)

    #print(question)

    answer = user_query.user_input
    feedback = answer_feedback(question, answer) 
    feedback = feedback.replace("\n", "<br>") 

    nextquestion = generate_question()
    with open(conversation_file, 'a') as file:
        file.write("\n"+nextquestion.replace("\n", " "))  
    
    return {"feedback": feedback, 'nextquestion': nextquestion}

if __name__ == '__main__':
    uvicorn.run("quiz:app", port=8000, reload=True)

    # conversation_file = "./conversations/question_20240203223737.txt"
    # question = read_last_line_simple(conversation_file)
    # print(question)

    # answer = 'START'
    # while answer != 'q':
    #     qustion = generate_question()
    #     print(qustion)

    #     answer = input("Your answer: ")
    #     # print(answer)
        
    #     feedback = answer_feedback(qustion, answer)
    #     print(feedback, "\n\n")

    
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
