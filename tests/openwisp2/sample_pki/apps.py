from immunity_controller.pki.apps import PkiConfig


class SamplePkiConfig(PkiConfig):
    name = 'immunity22.sample_pki'
    label = 'sample_pki'


del PkiConfig
