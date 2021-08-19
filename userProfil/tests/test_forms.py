from django.test import TransactionTestCase

from userProfil.forms import PasswordChange, MailChange, PseudoChange


class TestUserProfilForm(TransactionTestCase):
	""" class testing user profil form """

	def test_passwordChangeFormValidity(self):
		passwordChange = PasswordChange(data={'newPassword': 'newMdp', 
			'confirmation': 'newMdp','oldPassword': 'oldPassword'})

		self.assertTrue(passwordChange.is_valid())


	def test_mailChangeForm(self):
		mailChange = MailChange(data={'newMail': "newMail@mail.fr", 'confirmation': "newMail@mail.fr"})

		self.assertTrue(mailChange.is_valid())


	def test_pseudoChangeForm(self):
		pseudoChange = PseudoChange(data = {'pseudo': 'test'})

		self.assertTrue(pseudoChange.is_valid())