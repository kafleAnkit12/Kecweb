# Generated by Django 4.1.7 on 2023-03-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_subscriber_resultdata_bs'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='symbol',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
