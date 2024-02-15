from ._anvil_designer import TestsTemplate
from anvil import *

class Tests(TestsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        from .. import test_client
        self.ctests.test_modules = [test_client]
        self.ctests.card_roles = ['tonal-card', 'elevated-card', 'elevated-card']
        self.ctests.icon_size = 30
        self.ctests.btn_role = 'filled-button'
