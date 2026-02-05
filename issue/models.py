from django.db import models
from django.contrib.auth.models import User
from books.models import Books
from django.utils import timezone
# Create your models here.

class Issue(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now())
    return_date = models.DateField(null=True,blank=True)

    @property
    def fine(self):
        if self.return_date:
            days = (self.return_date - self.issue_date).days
            if days > 15:
                return (days - 15) * 5
        return 0


