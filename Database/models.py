from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class MainModel(DeclarativeBase):
    pass



class Todo(MainModel):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)