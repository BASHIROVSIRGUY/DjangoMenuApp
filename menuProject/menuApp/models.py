from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(null=True, verbose_name="Текст")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="url-slug")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'link'
        abstract = True


class MenuItemFirstLvl(MenuItem):
    def get_absolute_url(self):
        return reverse("menu:first_level",
                       kwargs={"first_slug": self.slug})

    class Meta:
        verbose_name = "Элемент первого уровня"
        verbose_name_plural = "Элементы первого уровня"


class MenuItemSecondLvl(MenuItem):
    parent = models.ForeignKey(MenuItemFirstLvl, on_delete=models.CASCADE, related_name="second_lvl")

    def get_absolute_url(self):
        return reverse("menu:second_level",
                       kwargs={'first_slug': self.parent.slug,
                               'second_slug': self.slug})

    class Meta:
        verbose_name = "Элемент второго уровня"
        verbose_name_plural = "Элементы второго уровня"


class MenuItemThirdLvl(MenuItem):
    parent = models.ForeignKey(MenuItemSecondLvl, on_delete=models.CASCADE, related_name="third_lvl")

    def get_absolute_url(self):
        return reverse("menu:third_level",
                       kwargs={'first_slug': self.parent.parent.slug,
                               'second_slug': self.parent.slug,
                               'third_slug': self.slug})

    class Meta:
        verbose_name = "Элемент третьего уровня"
        verbose_name_plural = "Элементы третьего уровня"


