from django.db import models

# Create your models here.
class books(models.Model):
    bname=models.CharField(max_length=45)
    page=models.IntegerField(null=True)


    def __str__(self):
        return self.bname
class auther(models.Model):
    aname=models.CharField(max_length=54)
    bname=models.ForeignKey(books,on_delete=models.CASCADE,default=True)
    age=models.IntegerField(default=True)

    def __str__(self):
        return self.aname
class auther1(models.Model):
    aname=models.CharField(max_length=54)
    bname=models.ManyToManyField(books)
    age=models.IntegerField(default=True)

    def __str__(self):
        return self.aname
    def written(self):
        return ",".join([str(b) for b in self.bname.all()])

