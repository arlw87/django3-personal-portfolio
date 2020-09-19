from django.db import models

# Create your models here.
class Technologies(models.Model):
    title = models.CharField(
        max_length = 30
        )

    tech_image = models.ImageField(
        #LOCATION TO UPLOAD THE IMAGES TOO
        upload_to='tech/images/'
    )

    #returns the default name the class instance
    #required to see the name in the admin browser
    def __str__(self):
        return self.title
