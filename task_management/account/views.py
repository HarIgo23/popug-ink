import os

from authlib.integrations.django_client import OAuth

ruby_oauth = {
    'name': 'ruby_oauth',
    'client_id': os.environ.get("OAUTH_CLIENT_ID"),
    'client_secret': os.environ.get("OAUTH_CLIENT_SECRET"),
    'request_token_url': os.environ.get("OAUTH_REQUEST_URL"),
    'request_token_params': None,
    'access_token_url': os.environ.get("OAUTH_ACCESS_URL"),
    'access_token_params': None,
    'refresh_token_url': None,
    'authorize_url': os.environ.get("OAUTH_AUTH_URL"),
    'api_base_url': os.environ.get("OAUTH_API_BASE"),
    'client_kwargs': None
}

oauth = OAuth()
oauth.register(
    name=ruby_oauth['name'],
    client_id=ruby_oauth['client_id'],
    client_secret=ruby_oauth['client_secret'],
    access_token_url=ruby_oauth['access_token_url'],
    authorize_url=ruby_oauth['authorize_url'],
)


def login(request):
    redirect_uri = request.build_absolute_uri('/authorize')
    return oauth.ruby_oauth.authorize_redirect(request, redirect_uri)


def authorize(request):
    token = oauth.ruby_oauth.authorize_access_token(request)
    resp = oauth.ruby_oauth.get('user', token=token)
    resp.raise_for_status()
    profile = resp.json()
    print(profile)
    # do something with the token and profile
    return '...'
