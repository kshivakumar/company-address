"""address models"""

from django.db import models


class CompanyAddress(models.Model):

    company_name = models.TextField()
    building_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=15)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        db_table = 'company_address'
