from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum
from django.contrib.auth.models import User
class Penalty_train_statistic(models.Model):
    train_name = models.CharField(max_length=50, default='Penalty train', null=False)
    player = models.ForeignKey(User, on_delete=models.PROTECT, related_name='penalty')
    day = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, )
    ninety_left = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_right = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_left = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_right = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    zero = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    penalty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.train_name

    def get_absolute_url(self):
        return reverse('Penalty_train_statistic', kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Penalty_train_statistic'
        ordering = ['-created_at']


class Steffen_carry_train_statistic(models.Model):
    train_name = models.CharField(max_length=50, default='Steffen carry train', null=False, )
    player = models.ForeignKey(User, on_delete=models.PROTECT, related_name='steffan_carry_train')
    day = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, )
    ninety_left_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_right_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_left_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_right_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    zero_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_left_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_right_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_left_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_right_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    zero_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_left_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_right_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_left_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_right_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    zero_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_left_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ninety_right_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_left_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fortyfive_right_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    zero_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def get_absolute_url(self):
        return reverse('Steffen_carry_train_statistic', kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Steffen_carry_train_statistic'
        ordering = ['-created_at']


class Steffen_carry_train_pro_statistic(models.Model):
    train_name = models.CharField(max_length=50, default='Steffen carry train pro', null=False)
    player = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name='steffan_carry_train_pro',
                               default='По каким то причинам имени игрока нет')
    day = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, )
    ninety_left_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_right_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_left_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_right_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    zero_1level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_left_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_right_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_left_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_right_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    zero_2level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_left_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_right_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_left_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_right_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    zero_3level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_left_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ninety_right_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_left_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    fortyfive_right_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    zero_4level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def get_absolute_url(self):
        return reverse('Steffen_carry_train_pro_statistic', kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Steffen_carry_train_pro_statistic'
        ordering = ['-created_at']


class Images(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='photo_url')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Images'
        ordering = ['-created_at']


# class Players(models.Model):
#     username = models.CharField(max_length=20,  null=True)
#     password1 = models.CharField(max_length=20, null=True)
#     password2 = models.CharField(max_length=20, null=True)
#     email = models.EmailField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse('user', kwargs={"id": self.id})
#
#     class Meta:
#         verbose_name_plural = 'Players'
#         ordering = ['-created_at']

