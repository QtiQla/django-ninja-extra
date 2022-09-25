import typing as t
from unittest import mock

from injector import Binder, Injector, Module
from django.apps import apps
from ninja_extra.modules import NinjaExtraModule
from ninja_extra.dependency_resolver import (
    get_injector,
    register_injector_modules,
    service_resolver,
)


class MyServiceModule(Module):
    def configure(self, binder: Binder) -> None:
        pass


class Service1:
    pass


class Service2:
    pass


def test_get_injector():
    injector = get_injector()
    assert isinstance(injector, Injector)


def test_service_resolver_returns_object_or_list_or_objects():
    service1 = service_resolver(Service1)
    assert isinstance(service1, Service1)

    service1, service2 = service_resolver(Service1, Service2)
    assert isinstance(service1, Service1)
    assert isinstance(service2, Service2)


def test_register_injector_modules_works():
    with mock.patch.object(MyServiceModule, "configure") as mock_configure:
        register_injector_modules(MyServiceModule)
        assert mock_configure.call_count == 1


def test_ninja_default_module_get_context():
    app = t.cast(t.Any, apps.get_app_config("ninja_extra"))
    assert isinstance(app.ninja_extra_module, NinjaExtraModule)

    assert app.ninja_extra_module.get_route_context() is None
    route_context = mock.Mock()
    app.ninja_extra_module.set_route_context(route_context)

    assert app.ninja_extra_module.get_route_context() is route_context
