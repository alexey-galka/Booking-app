from app.shared.base import CommonService
from app.users.models import Users


class UsersService(CommonService):
    model = Users
