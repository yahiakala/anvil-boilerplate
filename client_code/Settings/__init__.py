from ._anvil_designer import SettingsTemplate
import anvil
import anvil.users
from anvil_extras import routing

from .. import Global


@routing.route('settings')
class Settings(SettingsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.admin_data = {}
        self.admin_data['sites'] = ['url 1', 'url 2']
        self.link_portal.url = Global.customer_portal
        if self.link_portal.url:
            self.link_portal.visible = True
        # self.rp_websites.items = self.admin_data['sites']
        # self.user = Global.user

    def btn_chg_pw_click(self, **event_args):
        self.lbl_pw_error.visible = False
        user = Global.user
        if self.tb_oldpw.text and self.tb_newpw.text:
            print('Changing password')
            try:
                anvil.users.reset_password(self.tb_oldpw.text, self.tb_newpw.text)
                self.lbl_pw_error.text = 'Password Changed!'
                self.lbl_pw_error.visible = True
                self.tb_oldpw.text = ''
                self.tb_newpw.text = ''
            except anvil.users.AuthenticationFailed:
                print('Auth failed')
                self.lbl_pw_error.text = 'Old password is incorrect.'
                self.lbl_pw_error.visible = True
            except anvil.users.PasswordNotAcceptable:
                self.lbl_pw_error.text = 'Passwords must be 8 characters or more.'
                self.lbl_pw_error.visible = True
        else:
            self.lbl_pw_error.text = 'Old or new entered password is blank.'
            self.lbl_pw_error.visible = True
        

    def btn_add_mfa_click(self, **event_args):
        """This method is called when the button is clicked"""
        anvil.users.mfa.configure_mfa_with_form(allow_cancel=True)
