from django.db import migrations

from immunity_controller.geo.migrations import assign_permissions_to_groups


class Migration(migrations.Migration):
    dependencies = [('sample_geo', '0001_initial')]

    operations = [
        migrations.RunPython(
            assign_permissions_to_groups, reverse_code=migrations.RunPython.noop
        )
    ]
