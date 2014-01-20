from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig as SessionFactory

from sqlalchemy import engine_from_config

import restauth

from .models import DBSession, Base


from pyramid.asset import resolve_asset_spec

def do(spec):
    name = resolve_asset_spec(spec)[0]
    return __import__(name, globals(), locals())


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    # SQLA
    # ====
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    # Configurator
    # ============
    config = Configurator(settings=settings,
                    session_factory=SessionFactory('pyramid_backbone_simple'))
    config.include('pyramid_chameleon')
    
    # Authentication API
    # ==================
    # Note: Can I put this elsewhere? This is a little Pylons-ish
    #   (except the config isn't global.)
    rest_auth = restauth.PyramidAuthApiServer(
                    'server1',
                    remotes={'client1': '12345'},
                    passes=10)
    config.add_settings({'auth_api': rest_auth})
    
    config.add_view(restauth.ping_view(), route_name='api_ping',
                    request_method='GET', renderer='json')

    # Routes
    # ======
    # Users RESTful API
    config.add_route('api_ping', '/api/v1/ping')
    config.add_route('api_users', '/api/v1/users')
    config.add_route('api_user', '/api/v1/users/{id}')

    # Site pages.
    config.add_route('site_index', '/')
    config.add_route('site_users', '/users')

    # Static Views
    config.add_static_view('/js/lib', path='_js:lib', cache_max_age=3660)
    config.add_static_view('/js/site', path='_js:site', cache_max_age=0)
    config.add_static_view('/js/tmpl', path='_templates:backbone', cache_max_age=0)


    config.scan()



    return config.make_wsgi_app()