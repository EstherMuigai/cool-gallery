from django.db import models

class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,number):
        return cls.objects.get(pk = number)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)
    image = models.ForeignKey(Image)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name