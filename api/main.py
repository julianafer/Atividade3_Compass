from fastapi import FastAPI

from api.models.MockModel import MockModel
from api.models.InferenceRequest import InferenceRequest
from api.models.InferenceResponse import InferenceResponse

app = FastAPI()

# Carregar o modelo (mockado)
model = MockModel()

@app.post("/api/v1/inference", response_model=InferenceResponse)
async def perform_inference(request: InferenceRequest):
    # Extrair dados do request
    data = request.dict()

    # Realizar inferência (mockada)
    result = model.predict(data)

    # Retornar resposta
    return InferenceResponse(result=result)

# comando para rodar:
# python -m uvicorn api.main:app --reload