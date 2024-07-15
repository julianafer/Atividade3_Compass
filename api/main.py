from fastapi import FastAPI

from api.models.ModelLoader import ModelLoader
from api.schemas.InferenceRequest import InferenceRequest
from api.schemas.InferenceResponse import InferenceResponse

import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()
bucket_name = os.getenv('BUCKET_NAME')
model_key = os.getenv('MODEL_KEY')

# Carregar o modelo do S3
model_loader = ModelLoader(bucket_name, model_key)
model_loader.load_model()

@app.post("/api/v1/inference", response_model=InferenceResponse)
async def perform_inference(request: InferenceRequest):
    # Extrair dados do request
    data = [list(request.dict().values())]

    # Realizar inferência
    result = model_loader.predict(data)

    # Retornar resposta
    return InferenceResponse(result=result[0])


# comando para rodar:
# python -m uvicorn api.main:app --reload