# Generated by Django 2.2.4 on 2019-08-20 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190820_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Subject', verbose_name='课程'),
        ),
    ]
