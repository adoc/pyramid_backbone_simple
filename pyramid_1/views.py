from pyramid.response import Response
from pyramid.view import view_config
import pyramid.httpexceptions as exc

import transaction

from sqlalchemy.exc import DBAPIError

from .models import DBSession, MyModel


def DBCommit():
    try:
        transaction.commit()
    except DBAPIError:
        transaction.rollback()
        raise
    else:
        return True


@view_config(route_name='users', request_method='GET', renderer='json')
def users_get(request):
    """Query and return a list of users."""

    users = DBSession.query(MyModel).all()
    return [{'id': user.id, 'name': user.name, 'value': user.value} for user in
                users]


@view_config(route_name='users', request_method='POST', renderer='json')
def users_post(request):
    """Create a new user."""

    name = request.params['name']    
    value = int(request.params['value'])
    user = MyModel(name=name, value=value)
    DBSession.add(user)
    return True


@view_config(route_name='user', request_method='GET', renderer='json')
def user_get(request):
    """Get a specific user by `id`."""

    id_ = int(request.matchdict['id'])
    user = DBSession.query(MyModel).get(id_)
    return {'id': user.id, 'name': user.name, 'value': user.value}


@view_config(route_name='user', request_method='PUT', renderer='json')
def user_put(request):
    """Update an existing user with `id`"""

    id_ = int(request.matchdict['id'])
    name = request.params['name']
    value = request.params['value']
    user = DBSession.query(MyModel).get(id_)
    user.name = name
    user.value = value
    DBSession.add(user)
    DBCommit()
    return True


@view_config(route_name='user', request_method='DELETE', renderer='json')
def user_delete(request):
    """Delete a user with `id`."""

    id_ = int(request.matchdict['id'])
    user = DBSession.query(MyModel).get(id_)
    DBSession.delete(user)
    DBCommit()
    return True