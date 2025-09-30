import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from .users_repository import UsersRepository

@pytest.mark.skip(reason="Insert in DB")
def test_users_repository():
    db_conn = DbConnectionHandler()
    user_repo = UsersRepository(db_conn)

    person_name = "meu Nome de Teste"
    age = 55
    height = 7.34

    user_repo.insert_user(person_name, age, height)
    users = user_repo.select_user(person_name)
    assert isinstance(users, list)
    assert len(users) == 1
    assert users[0].person_name == person_name
    assert users[0].age == age
    assert users[0].height == height