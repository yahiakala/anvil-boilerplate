from ._anvil_designer import BlankTemplateTemplate
from anvil import *


class BlankTemplate(BlankTemplateTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)