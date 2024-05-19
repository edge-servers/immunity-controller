from openwisp_controller.connection.apps import ConnectionConfig


class SampleConnectionConfig(ConnectionConfig):
    name = 'immunity22.sample_connection'
    label = 'sample_connection'


del ConnectionConfig
