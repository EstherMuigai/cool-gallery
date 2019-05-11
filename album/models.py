from django.db import models

class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,blank =True)

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

    @classmethod
    def filter_by_location(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    def __str__(self):
        return self.name