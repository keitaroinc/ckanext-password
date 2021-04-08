"""
Copyright (c) 2017 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
        '^((?=.*\d)(?=.*[a-z])(?=.*[A-Z])|(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*])|(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*])|(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*])).{8,16}$'
    )
    match = re.match(regex, password)
    if match is None:
        log.error('Detected weak password. Aborting user registration.')
        return False
    return True

