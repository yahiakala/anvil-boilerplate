from ._anvil_designer import RouterTemplate
from anvil import *
import anvil.users

from .. import Global
from .. import utils

from anvil_extras import routing

from ..HomeAnon import HomeAnon
from ..HomeDetail import HomeDetail
from ..Settings import Settings
from ..BlankTemplate import BlankTemplate
from ..Signin import Signin
from ..Tests import Tests


@routing.template(path='', priority=0, condition=None)
class Router(RouterTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.link_home.tag.url_hash = ''
        self.link_dev.tag.url_hash = 'tests'
        self.link_logout.tag.url_hash = 'logout'
        self.link_settings.tag.url_hash = 'settings'
        self.link_login.tag.url_hash = 'signin'
        self.link_signup.tag.url_hash = 'signup'
        
        user = Global.user
        self.set_account_state(user)

    def nav_click(self, sender, **event_args):
        if sender.tag.url_hash == '':
            if Global.user:
                self.set_account_state(Global.user)
                routing.set_url_hash('homedetail')
            else:
                routing.set_url_hash('homeanon')
        else:
            routing.set_url_hash(sender.tag.url_hash)

    def on_navigation(self, url_hash, url_pattern, url_dict, unload_form):
        """Whenever a new route is loaded."""
        for link in self.cp_sidebar.get_components():
            if type(link) == Link:
                link.role = 'selected' if link.tag.url_hash == url_hash else None
        if url_hash in ['homeanon', 'homedetail']:
            self.link_home.role = 'selected'

    def on_form_load(self, url_hash, url_pattern, url_dict, form):
        """Any time a form is loaded."""
        self.set_account_state(Global.user)

    def link_signup_click(self, **event_args):
        """This method is called when the link is clicked"""
        utils.register()

    def link_login_click(self, **event_args):
        """This method is called when the link is clicked"""
        utils.login()

    def icon_logout_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.users.logout()
        self.set_account_state(None)
        Global.user = None
        self.nav_click(self.link_home)

    def set_account_state(self, user):
        self.icon_logout.visible = user is not None
        self.link_logout.visible = user is not None
        self.link_login.visible = user is None
        self.link_signup.visible = user is None
        self.link_settings.visible = user is not None
        self.link_dev.visible = user is not None and 'dev' in Global.permissions

    def link_help_click(self, **event_args):
        """This method is called when the link is clicked"""
        alert('For help, contact example@example.com')
