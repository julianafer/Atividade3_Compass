from fastapi import APIRouter, HTTPException
import xgboost as xgb


router = APIRouter() # creates a instance of APIRoute


@router.get("/")
def read_root():
    return {
        "message": "API no Ar!"
    }

@router.post("/api/v1/inference")
def inference(request: InferenceRequest):
    try:

