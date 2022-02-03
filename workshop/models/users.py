from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UpdateUsers(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class BaseUsers(UpdateUsers):
    id: int
    register_data: datetime


class Update_fields_Users(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
