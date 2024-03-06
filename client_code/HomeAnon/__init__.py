from ._anvil_designer import HomeAnonTemplate
from anvil import *
from .. import utils
from anvil_extras import routing
from ..BlankTemplate import BlankTemplate
from ..Signin import Signin

from .. import Global


@routing.route('')
@routing.route('homeanon')
@routing.route('home', url_keys=['action'])
class HomeAnon(HomeAnonTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.action = self.url_dict.get('action', None)

        if self.action and self.action == 'login':
            self.btn_login_click()
        elif self.action and self.action == 'signup':
            self.btn_register_click()

        if Global.user:
            routing.set_url_hash('homedetail')
        else:
            routing.set_url_hash('signin')

    def btn_login_click(self, **event_args):
        routing.set_url_hash('signin')

    def btn_register_click(self, **event_args):
        routing.set_url_hash('signup')
