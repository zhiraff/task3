import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, model_validator, Field, ConfigDict
from pydantic import EmailStr


__all__ = [
    # "UserModel",
    # "UserAddModel",
    # "PageUserModel",
    # "UserBaseModel",
    # "UserUpdateModel"
    "User",
    "UserCreate",
    "UserUpdate"
]

#
# class UserBaseModel(BaseModel):
#     name: str = Field("name", defaut='vlasovavi', to_lower=True)
#     surname: str = Field("surname", defaut='vlasovavi', to_lower=True)
#     model_config = ConfigDict(from_attributes=True)
#
# class UserModel(UserBaseModel):
#     id: UUID
#
#     def find_exist(self):
#         return dict(
#             name=self.name,
#             surname=self.surname,
#         )
#
#
# class UserAddModel(UserBaseModel):
#     password: str = Field()
#     confirm_password: str = Field()
#
#     @model_validator(mode='after')
#     def check_query(self):
#         if self.password:
#             if self.password != self.confirm_password:
#                 raise ValueError('Password mismatch')
#         return self
#
#
# class UserUpdateModel(UserBaseModel):
#     id: UUID
#     password: Optional[str] = Field(default=None)
#     confirm_password: Optional[str] = Field(default=None)
#
#     @model_validator(mode='after')
#     def check_query(self):
#         if self.password:
#             if self.password != self.confirm_password:
#                 raise ValueError('Password mismatch')
#         return self
#
#
# class PageUserModel(BaseModel):
#     page: int
#     limit: int
#     pages: int
#     count: int
#     data: Optional[List[UserModel]]
#
#     class Config:
#         pass

class BaseSchema(BaseModel):
    """Base Schema with ORM mode enabled."""
    model_config = ConfigDict(from_attributes=True)

class User(BaseSchema):
    """User response schema."""
    id: UUID
    name: str
    surname: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

class UserCreate(BaseSchema):
    """Schema for creating users."""
    name: str
    surname: str
    password: str = Field()
    confirm_password: str = Field()

    @model_validator(mode='after')
    def check_query(self):
        if self.password:
            if self.password != self.confirm_password:
                raise ValueError('Password mismatch')
        return self

class UserUpdate(BaseSchema):
    """Schema for updating users."""
    name: str | None = None
    surname: str | None = None
