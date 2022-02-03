from datetime import datetime
from pydantic import BaseModel


class BaseUsersList(BaseModel):
    id: int
    username: str
    email: str
    password: str
    register_data: datetime

    class Config:
        orm_mode = True
