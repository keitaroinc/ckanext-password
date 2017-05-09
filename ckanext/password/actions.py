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
            msg = _('Password must consist of 8-16 alphanumeric characters, contain at least one uppercase \
                    letter and at least one of the following special characters: !, @, #, $, %, ^, &, *.')
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
                msg = _('Password must consist of 8-16 alphanumeric characters, contain at least one uppercase \
                        letter and at least one of the following special characters: !, @, #, $, %, ^, &, *.')
            raise l.ValidationError({'password': [msg]})
    return l.action.update.user_update(context, data_dict)
