import dataclasses
import inspect
from functools import partial
from typing import Any, Callable, Dict, List, Tuple, Type, TypeVar, cast

from fastapi.routing import APIRouter

from .route_args import EndpointDefinition, EndpointType

AnyCallable = TypeVar('AnyCallable', bound=Callable[..., Any])


class RoutableMeta(type):
    """This is a meta-class that converts all the methods that were marked by a route/path decorator into values on a
    class member called _endpoints that the Routable constructor then uses to add the endpoints to its router."""
    def __new__(cls: Type[type], name: str, bases: Tuple[Type[Any]], attrs: Dict[str, Any]) -> 'RoutableMeta':
        endpoints: List[EndpointDefinition] = []
        for v in attrs.values():
            if inspect.isfunction(v) and hasattr(v, '_endpoint'):
                endpoints.append(v._endpoint)
        attrs['_endpoints'] = endpoints
        return cast(RoutableMeta, type.__new__(cls, name, bases, attrs))


class Routable(metaclass=RoutableMeta):
    """Base class for all classes the want class-based routing.

    This Uses RoutableMeta as a metaclass and various decorators like @get or @post from the decorators module. The
    decorators just mark a method as an endpoint. The RoutableMeta then converts those to a list of desired endpoints in
    the _endpoints class method during class creation. The constructor constructs an APIRouter and adds all the routes
    in the _endpoints to it so they can be added to an app via FastAPI.include_router or similar.
    """
    _endpoints: List[EndpointDefinition] = []

    def __init__(self, *args, **kwargs) -> None:
        self.router = APIRouter(*args, **kwargs)
        for endpoint in self._endpoints:
            if endpoint.type() == EndpointType.WEBSOCKET:
                self.router.add_api_websocket_route(path=endpoint.args.path,
                                                    endpoint=partial(endpoint.endpoint, self),
                                                    name=endpoint.args.name)
            else:
                self.router.add_api_route(endpoint=partial(endpoint.endpoint, self),
                                          **dataclasses.asdict(endpoint.args))
