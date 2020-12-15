from django import forms


FOOD_CHOICES = (
    ('orange', 'orange'),
    ('pineapple', 'pineapple'),
    ('juice', 'juice'),
)

class FoodList(forms.Form):
    item_name = forms.ChoiceField(choices=FOOD_CHOICES)
