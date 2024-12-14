from ._anvil_designer import GoogleButtonTemplate
from anvil import *


class GoogleButton(GoogleButtonTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self._props = properties
        self.init_components(**properties)
        self.dom_nodes['anvil-ss-google-button'].addEventListener("click", self._handle_click)

    def _handle_click(self, event):
        if self.enabled:
            self.raise_event("click")