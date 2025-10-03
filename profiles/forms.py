from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """Form for users to update their profile settings"""
    
    class Meta:
        model = UserProfile
        fields = ['profession', 'receive_alerts']
        widgets = {
            'profession': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-[#0F0F10] border border-gray-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-white transition duration-300'
            }),
            'receive_alerts': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-white bg-[#0F0F10] border-gray-600 rounded focus:ring-white focus:ring-2'
            })
        }
        labels = {
            'profession': 'My Interest / Profession',
            'receive_alerts': 'Receive targeted space weather alerts'
        }
        help_texts = {
            'profession': 'Select your primary interest to receive relevant space weather alerts',
            'receive_alerts': 'Get notified about space weather events that may affect your activities'
        }
