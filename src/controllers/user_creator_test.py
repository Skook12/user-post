import pytest
from .user_creator import UserCreator

class UserRepositoryMock:
    def __init__(self):
        self.users = []

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        self.users.append({"name": person_name, "age": age, "height": height})

    def select_user(self, person_name: str) -> list:
        return [user for user in self.users if user["name"] == person_name]

class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
       self.select_user_att["person_name"] = person_name
       return [1,2,3]
    

def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UserCreator(user_repository)

    person_name = "John Doe"
    age = 30
    height = 1.75

    response = user_creator.insert_new_user(person_name, age, height)
    print(response)

def test_insert_new_user_with_error():
    user_repository = UserRepositoryMockWithError()
    user_creator = UserCreator(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_creator.insert_new_user("John Doe", 30, 1.75)
    print(exc_info.value)