from immunity_controller.config.tests.test_admin import TestAdmin as BaseTestAdmin
from immunity_controller.config.tests.test_admin import (
    TestDeviceGroupAdmin as BaseTestDeviceGroupAdmin,
)
from immunity_controller.config.tests.test_api import TestConfigApi as BaseTestConfigApi
from immunity_controller.config.tests.test_apps import TestApps as BaseTestApps
from immunity_controller.config.tests.test_config import TestConfig as BaseTestConfig
from immunity_controller.config.tests.test_config import (
    TestTransactionConfig as BaseTestTransactionConfig,
)
from immunity_controller.config.tests.test_controller import (
    TestController as BaseTestController,
)
from immunity_controller.config.tests.test_device import TestDevice as BaseTestDevice
from immunity_controller.config.tests.test_device_group import (
    TestDeviceGroup as BaseTestDeviceGroup,
)
from immunity_controller.config.tests.test_notifications import (
    TestNotifications as BaseTestNotifications,
)
from immunity_controller.config.tests.test_tag import TestTag as BaseTestTag
from immunity_controller.config.tests.test_template import (
    TestTemplate as BaseTestTemplate,
)
from immunity_controller.config.tests.test_template import (
    TestTemplateTransaction as BaseTestTemplateTransaction,
)
from immunity_controller.config.tests.test_views import TestViews as BaseTestViews
from immunity_controller.config.tests.test_vpn import TestVpn as BaseTestVpn
from immunity_controller.config.tests.test_vpn import (
    TestVpnTransaction as BaseTestVpnTransaction,
)
from immunity_controller.config.tests.test_vpn import TestVxlan as BaseTestVxlan
from immunity_controller.config.tests.test_vpn import TestWireguard as BaseTestWireguard


class TestAdmin(BaseTestAdmin):
    app_label = 'sample_config'


class TestDeviceGroupAdmin(BaseTestDeviceGroupAdmin):
    app_label = 'sample_config'


class TestConfig(BaseTestConfig):
    pass


class TestTransactionConfig(BaseTestTransactionConfig):
    pass


class TestController(BaseTestController):
    pass


class TestDevice(BaseTestDevice):
    pass


class TestDeviceGroup(BaseTestDeviceGroup):
    pass


class TestTag(BaseTestTag):
    pass


class TestTemplate(BaseTestTemplate):
    pass


class TestTemplateTransaction(BaseTestTemplateTransaction):
    pass


class TestNotifications(BaseTestNotifications):
    app_label = 'sample_config'


class TestViews(BaseTestViews):
    pass


class TestVpn(BaseTestVpn):
    pass


class TestVpnTransaction(BaseTestVpnTransaction):
    pass


class TestApps(BaseTestApps):
    pass


class TestConfigApi(BaseTestConfigApi):
    pass


class TestWireguard(BaseTestWireguard):
    pass


class TestVxlan(BaseTestVxlan):
    pass


del BaseTestAdmin
del BaseTestDeviceGroupAdmin
del BaseTestConfig
del BaseTestTransactionConfig
del BaseTestController
del BaseTestDevice
del BaseTestDeviceGroup
del BaseTestTag
del BaseTestTemplate
del BaseTestTemplateTransaction
del BaseTestNotifications
del BaseTestViews
del BaseTestVpn
del BaseTestVpnTransaction
del BaseTestApps
del BaseTestConfigApi
del BaseTestWireguard
del BaseTestVxlan
