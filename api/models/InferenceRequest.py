from pydantic import BaseModel, validator

class InferenceRequest(BaseModel):
    no_of_adults: int # Number of adults
    no_of_children: int # Number of Children
    no_of_weekend_nights: int # Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
    no_of_week_nights: int # Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
    type_of_meal_plan: str # Type of meal plan booked by the customer
    required_car_parking_space: float # Does the customer require a car parking space? (0 - No, 1- Yes)
    room_type_reserved: str # Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.
    lead_time: int # Number of days between the date of booking and the arrival date
    arrival_month: int # Month of arrival date
    arrival_date: int # Date of the month
    avg_price_per_room: float # Average price per day of the reservation; prices of the rooms are dynamic. (in euros)
    no_of_special_requests: int # Total number of special requests made by the customer (e.g. high floor, view from the room, etc)
    label_avg_price_per_room: int
    
    @validator('arrival_month')
    def validate_arrival_month(cls, value: int):
        if not (1 <= value <= 12):
            raise ValueError('Enter a valid month')
        return value
    
    @validator('arrival_date')
    def validate_arrival_date(cls, value: int):
        if not (1 <= value <= 31):
            raise ValueError('Enter a valid date')
        return value
    
    @validator('avg_price_per_room')
    def validate_avg_price_per_room(cls, value: float):
        if not (value * 100).is_integer():
            raise ValueError('The average price per room must have exactly two decimal places')
        return value