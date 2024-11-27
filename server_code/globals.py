import anvil.server
import anvil.tables.query as q
import anvil.users
from anvil.tables import app_tables
from anvil_squared.helpers import print_timestamp

from .helpers import get_permissions, usertenant_row_to_dict, validate_user

import anvil_squared.multi_tenant as mt

# --------------------
# Non tenanted globals
# --------------------
@anvil.server.callable(require_user=True)
def get_data(key):
    print_timestamp(f"get_data: {key}")
    # user = anvil.users.get_user(allow_remembered=True)
    if key == "all_permissions":
        return mt.authorization.get_all_permissions()


# ----------------
# Tenanted globals
# ----------------
@anvil.server.callable(require_user=True)
def get_tenanted_data(tenant_id, key):
    print_timestamp(f"get_tenanted_data: {key}")
    user = anvil.users.get_user(allow_remembered=True)

    if key == "users":
        return get_users_iterable(tenant_id, user)
    elif key == "permissions":
        return get_permissions(tenant_id, user)
    elif key == "usertenant":
        return get_usertenant_dict(tenant_id, user)


def get_users_iterable(tenant_id, user):
    """Get an iterable of the users."""
    tenant, usertenant, permissions = validate_user(tenant_id, user)
    if "see_members" not in permissions:
        return []
    return app_tables.usertenant.client_readable(
        q.only_cols("user"),
        tenant=tenant
    )


def get_usertenant_dict(tenant_id, user):
    """Get user tenant data including Notion settings"""
    tenant, usertenant, permissions = validate_user(tenant_id, user)

    data = usertenant_row_to_dict(usertenant)
    return data
