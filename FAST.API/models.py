from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class role(str, Enum):
    role_1 = "admin"
    role_2 = "aluno"
    role_3 = "instrutor"

class user(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name:str
    email:str
    role: List[role]    