from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from .interfaces.user_creator import UserCreatorInterface


class UserCreator(UserCreatorInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repo = users_repository

    def insert_new_user(self, person_name:str, age:int, height: float) -> dict:
        self.__check_if_user_exists(person_name)
        self.__create_new_user(person_name, age, height)
        return self.__format_response()

    def __check_if_user_exists(self, person_name:str) -> None:
        select_users = self.__users_repo.select_user(person_name)
        if (not select_users or len(select_users) == 0):
            return
        else:
            raise Exception('User already exists')
          
    def __create_new_user(self, person_name:str, age:int, height: float) -> None:
        self.__users_repo.insert_user(person_name, age, height)
        return
    
    def __format_response(self) -> dict:
        return {
            "Type": "Users",
            "count": 1,
            "message": "User created successfully"
        }