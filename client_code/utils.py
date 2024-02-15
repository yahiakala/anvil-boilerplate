import anvil
import datetime as dt

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