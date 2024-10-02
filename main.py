
from contextlib import asynccontextmanager
from fastapi import FastAPI
from Database.DatabaseManager import TablesManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await TablesManager.delete_tables()
    print("tables deleted")
    await TablesManager.create_tables()
    print("tables created")
    yield
    print("Server stopped")

app = FastAPI(lifespan=lifespan)