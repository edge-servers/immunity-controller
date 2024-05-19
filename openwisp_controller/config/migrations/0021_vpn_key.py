# Generated by Django 2.1.8 on 2019-04-22 23:55

import re

import django.core.validators
from django.db import migrations

import immunity_utils.base
import immunity_utils.utils


class Migration(migrations.Migration):

    dependencies = [('config', '0020_remove_config_organization')]

    operations = [
        migrations.AddField(
            model_name='vpn',
            name='key',
            field=immunity_utils.base.KeyField(
                db_index=True,
                default=immunity_utils.utils.get_random_key,
                help_text=None,
                max_length=64,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile('^[^\\s/\\.]+$'),
                        code='invalid',
                        message='This value must not contain spaces, dots or slashes.',
                    )
                ],
            ),
        )
    ]
