from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
  return 'images/{filename}'.format(filename=filename)

class retail_info(models.Model):
  retail_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, blank=False)
  email = models.EmailField(max_length = 254, blank=False, unique=True)
  contact_number1 = models.BigIntegerField(blank=False)
  contact_number2 = models.BigIntegerField(blank=True, null=True)
  retail_size = models.IntegerField(blank=False)
  it_automation = models.CharField(max_length=50, blank=False)
  no_of_mobile = models.IntegerField(blank=False)
  no_of_tab = models.IntegerField(blank=False)
  no_of_computer = models.IntegerField(blank=False)
  no_of_printer = models.IntegerField(blank=False)
  no_of_scanner = models.IntegerField(blank=False)
  latitude = models.FloatField(blank=False)
  longitude = models.FloatField(blank=False) 
  date_time = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(_("Image"),upload_to=upload_to, blank=False)

  def __str__(self):
    return self.email
