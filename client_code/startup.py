import anvil

from anvil_extras import routing

from .Router import Router
from .HomeAnon import HomeAnon


hash, pattern, dict = routing.get_url_components()

routing.set_url_hash(hash)

routing.launch()