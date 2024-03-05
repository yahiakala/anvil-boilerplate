from ._anvil_designer import SignupTemplate
from anvil import *
import anvil.users
from anvil_extras import routing

from .. import utils
from .. import Global


@routing.route('signup')
class Signup(SignupTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def btn_google_click(self, **event_args):
        """This method is called when the button is clicked"""
        try:
            user = anvil.users.signup_with_google(remember=True)
        except anvil.users.UserExists as e:
            anvil.alert(str(e.args[0]))
            user = None
            routing.set_url_hash('signin')
        
        if user:
            Global.user = user
            routing.set_url_hash('homedetail')

    def btn_signup_click(self, **event_args):
        """This method is called when the button is clicked"""

        proceed = self.tb_password_repeat_lost_focus()
        if proceed:
            user = utils.signup_with_email(
                self.tb_email.text, self.tb_password.text
            )
            if user:
                # Still needs to verify email
                routing.set_url_hash('homeanon')

    def tb_password_repeat_lost_focus(self, **event_args):
        """This method is called when the TextBox loses focus."""
        if len(self.tb_email.text) < 5 or "@" not in self.tb_email.text or "." not in self.tb_email.text:
            self.lbl_error.text = "Enter an email address"
        elif self.tb_password.text == '' or self.tb_password.text is None:
            self.lbl_error.text = 'Please enter a password.'
        elif self.tb_password_repeat.text != self.tb_password.text:
            self.lbl_error.text = 'Passwords do not match.'
        else:
            self.lbl_error.visible = False
            return True

        self.lbl_error.visible = True
        return False
