from django.db import models

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,number):
        return cls.objects.get(pk = number)
        