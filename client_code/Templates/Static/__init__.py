from ._anvil_designer import StaticTemplate
from anvil import *


class Static(StaticTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
