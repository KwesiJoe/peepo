from django.test import Client, TestCase
from django.urls import reverse



class HomepageTest(TestCase):

	def test_homepage_return_status200(self):
		response =  self.client.get(reverse("homepage"))
		self.assertEqual(200, response.status_code, "successful")