from src.models.connection.db_connection_handler import DbConnectionHandler
from src.models.entities.users import Users
from .interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):
    def __init__(self, db_conn_handler: DbConnectionHandler):
        self.__db_conn_handler = db_conn_handler
  
    def insert_user(self, person_name:str, age:int, height: float) -> None:
        with self.__db_conn_handler as database:
            try:
                new_user = Users(
                    person_name=person_name,
                    age=age,
                    height=height
                )
                database.session.add(new_user)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def select_user(self, person_name: str) -> list[Users]:
        with self.__db_conn_handler as database:
            users = (
                database.session
                .query(Users)
                .filter(Users.person_name == person_name)
                .all()
            )
            return users