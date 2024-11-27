# TODO: move most of this to anvil squared
from anvil.tables import app_tables
import anvil.tables.query as q
# from anvil_squared.helpers import print_timestamp
import anvil.secrets


role_dict = {
    'Member': ['see_profile'],
    'Admin': ['see_profile', 'see_members', 'edit_members', 'delete_members', 'delete_admin', 'edit_roles'],
}

perm_list = []
for key, val in role_dict.items():
    perm_list = perm_list + val

perm_list = list(set(perm_list))


def upsert_role(usertenant, role_name):
    role = app_tables.roles.get(tenant=usertenant['tenant'], name=role_name)
    if not usertenant['roles']:
        usertenant['roles'] = [role]
    elif role not in usertenant['roles']:
        usertenant['roles'] = usertenant['roles'] + [role]
    return usertenant


def remove_role(usertenant, role_names):
    usertenant['roles'] = [i for i in usertenant['roles'] if i['name'] not in role_names]
    if len(usertenant['roles']) == 0:
        # Deal with a quirk of empty lists.
        usertenant['roles'] = None
    return usertenant


def populate_permissions():
    """Populate the permissions table."""
    print_timestamp('populate_permissions')
    if len(app_tables.permissions.search()) == 0:
        for perm in perm_list:
            app_tables.permissions.add_row(name=perm)


def populate_roles(tenant):
    """Some basic roles."""
    print_timestamp('populate_roles')
    
    for key, val in role_dict.items():
        perm_rows = app_tables.permissions.search(name=q.any_of(*val))
        if len(perm_rows) == 0:
            populate_permissions()
            perm_rows = app_tables.permissions.search(name=q.any_of(*val))
            
        is_it_there = app_tables.roles.get(name=key, tenant=tenant)
        if not is_it_there:
            app_tables.roles.add_row(name=key, tenant=tenant, permissions=list(perm_rows), can_edit=False)
    return app_tables.roles.search(tenant=tenant)


def decrypt(something):
    if something:
        return anvil.secrets.decrypt_with_key("encryption_key", something)
    else:
        return ''


def list_to_csv(data):
    """Output a list of dicts to csv."""
    import io
    import csv
    import anvil.media
    
    output = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    # Write the header
    writer.writeheader()
    # Write the data
    for row in data:
        writer.writerow(row)
    # Get the CSV content
    csv_content = output.getvalue()
    # Close the string buffer
    output.close()
    
    # Create a media object from the CSV content
    csv_file = anvil.BlobMedia('text/csv', csv_content.encode('utf-8'), 'data.csv')
    return csv_file


# --------------------
# Return rows as dicts
# --------------------
def usertenant_row_to_dict(row):
    # TODO: generalize and move to anvil squared
    row_dict = {
        'email': row['user']['email'],
        'last_login': row['user']['last_login'],
        'signed_up': row['user']['signed_up'],
        'permissions': get_permissions(None, row['user'], tenant=row['tenant'], usertenant=row),
        'roles': get_user_roles(None, None, row, row['tenant'])
    }
    return row_dict


def role_row_to_dict(role):
    if role['permissions']:
        role_perm = [j['name'] for j in role['permissions']]
    else:
        role_perm = []
    return {
        'name': role['name'],
        'last_update': role['last_update'],
        'guides': app_tables.rolefiles.search(role=role),
        'permissions': role_perm,
        'can_edit': role['can_edit']
    }