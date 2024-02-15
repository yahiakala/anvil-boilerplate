from ._anvil_designer import HomeAnonTemplate
from anvil import *
from .. import utils
from anvil_extras import routing

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

    def btn_login_click(self, **event_args):
        utils.login()

    def btn_register_click(self, **event_args):
        utils.register()
