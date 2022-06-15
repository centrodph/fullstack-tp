# Generated by Django 4.0.5 on 2022-06-15 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_interviewstatus_alter_interview_candidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='interviewstatuses', to='interview.interviewstatus'),
            preserve_default=False,
        ),
    ]
