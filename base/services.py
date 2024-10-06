from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """
    Побудова шляху до файлу, format: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.id}/{file.name}'


def validate_size_image(file_obj):
    """
    Перевірка розміру файла
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальний розмір файлу {megabyte_limit}MB")
