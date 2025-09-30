import pytest
from db_connection_handler import DbConnectionHandler

@pytest.mark.skip(reason="Integration with DB")
def test_db_connection_handler():
    db_coon_handler = DbConnectionHandler()

    assert db_coon_handler.session is None

    with db_coon_handler:
        assert db_coon_handler.session is not None