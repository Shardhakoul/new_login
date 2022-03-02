from django.db import models

# Create your models here.

class Circle(models.Model):
    circle_id = models.AutoField(primary_key = True)
    circle_name = models.CharField(max_length = 100)
    admin_username = models.CharField(max_length=100)
    no_of_users = models.IntegerField(default = 0)
    #circle_display_image = models.ImageField(upload_to = 'images/')

class CircleUsers(models.Model):
    class Meta:
        unique_together = (('circle_id', 'user_id'),)
    circle_id = models.ForeignKey(Circle, on_delete = models.CASCADE)
    user_id = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    is_admin = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)

class CirclePolicies(models.Model):
    circle_id = models.ForeignKey(Circle, on_delete = models.CASCADE)
    policy_id = models.IntegerField(default = 0)

class Policy(models.Model):
    policy_id = models.IntegerField(default = 0, primary_key = True)
    policy_name = models.CharField(max_length = 20)
    policy_desc = models.CharField(max_length = 1000)
    policy_level = models.IntegerField(default = 0)
