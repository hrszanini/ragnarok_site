import pydantic
import typing
import controllers


class NewUser(pydantic.BaseModel):
    user_id: str
    user_password: str
    user_email: str
    user_birthday: str


class Login(pydantic.BaseModel):
    user_id: str
    user_password: str
    new_password: typing.Optional[str]
    _new_password = pydantic.validator('new_password', allow_reuse=True)(controllers.validate_password)