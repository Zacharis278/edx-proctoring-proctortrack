"""
Base implementation of a REST backend, following the API documented in
docs/backends.rst
"""
from edx_proctoring.backends.rest import BaseRestProctoringProvider


class ProctortrackBackendProvider(BaseRestProctoringProvider):
    """
    Base class for official REST API proctoring service.
    Subclasses must override base_url and may override the other url
    properties
    """
    base_url = 'https://prestaging.verificient.com'

    @property
    def instructor_url(self):
        "Returns the instructor dashboard url"
        return self.base_url + u'/launch/edx/instructor/{client_id}/?jwt={jwt}'

    def __init__(self, client_id=None, client_secret=None, **kwargs):
        """
        Initialize REST backend.
        client_id: provided by backend service
        client_secret: provided by backend service
        """
        super(ProctortrackBackendProvider, self).__init__(**kwargs)
        self.session.oauth_uri = '/edx/oauth2/access_token'

