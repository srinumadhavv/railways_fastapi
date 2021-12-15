from pydantic import BaseModel,EmailStr,ValidationError, validator
from datetime import datetime


class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str
    mobile:int
    password2:str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v