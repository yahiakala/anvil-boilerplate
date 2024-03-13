import anvil

from anvil_extras import routing

from .Router import Router
from .BlankTemplate import BlankTemplate
from .Static import Static

hash, pattern, dict = routing.get_url_components()

routing.set_url_hash(hash)

routing.launch()