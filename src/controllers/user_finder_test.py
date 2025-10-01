import pytest
from .user_finder import UserFinder
from ..models.entities.users import Users


class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return[
           Users(
               id=123,
               person_name = "mocked_person",
               age = 30,
               height = 1.75
           )
       ]
        
class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return[]      

def test_find_by_person_name():
    person_name = "mocked_person"
    user_repository = UserRepositoryMock()
    user_finder = UserFinder(user_repository)

    response = user_finder.find_by_person_name(person_name)
    print(response)
    print(user_repository.select_user_att)
    
    assert user_repository.select_user_att["person_name"] == person_name
    assert isinstance(response, dict)
    assert response["Type"] == "Users"
    assert "users" in response
    assert isinstance(response["users"], list)

def test_find_by_person_name_with_error():
    user_repository = UserRepositoryMockWithError()
    user_finder = UserFinder(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_finder.find_by_person_name("my_person_name")
    print(exc_info.value)
    
    




    