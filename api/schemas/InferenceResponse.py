from pydantic import BaseModel

class InferenceResponse(BaseModel):
    result: int