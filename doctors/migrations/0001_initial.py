# Generated by Django 3.1.7 on 2021-02-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id_doctors', models.IntegerField(db_column='id_Doctors', primary_key=True, serialize=False)),
                ('name_doctors', models.CharField(blank=True, db_column='name_Doctors', max_length=45, null=True)),
                ('passwords', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'doctors',
                'managed': False,
            },
        ),
    ]
