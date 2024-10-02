from Database.Database import engine
from Database.models import MainModel
class TablesManager:
    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(MainModel.metadata.create_all)

    @staticmethod
    async def delete_tables():
        async with engine.begin() as conn:
            await conn.run_sync(MainModel.metadata.drop_all)

