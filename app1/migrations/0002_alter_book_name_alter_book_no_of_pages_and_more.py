# Generated by Django 4.0.5 on 2022-06-12 10:04

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='no_of_pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='student_book', to='app1.student'),
        ),
        migrations.AlterField(
            model_name='school',
            name='contact_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='For e.g 1234-567-890, 1234-567890, etc.', max_length=128, null=True, region=None, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='student_school', to='app1.school'),
        ),
    ]