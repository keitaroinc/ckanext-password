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
import ckan.logic as l
import ckanext.password.helpers as _h
from ckan.common import _

try:
    # CKAN 2.7 and later
    from ckan.common import config
except ImportError:
    # CKAN 2.6 and earlier
    from pylons import config

log = logging.getLogger(__name__)


def user_create(context, data_dict):
    password = data_dict.get('password1', '')
    if 'password' in data_dict:
        password = data_dict['password']

    valid = _h.validate_password(password)
    if not valid:
        msg = config.get('ckanext.password.invalid_password_message', None)
        if msg is None:
            msg = _('Password must consist of at least 8 characters and at least three of following four character \
                     types: Uppercase letter, Lowercase letter, Number, Special characters: !, @, #, $, %, ^, &, *.')
        raise l.ValidationError({'password': [msg]})
    return l.action.create.user_create(context, data_dict)


def user_update(context, data_dict):
    password = data_dict.get('password1', '')
    if 'password' in data_dict:
        password = data_dict['password']

    if password != '':
        valid = _h.validate_password(password)
        if not valid:
            msg = config.get('ckanext.password.invalid_password_message', None)
            if msg is None:
                msg = _('Password must consist of at least 8 characters and at least three of following four character \
                     types: Uppercase letter, Lowercase letter, Number, Special characters: !, @, #, $, %, ^, &, *.')
            raise l.ValidationError({'password': [msg]})
    return l.action.update.user_update(context, data_dict)

