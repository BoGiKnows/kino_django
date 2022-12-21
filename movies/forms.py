from django import forms
from .models import Reviews, RatingStar, Rating
from captcha.fields import ReCaptchaField


class ReviewForm(forms.ModelForm):
    """
    Форма отзыва
    """
    # captcha = ReCaptchaField(
    #     public_key='6LcoqJUjAAAAAE7Z7DFyONI8yL_0ZgjIcKTQurEV',
    #     private_key='6LcoqJUjAAAAAIgZLmZzW-2pAJSm-htzpRtSZ2BJ'
    # )
    class Meta:
        model = Reviews
        fields = ('name', "email", "text")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.Textarea(attrs={'class': 'form-control border'}),
        }


class RatingForm(forms.ModelForm):
    """
    Форма добавления рейтинга
    """
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)