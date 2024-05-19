from immunity_users.tests.test_admin import TestUsersAdmin

from .mixins import GetEditFormInlineMixin


class TestUsersIntegration(GetEditFormInlineMixin, TestUsersAdmin):
    """
    tests integration with immunity_users
    """

    is_integration_test = True


del TestUsersAdmin
