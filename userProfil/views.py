from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

from django.core.mail import send_mail

from substitutesearch.management.commands.database_function import search_mail, search_profil

from authentification.forms import IdentificationForm
from substitutesearch.forms import SearchForm


from .forms import PasswordChange, MailChange, PseudoChange

def change_password(request):
	""" view allowing the user to change the password """

	passwordChange = PasswordChange()
	mailChange = MailChange()
	pseudoChange = PseudoChange()

	identifiantForm = IdentificationForm()
	searchForm = SearchForm()


	newPassword = request.POST.get('newPassword')
	confirmation = request.POST.get('confirmation')
	oldPassword = request.POST.get('oldPassword')

	user = request.user

	template = '/'

	if user.check_password(oldPassword) and newPassword == confirmation:
		user.set_password(newPassword)
		user.save()

		logout(request)
	else:
		template = "pages/account.html"
		return render(request, template, locals())

	return redirect(template)

def change_mail(request):
	""" view allowing the user to change the password """

	passwordChange = PasswordChange()
	mailChange = MailChange()
	pseudoChange = PseudoChange()

	identifiantForm = IdentificationForm()
	searchForm = SearchForm()


	newMail = request.POST.get('newMail')
	confirmation = request.POST.get('confirmation')

	user = request.user

	if newMail == confirmation:
		if search_mail(newMail):
			messages.warning(request, "e-mail déja pris")
		else:
			user.email = newMail
			profil = search_profil(user.username)

			if profil:
				profil[0].mailAdress = newMail
				profil[0].save()
			else:
				pass

			user.save()

			send_mail('changement de mail', 'votre mail a bien été changer', 'mauricedonovandevellopement@gmail.com', [newMail], fail_silently=False)

			logout(request)
	else:
		template = "pages/account.html"
		messages.warning(request, "confirmation invalide")
		return render(request, template, locals())

	template = '/'


	return redirect(template)


def change_pseudo(request):
	""" view allowing the user to change the password """

	passwordChange = PasswordChange()
	mailChange = MailChange()
	pseudoChange = PseudoChange()

	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	pseudo = request.POST.get('pseudo')

	user = request.user

	template = 'pages/account.html'

	profil = search_profil(user.username)
	profil[0].name = pseudo
	user.username = pseudo

	user.save()
	profil[0].save()


	return render(request, template, locals())