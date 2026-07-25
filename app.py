import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="a simple api server"
)

@app.get("/")
def home():
    return {"status": "running"}

prompt1 = ChatPromptTemplate.from_template("give the answer about {topic} in a 5 lines")

add_routes(
    app,
    prompt1 | model,
    path="/answer"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port = 5000)




