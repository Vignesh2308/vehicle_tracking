# Generated by Django 3.0.3 on 2020-02-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_data_data2'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='button1',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='button2',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='button3',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='button4',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
