from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from .interfaces.user_finder import UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repo = users_repository
    
    def find_by_person_name(self, person_name: str) -> dict:
        selected_users = self.__select_and_validate_user(person_name)
        return self.__format_response(selected_users)
        
    def __select_and_validate_user(self, person_name: str) -> list:
        select_users = self.__users_repo.select_user(person_name)
        if (not select_users or len(select_users) == 0):
            raise Exception('User not found')
        return select_users
    
    def __format_response(self, select_users: list) -> dict:
        formatted_users = []
        for users in select_users:
            formatted_users.append({
                "id": users.id,
                "person_name": users.person_name,
                "age": users.age,
                "height": users.height
            }) 
        return {
            "Type": "Users",
            "count": len(formatted_users),
            "users": formatted_users
        }