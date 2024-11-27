from sqlalchemy import Integer, String, MetaData, Column, Table, Boolean, ForeignKey, TIMESTAMP, Date

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("second_name", String, nullable=True),
    Column("email", String, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)

)

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=True),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("is_completed", Boolean, nullable=False),
    Column("start_date", Date),
    Column('expired_date', Date)
)
