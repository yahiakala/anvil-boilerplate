import anvil
import datetime as dt
import anvil.users
from anvil_extras import routing

from . import Global


def login():
    Global.user = anvil.users.login_with_form(allow_cancel=True)
    if Global.user:
        routing.set_url_hash('homedetail', load_from_cache=False)


def register():
    Global.user = anvil.users.signup_with_form(allow_cancel=True)
    if Global.user:
        routing.set_url_hash('homedetail', load_from_cache=False)


def print_timestamp(input_str):
    # eastern_tz = pytz.timezone('US/Eastern')
    # current_time = dt.datetime.now(eastern_tz)
    # formatted_time = current_time.strftime('%H:%M:%S.%f')
    print(input_str, " : ", dt.datetime.now().strftime("%H:%M:%S.%f"))


def login_with_link(email):
    pass
    # target_email = _email_token_login_with_form(email_box.text if email_box else "")
    # if target_email:
    #     send_token_login_email(target_email)
    #     alert("An email with a login link has been sent to you. You can now close this window.", buttons=[], dismissible=False)

def reset_password(email):
    pass
    # reset_email_box = TextBox(placeholder="email@address.com", text=email_box.text)
    # pnl = LinearPanel()
    # pnl.add_component(reset_email_box)
    # if alert(pnl, title="Reset password by email", buttons=[("OK", True, "primary"), ("Cancel", False, "default")]):
    #     send_password_reset_email(reset_email_box.text)
    #     error_lbl.text = "Requested password reset for " + reset_email_box.text + ". Check your email."
    # else:
    #     error_lbl.text = ""

def login_with_email(email, password, mfa=True):
    """Login with email with optional mfa."""
    u = anvil.users.get_user()
    if u:
        return u

    try:
        if mfa:
            r = anvil.users.mfa.mfa_login_with_form(email, password)
            if r == 'reset_mfa':
                anvil.users.mfa.send_mfa_reset_email(email)
                anvil.alert("Requested 2-factor authentication reset for " + email + ". Check your email.")
            elif r == None:
                return None
            else:
                return anvil.users.login_with_email(email, password, mfa=r, remember=True)
        else:
            return anvil.users.login_with_email(email, password, remember=True)
    except anvil.users.AuthenticationFailed as e:
        anvil.alert(e.args[0])
        return None


def signup_with_email(email, password, mfa=True, confirm_email=True):
    try:
        if mfa:
            mfa_method, _ = anvil.users.mfa._configure_mfa(email, None, False, [("Cancel", None)], "Sign up")
            user = anvil.server.call("anvil.private.users.signup_with_email", email, password, mfa_method=mfa_method, remember=True)
            # user = anvil.users.signup_with_email(email, password, mfa_method=mfa_method, remember=True)
        else:
            user = anvil.users.signup_with_email(email, password, remember=True)

        if confirm_email:
            anvil.alert(
                "We've sent a confirmation email to " + email + ". Open your inbox and click the link to complete your signup.",
                title="Confirm your Email",
                buttons=[("OK", None, "primary")]
            )

    except anvil.users.UserExists as e:
        anvil.alert(str(e.args[0]))
        return None

    except anvil.users.PasswordNotAcceptable as e:
        anvil.alert(str(e.args[0]))
        return None

    return user