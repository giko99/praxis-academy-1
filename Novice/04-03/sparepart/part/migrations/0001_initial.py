# Generated by Django 2.0 on 2020-09-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sukucadang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.CharField(max_length=100)),
                ('jenis', models.CharField(max_length=100)),
                ('kendaraan', models.CharField(max_length=100)),
                ('jumlah', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sukucadang',
            },
        ),
    ]
