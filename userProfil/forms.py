#!/usr/bin/python3

from django import forms


class PasswordChange(forms.Form):
	newPassword = forms.CharField(
		label='nouveau mot de passe',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
	)

	confirmation = forms.CharField(
		label='confirmation',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
		required=True
	)

	oldPassword = forms.CharField(
		label='ancien mot de passe',
		max_length=100,
		widget=forms.PasswordInput(attrs={'class': 'form-control'}),
		required=True
	)


class MailChange(forms.Form):
	newMail = forms.CharField(
		label='nouvel e-mail',
		max_length=100,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True)

	confirmation = forms.CharField(
		label='confirmation',
		max_length=100,
		widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True)


class PseudoChange(forms.Form):
	pseudo = forms.CharField(
		label='pseudo',
		max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control'}),
		required=True
	)