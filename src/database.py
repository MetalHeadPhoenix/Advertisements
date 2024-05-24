from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData



#For sqlite3 used as test database
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}



class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)





