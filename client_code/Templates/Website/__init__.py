from ._anvil_designer import WebsiteTemplate
from anvil import *
import anvil.js


class Website(WebsiteTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        if anvil.js.window.navigator.userAgent.lower().find("mobi") > -1:
            self.btn_nav.visible = True

            self.fp_header_right.clear()
            self.fp_header_right.add_component(self.btn_nav)
            self.fp_header_right.align = 'justify'
            
            self.cp_sidebar.add_component(self.btn_signup)
            self.cp_sidebar.add_component(self.btn_signin)
            self.btn_signup.align = 'left'
            self.btn_signin.align = 'left'
            self.btn_signup.role = None 
            self.btn_signin.role = None

            self.fp_footer.align = 'center'

    def btn_signin_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

    def btn_signup_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

    def btn_nav_click(self, **event_args):
        """This method is called when the button is clicked"""
        print('btn_nav_click')
        if self.btn_nav.icon == 'fa:bars':
            self.btn_nav.icon = 'fa:close'
        else:
            self.btn_nav.icon = 'fa:bars'
        self.call_js('clickNav')
