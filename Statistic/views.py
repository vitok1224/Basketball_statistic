import instance as instance
import pytz as pytz
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import *
from .forms import *

from django_delayed_union import DelayedUnionQuerySet
from django_delayed_union import DelayedIntersectionQuerySet
from django_delayed_union import DelayedDifferenceQuerySet

from django.contrib.auth.mixins import LoginRequiredMixin


def USER_SIGN_UP(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно создали учетную запись")
            return redirect('sign_up_url')
            # user = form.save()
            # login(request, user)
            # return redirect('login')
        else:
            messages.error(request, 'Неизвестная ошибка на сервере')
    else:
        form = UserRegistration
    return render(request, template_name='SIGN_UP.html', context={'form': form})


def USER_SIGN_IN(request):
    return render(request, template_name='SIGN_IN.html')


def Home(request):
    penalty_query = Penalty_train_statistic.objects.all().values_list(
        'id', 'train_name', 'player', 'day', 'created_at', 'updated_at', 'is_published', 'ninety_left',
        'ninety_right', 'fortyfive_left', 'fortyfive_right', 'zero', 'penalty', 'id', 'id', 'id', 'id', 'id', 'id',
        'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id',
    )

    steff_query = Steffen_carry_train_statistic.objects.all().values_list(
        'id', 'train_name', 'player', 'day', 'created_at', 'updated_at', 'is_published', 'ninety_left_1level',
        'ninety_right_1level', 'fortyfive_left_1level', 'fortyfive_right_1level', 'zero_1level',
        'ninety_left_2level', 'ninety_right_2level', 'fortyfive_left_2level', 'fortyfive_right_2level',
        'zero_2level', 'ninety_left_3level', 'ninety_right_3level', 'fortyfive_left_3level',
        'fortyfive_right_3level', 'zero_3level', 'ninety_left_4level', 'ninety_right_4level',
        'fortyfive_left_4level', 'fortyfive_right_4level', 'zero_4level',
    )

    steff_pro_query = Steffen_carry_train_pro_statistic.objects.all().values_list(
        'id', 'train_name', 'player', 'day', 'created_at', 'updated_at', 'is_published', 'ninety_left_1level',
        'ninety_right_1level', 'fortyfive_left_1level', 'fortyfive_right_1level', 'zero_1level',
        'ninety_left_2level', 'ninety_right_2level', 'fortyfive_left_2level', 'fortyfive_right_2level',
        'zero_2level', 'ninety_left_3level', 'ninety_right_3level', 'fortyfive_left_3level',
        'fortyfive_right_3level', 'zero_3level', 'ninety_left_4level', 'ninety_right_4level',
        'fortyfive_left_4level', 'fortyfive_right_4level', 'zero_4level',
    )

    statistics = penalty_query.union(steff_query, steff_pro_query).order_by('-created_at')
    penalty_train_statistics_all = Penalty_train_statistic.objects.all()
    steffen_carry_train_statistics_all = Steffen_carry_train_statistic.objects.all()
    players = User.objects.all()
    context = {
        'statistics': statistics,
        'penalty_train_statistics_all': penalty_train_statistics_all,
        'steffen_carry_train_statistics_all': steffen_carry_train_statistics_all,
        'players': players
    }
    return render(request=request, template_name='Home.html', context=context)
