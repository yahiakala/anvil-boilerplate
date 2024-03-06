import anvil

from anvil_extras import routing

from .Router import Router
from .HomeAnon import HomeAnon
from .BlankTemplate import BlankTemplate

hash, pattern, dict = routing.get_url_components()

print(hash)
print(pattern)
routing.set_url_hash(hash)

routing.launch()