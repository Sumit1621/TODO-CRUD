# Generated by Django 5.1.5 on 2025-03-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Todo", "0002_alter_todo_options_todo_order_todo_priority_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={},
        ),
        migrations.RemoveField(
            model_name="todo",
            name="order",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="priority",
        ),
        migrations.AlterField(
            model_name="todo",
            name="description",
            field=models.TextField(),
        ),
    ]
