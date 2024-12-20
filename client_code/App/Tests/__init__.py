import anvil.server
from anvil import *
from routing import router

from ...Global import Global
from ._anvil_designer import TestsTemplate


class Tests(TestsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        from .. import test_client

        self.ctests.test_modules = [test_client]
        self.ctests.card_roles = ["tonal-card", "elevated-card", "elevated-card"]
        self.ctests.icon_size = 30
        self.ctests.btn_role = "filled-button"

    def tb_impersonate_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        self.user = anvil.server.call("impersonate_user", self.tb_impersonate.text)
        # reset the globals
        Global.clear_global_attributes()
        router.navigate(path="/")
