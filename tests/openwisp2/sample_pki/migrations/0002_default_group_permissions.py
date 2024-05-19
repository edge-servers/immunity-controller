from django.db import migrations

from immunity_controller.pki.migrations import assign_permissions_to_groups


class Migration(migrations.Migration):
    dependencies = [('sample_pki', '0001_initial')]

    operations = [
        migrations.RunPython(
            assign_permissions_to_groups, reverse_code=migrations.RunPython.noop
        )
    ]
