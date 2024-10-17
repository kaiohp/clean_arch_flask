from src.data.use_cases.user_register import UserRegister
from src.infra.db.repositories.users_repository import UsersRepository
from src.presentation.controllers.user_registry_controller import (
    UserRegistryController,
)


def user_register_compose():
    repository = UsersRepository()
    use_case = UserRegister(repository)
    controller = UserRegistryController(use_case)

    return controller.handle
