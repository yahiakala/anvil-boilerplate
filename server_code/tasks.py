import anvil.server
import anvil.users
from anvil.tables import app_tables


@anvil.server.callable(require_user=True)
def get_permissions():
    # TODO: add to anvil extras
    user = anvil.users.get_user(allow_remembered=True)
    usermap = app_tables.usermap.get(user=user)
    user_permissions = set(
        permission["name"]
        for role in usermap["roles"]
        for permission in role["permissions"]
    )
    return list(user_permissions)