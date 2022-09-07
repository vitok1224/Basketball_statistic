from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import *


class Penalty_train_statisticAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['id', 'player', 'day', 'created_at', 'updated_at', 'is_published',
                    'ninety_left',
                    'ninety_right',
                    'fortyfive_left',
                    'fortyfive_right',
                    'zero',
                    'penalty']
    fields = ['train_name', 'id', 'player', 'day',
              'ninety_left',
              'ninety_right',
              'fortyfive_left',
              'fortyfive_right',
              'zero',
              'penalty',
              'is_published',
              'created_at', 'updated_at']
    readonly_fields = ['id', 'train_name', 'id', 'created_at', 'updated_at']
    list_display_links = ['id']
    list_filter = ['player', 'is_published']


class Steffen_carry_train_statisticAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['id', 'player', 'day', 'created_at', 'updated_at', 'is_published',
                    'ninety_left_1level',
                    'ninety_right_1level',
                    'fortyfive_left_1level',
                    'fortyfive_right_1level',
                    'zero_1level',
                    'ninety_left_2level',
                    'ninety_right_2level',
                    'fortyfive_left_2level',
                    'fortyfive_right_2level',
                    'zero_2level',
                    'ninety_left_3level',
                    'ninety_right_3level',
                    'fortyfive_left_3level',
                    'fortyfive_right_3level',
                    'zero_3level',
                    'ninety_left_4level',
                    'ninety_right_4level',
                    'fortyfive_left_4level',
                    'fortyfive_right_4level',
                    'zero_4level',
                    ]
    fields = ['train_name', 'id', 'player', 'day',
              'ninety_left_1level',
              'ninety_right_1level',
              'fortyfive_left_1level',
              'fortyfive_right_1level',
              'zero_1level',
              'ninety_left_2level',
              'ninety_right_2level',
              'fortyfive_left_2level',
              'fortyfive_right_2level',
              'zero_2level',
              'ninety_left_3level',
              'ninety_right_3level',
              'fortyfive_left_3level',
              'fortyfive_right_3level',
              'zero_3level',
              'ninety_left_4level',
              'ninety_right_4level',
              'fortyfive_left_4level',
              'fortyfive_right_4level',
              'zero_4level',
              'is_published',
              'created_at', 'updated_at'
              ]
    readonly_fields = ['train_name', 'id', 'created_at', 'updated_at']
    list_display_links = ['id']
    list_filter = ['player', 'is_published']


class Steffen_carry_train_pro_statisticAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['id', 'player', 'day', 'created_at', 'updated_at', 'is_published',
                    'ninety_left_1level',
                    'ninety_right_1level',
                    'fortyfive_left_1level',
                    'fortyfive_right_1level',
                    'zero_1level',
                    'ninety_left_2level',
                    'ninety_right_2level',
                    'fortyfive_left_2level',
                    'fortyfive_right_2level',
                    'zero_2level',
                    'ninety_left_3level',
                    'ninety_right_3level',
                    'fortyfive_left_3level',
                    'fortyfive_right_3level',
                    'zero_3level',
                    'ninety_left_4level',
                    'ninety_right_4level',
                    'fortyfive_left_4level',
                    'fortyfive_right_4level',
                    'zero_4level',
                    ]
    fields = ['train_name', 'player', 'day',
              'ninety_left_1level',
              'ninety_right_1level',
              'fortyfive_left_1level',
              'fortyfive_right_1level',
              'zero_1level',
              'ninety_left_2level',
              'ninety_right_2level',
              'fortyfive_left_2level',
              'fortyfive_right_2level',
              'zero_2level',
              'ninety_left_3level',
              'ninety_right_3level',
              'fortyfive_left_3level',
              'fortyfive_right_3level',
              'zero_3level',
              'ninety_left_4level',
              'ninety_right_4level',
              'fortyfive_left_4level',
              'fortyfive_right_4level',
              'zero_4level',
              'is_published',
              'created_at', 'updated_at'
              ]
    readonly_fields = ['train_name', 'id', 'created_at', 'updated_at']
    list_display_links = ['id']
    list_filter = ['player', 'is_published']


# class PlayersAdmin(admin.ModelAdmin):
#     save_as = True
#     list_display = ['id', 'username', 'created_at', 'updated_at']
#     fields = ['id', 'username', 'created_at', 'updated_at']
#     readonly_fields = ['id', 'created_at', 'updated_at']
#     list_display_links = ['id']
#
#
# players = Images.objects.all()
# for item in players:
#     if item.created_at == item.updated_at:
#         list_display = ['id', 'name', 'created_at', ]
#        list_display_links = ['id']
#         fields = ['id', 'name', 'created_at', ]
#         readonly_fields = ['id', 'created_at', ]
#         break


class ImagesAdmin(admin.ModelAdmin):
    save_as = True

    list_display = ['id', 'photo', 'get_photo', 'created_at', 'updated_at']
    fields = ['id', 'photo', 'get_photo', 'created_at', 'updated_at']
    readonly_fields = ['id', 'get_photo', 'created_at', 'updated_at']
    list_display_links = ['id']

    #  images = Images.objects.all()
    #  for item in images:
    #     if item.created_at != item.updated_at:
    #        list_display = ['id', 'photo', 'get_photo', 'created_at', 'updated_at']
    #         fields = ['id', 'photo', 'get_photo', 'created_at', 'updated_at']
    #        readonly_fields = ['id', 'get_photo', 'created_at', 'updated_at']
    #       list_display_links = ['id']
    #       break

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'photo'


admin.site.register(Penalty_train_statistic, Penalty_train_statisticAdmin)
admin.site.register(Steffen_carry_train_statistic, Steffen_carry_train_statisticAdmin)
admin.site.register(Steffen_carry_train_pro_statistic, Steffen_carry_train_pro_statisticAdmin)
admin.site.register(Images, ImagesAdmin)
# admin.site.register(Players, PlayersAdmin)