import anvil
import datetime as dt
import anvil.users
from anvil_extras import routing

from . import Global


def print_timestamp(input_str):
    # eastern_tz = pytz.timezone('US/Eastern')
    # current_time = dt.datetime.now(eastern_tz)
    # formatted_time = current_time.strftime('%H:%M:%S.%f')
    print(input_str, " : ", dt.datetime.now().strftime("%H:%M:%S.%f"))