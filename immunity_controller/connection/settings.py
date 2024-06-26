from django.conf import settings

DEFAULT_CONNECTORS = (
    ('immunity_controller.connection.connectors.ssh.Ssh', 'SSH'),
    (
        'immunity_controller.connection.connectors.openwrt.snmp.OpenWRTSnmp',
        'OpenWRT SNMP',
    ),
    (
        'immunity_controller.connection.connectors.airos.snmp.AirOsSnmp',
        'Ubiquiti AirOS SNMP',
    ),
)

CONNECTORS = getattr(settings, 'IMMUNITY_CONNECTORS', DEFAULT_CONNECTORS)

DEFAULT_UPDATE_STRATEGIES = (
    ('immunity_controller.connection.connectors.openwrt.ssh.OpenWrt', 'OpenWRT SSH'),
    (
        'immunity_controller.connection.connectors.openwrt.ssh.Immunity',
        'Immunity 1.x SSH',
    ),
)

UPDATE_STRATEGIES = getattr(
    settings, 'IMMUNITY_UPDATE_STRATEGIES', DEFAULT_UPDATE_STRATEGIES
)

CONFIG_UPDATE_MAPPING = getattr(
    settings,
    'IMMUNITY_CONFIG_UPDATE_MAPPING',
    {
        'netjsonconfig.OpenWrt': DEFAULT_UPDATE_STRATEGIES[0][0],
        'netjsonconfig.Immunity': DEFAULT_UPDATE_STRATEGIES[1][0],
    },
)

SSH_AUTH_TIMEOUT = getattr(settings, 'IMMUNITY_SSH_AUTH_TIMEOUT', 2)
SSH_BANNER_TIMEOUT = getattr(settings, 'IMMUNITY_SSH_BANNER_TIMEOUT', 60)
SSH_COMMAND_TIMEOUT = getattr(settings, 'IMMUNITY_SSH_COMMAND_TIMEOUT', 30)
SSH_CONNECTION_TIMEOUT = getattr(settings, 'IMMUNITY_SSH_CONNECTION_TIMEOUT', 5)

# this may get overridden by immunity-monitoring
UPDATE_CONFIG_MODEL = getattr(settings, 'IMMUNITY_UPDATE_CONFIG_MODEL', 'config.Device')
USER_COMMANDS = getattr(settings, 'IMMUNITY_CONTROLLER_USER_COMMANDS', [])
ORGANIZATION_ENABLED_COMMANDS = getattr(
    settings, 'IMMUNITY_CONTROLLER_ORGANIZATION_ENABLED_COMMANDS', {'__all__': '*'}
)
MANAGEMENT_IP_ONLY = getattr(settings, 'IMMUNITY_CONTROLLER_MANAGEMENT_IP_ONLY', True)
