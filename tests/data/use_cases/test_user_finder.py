from src.data.use_cases.user_finder import UserFinder
from tests.infra.db.repositories.users_repository_spy import UsersRepositorySpy


def test_find():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    first_name = 'John'
    users = user_finder.find(first_name)

    assert repo.get_user_by_first_name_params['first_name'] == first_name
    assert users['type'] == 'Users'
    assert len(users['attributes']) == users['count']
    assert users['attributes'] is not None
