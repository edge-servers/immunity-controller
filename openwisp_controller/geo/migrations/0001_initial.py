# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 16:35
import uuid

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import django.utils.timezone
import django_loci.storage
import model_utils.fields
import swapper
from django.conf import settings
from django.db import migrations, models

import immunity_users.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        swapper.dependency(
            *swapper.split(settings.AUTH_USER_MODEL), version='0004_default_groups'
        ),
        swapper.dependency('config', 'Device'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLocation',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'indoor',
                    models.CharField(
                        blank=True,
                        max_length=64,
                        null=True,
                        verbose_name='indoor position',
                    ),
                ),
                (
                    'content_object',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('config', 'Device'),
                    ),
                ),
            ],
            options={'abstract': False},
            bases=(immunity_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                ('floor', models.SmallIntegerField(verbose_name='floor')),
                (
                    'image',
                    models.ImageField(
                        help_text='floor plan image',
                        storage=django_loci.storage.OverwriteStorage(),
                        upload_to=django_loci.storage.OverwriteStorage.upload_to,
                        verbose_name='image',
                    ),
                ),
            ],
            options={'abstract': False},
            bases=(immunity_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        help_text=(
                            'A descriptive name of the location '
                            '(building name, company name, etc.)'
                        ),
                        max_length=75,
                        verbose_name='name',
                    ),
                ),
                (
                    'type',
                    models.CharField(
                        choices=[
                            (
                                'outdoor',
                                (
                                    'Outdoor environment (eg: street, square, garden, '
                                    'land)'
                                ),
                            ),
                            (
                                'indoor',
                                (
                                    'Indoor environment (eg: building, roofs, subway, '
                                    'large vehicles)'
                                ),
                            ),
                        ],
                        db_index=True,
                        help_text=(
                            'indoor locations can have floorplans associated to them'
                        ),
                        max_length=8,
                    ),
                ),
                (
                    'is_mobile',
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text='is this location a moving object?',
                        verbose_name='is mobile?',
                    ),
                ),
                (
                    'address',
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=256,
                        verbose_name='address',
                    ),
                ),
                (
                    'geometry',
                    django.contrib.gis.db.models.fields.GeometryField(
                        blank=True, null=True, srid=4326, verbose_name='geometry'
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('immunity_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={'abstract': False},
            bases=(immunity_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.AddField(
            model_name='floorplan',
            name='location',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='geo.Location'
            ),
        ),
        migrations.AddField(
            model_name='floorplan',
            name='organization',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=swapper.get_model_name('immunity_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AddField(
            model_name='devicelocation',
            name='floorplan',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='geo.FloorPlan',
            ),
        ),
        migrations.AddField(
            model_name='devicelocation',
            name='location',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='geo.Location',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='floorplan', unique_together=set([('location', 'floor')])
        ),
    ]
