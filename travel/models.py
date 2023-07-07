from django.db import models

class CustomerFeedback(models.Model):
    customer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    service_views = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.customer_name
