
### This program is updated from 
### https://github.com/anoopshrma/Chatgpt-using-GPT-4
### https://pythonwarriors.com/how-to-make-chatgpt-remember-our-previous-conversations/

from fastapi import FastAPI, Request, Form, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel 
from typing import Optional 
import httpx
from starlette.responses import RedirectResponse

from datetime import datetime
import os
import json
import random
import ast
import openai
import uvicorn

app = FastAPI()

##### MAIN WEBPAGE #####

app.mount("/css", StaticFiles(directory="templates/css"), name="css")
app.mount("/images", StaticFiles(directory="templates/images"), name="images")
app.mount("/script", StaticFiles(directory="templates/script"), name="script")

templates = Jinja2Templates(directory="templates")
 
# @app.get("/", response_class=HTMLResponse)
# async def inputname(request: Request):  
#     return templates.TemplateResponse("inputname.html", {"request": request})

@app.get("/", response_class=RedirectResponse)
async def redirect_to_google():
    return RedirectResponse(url="https://cmu.to/DiToolQuiz")

########################################################
#### GET STUDENT INFO FROM CMU AUTH ####
########################################################

async def fetch_basic_info_with_token(access_token: str):
    url = "https://misapi.cmu.ac.th/cmuitaccount/v1/api/cmuitaccount/basicinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
        if response.status_code == 200:
            # Successfully retrieved data, return as JSON
            return response.json()
        else:
            # Forward the error from the external API
            raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get("/callback", response_class=HTMLResponse)
async def handle_callback(request: Request, code: str = Query(...), state: str = Query(...)):  # Corrected parameter type
    token_url = "token_url"
    client_id = "client_id"
    client_secret = "client_secret"
    redirect_uri = "http://202.80.238.234:9443/callback"
    grant_type = "authorization_code"
    
    data = {
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type,
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    async with httpx.AsyncClient() as client:
        token_response = await client.post(token_url, data=data, headers=headers)
        
        if token_response.status_code == 200:
            token_data = token_response.json()
            access_token = token_data.get("access_token")
            
            # Use the access token to fetch basic info
            basic_info = await fetch_basic_info_with_token(access_token)
            
            # Render the welcome.html template with the fetched basic info
            # htmlreturn = "welcome_"+state+".html"
            htmlreturn = "welcome.html"
            return templates.TemplateResponse(htmlreturn, {"request": request, "basic_info": basic_info, "state": state})
        else:
            # Handle error in token acquisition
            raise HTTPException(status_code=token_response.status_code, detail="Error obtaining token")

#############################################
#############################################
def get_student_details(
    studentID: Optional[str] = Query(None),
    studentName: Optional[str] = Query(None),
    form_studentID: str = Form(None),
    form_studentName: str = Form(None), 
):
    final_studentID = form_studentID if form_studentID is not None else studentID
    final_studentName = form_studentName if form_studentName is not None else studentName
    
    if not final_studentID or not final_studentName:
        raise HTTPException(status_code=400, detail=f"{final_studentID} Student ID and {final_studentName} name are required")
        
    return {"studentID": final_studentID, "studentName": final_studentName}

@app.post("/contents", response_class=HTMLResponse)
@app.get("/contents", response_class=HTMLResponse)
async def mainpage(request: Request, student_details: dict = Depends(get_student_details)):
    htmlreturn = "contents.html"  # WILL CHANGE IN THE FUTURE TO ACCEPT MORE COURESE through state 
    return templates.TemplateResponse(htmlreturn, {"request": request, **student_details})


### QUIZ ###
from quiz.main import router as quiz

app.include_router(quiz, prefix="/quiz")
app.mount("/quiz/css", StaticFiles(directory="quiz/templates/css"), name="quiz/css")
app.mount("/quiz/images", StaticFiles(directory="quiz/templates/images"), name="quiz/images") 

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, log_level="info")
