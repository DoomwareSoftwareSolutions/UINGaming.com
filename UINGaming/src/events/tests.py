"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from src.events.models import Event


class EventTest(TestCase):
	def testEventsRawCreation(self):
		e = Event(head = "hello", body = "123452", image = "asd.jpg",game = "lol",date="2013-09-10")
		e2 = Event(head = "hello2", body = "123452", image = "asd.jpg",game = "lol",date="2013-09-22")
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
		u = Event.add("Event1","body",'hads','lol',"2013-09-10")
		U = Event.objects.filter(head = "Event1").get()
		self.assertEqual(u, U)
		u2 = Event.add("Event2","body",'hads','lol',"2013-09-12")
		U = Event.objects.filter(head = "Event2").get()
		self.assertEqual(u2, U)
	
	def testDate(self):
		self.assertTrue(Event.isValidDate('2013-09-10')) 
		self.assertTrue(Event.isValidDate('2013-01-10')) 
		self.assertTrue(Event.isValidDate('2013-12-10')) 
		
		self.assertFalse(Event.isValidDate('2013-00-10'))
		self.assertFalse(Event.isValidDate('2013-13-10')) 
		self.assertFalse(Event.isValidDate('2013-asd-10')) 
