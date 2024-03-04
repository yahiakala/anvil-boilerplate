from ._anvil_designer import SignupTemplate
from anvil import *
import anvil.users
from anvil_extras import routing

from .. import Global


@routing.route('signup')
class Signup(SignupTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def btn_google_click(self, **event_args):
        """This method is called when the button is clicked"""
        user = anvil.users.signup_with_google(remember=True)
        # TODO: catch UserExists exception
        if user:
            Global.user = user
            routing.set_url_hash('homedetail')

    def btn_signup_click(self, **event_args):
        """This method is called when the button is clicked"""
        proceed = self.tb_password_repeat_lost_focus()
        if proceed and self.tb_password.text == self.tb_password_repeat.text:
            user = anvil.users.signup_with_email(
                self.tb_email.text, self.tb_password.text, remember=True
            )
            if user:
                Global.user = user
                routing.set_url_hash('homedetail')

    def tb_password_repeat_lost_focus(self, **event_args):
        """This method is called when the TextBox loses focus"""
        if self.tb_password_repeat.text != '' and self.tb_password_repeat.text != self.tb_password.text:
            self.lbl_password_match.visible = True
            return False
        else:
            self.lbl_password_match.visible = False
        # TODO: password strength checker
        return True
