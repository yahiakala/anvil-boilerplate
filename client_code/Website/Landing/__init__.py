from ._anvil_designer import LandingTemplate
from anvil import *


class Landing(LandingTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.