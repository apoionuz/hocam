# Generated by Django 4.1.1 on 2022-10-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(4, 'AA'), (3.5, 'BA'), (3, 'BB'), (2.5, 'CB'), (2, 'CC'), (1.5, 'DC'), (1, 'DD'), (0.5, 'FD'), (0, 'FF')], null=True),
        ),
    ]