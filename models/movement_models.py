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
    id_movement: int = 0
    username: str
    date: datetime = datetime.now()
    movement: str # Income or Outcome
    movement_type: str # Fixed or Variable
    movement_category: str
    description: str
    amount: int
    actual_balance: int
