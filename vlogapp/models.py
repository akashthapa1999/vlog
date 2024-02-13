from django.db import models

# Create your models here.

class vlogDetails(models.Model):
    first_name = models.CharField("fname", max_length=50)
    last_name =models.CharField("lname", max_length=50)
    Date = models.DateField("table_date", auto_now=False, auto_now_add=False)
    img = models.ImageField("img", upload_to="img/")
    email  = models.EmailField("table_email", max_length=254)
    thought = models.TextField("thought")
