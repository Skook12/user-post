from src.controllers.interfaces.user_finder import UserFinderInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class UserFinderView:
    def __init__(self, controller: UserFinderInterface):
        self.__controller = controller
    
    def handle_find_by_person_name(self, req: HttpRequest) -> HttpResponse:
        try:
            person_name = req.params['person_name']
            response = self.__controller.find_by_person_name(person_name)
            return HttpResponse(200, response)
        except Exception as e:
            return HttpResponse(500, {'error': str(e)})
    
    