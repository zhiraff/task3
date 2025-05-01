from uuid import UUID

from advanced_alchemy.extensions.litestar.providers import create_service_dependencies
from litestar import Controller, get, post, patch, delete
from litestar.params import Parameter
from litestar.plugins.sqlalchemy import service
from sqlalchemy.ext.asyncio import AsyncSession


from schemas import User, UserCreate, UserUpdate
from services import UserService


class UserController(Controller):
    """User CRUD endpoints."""

    path = "/users"
    dependencies = create_service_dependencies(
        UserService,
        key="user_service",
        filters={"id_filter": UUID, "pagination_type": "limit_offset", "search": "name"}
    )
    tags = ["Users"]

    @get()
    async def list_users(
        self,
        db_session: AsyncSession,
    ) -> service.OffsetPagination[User]:
        """List all users with pagination."""
        us = UserService(session=db_session)
        results, total = await us.list_and_count()
        return us.to_schema(data=results, total=total, schema_type=User)

    @post()
    async def create_user(
        self,
        data: UserCreate,
        db_session: AsyncSession,
    ) -> User:
        """Create a new author."""
        us = UserService(session=db_session)
        obj = await us.create(data=data)
        return us.to_schema(data=obj, schema_type=User)


    @get(path="/{user_id:uuid}")
    async def get_user(
        self,
        db_session: AsyncSession,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to retrieve.",
        ),
    ) -> User:
        """Get an existing user."""
        us = UserService(session=db_session)
        obj = await us.get(user_id)
        return us.to_schema(data=obj, schema_type=User)

    @patch(path="/{user_id:uuid}")
    async def update_author(
        self,
        data: UserUpdate,
        db_session: AsyncSession,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to update.",
        ),
    ) -> User:
        """Update a user."""
        us = UserService(session=db_session)
        obj = await us.update(data=data, item_id=user_id)
        return us.to_schema(obj, schema_type=User)

    @delete(path="/{user_id:uuid}")
    async def delete_user(
        self,
        db_session: AsyncSession,
        user_id: UUID = Parameter(
            title="User ID",
            description="The user to delete.",
        ),
    ) -> None:
        us = UserService(session=db_session)
        """Delete an user from the system."""
        _ = await us.delete(user_id)