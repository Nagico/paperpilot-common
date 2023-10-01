# Generated by Django 4.2.5 on 2023-10-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    def __init__(self, name, app_label):
        # overriding application operated upon
        super(Migration, self).__init__(name, "admin")

    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name="logentry",
        #     name="user",
        # ),
        migrations.AddField(
            model_name="logentry",
            name="user_id",
            field=models.IntegerField(default=0, verbose_name="user"),
        ),
    ]
