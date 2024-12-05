from anvil import *

from ._anvil_designer import HomeTemplate


class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # anvil.server.call('do_admin')
        # Any code you write here will run before the form opens.

    def form_show(self, **event_args):
        """This method is called when the form is shown on the page"""
        pass
