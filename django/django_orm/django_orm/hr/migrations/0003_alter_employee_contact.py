# Generated by Django 4.2.6 on 2023-10-12 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_contact_employee_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.contact'),
        ),
    ]
