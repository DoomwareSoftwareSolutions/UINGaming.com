from django.test import TestCase, LiveServerTestCase
from django.test.client import Client
from django.core import serializers
from src.users.models import User

import json

class UserTest(TestCase):

	def testUsersRawCreation(self):
		u = User(username = "hello", hashedID = "123452", email = "hello@hello.com")
		u2 = User(username = "hello2", hashedID = "123452", email = "hello2@hello.com")
		u.save()
		U = User.objects.filter(username = "hello").get();
		self.assertEqual(u.username, U.username)
		self.assertNotEqual(u2.username, U.username)
		U = User.objects.filter(username = "hello2");
		self.assertEqual(0, U.count())
		u2.save()
		U = User.objects.filter(username = "hello2");
		self.assertEqual(1, U.count())
		
	def testUsersCreation(self):
		u = User.add("user1","passwd",'user1@mail.com')
		U = User.objects.filter(username = "user1").get()
		self.assertEqual(u, U)
		u2 = User.add("user2", 'passwd','mail@mail.com')
		U = User.objects.filter(username = "user2").get()
		self.assertEqual(u2, U)
	
	def testUsersPartialUsernameSearch(self):
		u = User.add("tomas","passwd",'user1@mail.com')
		U = User.getByPartialUsername("tom")
		self.assertEqual(u, U)
		U = User.getByPartialUsername("tomas")
		self.assertEqual(u, U)
		u2 = User.add("fede", 'passwd','mail@mail.com')
		U2 = User.getByPartialUsername("fe")
		self.assertEqual(u2, U2)
		U2 = User.getByPartialUsername("fede")
		self.assertEqual(u2, U2)
		U = User.getByPartialUsername("ToMaS")
		self.assertEqual(u, U)
		U = User.getByPartialUsername("To")
		self.assertEqual(u, U)
	
	def testTwoEqualUsersCreation(self):
		u = User.add("user1","passwd",'user1@mail.com')
		u2 = User.add("user1","passwd",'user1@mail.com')
		self.assertIsNone(u2)
		u2 = User.add("user1","passwd", "mail@mail.com")
		self.assertIsNone(u2)
	
		
	def testUserGetByUsername(self):
		self.assertEqual(User.getByUsername("user1"), None)
		u = User.add("user1","passwd",'user1@mail.com')
		self.assertEqual(User.getByUsername("user1"), u)
		self.assertEqual(User.getByUsername("user2"), None)
		
	def testUserValidation(self):
		User.add("user1","passwd",'user1@mail.com')
		User.add("user2","passwd2",'user2@mail.com')		
		result = User.isValidLogin("user1","passwd")
		self.assertEqual(result, True)
		result = User.isValidLogin("user1","passwd2")
		self.assertEqual(result, False)
		result = User.isValidLogin("user2","passwd")
		self.assertEqual(result, False)
		result = User.isValidLogin("user2","passwd2")
		self.assertEqual(result, True)
		result = User.isValidLogin("user","passwd5")
		self.assertEqual(result, False)
	
	def testCompleteFields(self):
		User.add("user1","passwd",'user1@mail.com','User1','One')
		User.add("user2","passwd2",'user2@mail.com','User2', 'Two')
		u = User.getByUsername("user1")
		self.assertEqual(u.firstname, 'User1')
		self.assertEqual(u.lastname, 'One')
		u2 = User.getByUsername("user2")
		self.assertEqual(u2.firstname, 'User2')
		self.assertEqual(u2.lastname, 'Two')
		
	def testUpdateUserPassword(self):
		u = User.add("user1","passwd",'user1@mail.com')
		self.assertTrue(User.isValidLogin("user1","passwd"))
		u.updateUserPassword("newpasswd")
		self.assertFalse(User.isValidLogin("user1","passwd"))
		self.assertTrue(User.isValidLogin("user1","newpasswd"))
				
	def testUpdateUserEmail(self):
		User.add("user1","passwd",'user1@mail.com','User1','One')
		u = User.getByUsername("user1")
		self.assertEqual(u.email, 'user1@mail.com')
		u.updateUserEmail('user2@mail.com')
		u = User.getByUsername("user1")
		self.assertEqual(u.email, 'user2@mail.com')
		
	def testUpdateUserFirstName(self):
		User.add("user1","passwd",'user1@mail.com','User1','One')
		u = User.getByUsername("user1")
		self.assertEqual(u.firstname, 'User1')
		u.updateUserFirstname('User2')
		u = User.getByUsername("user1")
		self.assertEqual(u.firstname, 'User2')
		
	def testUpdateUserLastName(self):
		User.add("user1","passwd",'user1@mail.com','User1','One')
		u = User.getByUsername("user1")
		self.assertEqual(u.lastname, 'One')
		u.updateUserLastname('Two')
		u = User.getByUsername("user1")
		self.assertEqual(u.lastname, 'Two')
		
	def testUsernameValidation(self):
		self.assertTrue(User.isValidUsername('abcdef12345_ghijk678')) #Normal characters
		self.assertTrue(User.isValidUsername('abcdef12345-ghijk678')) #Normal characters
		self.assertTrue(User.isValidUsername('abcdef1_345_ghijk678')) #Two Undercords
		self.assertTrue(User.isValidUsername('abcdef1-345-ghijk678')) #Two cords
		self.assertTrue(User.isValidUsername('123')) #ThreeChars
		self.assertTrue(User.isValidUsername('12345678901234567890')) #TwentyChars
		
		self.assertFalse(User.isValidUsername('')) #Empty
		self.assertFalse(User.isValidUsername('12')) #TwoChars
		self.assertFalse(User.isValidUsername('123456789012345678901')) #TwentyOneChars
		self.assertFalse(User.isValidUsername('randomchars++=?')) #Rare Characters
		
	def testPasswordValidation(self):
		self.assertTrue(User.isValidPassword('abcdef12345_ghijk678')) #Normal characters
		self.assertTrue(User.isValidPassword('abcdef12345-ghijk678')) #Normal characters
		self.assertTrue(User.isValidPassword('abcdef1_345_ghijk678')) #Two Undercords
		self.assertTrue(User.isValidPassword('abcdef1-345-ghijk678')) #Two cords
		self.assertTrue(User.isValidPassword('123')) #ThreeChars
		self.assertTrue(User.isValidPassword('12345678901234567890')) #TwentyChars
		self.assertTrue(User.isValidPassword('randomchars++=?')) #Rare Characters
		
		self.assertFalse(User.isValidPassword('')) #Empty
		self.assertFalse(User.isValidPassword('12')) #TwoChars
		self.assertFalse(User.isValidPassword('123456789012345678901')) #TwentyOneChars
		
	def testEmailValidation(self):
		self.assertTrue(User.isValidEmail('unstring@otrostring.str')) #Normal mail
		
		self.assertFalse(User.isValidEmail('unstring@otrostring')) #Mail without.com
		self.assertFalse(User.isValidEmail('unstring@otrostring.')) #Mail without com
		self.assertFalse(User.isValidEmail('unstring.com')) #Mail without @
		self.assertFalse(User.isValidEmail('@otrostring.com')) #Mail without name
		self.assertFalse(User.isValidEmail('otrostring')) #Normal string
		

class SigninApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
	
	def testOKLoginReturnErrorCode0(self):
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signin'),'{"username":"user1", "password":"1234"}',content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],0)
		self.assertEqual(dic['username'],'user1')
		cookie = response.cookies.get('user_id').value.split(':')[0]
		self.assertEqual(cookie,'user1')
		
	def testWrongUsernameReturnErrorCode1(self):
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signin'),'{"username":"user2", "password":"1234"}',content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		self.assertEqual(dic['username'],'user2')
	
	def testWrongPasswordReturnErrorCode1(self):
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signin'),'{"username":"user1", "password":"12345"}',content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		self.assertEqual(dic['username'],'user1')
		
	def testBothWrongReturnErrorCode1(self):
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signin'),'{"username":"user2", "password":"12345"}',content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		self.assertEqual(dic['username'],'user2')
		
	def testInvalidParamsReturnErrorCode6(self):
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signin'))
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],6)
		
	def testOtherMethodsResponse405(self):
		response = self.client.get('%s%s' % (self.live_server_url, '/api/signin'))
		self.assertEqual(response.status_code,405)
		response = self.client.head('%s%s' % (self.live_server_url, '/api/signin'))
		self.assertEqual(response.status_code,405)
		response = self.client.put('%s%s' % (self.live_server_url, '/api/signin'),'{"username":"user2", "password":"12345"}',content_type='application/json')
		self.assertEqual(response.status_code,405)
		response = self.client.delete('%s%s' % (self.live_server_url, '/api/signin'))
		self.assertEqual(response.status_code,405)
		response = self.client.options('%s%s' % (self.live_server_url, '/api/signin'))
		self.assertEqual(response.status_code,405)
		

class SignupApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
	
	def testOKSignupReturnErrorCode0(self):
		data = '{"username":"user2", "password":"1234", "vpassword":"1234", "email":"us@er.com"}'
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'),data,content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],0)
		self.assertEqual(dic['username'],'user2')
		
	def testInvalidUsernameReturnErrorCode1(self):
		data = '{"username":"user2?", "password":"1234", "vpassword":"1234", "email":"us@er.com"}'
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'),data,content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
	
	def testInvalidPasswordReturnErrorCode2(self):
		data = '{"username":"user2", "password":"12", "vpassword":"12", "email":"us@er.com"}'
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'),data,content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],2)
	
	def testPasswordsNotMatchingReturnErrorCode3(self):
		data = '{"username":"user2", "password":"12345", "vpassword":"1234", "email":"us@er.com"}'
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'),data,content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],3)
		
	def testInvalidEmailReturnErrorCode4(self):
		data = '{"username":"user2", "password":"1234", "vpassword":"1234", "email":"us"}'
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'),data,content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],4)
	
	def testUsernameNotUniqueReturnErrorCode5(self):
		data = '{"username":"user1", "password":"1234", "vpassword":"1234", "email":"us@er.com"}'
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'),data,content_type='application/json')
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],5)
	
	def testInvalidParamsReturnErrorCode6(self):
		response = self.client.post('%s%s' % (self.live_server_url, '/api/signup'))
		self.assertEqual(response.status_code,200)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],6)
		
	def testOtherMethodsResponse405(self):
		response = self.client.get('%s%s' % (self.live_server_url, '/api/signup'))
		self.assertEqual(response.status_code,405)
		response = self.client.head('%s%s' % (self.live_server_url, '/api/signup'))
		self.assertEqual(response.status_code,405)
		response = self.client.put('%s%s' % (self.live_server_url, '/api/signup'))
		self.assertEqual(response.status_code,405)
		response = self.client.delete('%s%s' % (self.live_server_url, '/api/signup'))
		self.assertEqual(response.status_code,405)
		response = self.client.options('%s%s' % (self.live_server_url, '/api/signup'))
		self.assertEqual(response.status_code,405)
	
class LogoutApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
		self.url = self.live_server_url + '/api/logout'
	
	def testLogoutAfterLoginDeleteUserCookieAndReturnErrorCode0(self):
		data = '{"username":"user2", "password":"1234"}'
		response = self.client.post(self.live_server_url + '/api/signin','{"username":"user1", "password":"1234"}',content_type='application/json')
		cookie = response.cookies.get('user_id').value.split(':')[0]
		self.assertEqual(cookie,'user1')
		response = self.client.get(self.url)
		cookie = response.cookies.get('user_id').value
		self.assertEqual(cookie,'')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],0)
		
	def testLogoutWithoutLoginReturnErrorCode1(self):
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		
	def testOtherMethodsResponse405(self):
		response = self.client.post(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.head(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.put(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.options(self.url)
		self.assertEqual(response.status_code,405)
		
class PaswordRecoverApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
		self.url = self.live_server_url + '/api/password_recover'
	
	def testPostOkGivesErrorCode0AndSetCookie(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok').value.split(':')[0]
		self.assertEqual(cookie,'user1|u1@user.com')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],0)
	
	def testPostTwiseGivesErrorCode1(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		
	def testPostInvalidUsernameGivesErrorCode2AndSetsNoCookie(self):
		response = self.client.post(self.url,'{"username":"user1?"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok',None)
		self.assertIsNone(cookie)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],2)
		
	def testPostNonExistingUsernameGivesErrorCode3AndSetsNoCookie(self):
		response = self.client.post(self.url,'{"username":"user2"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok',None)
		self.assertIsNone(cookie)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],3)
		
	def testPostInvalidParametersGivesErrorCode6AndSetsNoCookie(self):
		response = self.client.post(self.url)
		cookie = response.cookies.get('lpwd_ok',None)
		self.assertIsNone(cookie)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],6)
		
	def testGetAfterPostingCorrectUsernameReturnTrueInRecoverCookie(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertTrue(dic['recover-cookie'])
		self.assertEqual(dic['username'],'user1')
		self.assertEqual(dic['email'],'u1@user.com')
	
	def testGetWithoutPostingCorrectUsernameReturnFalseInRecoverCookie(self):
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertFalse(dic['recover-cookie'])
		
	def testGetAfterPostingNonCorrectUsernameReturnFalseInRecoverCookie(self):
		response = self.client.post(self.url,'{"username":"user2"}',content_type='application/json')
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertFalse(dic['recover-cookie'])
		
	def testGetAfterPostingNonValidUsernameReturnFalseInRecoverCookie(self):
		response = self.client.post(self.url,'{"username":"user2?"}',content_type='application/json')
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertFalse(dic['recover-cookie'])
		
	def testGetAfterPostingCorrectUsername(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertTrue(dic['recover-cookie'])
		
	def testOtherMethodsResponse405(self):
		response = self.client.head(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.put(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.options(self.url)
		self.assertEqual(response.status_code,405)
		
class PasswordRecoverResetApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
		self.url = self.live_server_url + '/api/password_recover_reset'
		
	def testGetAfterStartingPasswordRecoveryProcessShouldRemoveCookie(self):
		response = self.client.post(self.live_server_url + '/api/password_recover','{"username":"user1"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok').value.split(':')[0]
		self.assertEqual(cookie,'user1|u1@user.com')
		response = self.client.get(self.url)
		cookie = response.cookies.get('lpwd_ok').value
		self.assertEqual(cookie,'')
		
	def testGetWithoutStartingPasswordRecoveryProcessShouldReturnErrorCode1(self):
		response = self.client.get(self.url)
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		
	def testOtherMethodsResponse405(self):
		response = self.client.post(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.head(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.put(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.options(self.url)
		self.assertEqual(response.status_code,405)
		
class PasswordRecoveryFormApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
		self.url = self.live_server_url + '/api/password_recover'
		self.user1_url = self.url + '/user1'
		
	def testChangingPasswordWithPasswordRecoveryCookieReturnErrorCode0(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok').value.split(':')[0]
		self.assertEqual(cookie,'user1|u1@user.com')
		response = self.client.post(self.user1_url, '{"password":"12345","vpassword":"12345"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],0)
	
	def testChangingPasswordWithoutPasswordRecoveryCookieReturnErrorCode1(self):
		response = self.client.post(self.user1_url, '{"password":"12345","vpassword":"12345"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)

	def testInvalidPasswordReturnErrorCode2(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok').value.split(':')[0]
		self.assertEqual(cookie,'user1|u1@user.com')
		response = self.client.post(self.user1_url, '{"password":"12","vpassword":"12"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],2)
			
	def testPasswordNotMatchingReturnErrorCode3(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok').value.split(':')[0]
		self.assertEqual(cookie,'user1|u1@user.com')
		response = self.client.post(self.user1_url, '{"password":"1235","vpassword":"12345"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],3)
		
	def testNotExistingUserGivesErrorCode4(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		cookie = response.cookies.get('lpwd_ok').value.split(':')[0]
		self.assertEqual(cookie,'user1|u1@user.com')
		u = User.getByUsername('user1')
		u.delete()
		response = self.client.post(self.user1_url, '{"password":"12345","vpassword":"12345"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],4)
		
	def testChangingCookieReturnErrorCode1(self):
		response = self.client.post(self.url,'{"username":"user1"}',content_type='application/json')
		mail = response.cookies.get('lpwd_ok').value.split(':')[0].split('|')[1]
		hashs = response.cookies.get('lpwd_ok').value.split(':')[1]
		self.client.cookies.get('lpwd_ok').set('lpwd_ok','user2|' + mail,'user2|' + mail + ':' + hashs)
		response = self.client.post(self.user1_url, '{"password":"12345","vpassword":"12345"}',content_type='application/json')
		dic = json.loads(response.content)
		self.assertEqual(dic['error-code'],1)
		
	def testOtherMethodsResponse405(self):
		response = self.client.get(self.user1_url)
		self.assertEqual(response.status_code,405)
		response = self.client.head(self.user1_url)
		self.assertEqual(response.status_code,405)
		response = self.client.put(self.user1_url)
		self.assertEqual(response.status_code,405)
		response = self.client.delete(self.user1_url)
		self.assertEqual(response.status_code,405)
		response = self.client.options(self.user1_url)
		self.assertEqual(response.status_code,405)
		
class UserProfileApiTests(LiveServerTestCase):
	def setUp(self):
		User.add('user1','1234','u1@user.com')
		User.add('user2','12345','u2@user.com','User','Two')
		self.url = self.live_server_url + '/api/users'
		
	def testObtaingUser1InfoReturnOk(self):
		response = self.client.post(self.live_server_url + '/api/signin','{"username":"user1", "password":"1234"}',content_type='application/json')
		response = self.client.get(self.url + '?user=user1')
		info = json.loads(response.content)
		self.assertEqual(info['error-code'],0)
		self.assertEqual(info['username'],'user1')
		self.assertEqual(info['email'],'u1@user.com')
		
	def testObtaingUser2InfoReturnOk(self):
		response = self.client.post(self.live_server_url + '/api/signin','{"username":"user2", "password":"12345"}',content_type='application/json')
		response = self.client.get(self.url + '?user=user2')
		info = json.loads(response.content)
		self.assertEqual(info['error-code'],0)
		self.assertEqual(info['username'],'user2')
		self.assertEqual(info['email'],'u2@user.com')
		self.assertEqual(info['firstname'],'User')
		self.assertEqual(info['lastname'],'Two')
		
	def testOtherMethodsResponse405(self):
		response = self.client.head(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.put(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.delete(self.url)
		self.assertEqual(response.status_code,405)
		response = self.client.options(self.url)
		self.assertEqual(response.status_code,405)
