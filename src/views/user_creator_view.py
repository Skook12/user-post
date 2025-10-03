from src.controllers.interfaces.user_creator import UserCreatorInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class UserCreatorView:
    def __init__(self, controller: UserCreatorInterface):
        self.__controller = controller
    
    def handle_insert_new_user(self, req: HttpRequest) -> HttpResponse:
        try:
            person_name = req.body['person_name']
            age = req.body['age']
            height = req.body['height']
            
            response = self.__controller.insert_new_user(person_name, age, height)
            return HttpResponse(200, response)
        except Exception as e:
            return HttpResponse(500, {'error': str(e)})
    
    