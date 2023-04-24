from django import forms

from .models import Item, MarketCommunication


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'desc', 'price', 'image', 'condition', 'category', 'location', 'market_status']


class MarketCommunicationForm(forms.ModelForm):
    class Meta:
        model = MarketCommunication
        fields = [ 'comment', 'email', 'name']
        



# class ItemStatusForm(forms.Form):
    
#     status = forms.ChoiceField(choices=[('available', 'Available'), ('sold', 'Sold')], widget=forms.RadioSelect)


# , INTEREST_CHOICES
# class ItemInterestForm(forms.Form):
#     interest = forms.ChoiceField(choices=INTEREST_CHOICES, widget=forms.RadioSelect)