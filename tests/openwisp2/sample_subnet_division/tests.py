from immunity_controller.subnet_division.tests.test_admin import (
    TestDeviceAdmin as BaseTestDeviceAdmin,
)
from immunity_controller.subnet_division.tests.test_admin import (
    TestIPAdmin as BaseTestIPAdmin,
)
from immunity_controller.subnet_division.tests.test_admin import (
    TestSubnetAdmin as BaseTestSubnetAdmin,
)
from immunity_controller.subnet_division.tests.test_models import (
    TestSubnetDivisionRule as BaseTestSubnetDivisionRule,
)


class TestDeviceAdmin(BaseTestDeviceAdmin):
    config_label = 'sample_config'


class TestSubnetAdmin(BaseTestSubnetAdmin):
    config_label = 'sample_config'


class TestSubnetDivsionRule(BaseTestSubnetDivisionRule):
    pass


class TestIPAdmin(BaseTestIPAdmin):
    pass


del BaseTestDeviceAdmin
del BaseTestSubnetAdmin
del BaseTestSubnetDivisionRule
del BaseTestIPAdmin
