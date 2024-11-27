import anvil.server
import anvil.users
from anvil.tables import app_tables

from .globals import get_tenant_single
from .helpers import populate_roles, usertenant_row_to_dict, validate_user


@anvil.server.callable(require_user=True)
def create_tenant_single():
    """Create a tenant."""
    # TODO: move to anvil squared, generalize
    user = anvil.users.get_user(allow_remembered=True)
    if len(app_tables.tenants.search()) != 0:
        return None

    tenant = app_tables.tenants.add_row(name="Main", new_roles=["Member"])
    _ = populate_roles(tenant)
    admin_role = app_tables.roles.get(tenant=tenant, name="Admin")
    _ = app_tables.usertenant.add_row(tenant=tenant, user=user, roles=[admin_role])
    return get_tenant_single(user, tenant)


@anvil.server.callable(require_user=True)
def impersonate_user(email):
    # TODO: validate user.
    # TODO: move to anvil squared
    new_user = app_tables.users.get(email=email)
    anvil.users.force_login(new_user)
    return new_user