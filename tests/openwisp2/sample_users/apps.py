from immunity_users.apps import ImmunityUsersConfig


class SampleUsersConfig(ImmunityUsersConfig):
    name = 'immunity22.sample_users'
    label = 'sample_users'


del ImmunityUsersConfig
