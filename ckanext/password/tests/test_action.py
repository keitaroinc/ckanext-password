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

from nose.tools import assert_raises

from ckan.tests import helpers, factories
from ckan import plugins
from ckan import logic


class ActionBase(object):
    @classmethod
    def setup_class(self):
        if not plugins.plugin_loaded('custom_password_criteria'):
            plugins.load('custom_password_criteria')

    def setup(self):
        helpers.reset_db()

    @classmethod
    def teardown_class(self):
        if plugins.plugin_loaded('custom_password_criteria'):
            plugins.unload('custom_password_criteria')

class TestCalendarActions(ActionBase):
    def test_create_user_with_invalid_password(self):
        pass

    def test_create_user_with_valid_password(self):
        pass