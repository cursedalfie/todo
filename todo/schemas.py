from datetime import datetime
from sqlite3.dbapi2 import Date
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import TIMESTAMP


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int
    is_completed: Optional[bool] = None
    expired_date: datetime


class TodoRead(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    is_completed: bool
    start_date: datetime
    expired_date: datetime


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    expired_date: datetime
