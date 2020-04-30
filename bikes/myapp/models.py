import datetime

from django.db import models
from django.utils import timezone
from django.db import connection

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        
class UserDetails(models.Model):
    userid = models.TextField()
    usernumber = models.TextField()
    def __str__(self):
        return self.userid

class abcdfunction(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ProductName='a')

class efghfunction(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ProductOwner='th')

class ProductDetails(models.Model):
    ProductNumber = models.TextField()
    ProductName = models.TextField()
    ProductOwner = models.TextField()
    fivestar = models.IntegerField()
    fourstar = models.IntegerField()
    threestar = models.IntegerField()
    twostar = models.IntegerField()
    onestar = models.IntegerField()
    objects = models.Manager()
    abcd = abcdfunction()
    efgh = efghfunction()
    def __str__(self):
        return self.ProductName
    def nofivestar(self):
        return self.fivestar
    def my_custom_sql(self):
    	with connection.cursor() as cursor:
        	cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        	cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        	row = cursor.fetchone()
    	return row

class PurchaseDetails(models.Model):
    usernumber = models.ForeignKey("UserDetails", on_delete=models.SET_NULL, null=True)
    ProductNumber = models.ForeignKey("ProductDetails", on_delete=models.SET_NULL, null=True)
    feedback = models.IntegerField(default=0)
    def __str__(self):
        return self.usernumber




