from datetime import datetime, UTC

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from Models.models import todos
from auth.database import get_async_session, Todo
from todo.schemas import TodoCreate, TodoUpdate

todorouter = APIRouter()


@todorouter.post('/create_todo')
async def create_todo(new_todo: TodoCreate, session: AsyncSession = Depends(get_async_session)):
    statement = insert(todos).values(**new_todo.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 200}


@todorouter.put('/edit_todo/{todo_id}')
async def edit_todo(todo_id: int, todo_edit: TodoUpdate, session: AsyncSession = Depends(get_async_session)):
    if todo_edit.expired_date < datetime.now(UTC):
        print("INVALID DATA")
    statement = (
        update(Todo)
        .where(Todo.id == todo_id)
    )
    await session.execute(statement)
    await session.commit()
    return {'status': 200}


@todorouter.delete('/delete_todo/{todo_id}')
async def delete_todo(todo_id: int, session: AsyncSession = Depends(get_async_session)):
    statement = (
        delete(Todo)
        .where(Todo.id == todo_id)
    )
    await session.execute(statement)
    await session.commit()
    return {'status': 200}


@todorouter.get('/getall_todos')
async def getall_todo(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(todos))
    return result.mappings().all()


@todorouter.get('/getone_todo/{todo_id}')
async def getone_todo(todo_id: int, session: AsyncSession = Depends(get_async_session)):
    querry = (
        select(Todo)
        .where(Todo.id == todo_id)
    )
    result = await session.execute(querry)
    return result.mappings().first()