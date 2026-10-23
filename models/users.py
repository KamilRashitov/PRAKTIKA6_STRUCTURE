from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }
    )


class NewUser(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }
    )


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }
    )