from anvil_squared.globals import GlobalCache

_global_dict = {
    "user": None,
    "is_mobile": None,
    "customer_portal": None,
    "tenant": None,
    "tenant_id": None,
}

_tenanted_dict = {"permissions": None, "usertenant": None}

Global = GlobalCache(_global_dict, _tenanted_dict)

AppName = "SaaS Boilerplate"
