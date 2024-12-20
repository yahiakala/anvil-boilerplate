import anvil.users
from anvil import *
from routing import router

from ...Global import Global
from ._anvil_designer import RouterTemplate


class Router(RouterTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        user = Global.user
        self.set_account_state(user)

    def on_form_load(self, url_hash, url_pattern, url_dict, form):
        """Any time a form is loaded."""
        self.set_account_state(Global.user)

    def set_account_state(self, user):
        self.nav_admin.visible = (
            user is not None and "see_members" in Global.permissions
        )

    def link_help_click(self, **event_args):
        """This method is called when the link is clicked"""
        alert("For help, contact example@example.com")

    def nav_logout_click(self, **event_args):
        """This method is called when the component is clicked"""
        with anvil.server.no_loading_indicator:
            anvil.users.logout()
            self.set_account_state(None)
            router.clear_cache()
            Global.clear_global_attributes()
            router.navigate(path="/signin")
