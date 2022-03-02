# Generated by Django 4.0.2 on 2022-02-28 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('circle_id', models.AutoField(primary_key=True, serialize=False)),
                ('circle_name', models.CharField(max_length=100)),
                ('admin_username', models.CharField(max_length=100)),
                ('no_of_users', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('policy_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('policy_name', models.CharField(max_length=20)),
                ('policy_desc', models.CharField(max_length=1000)),
                ('policy_level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CirclePolicies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.IntegerField(default=0)),
                ('circle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle.circle')),
            ],
        ),
        migrations.CreateModel(
            name='CircleUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_member', models.BooleanField(default=False)),
                ('circle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle.circle')),
            ],
            options={
                'unique_together': {('circle_id', 'user_id')},
            },
        ),
    ]