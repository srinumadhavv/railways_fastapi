from .. import models,schemas,utils
from fastapi import status,HTTPException,Depends,APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user( user : schemas.UserCreate, db : Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    hashed_password2 = utils.hash(user.password2)
    user.password = hashed_password
    user.password2 = hashed_password2
    print(user)
    new_user= models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



    