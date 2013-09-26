"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from src.events.models import Event,EventMembership
from src.users.models import User
import datetime

class EventTest(TestCase):
	def testEventsRawCreation(self):
		e = Event(head = "hello", body = "123452", image = "asd.jpg",game = "lol",date="2013-09-10",inscriptionDeadline="2013-09-10")
		e2 = Event(head = "hello2", body = "123452", image = "asd.jpg",game = "lol",date="2013-09-22",inscriptionDeadline="2013-09-10")
		e.save()
		E = Event.objects.filter(head = "hello").get();
		self.assertEqual(e.head, E.head)
		
		self.assertNotEqual(e2.head, E.head)
		E2 = Event.objects.filter(head = "hello2");
		self.assertEqual(0, E2.count())
		e2.save()
		E2 = Event.objects.filter(head = "hello2");
		self.assertEqual(1, E2.count())
	
			
	def testEventsCreation(self):
		u = Event.add("Event1","body",'hads','lol',"2013-09-10",inscriptionDeadline="2013-09-10")
		U = Event.objects.filter(head = "Event1").get()
		self.assertEqual(u, U)
		u2 = Event.add("Event2","body",'hads','lol',"2013-09-12",inscriptionDeadline="2013-09-10")
		U = Event.objects.filter(head = "Event2").get()
		self.assertEqual(u2, U)
	
	# def testQuery(self):
	# 	u = Event.add(head="Event1",body="body",image='hads',game='lol',date="2013-09-10",inscriptionDeadline="2013-09-10")
	# 	all_entries = Event.objects.all()
	# 	query = all_entries[0].toDict()
	# 	query['date']=str(query['date'])
	# 	query['inscriptionDeadline']=str(query['inscriptionDeadline'])
		
	# 	testDict = {'body': u'body', 'head': u'Event1', "enrolledUsers":[],'inscriptionDeadline': '2013-09-10 05:00:00+00:00', 'image': u'hads', 'game': u'lol', 'date': '2013-09-10 05:00:00+00:00', u'id': 6L}
	# 	self.assertEqual(query,testDict)
		
	
	def testMembership(self):
		u = User.add('ringoStarr','1234','u1@user.com')
		e = Event.add("Concert","body",'hads','lol',"2013-09-10","2013-09-12")
		m1 = EventMembership(user=u, event=e,
			teamName = "LaMera",
			teamMembers = "Mattlike, Ciboulette",
			paid = False)
		m1.save()
		u2 = User.add('paulMcCartney','4321','u1@user.com')
		m2 = EventMembership(user=u2, event=e,
			teamName = "LamerLa",
			teamMembers = "FedeChampion",
			paid = False)
		m2.save()
		

	def testMembEventQuery(self):
		u = User.add('ringoStarr','1234','u1@user.com')
		u2 = User.add('paulMcCartney','1234','u1@user.com')
		e = Event.add("Concert","body",'hads','lol',"2013-09-10","2013-09-12")
		m1 = EventMembership(user=u, event=e,
			teamName = "LaMera",
			teamMembers = "Mattlike, Ciboulette",
			paid = False)
		m1.save()	

		m2 = EventMembership(user=u2, event=e,
			teamName = "LaMera2",
			teamMembers = "Mattlike2, Ciboulette2",
			paid = False)
		m2.save()	
		memberships = EventMembership.getByEvent(5)
		self.assertEqual(memberships[0].teamName,"LaMera")
		self.assertEqual(memberships[1].teamName,"LaMera2")
		memberships = EventMembership.getByEvent(10)

	def testMembEventQueryEmptyEvent(self):
		u = User.add('ringoStarr','1234','u1@user.com')
		u2 = User.add('paulMcCartney','1234','u1@user.com')
		e = Event.add("Concert","body",'hads','lol',"2013-09-10","2013-09-12")
	
		memberships = EventMembership.getByEvent(5)
		self.assertEqual(memberships,[])
		memberships = EventMembership.getByEvent(10)
		self.assertEqual(memberships,[])