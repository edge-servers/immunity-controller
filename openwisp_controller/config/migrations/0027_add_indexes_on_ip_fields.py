# Generated by Django 3.0.4 on 2020-04-15 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('config', '0026_hardware_id_not_unique')]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='last_ip',
            field=models.GenericIPAddressField(
                blank=True,
                db_index=True,
                help_text=(
                    'indicates the IP address logged from the '
                    'last request coming from the device'
                ),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='device',
            name='management_ip',
            field=models.GenericIPAddressField(
                blank=True,
                db_index=True,
                help_text=(
                    'IP address used by Immunity to reach the device when '
                    'performing any type of push operation or active check. The '
                    'value of this field is generally sent by the device and hence '
                    'does not need to be changed, but can be changed or cleared '
                    'manually if needed.'
                ),
                null=True,
            ),
        ),
    ]
