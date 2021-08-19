from django.test import TestCase, Client
from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from authentification.models import Profil


class TestUserProfil(TestCase):
	""" class for testing user profil """


	def test_passwordChange(self):
		self.user = User.objects.create(username='testprofil',
			first_name='testprofil',
			last_name='test',
			email='testprofil@testouille.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)
		profil.save()

		self.client.login(username=self.user.username, password='test')

		response = self.client.post('/userProfil/change_password/', {'newPassword': 'test2',
			'confirmation': 'test2', 'oldPassword': 'test'})

		self.assertEquals(response.status_code, 302)
		self.assertEquals(response['location'], '/')


	def test_mailChange(self):
		self.user = User.objects.create(username='testprofil',
			first_name='testprofil',
			last_name='test',
			email='testprofil@testouille.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)
		profil.save()

		self.client.login(username=self.user.username, password='test')

		response = self.client.post('/userProfil/change_mail/', {'newMail': 'testprofil@test.com',
			'confirmation': 'testprofil@test.com'})

		self.assertEquals(response.status_code, 302)
		self.assertEquals(response['location'], '/')


	def test_pseudoChange(self):
		self.user = User.objects.create(username='testprofil',
			first_name='testprofil',
			last_name='test',
			email='testprofil@testouille.fr')

		self.user.set_password("test")
		self.user.save()

		profil = Profil(name=self.user.username, mailAdress=self.user.email, user=self.user)
		profil.save()

		self.client.login(username=self.user.username, password='test')

		response = self.client.post('/userProfil/change_pseudo/', {'pseudo': 'testpseudo'})

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/account.html')