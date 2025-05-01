# from litestar.plugins.sqlalchemy.repository import SQLAlchemyAsyncRepository
# from litestar.plugins.sqlalchemy.service import SQLAlchemyAsyncRepositoryService

from litestar.plugins.sqlalchemy import repository, service

from models import UserModel


class UserService(service.SQLAlchemyAsyncRepositoryService[UserModel]):
    """User service."""
    class Repo(repository.SQLAlchemyAsyncRepository[UserModel]):
        """User repository."""
        model_type = UserModel
    repository_type = Repo