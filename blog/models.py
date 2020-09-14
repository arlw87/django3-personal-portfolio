from django.db import models

# Create your models here.
class Blog(models.Model):
    #blogs have title, date and text / html
        title = models.CharField(
            max_length = 40
        )

        date = models.DateField()

        blogContent = models.TextField()

        #returns the default name the class instance
        #required to see the name in the admin browser
        def __str__(self):
            return self.title
