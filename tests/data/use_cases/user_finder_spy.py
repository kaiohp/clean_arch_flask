from datetime import date

from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


class UserFinderSpy(UserFinderInterface):
    def __init__(self) -> None:
        self.find_params = {}

    def find(self, first_name: str) -> dict:
        self.find_params['first_name'] = first_name
        return {
            'type': 'Users',
            'count': 1,
            'attributes': [
                {
                    'first_name': first_name,
                    'last_name': 'Doe',
                    'birth_date': date(2000, 1, 1),
                }
            ],
        }
