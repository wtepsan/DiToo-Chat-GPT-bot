from fastapi import FastAPI, APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from openai import OpenAI

from datetime import datetime
import os
import json
import random
import ast
import openai
import uvicorn

# print("THE LOCATION: ", os.getcwd())

########################################################
########################################################
########################################################

router = APIRouter() 

### SET UP VARIABLE ###
PATH_CHAPTER = "quiz"

def questions_generator(chapter, section):
    question_file_name = str(chapter)+"_"+str(section)+".txt"
    questions_file = PATH_CHAPTER+"/lessons/" + question_file_name
    ### SET UP VARIABLE ###

    with open(questions_file, "r") as file:
        # Read the entire file content
        questions_list = file.read()

    questions_answers = json.loads(questions_list) 
    question_N = len(questions_answers)

    return chapter, section, questions_answers, question_N

OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)

def answer_feedback(question, criteria, correct_answer, answer):
    #where the correct answer is {correct_answer}.\

    prompt_text = f"I will now provide a question and the answer. I would like you to mark and provide feedback on a response. If the question is {question} and with the correct answer: {correct_answer}, provide the marks out of 10 and feedback for response: {answer}."

    # print(prompt_text)
    prompt = [{'role':'user', 
               'content': prompt_text}]

    response = client.chat.completions.create(
        model= "gpt-4", #"gpt-3.5-turbo-0125", #GPT-3.5-turbo "gpt-4", #"gpt-3.5-turbo", # "gpt-4", 
        messages=prompt,
        max_tokens=250
    )

    feedback = response.choices[0].message.content 

    return feedback

### QUIZ PAGE ###
templates_quiz = Jinja2Templates(directory= PATH_CHAPTER+"/templates")
@router.get("/", response_class=HTMLResponse)
async def start_quiz(request: Request, chapter:str, section:str, topic:str, studentID:str, studentName:str): # , name: str = Form(...)):

    _, _, questions_answers, question_N = questions_generator(chapter, section)

    print(studentID, studentName)
    student_ID = studentID      #"490510643"
    student_name = studentName  #"Firstname Lastname"
    conversation_ID = student_ID+"_" + datetime.now().strftime('%Y%m%d%H%M%S')
    question_order = list(range(question_N))
    # random.shuffle(question_order)

    initial_question = questions_answers[question_order[0]]['question']

    responses = {"request": request, \
                "question_N": question_N, \
                "chapter": chapter, \
                "section": section, \
                "topic": topic, \
                "student_ID": student_ID, \
                "student_name": student_name, \
                "conversation_ID": conversation_ID, \
                "initial_question": initial_question, \
                "question_order": question_order, \
                "question_N": question_N}

    return templates_quiz.TemplateResponse("quiz.html", responses)

### SEND ANSWER TO EVALUATE ###
class UserQuery(BaseModel):
    user_input: str
    chapter: str
    section: str
    student_ID: str
    student_name: str
    conversation_ID: str
    question_order: list
    question_now: int

@router.post("/response_evaluation")
async def evaluate_response(user_query: UserQuery):

    responsed_answer = user_query.user_input 
    chapter = user_query.chapter
    section = user_query.section
    student_ID = user_query.student_ID
    student_name = user_query.student_name
    conversation_ID = user_query.conversation_ID
    question_order = user_query.question_order
    question_now = user_query.question_now

    # print(responsed_answer)
    # chapter, section, questions_answers, question_N
    _, _, questions_answers, question_N = questions_generator(chapter, section)

    converstation_path = PATH_CHAPTER + "/conversations"+ "/"+student_ID+"/"
    if not os.path.exists(converstation_path):
        os.makedirs(converstation_path)
        print(f"Folder '{converstation_path}' created")

    converstation_filename = chapter+"_"+section+"_"+conversation_ID+".txt"
    conversation_file = converstation_path+converstation_filename

    if question_now <= question_N-1:

        question_order_now = question_order[question_now]

        question = questions_answers[question_order_now]['question']
        criteria = questions_answers[question_order_now]['criteria']
        correct_answer = questions_answers[question_order_now]['answer']

        feedback = answer_feedback(question, criteria, correct_answer, responsed_answer)
        with open(conversation_file, 'a') as file:
            file.write("Question: "+question + "\n")  
            file.write("Answer: "+responsed_answer + "\n")  
            file.write("Evaluation: "+feedback+"\n\n") 

        feedback = feedback.replace("\n", "<br>") 
        if question_now < question_N-1:
            question_order_next = question_order[question_now+1]
            nextquestion = questions_answers[question_order_next]['question'] 
            return {"feedback": feedback, 'nextquestion': nextquestion}
        elif question_now == question_N-1:
            nextquestion = "No more question. Thank you for your attempt!" 
            return {"feedback": feedback, 'nextquestion': nextquestion}
    else:
        nextquestion = "No more question. Thank you for your attempt!" 
        return {"feedback": "Great JOB", 'nextquestion': nextquestion}
    
############################################################################# 
#############################################################################
#############################################################################

if __name__ == '__main__':
    uvicorn.run("main:router", port=8000, reload=True)
