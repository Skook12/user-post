from pydantic import BaseModel, constr, ValidationError

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def user_creator_validator(http_request: any) -> None:
    class BodyData(BaseModel):
        person_name: constr(min_length=3) # type:ignore
        age: int
        height: float
    
    try:
        BodyData(**http_request.body )
    except ValidationError as exception:
        raise HttpUnprocessableEntityError(exception.errors()) from exception
