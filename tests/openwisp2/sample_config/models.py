from django.db import models

from immunity_controller.config.base.config import AbstractConfig
from immunity_controller.config.base.device import AbstractDevice
from immunity_controller.config.base.device_group import AbstractDeviceGroup
from immunity_controller.config.base.multitenancy import (
    AbstractOrganizationConfigSettings,
    AbstractOrganizationLimits,
)
from immunity_controller.config.base.tag import (
    AbstractTaggedTemplate,
    AbstractTemplateTag,
)
from immunity_controller.config.base.template import AbstractTemplate
from immunity_controller.config.base.vpn import AbstractVpn, AbstractVpnClient


class DetailsModel(models.Model):
    details = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        abstract = True


class Device(DetailsModel, AbstractDevice):
    """
    Concrete Device model
    """

    class Meta(AbstractDevice.Meta):
        abstract = False


class DeviceGroup(DetailsModel, AbstractDeviceGroup):
    """
    Concrete Device model
    """

    class Meta(AbstractDeviceGroup.Meta):
        abstract = False


class Config(DetailsModel, AbstractConfig):
    """
    Concrete Config model
    """

    class Meta(AbstractConfig.Meta):
        abstract = False


class TemplateTag(DetailsModel, AbstractTemplateTag):
    """
    immunity-controller TemplateTag model
    """

    class Meta(AbstractTemplateTag.Meta):
        abstract = False


class TaggedTemplate(DetailsModel, AbstractTaggedTemplate):
    """
    immunity-controller TaggedTemplate model
    """

    class Meta(AbstractTaggedTemplate.Meta):
        abstract = False


class Template(DetailsModel, AbstractTemplate):
    """
    immunity-controller Template model
    """

    class Meta(AbstractTemplate.Meta):
        abstract = False


class Vpn(DetailsModel, AbstractVpn):
    """
    immunity-controller VPN model
    """

    class Meta(AbstractVpn.Meta):
        abstract = False


class VpnClient(DetailsModel, AbstractVpnClient):
    """
    m2m through model
    """

    class Meta(AbstractVpnClient.Meta):
        abstract = False


class OrganizationConfigSettings(DetailsModel, AbstractOrganizationConfigSettings):
    """
    Configuration management settings
    specific to each organization
    """

    class Meta(AbstractOrganizationConfigSettings.Meta):
        abstract = False


class OrganizationLimits(DetailsModel, AbstractOrganizationLimits):
    """
    Number of allowed devices specific to each organization
    """

    class Meta(AbstractOrganizationLimits.Meta):
        abstract = False
