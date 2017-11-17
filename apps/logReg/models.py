from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
  # Create your models here.
NAME_REGEX = re.compile(r"(^[A-Z][-a-zA-Z]+$)")
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
  # uploaded_by_id = models.ForeignKey(users, related_name = "uploader")
  # likes = models.ManyToManyField(users, related_name = "likes")

class usersManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        f_name = postData['f_name']
        l_name = postData['l_name']
        email = postData['email']
        pw1 = postData['pw1']
        pw2 = postData['pw2']


        if not NAME_REGEX.match(f_name) or not NAME_REGEX.match(l_name):
            errors['name'] = "First name or last name is invalid"

        if not EMAIL_REGEX.match(email):
            errors['email'] = "Email is invalid"
        if users.objects.filter(email=email):
            errors['email_exist'] = "Email has been used"

        if not PASS_REGEX.match(pw1):
            errors['pw1'] = "Password is invalid"

        if pw1 != pw2:
            errors['pw2'] = "Password does not match"

        return errors

    def log_validator(self, postData):
        errors = {}

        log_email = postData['email']
        log_pw = postData['pw']

        try:
            users.objects.get(email=log_email)
            db_pw = users.objects.get(email=log_email).pw
            if not bcrypt.checkpw(log_pw.encode(), db_pw.encode()):
                errors['not_match'] = "Invalid password"
        except:
            errors['not_email'] = "Invalid email"

        return errors

class users(models.Model):
  f_name = models.CharField(max_length=30)
  l_name = models.CharField(max_length=30)
  email = models.CharField(max_length=50)
  pw = models.CharField(max_length=30)
  objects = usersManager()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
