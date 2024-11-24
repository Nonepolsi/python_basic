from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.forms import (
    CharField,
    TextInput,
    PasswordInput,
    EmailField,
)



class CustomUserCreationForm(UserCreationForm):

    username = CharField(label="Имя пользователя", widget=TextInput(attrs={"class": "form-input"}))
    email = EmailField(label="Почта", widget=TextInput(attrs={"class": "form-input"}))
    password1 = CharField(label="Пароль", widget=PasswordInput(attrs={"class": "form-input"}))
    password2 = CharField(label="Повтор пароля", widget=PasswordInput(attrs={"class": "form-input"}))

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",     
        }
        widgets = {
            "first_name": TextInput(attrs={"class": "form-input"}),
            "last_name": TextInput(attrs={"class": "form-input"}),
        }

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        print(username, email)

        if any(item in username for item in ["@", "+"]):
            self.add_error("username", "Символы @ and + запрещены")
        
        if get_user_model().objects.filter(email__iexact=email).exists():
            self.add_error("email", "Пользователь с такой почтой уже зарегистрирован")

        return cleaned_data



class CustomUserLoginForm(AuthenticationForm):

    username = CharField(
        label="Имя пользователя",
        widget=TextInput(attrs={"class": "form-input"})
    )

    password = CharField(
        label="Пароль",
        widget=PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = get_user_model()
        fields = ("username", "password")



class CustomUserChangeForm(UserChangeForm):
    username = CharField(disabled=True, label="Имя пользователя", widget=TextInput(attrs={"class": "form-input"}))
    email = EmailField(disabled=True, label="Почта", widget=TextInput(attrs={"class": "form-input"}))
    password = None
 
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "first_name": TextInput(attrs={"class": "form-input"}),
            "last_name": TextInput(attrs={"class": "form-input"}),
        }



class CustomUserPasswordChangeForm(PasswordChangeForm):
    old_password = CharField(label="Старый пароль", widget=PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = CharField(label="Новый пароль", widget=PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = CharField(label="Подтверждение пароля", widget=PasswordInput(attrs={'class': 'form-input'}))