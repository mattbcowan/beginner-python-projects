from optparse import Option
from typing import Optional
from pydantic import BaseModel, Field


class ResourceSchema(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    stack_size: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Iron Ingot",
                "description": "Iron in its purest form. For an engineer.",
                "stack_size": 100,
            }
        }


class UpdateResourceModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    stack_size: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Iron Ingot",
                "description": "Iron in its purest form. For an engineer.",
                "stack_size": 200,
            }
        }


def ResponseModel(data, message):
    return {"data": [data], "code": 200, "message": message}


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
