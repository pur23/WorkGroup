from fastapi import FastAPI, HTTPException,Depends
from sqlmodel import Session,select
from typing import List

from databases import create_db_and_tables,engine,get_session
from models import Owner, Pet,PetCreate,OwnerCreate ,PetReadWithOwner,OwnerRead,OwnerReadWithPets


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def helloWorld():
    return {"message":"Hello World"}

@app.post("/owner/")
def create_Owner(*, session: Session = Depends(get_session),owner: OwnerCreate):
        db_owner = Owner.from_orm(owner)
        session.add(db_owner)
        session.commit()
        session.refresh(db_owner)
        return db_owner

@app.get("/owner/",response_model=List[OwnerRead])
def read_Owner(*, session: Session = Depends(get_session)):
        owner = session.exec(select(Owner)).all()
        return owner

@app.get("/owner/{owner_id}", response_model=OwnerReadWithPets)
def read_owner(*, session: Session = Depends(get_session),owner_id: int):
    owner = session.get(Owner, owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner


@app.post("/pet/")
def create_Pet(*, session: Session = Depends(get_session),pet: PetCreate):
    db_pet = Pet.from_orm(pet)
    session.add(db_pet)
    session.commit()
    session.refresh(db_pet)
    return db_pet

@app.get("/pet/",response_model=List[PetReadWithOwner])
def read_Pet(*, session: Session = Depends(get_session)):
    pet = session.exec(select(Pet)).all()
    return pet
