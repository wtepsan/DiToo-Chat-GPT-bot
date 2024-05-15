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

# app.mount("/css", StaticFiles(directory="templates/css"), name="css")

templates = Jinja2Templates(directory="templates")

 
 
FOLDER = "./midtermsurvey/"
if not os.path.exists(FOLDER): 
    os.makedirs(FOLDER)
    print(f"Folder '{FOLDER}' was created.")
else:
    print(f"Folder '{FOLDER}' already exists.")

surveyquestion_file = FOLDER+"surveyquestions.txt"  

surveyquestions = []
with open(surveyquestion_file, 'r') as file: 
    for line in file:
        surveyquestions.append(line.strip())

#### FAST API APP ####
@app.get("/midtermsurvey", response_class=HTMLResponse)
async def read_form(request: Request):
    current_datetime = datetime.now()
    survey_ID = current_datetime.strftime('%Y%m%d%H%M%S')
    survey_file = FOLDER+"/survey_"+survey_ID+".txt"

    first_question = surveyquestions[0]

    with open(survey_file, 'a') as file:
        file.write(first_question)  

    return templates.TemplateResponse("midtermsurvey.html", {"request": request, "survey_ID":survey_ID, "first_question": first_question})

class UserQuery(BaseModel):
    user_input: str 
    survey_ID: str
    question_number: int

@app.post("/answersurvey")
async def chatgpt_endpoint(user_query: UserQuery):
    survey_ID = user_query.survey_ID
    survey_file = FOLDER+"/survey_"+survey_ID+".txt"
    answer = user_query.user_input  
    question_number = user_query.question_number

    if question_number < 10:            
        nextquestion = surveyquestions[question_number]   
        with open(survey_file, 'a') as file:
            file.write("\n"+answer)  
            file.write("\n\n"+nextquestion.replace("\n", " "))  
    else: 
        with open(survey_file, 'a') as file:
            file.write("\n"+answer)
            nextquestion = "That all the survey questions! You can close this survey. Thank you very much."

    return {'answer':answer  ,'nextquestion': nextquestion}

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)