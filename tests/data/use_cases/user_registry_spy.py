from datetime import date

from src.domain.use_cases.user_register import (
    UserRegister as UserResgisterInterface,
)


class UserRegisterSpy(UserResgisterInterface):
    def __init__(self) -> None:
        self.register_params = {}

    def register(
        self, first_name: str, last_name: str, birth_date: date
    ) -> dict:
        self.register_params['first_name'] = first_name
        self.register_params['last_name'] = last_name
        self.register_params['birth_date'] = birth_date

        return {
            'type': 'Users',
            'count': 1,
            'attributes': [
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'birth_date': birth_date,
                }
            ],
        }
