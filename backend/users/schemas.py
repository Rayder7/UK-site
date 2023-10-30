from fastapi_users import schemas
import uuid


class UserRead(schemas.BaseUser[uuid.UUID]):
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
