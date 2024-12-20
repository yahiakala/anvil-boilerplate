import anvil.server

# from routing.router import TemplateWithContainerRoute as BaseRoute
from routing.router import Redirect, Route

from .Global import Global


class EnsureUserMixin:
    def before_load(self, **loader_args):
        if not Global.user:
            raise Redirect(path="/signin")
        if Global.user and Global.get_s("tenant") is None:
            Global.tenant = anvil.server.call("get_tenant_single_squared")
            if Global.get_s("tenant") is None:
                Global.tenant = anvil.server.call("create_tenant_single")
            try:
                Global.tenant_id = Global.tenant.get_id()
            except Exception:
                Global.tenant_id = Global.tenant["id"]
            print(Global.permissions)
            print(Global.tenant)
            if "delete_members" in Global.permissions and (
                Global.tenant["name"] is None or Global.tenant["name"] == ""
            ):
                raise Redirect(path="/app/admin")


class SignRoute(Route):
    # template = "Templates.Static"
    path = "/"
    form = "Auth.Sign"
    cache_form = True


class SigninRoute(Route):
    # template = "Templates.Static"
    path = "/signin"
    form = "Auth.Signin"
    cache_form = True


class SignupRoute(Route):
    # template = "Templates.Static"
    path = "/signup"
    form = "Auth.Signup"
    cache_form = True


class HomeRoute(EnsureUserMixin, Route):
    # template = "Templates.Router"
    path = "/app/home"
    form = "App.Home"
    cache_form = True


class SettingsRoute(EnsureUserMixin, Route):
    # template = "Templates.Router"
    path = "/app/settings"
    form = "App.Settings"
    cache_form = True


class AdminRoute(EnsureUserMixin, Route):
    # template = "Templates.Router"
    path = "/app/admin"
    form = "App.Admin"
    cache_form = True


class TestsRoute(EnsureUserMixin, Route):
    # template = "Templates.Router"
    path = "/app/tests"
    form = "App.Tests"
    cache_form = True
