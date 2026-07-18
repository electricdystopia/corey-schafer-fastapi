from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):
    title: str = Field(min_length=1,max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1,max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int #avoid naming fields as id as it is a python builtin
    #but for database models and api responses its standard
    date_posted: str

    model_config = ConfigDict(from_attributes=True)