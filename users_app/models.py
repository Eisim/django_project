from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    social_link = models.EmailField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name="Аватар")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"Профиль: {self.user.username}"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)
