from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm
from .models import Post, Person

User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    add_form = UserCreationForm # ユーザー作成画面
    form = UserChangeForm # ユーザー編集画面
    
    # 一覧画面で表示する
    list_display = ('username', 'email', 'is_staff', 'user_type', 'company_name')
    
    # ユーザー編集画面で表示する要素
    fieldsets = (
        ('ユーザー情報', {'fields': ('username', 'email', 'password', 'user_type', 'company_name', 'capital', 'website', 'permit_license')}),
        ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    
    # ユーザー作成画面で表示する要素
    add_fieldsets = (
        ('ユーザー情報', {'fields': ('username', 'email', 'password', 'confirm_password', 'user_type')}),
    )
    
admin.site.register(User, CustomizeUserAdmin)
admin.site.register(Post)
admin.site.register(Person)


# Register your models here.
