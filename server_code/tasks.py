import anvil.server
import anvil.users
from anvil.tables import app_tables
from anvil_extras.authorisation import authorisation_required
from anvil_extras import authorisation

authorisation.set_config(get_roles='usermap')


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

@anvil.server.callable(require_user=True)
@authorisation_required('admin')
def do_admin():
    print('doing admin thing.')
    pass