from django.db import models


class Favorites(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    temp_user = models.CharField(max_length=255, blank=True, null=True)

    cpu = models.ManyToManyField("product.CPU", blank=True, verbose_name="Процессоры")
    gpu = models.ManyToManyField("product.GPU", blank=True, verbose_name="Видеокарты")

    def __str__(self):
        if self.user:
            return self.user.username
        return self.temp_user

    class Meta:
        verbose_name = "избранное"
        verbose_name_plural = "избранное"
