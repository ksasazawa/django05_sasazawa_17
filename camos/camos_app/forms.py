from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Post

User = get_user_model() # Userに、このアプリで利用する設定のユーザークラスを格納

class UserCreationForm(forms.ModelForm):
    # ModelFormの内容をパスワードだけ上書き
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type')
        
    # フォーム入力された値に処理を入れる（パスワードチェック）
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("パスワードが一致しません")
        
    # セーブ処理を上書き（パスワードを暗号化して保存）
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user

class ClientCreationForm(forms.ModelForm):
    # ModelFormの内容をパスワードだけ上書き
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput())
    user_type = forms.CharField(max_length=10, initial='client', widget=forms.HiddenInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'company_name', 'site_name', 'password')
        
    # フォーム入力された値に処理を入れる（パスワードチェック）
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("パスワードが一致しません")
        
    # セーブ処理を上書き（パスワードを暗号化して保存）
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user
    
class SupplierCreationForm(forms.ModelForm):
    # ModelFormの内容をパスワードだけ上書き
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='confirm_password', widget=forms.PasswordInput())
    user_type = forms.CharField(max_length=10, initial='supplier', widget=forms.HiddenInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'company_name', 'capital', 'website', 'permit_license', 'password')
        
    # フォーム入力された値に処理を入れる（パスワードチェック）
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("パスワードが一致しません")
        
    # セーブ処理を上書き（パスワードを暗号化して保存）
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user
    
class ClientLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    # user_type = forms.CharField(max_length=10, initial='client', widget=forms.HiddenInput)
    
class SupplierLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    # user_type = forms.CharField(max_length=10, initial='supplier', widget=forms.HiddenInput)
    
class UserChangeForm(forms.ModelForm):
    # ModelFormの内容を上書き
    password = ReadOnlyPasswordHashField()
    website = forms.URLField(required=False)
    permit_license = forms.FileField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type', 'company_name', 'site_name', 'capital', 'website', 'permit_license', 'is_staff', 'is_active', 'is_superuser')
    
    # すでに登録されているパスワードを返す
    def clean_password(self):
        return self.initial['password']
    
class ClientChangeForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'名前'}))
    company_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'会社名'}))
    site_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'現場名'}))
    # class Meta:
    #     model = User
    #     fields = ('username', 'company_name', 'site_name')
    
class SupplierChangeForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'名前'}))
    company_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'会社名'}))
    capital = forms.IntegerField()
    website = forms.URLField(widget=forms.TextInput(attrs={'placeholder':'WEBサイト'}))
    
class PostForm(forms.Form):
    qualification_list = [
        ("２級土木施工管理", "２級土木施工管理")
        , ("１級土木施工管理", "１級土木施工管理")
        , ("２級建築施工管理", "２級建築施工管理")
        , ("１級建築施工管理", "１級建築施工管理")
        , ("２級電気工事施工管理", "２級電気工事施工管理")
        , ("１級電気工事施工管理", "１級電気工事施工管理")
        , ("２級管工事施工管理", "２級管工事施工管理")
        , ("１級管工事施工管理", "１級管工事施工管理")
        , ("２級造園施工管理", "２級造園施工管理")
        , ("１級造園施工管理", "１級造園施工管理")
        , ("２級電気通信工事施工管理", "２級電気通信工事施工管理")
        , ("１級電気通信工事施工管理", "１級電気通信工事施工管理")
        , ("資格不問", "資格不問")
        ]
    agent_list = [
        # ("株式会社夢真", "株式会社夢真")
        # , ("株式会社テクノプロ・コンストラクション", "株式会社テクノプロ・コンストラクション")
        # , ("共同エンジニアリング株式会社", "共同エンジニアリング株式会社")
        # , ("株式会社アーキ・ジャパン", "株式会社アーキ・ジャパン")
        # , ("株式会社TS工研", "株式会社TS工研")
        # , ("ブライザ株式会社", "ブライザ株式会社")
        # , ("株式会社ウィルオブ・コンストラクション", "株式会社ウィルオブ・コンストラクション")   
    ]
    users = User.objects.filter(user_type="supplier")
    for user in users:
        agent_list.append((user.company_name, user.company_name))
        print(user.company_name)
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
    job = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'業務内容'}))
    qualification = forms.MultipleChoiceField(choices = qualification_list, widget=forms.CheckboxSelectMultiple)
    location = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'勤務地'}))
    body = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder':'入力してください'}))
    price = forms.IntegerField()
    agent = forms.MultipleChoiceField(choices = agent_list, widget=forms.CheckboxSelectMultiple)
    create_user = forms.IntegerField()
    create_user_company = forms.CharField(max_length=255)
    
class PersonForm(forms.Form):
    qualification_list = [
        ("２級土木施工管理", "２級土木施工管理")
        , ("１級土木施工管理", "１級土木施工管理")
        , ("２級建築施工管理", "２級建築施工管理")
        , ("１級建築施工管理", "１級建築施工管理")
        , ("２級電気工事施工管理", "２級電気工事施工管理")
        , ("１級電気工事施工管理", "１級電気工事施工管理")
        , ("２級管工事施工管理", "２級管工事施工管理")
        , ("１級管工事施工管理", "１級管工事施工管理")
        , ("２級造園施工管理", "２級造園施工管理")
        , ("１級造園施工管理", "１級造園施工管理")
        , ("２級電気通信工事施工管理", "２級電気通信工事施工管理")
        , ("１級電気通信工事施工管理", "１級電気通信工事施工管理")
        , ("資格なし", "資格なし")
        ]
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'名前'}))
    age = forms.IntegerField()
    sex = forms.fields.ChoiceField(
        choices = (
            ("male", "male"),
            ("female", "female"),
            ("others", "others"),
        ),
        initial="male",
        required=True,
        widget=forms.widgets.Select()
    )
    # sex = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'性別'}))
    qualification = forms.MultipleChoiceField(choices = qualification_list, widget=forms.CheckboxSelectMultiple)
    # experience = forms.BooleanField()
    construction1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'経験工事１'}))
    construction2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'経験工事２'}))
    construction3 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'経験工事３'}))
    
class ResultForm(forms.Form):
    result = forms.fields.ChoiceField(
        choices = (
            ("offer", "会いたい"),
            ("reject", "お見送り"),
        ),
        initial="選択してください",
        required=True,
        widget=forms.widgets.Select()
    )
        
        
    

