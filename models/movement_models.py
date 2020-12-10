from pydantic import BaseModel
from datetime import datetime

class MovementIn(BaseModel):
    username: str
    movement: str # Income or Outcome
    movement_type: str # Fixed or Variable
    movement_category: str
    description: str
    amount: int

class MovementOut(BaseModel):
    id_movement: int
    username: str
    date: datetime = datetime.now()
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int
    actual_balance: int
