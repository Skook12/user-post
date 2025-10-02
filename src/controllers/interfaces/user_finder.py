from abc import ABC, abstractmethod


class UserFinderInterface(ABC):
    @abstractmethod
    def find_by_person_name(self, person_name: str) -> dict:
        pass