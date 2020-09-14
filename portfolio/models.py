from django.db import models

# Create your models here.
#uses inheritance in the brackets
class PortfolioProject(models.Model):
    title = models.CharField(
        max_length = 40
    )

    description = models.CharField(
        max_length = 200
    )

    project_image = models.ImageField(
        #LOCATION TO UPLOAD THE IMAGES TOO
        upload_to='portfolio/images/'
    )

    project_url = models.URLField(blank=True)

    #returns the default name the class instance
    #required to see the name in the admin browser
    def __str__(self):
        return self.title
