from django.db import models

class FeedBack(models.Model):
   name = models.CharField(max_length=100,null=True)
   email = models.EmailField()
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.name + ' - ' + self.email   
   