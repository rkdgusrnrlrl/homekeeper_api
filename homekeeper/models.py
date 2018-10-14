from django.db import models

INOUT_CHOICES = (
    ('IN', '수입'),
    ('OUT', '지출'),
)


class Homekeeper(models.Model):
    hk_id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pay_date = models.DateField()
    inout = models.CharField(max_length=2, choices=INOUT_CHOICES)
    contents = models.TextField()
    money = models.IntegerField()
