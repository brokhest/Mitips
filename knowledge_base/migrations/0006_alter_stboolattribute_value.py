# Generated by Django 4.0.4 on 2022-05-19 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0005_alter_floatattribute_car_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stboolattribute',
            name='value',
            field=models.CharField(default='yes, no,', max_length=10, null=True),
        ),
    ]