from ._anvil_designer import SigninTemplate
from anvil import *
import anvil.users
import time
from anvil_extras import routing

from .. import utils
from .. import Global


# @routing.route('', template='Static')
@routing.route('signin', template='Static', url_keys=[routing.ANY])
class Signin(SigninTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.user = Global.user
        self.route_user()

        is_mobile = anvil.js.window.navigator.userAgent.lower().find("mobi") > -1
        if is_mobile:
            self.spacer_1.visible = False
            self.cp_login.role = 'tonal-card'
    
    def form_show(self, **event_args):
        time.sleep(0.3)  # Hack around weird initialization of flowpanel
        # self.fp_outer.visible = True

    def route_user(self, **event_args):
        """Send the user on their way."""
        if 'redirect' in self.url_dict and self.user:
            self.tb_email.text = ''
            self.tb_password.text = ''
            Global.user = self.user
            anvil.js.window.location.href = self.url_dict['redirect']
        elif self.user:
            self.tb_email.text = ''
            self.tb_password.text = ''
            Global.user = self.user
            routing.set_url_hash('app')
    
    def btn_google_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Note: if user does not exist, it just creates a user.
        self.user = anvil.users.login_with_google(remember=True)
        self.route_user()

    def link_forgot_click(self, **event_args):
        """This method is called when the link is clicked"""
        if not self.tb_email.text:
            self.lbl_error.text = 'Please enter a valid email.'
            self.lbl_error.visible = True
        else:
            anvil.users.send_password_reset_email(self.tb_email.text)
            self.lbl_error.text = f'Please check your email ({self.tb_email.text}) for a password reset link.'
            self.lbl_error.visible = True

    def link_signup_click(self, **event_args):
        """This method is called when the link is clicked"""
        routing.set_url_hash(url_pattern='signup', url_dict=self.url_dict)

    def btn_signin_click_custom(self, **event_args):
        """This method is called when the button is clicked"""
        self.lbl_error.visible = False
        self.user = anvil.users.get_user(allow_remembered=True)
        email = self.tb_email.text
        password = self.tb_password.text
        if self.user:
            self.route_user()
        else:
            try:
                self.user = anvil.server.call('login_with_email_custom', email, password)
                # self.user = anvil.users.login_with_email(email, password, remember=True)
                self.route_user()
            except anvil.users.MFARequired as e:
                r = anvil.users.mfa.mfa_login_with_form(email, password)
                if r == 'reset_mfa':
                    anvil.users.mfa.send_mfa_reset_email(email)
                    self.lbl_error.text = "Requested 2-factor authentication reset for " + email + ". Check your email."
                elif r == None:
                    self.lbl_error.text = "Cancelled login."
                else:
                    self.user = anvil.users.login_with_email(email, password, mfa=r, remember=True)
                    self.route_user()
            except anvil.users.AuthenticationFailed as e:
                self.lbl_error.text = e.args[0]
                self.lbl_error.visible = True
            except anvil.users.EmailNotConfirmed as e:
                self.lbl_error.text = "You haven't confirmed your email address. Please check your email and click the confirmation link, or reset your password."
                self.lbl_error.visible = True
            except anvil.users.TooManyPasswordFailures as e:
                self.lbl_error.text = e.args[0]
                self.lbl_error.visible = True

    def link_help_click(self, **event_args):
        """This method is called when the link is clicked"""
        alert("Email support@dreambyte.ai and we'll get back to you within 24-48 hours.")
