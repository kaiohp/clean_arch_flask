from datetime import date

from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.infra.db.models.users import Users


class UsersRepositorySpy(UsersRepositoryInterface):
    def __init__(self):
        self.insert_user_params = {}
        self.get_user_by_first_name_params = {}

    def insert_user(self, first_name, last_name, birth_date):
        self.insert_user_params['first_name'] = first_name
        self.insert_user_params['last_name'] = last_name
        self.insert_user_params['birth_date'] = birth_date
        return 1

    def get_user_by_first_name(self, first_name):
        self.get_user_by_first_name_params['first_name'] = first_name
        return [
            Users(
                id=1,
                first_name='John',
                last_name='Doe',
                birth_date=date(2000, 1, 1),
            ),
            Users(
                id=2,
                first_name='Jane',
                last_name='Doe',
                birth_date=date(2000, 1, 1),
            ),
        ]
