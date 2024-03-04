from ._anvil_designer import HomeDetailTemplate
from anvil import *
import anvil.server
from anvil_extras import routing


@routing.route('homedetail')
class HomeDetail(HomeDetailTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        anvil.server.call('do_admin')
        # Any code you write here will run before the form opens.
