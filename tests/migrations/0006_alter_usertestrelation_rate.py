# Generated by Django 4.0.4 on 2022-05-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_test_readers_alter_test_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertestrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ok'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')], null=True),
        ),
    ]
