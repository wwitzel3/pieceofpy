from objects import (
    ThirdPartyObject,
    third_party_adapter,
    )

from pyramid.renderers import JSON
from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('custom_object', '/custom_object.json')

    json_third_party = JSON()
    json_third_party.add_adapter(ThirdPartyObject, third_party_adapter)
    config.add_renderer('json_third_party', json_third_party)
    config.add_route('third_party', '/third_party.json')

    config.scan()
    return config.make_wsgi_app()
