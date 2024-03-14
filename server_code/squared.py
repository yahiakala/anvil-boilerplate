import anvil.server
from anvil.tables import app_tables
import anvil.users
import anvil.email

from anvil_squared import auth


@anvil.server.callable
def login_with_email_custom(email, password):
    """Try to log user in without MFA. Return exception if user has MFA configured."""
    return auth.login_with_email_squared(email, password)


@anvil.server.callable
def signup_with_email_custom(email, password, app_name):
    """Signup a new user. Require them to confirm email before logging in."""
    return auth.signup_with_email_squared(email, password, app_name)


@anvil.server.callable(require_user=True)
def add_mfa_method(password, mfa_method):
    """Add an mfa method."""
    # import bcrypt
    # user = anvil.users.get_user(allow_remembered=True)
    # if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
    #     if user['mfa']:
    #         check_mfa = [i for i in user['mfa'] if i['id'] == mfa_method['id']]
    #         if len(check_mfa) == 0:
    #             user['mfa'] = user['mfa'] + [mfa_method]
    #     else:
    #         user['mfa'] = [mfa_method]
    # else:
    #     raise anvil.users.AuthenticationFailed('Incorrect password')
    # return user
    return utils.add_mfa_method(password, mfa_method)


@anvil.server.callable(require_user=True)
def delete_mfa_method(password, id):
    """Delete mfa method if the password is correct."""
    # import bcrypt
    # user = anvil.users.get_user(allow_remembered=True)
    # if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
    #     user['mfa'] = [i for i in user['mfa'] if i['id'] != id]
    #     if len(user['mfa']) == 0:
    #         user['mfa'] = None
    # else:
    #     raise anvil.users.AuthenticationFailed('Incorrect password.')
    # return user
    return utils.delete_mfa_method(password, id)