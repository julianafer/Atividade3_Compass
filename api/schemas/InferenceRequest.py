from typing import Optional
from pydantic import BaseModel, validator

class InferenceRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    required_car_parking_space: int
    arrival_year: int
    arrival_date: int
    no_of_special_requests: int
    type_of_meal_plan: str
    room_type_reserved: str
    market_segment_type: str
    
    @validator('arrival_date')
    def validate_arrival_date(cls, value: int):
        if not (1 <= value <= 31):
            raise ValueError('Enter a valid date')
        return value
    
    @validator('required_car_parking_space')
    def validate_required_car_parking_space(cls, value: int):
        if not (0 <= value <= 1):
            raise ValueError('The value must be 0 or 1')
        return value