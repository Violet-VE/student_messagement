#########################################
# 作者：小纯洁				#
# 时间：2019.6.8			#
#########################################
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    # 手动定义
    # name=forms.CharField(label='姓名', max_length=128)
    # sex=forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    # profession=forms.CharField(label='职业', max_length=128)
    # email=forms.EmailField(label='Email', max_length=128)
    # qq=forms.CharField(label='QQ', max_length=128)
    # phone=forms.CharField(label='手机', max_length=128)
    class Meta:
        model = Student
        fields = (
            "name", "sex", "profession",
            "email", "qq", "phone"
        )

    def clean_qq(self):
        cleaned_data = self.cleaned_data["qq"]

        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字!')

        return int(cleaned_data)

    def clean_phone(self):
        cleaned_data = self.cleaned_data["phone"]

        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字!')

        return int(cleaned_data)
