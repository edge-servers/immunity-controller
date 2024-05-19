from openwisp_controller.config.apps import ConfigConfig


class SampleConfigConfig(ConfigConfig):
    name = 'immunity22.sample_config'
    label = 'sample_config'


del ConfigConfig
