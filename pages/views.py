from django.shortcuts import render
from django.http import HttpResponse

from authentification.forms import IdentificationForm
from substitutesearch.forms import SearchForm
from substitutesearch.management.commands.database_function import search_profil
from userProfil.forms import PasswordChange, MailChange, PseudoChange



def index(request):
	""" index pages """

	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/index.html'

	return render(request, template, locals())


def account(request):
	""" account pages """
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	passwordChange = PasswordChange()
	mailChange = MailChange()
	pseudoChange = PseudoChange()

	user = request.user
	profil = search_profil(user.username)

	if profil != False:
		profil = profil[0]

	template = 'pages/account.html'

	if request.user.is_authenticated:
		return render(request, template, locals())
	else:
		return HttpResponse('Unauthorized', status=401)


def legalMention(request):
	""" legal mentions pages """
	identifiantForm = IdentificationForm()
	searchForm = SearchForm()

	template = 'pages/legalMention.html'
	return render(request, template, locals())