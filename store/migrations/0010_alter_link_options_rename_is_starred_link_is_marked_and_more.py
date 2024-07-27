# Generated by Django 5.0.6 on 2024-07-27 07:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0009_alter_link_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="link",
            options={"ordering": ["-saved_on", "is_read"]},
        ),
        migrations.RenameField(
            model_name="link",
            old_name="is_starred",
            new_name="is_marked",
        ),
        migrations.RenameField(
            model_name="link",
            old_name="has_been_read",
            new_name="is_read",
        ),
    ]
