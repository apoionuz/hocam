# Generated by Django 4.1.1 on 2022-09-28 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='academician',
            name='lecture',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.lecture'),
            preserve_default=False,
        ),
    ]
