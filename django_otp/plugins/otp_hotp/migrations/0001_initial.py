# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_otp.plugins.otp_hotp.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HOTPDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text=b'Is this device ready for use?')),
                ('key', models.CharField(default=django_otp.plugins.otp_hotp.models.default_key, help_text=b'A hex-encoded secret key of up to 40 bytes.', max_length=80, validators=[django_otp.plugins.otp_hotp.models.key_validator])),
                ('digits', models.PositiveSmallIntegerField(default=6, help_text=b'The number of digits to expect in a token.', choices=[(6, 6), (8, 8)])),
                ('tolerance', models.PositiveSmallIntegerField(default=5, help_text=b'The number of missed tokens to tolerate.')),
                ('counter', models.BigIntegerField(default=0, help_text=b'The next counter value to expect.')),
                ('user', models.ForeignKey(help_text=b'The user that this device belongs to.', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'HOTP device',
            },
            bases=(models.Model,),
        ),
    ]
