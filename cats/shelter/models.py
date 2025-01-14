from django.db import models


class Shelter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    capacity = models.IntegerField(verbose_name="Вместимость")

    class Meta:
        verbose_name = "Приют"
        verbose_name_plural = "Приюты"

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE,  verbose_name="Приют")

    class Meta:
        verbose_name = "Кот"
        verbose_name_plural = "Коты"

    def __str__(self):
        return self.name


class Adoption(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, verbose_name="Кот")
    adopter_name = models.CharField(max_length=100, verbose_name="Имя усыновителя")
    adoption_date = models.DateField(verbose_name="Дата устройства")

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return f"{self.adopter_name} приютил {self.cat.name}"
