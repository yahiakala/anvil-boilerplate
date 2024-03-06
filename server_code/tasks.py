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
    try:
        user_permissions = set(
            permission["name"]
            for role in usermap["roles"]
            for permission in role["permissions"]
        )
        return list(user_permissions)
    except TypeError:
        return []


@anvil.server.callable(require_user=True)
@authorisation_required('admin')
def do_admin():
    print('doing admin thing.')
    pass


@anvil.server.callable
def login_with_email_mfa(email, password):
    """Try to log user in without MFA. Return exception if user has MFA configured."""
    import bcrypt
    user = app_tables.users.get(email=email)
    if user:
        if user['mfa'] is not None:
            raise anvil.users.MFARequired('User needs to enter MFA credentials.')
        elif user['confirmed_email'] != True:
            raise anvil.users.EmailNotConfirmed('Please confirm your email before logging in.')
        elif bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            anvil.users.force_login(user, remember=True)
            return user
        else:
            raise anvil.users.AuthenticationFailed('Password is incorrect.')