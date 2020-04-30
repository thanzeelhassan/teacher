from django import forms

class SignUp(forms.Form):
    product_owner = forms.CharField(initial = 'Product Owner')
    product_name = forms.CharField(initial = 'Product Name')
    star = forms.IntegerField(initial = 'Which Star rating ?')
    #first_name = forms.CharField(initial = 'First Name', )
    #last_name = forms.CharField(initial = 'Last Name')
    #email = forms.EmailField(help_text = 'write your email', )
    #Address = forms.CharField(required = False, )
    #Technology = forms.CharField(initial = 'Django', disabled = True, )
    #age = forms.IntegerField()
    #password = forms.CharField(widget = forms.PasswordInput)
    #re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)
