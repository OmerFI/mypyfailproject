from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


user = User(id=1, name="John Doe", age=25)

print(user.dict())
