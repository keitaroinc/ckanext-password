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