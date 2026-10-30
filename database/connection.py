from typing import Any, List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
from sqlmodel import SQLModel, Session, create_engine
from models.events import Event
database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string,echo=True,connect_args=connect_args)
def conn():
    SQLModel.metadata.create_all(engine_url)
def get_session():
    with Session(engine_url) as session:
      yield session