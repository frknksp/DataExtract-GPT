from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat_with_gpt import main

app = FastAPI()

# CORS ayarları ve izin verilen adresler
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str

@app.post("/generate_json/")
async def generate_json(user_message: UserMessage):
    result = main(user_message.message)
    return {"json_output": result}
