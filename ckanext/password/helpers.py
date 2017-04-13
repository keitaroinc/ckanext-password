# -*- coding: utf-8 -
import logging
import re

try:
    # CKAN 2.7 and later
    from ckan.common import config
except ImportError:
    # CKAN 2.6 and earlier
    from pylons import config

log = logging.getLogger(__name__)


def validate_password(password):
    # Validate password with regex
    regex = config.get(
        'ckanext.password.password_regex',
        '^([a-zA-Z0-9!@#$%^&*]{8,15})$'
    )
    match = re.match(regex, password)
    if match is None:
        log.error('Detected weak password. Aborting user registration.')
        return False
    return True
