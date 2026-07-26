from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length=1,max_length=50)
    email: EmailStr = Field(min_length=1,max_length=120) #pydantic has a customemailstr datatype; so we don't have to write our custom error handlers

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True) #tells pydantic to python object attr 
    #instead of keys in dict

    id: int #pOSTiD
    image_file: str | None 
    image_path: str

class PostBase(BaseModel):
    title: str = Field(min_length=1,max_length=100)
    content: str = Field(min_length=1)

class PostCreate(PostBase):
    user_id: int #TEMP

class PostResponse(PostBase):
    id: int #avoid naming fields as id as it is a python builtin
    #but for database models and api responses its standard
    date_posted: datetime
    user_id: int
    author: UserResponse

    model_config = ConfigDict(from_attributes=True)