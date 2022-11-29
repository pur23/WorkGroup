from typing import Optional,List
from sqlmodel import Field, SQLModel, Relationship


class OwnerBase(SQLModel):
    name: str = Field(index=True)
    address: str

class Owner(OwnerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pets: List["Pet"] = Relationship(back_populates="owner")
    
class OwnerCreate(OwnerBase):
    pass

class OwnerRead(OwnerBase):
    id:int

class PetBase(SQLModel):
    name: str
    age: int 
    owner_id:Optional[int] = Field(default=None, foreign_key="owner.id")

class Pet(PetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner: Optional[Owner] = Relationship(back_populates="pets")

class PetCreate(PetBase):
    pass

class PetRead(PetBase):
    id: int


class PetReadWithOwner(PetRead):
    owner: Optional[OwnerRead] = None

class OwnerReadWithPets(OwnerRead):
    pets: List[PetRead] = []

