# Generated by Django 4.1.1 on 2022-11-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatmodel',
            name='name',
            field=models.PositiveIntegerField(choices=[(1, 'Ekonom'), (2, 'Biznes'), (3, 'Premum')], verbose_name='seat class name'),
        ),
    ]
