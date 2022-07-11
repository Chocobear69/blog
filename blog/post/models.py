from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    text = models.TextField(null=True)

    is_hidden = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)
    last_updated_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey("customer.Customer", on_delete=models.SET_NULL, null=True)
