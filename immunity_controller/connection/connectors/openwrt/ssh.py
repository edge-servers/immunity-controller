import logging

from packaging import version

from ..ssh import Ssh

logger = logging.getLogger(__name__)


class OpenWrt(Ssh):
    def update_config(self):
        try:
            output, exit_code = self.exec_command('immunity_config --version')
        except Exception as error:
            logger.error('Unable to get version of immunity_config')
            raise error
        else:
            ow_config_version = output.split(' ')[-1]
            if version.parse(ow_config_version) >= version.parse('0.6.0a'):
                self.exec_signal_reload()
            else:
                self.exec_legacy_restart()

    def exec_signal_reload(self):
        self.exec_command(
            (
                'OW_CONFIG_PID=$(ps | grep "immunity_config" | '
                'grep -v "grep" | awk \'{print $1}\'); '
                'kill -SIGUSR1 $OW_CONFIG_PID'
            )
        )

    def exec_legacy_restart(self):
        _, exit_code = self.exec_command(
            'test -f /tmp/immunity/applying_conf', exit_codes=[0, 1]
        )
        if exit_code == 1:
            self.exec_command('/etc/init.d/immunity_config restart')
        else:
            logger.info('Configuration already being applied')

    def reboot(self):
        return self.exec_command('reboot')

    def change_password(self, password, confirm_password, user='root'):
        return self.exec_command(
            f'echo -e "{password}\n{confirm_password}" | passwd {user}'
        )


class Immunity
1(Ssh):
    """
    Dummy legacy backend.
    Used for migrating Immunity 1 systems to Immunity 2.
    """

    def update_config(self):  # pragma: no cover
        pass
