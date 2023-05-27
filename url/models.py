from django.db import models

# Create your models here.


class UrlDetail(models.Model):
    url = models.TextField()
    hashed_url = models.CharField(max_length=200,unique=True)
    use_limit = models.IntegerField(null=True,blank=True)
    used_count = models.IntegerField(default=0)




    class Meta:
        db_table = 'url_detail'

