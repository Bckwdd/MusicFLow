from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class AuthUser(models.Model):
    """
    Модель користувача на платформі
    """
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(
        upload_to="",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])],
    )

    @property
    def is_authenticated(self):
        """
        Завжди вертаю True. Це спосіб дізнатись чи був користувач 'authenticated'
        """
        return True

    def __str__(self):
        return self.email


class Follower(models.Model):
    """
    Модель підписників
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="owner")
    subscriber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="subscribers")

    def __str__(self):
        return f'{self.subscriber} підписаний на {self.user}'


class SocialLink(models.Model):
    """
    Модель посилань на соц. мережі користувача
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="social_links")
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.user}'
