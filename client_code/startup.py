import anvil

from anvil_extras import routing

from .Router import Router
from .BlankTemplate import BlankTemplate
from .Static import Static

@routing.redirect(path="app", priority=20, condition=lambda: Globals.user is None)
def redirect_no_user():
    return "sign"

hash, pattern, dict = routing.get_url_components()

routing.set_url_hash(hash)

routing.launch()