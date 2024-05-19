from openwisp_users.apps import OpenwispUsersConfig


class SampleUsersConfig(OpenwispUsersConfig):
    name = 'immunity22.sample_users'
    label = 'sample_users'


del OpenwispUsersConfig
