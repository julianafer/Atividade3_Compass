from pydantic import BaseModel

class InferenceRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    type_of_meal_plan: str
    # Adicione outros campos conforme necessário