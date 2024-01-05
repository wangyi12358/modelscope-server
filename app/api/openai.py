from fastapi import APIRouter, Body
from app.utils.response import response
import openai
import os

API_KEY = "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"

# openai.organization = "org-NwXjb0pP07z29fiSlNcifZ1F"
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()


@router.get("/models")
async def models():
    list = openai.Model.list()
    return response(data=list)


@router.post("/completions")
async def completions(
        model: str = Body(embed=True),
        prompt: str = Body(embed=True)
):
    print(model)
    print(prompt)
    response = openai.Completion.create(model, prompt, temperature=0, max_tokens=7)
    return response(data=response)