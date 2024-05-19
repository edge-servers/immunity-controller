from immunity_users.api.mixins import FilterByOrganizationManaged
from immunity_users.api.mixins import ProtectedAPIMixin as BaseProtectedAPIMixin


class ProtectedAPIMixin(BaseProtectedAPIMixin, FilterByOrganizationManaged):
    pass
