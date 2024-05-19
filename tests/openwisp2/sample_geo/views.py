from immunity_controller.geo.api.views import (
    DeviceCoordinatesView as BaseDeviceCoordinatesView,
)
from immunity_controller.geo.api.views import (
    DeviceLocationView as BaseDeviceLocationView,
)
from immunity_controller.geo.api.views import (
    FloorPlanDetailView as BaseFloorPlanDetailView,
)
from immunity_controller.geo.api.views import (
    FloorPlanListCreateView as BaseFloorPlanListCreateView,
)
from immunity_controller.geo.api.views import (
    GeoJsonLocationList as BaseGeoJsonLocationList,
)
from immunity_controller.geo.api.views import (
    LocationDetailView as BaseLocationDetailView,
)
from immunity_controller.geo.api.views import (
    LocationDeviceList as BaseLocationDeviceList,
)
from immunity_controller.geo.api.views import (
    LocationListCreateView as BaseLocationListCreateView,
)


class DeviceCoordinatesView(BaseDeviceCoordinatesView):
    pass


class DeviceLocationView(BaseDeviceLocationView):
    pass


class GeoJsonLocationList(BaseGeoJsonLocationList):
    pass


class LocationDeviceList(BaseLocationDeviceList):
    pass


class FloorPlanListCreateView(BaseFloorPlanListCreateView):
    pass


class FloorPlanDetailView(BaseFloorPlanDetailView):
    pass


class LocationListCreateView(BaseLocationListCreateView):
    pass


class LocationDetailView(BaseLocationDetailView):
    pass


device_coordinates = DeviceCoordinatesView.as_view()
device_location = DeviceLocationView.as_view()
geojson = GeoJsonLocationList.as_view()
location_device_list = LocationDeviceList.as_view()
list_floorplan = FloorPlanListCreateView.as_view()
detail_floorplan = FloorPlanDetailView.as_view()
list_location = LocationListCreateView.as_view()
detail_location = LocationDetailView.as_view()
