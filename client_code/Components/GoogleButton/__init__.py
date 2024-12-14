from ._anvil_designer import GoogleButtonTemplate
from anvil import *

from m3._utils.properties import anvil_prop, italic_property, property_with_callback, spacing_property, get_unset_spacing


class GoogleButton(GoogleButtonTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self._props = properties
        self.init_components(**properties)
        self.dom_nodes['anvil-ss-google-button'].addEventListener("click", self._handle_click)

    def _handle_click(self, event):
        event.preventDefault()
        if self.enabled:
            self.raise_event("click", event=event)
            
    def _anvil_get_unset_property_values_(self):
        el = self.dom_nodes["anvil-ss-google-button-text"]
        sp = get_unset_spacing(el, el, self.spacing)

        return {"spacing": sp}
      
    def _update_button_look(self, value=None):
        self._set_text()

    def _set_text(self):
        if self.text:
            self.dom_nodes['anvil-ss-google-button-text'].innerText = self.text

    def form_show(self, **event_args):
        self._update_button_look()

    text = property_with_callback("text", _update_button_look)
    italic = italic_property('anvil-ss-google-button-text')
    spacing = spacing_property('anvil-ss-google-button')

    @anvil_prop
    def enabled(self, value):
        if value:
            self.dom_nodes['anvil-ss-google-button'].removeAttribute("disabled")
        else:
            self.dom_nodes['anvil-ss-google-button'].setAttribute("disabled", " ")