from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    name : str
    comment: str