from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from django.conf import settings
from places.fields import PlacesField
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=30, blank=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_no = models.CharField(max_length=20,blank=True,null=True)
    served = models.IntegerField(blank=True,null=True)
    is_also_volunteer = models.BooleanField(blank=True,null=True)
    requested = models.IntegerField(blank=True,null=True)
    pincode = models.CharField(_('Pincode'),max_length=6,blank=True)
    address = models.CharField(_('Address'),max_length=200,blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class post(models.Model):
    title = models.CharField(max_length=200,blank=False)
    message = models.TextField()
    location = PlacesField()
    active_post = models.BooleanField(null=True,default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    datesub = models.DateTimeField(_('date published'),auto_now_add=True)
    claims = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='getclaims',blank=True)
    reports = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='getreports',blank=True)
    volunteers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='assignvolunteer',blank=True)
    timelimit = models.DateTimeField()
    def __str__(self):
        return self.title

    @property
    def get_volunteer(self):
        return self.volunteers.all()
    @property
    def get_claims(self):
        return self.claims.all()
    @property
    def get_reports(self):
        return self.reports.all()    

#script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBKzjwtu-tyyJQtPP3rFPxPRCgtZHgmKfs&callback=initMap"
 # type="text/javascript"></script>

class contact(models.Model):
    name = models.CharField(max_length=50,blank=False)
    email = models.CharField(max_length=50,blank=False)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.email + "_ " + self.name