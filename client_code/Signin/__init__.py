from ._anvil_designer import SigninTemplate
from anvil import *
import anvil.users
from anvil_extras import routing

from .. import utils
from .. import Global


@routing.route('signin')
class Signin(SigninTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def btn_google_click(self, **event_args):
        """This method is called when the button is clicked"""
        user = anvil.users.login_with_google(remember=True)
        if user:
            Global.user = user
            routing.set_url_hash('homedetail')

    def btn_signin_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.lbl_error = False
        try:
            user = utils.login_with_email(self.tb_email.text, self.tb_password.text)
            if user:
                Global.user = user
                routing.set_url_hash('homedetail')
        except anvil.users.EmailNotConfirmed as e:
            self.lbl_error = "You haven't confirmed your email address. Please check your email and click the confirmation link, or reset your password."
            self.lbl_error.visible = True

    def link_forgot_click(self, **event_args):
        """This method is called when the link is clicked"""
        anvil.users.send_password_reset_email(self.tb_email.text)
        alert(f'please check your email ({self.tb_email.text}) for a password reset link.')

    def link_signup_click(self, **event_args):
        """This method is called when the link is clicked"""
        routing.set_url_hash('signup')
