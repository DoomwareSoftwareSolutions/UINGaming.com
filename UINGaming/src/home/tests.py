"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from src.home.models import Slide, Feature


class SlidesTest(TestCase):
	def testSlidesRawCreation(self):
		s1 = Slide(image= 'static/img/leesin.jpg',
			  heading= 'Best Lee Sin LAS',
			  caption= 'Torneo 1vs1 top. Sos el mejor Lee Sin del server latinoamerica?',
			  linkText= 'Inscribirse',
			  linkRef= '#')
		s2 = Slide(image= 'static/img/zed.jpg',
			  heading= 'Zed',
			  caption= 'The master of shadows.',
			  linkText= 'Sign up today',
			  linkRef= '#')
		s1.save()
		S1 = Slide.objects.filter(heading = "Best Lee Sin LAS").get();
		self.assertEqual(s1.heading, S1.heading)
		
		self.assertNotEqual(s2.heading, S1.heading)
		S2 = Slide.objects.filter(heading = 'Zed');
		self.assertEqual(0, S2.count())
		s2.save()
		S2 = Slide.objects.filter(heading = 'Zed');
		self.assertEqual(1, S2.count())
	
			
	def testSlidesCreation(self):
		u = Slide.add('static/img/leesin.jpg','Best Lee Sin LAS','Torneo 1vs1 top. Sos el mejor Lee Sin del server latinoamerica?','Inscribirse','#')
		U = Slide.objects.filter(heading = "Best Lee Sin LAS").get()
		self.assertEqual(u, U)
		u2 = Slide.add('static/img/zed.jpg', 'Zed', 'The master of shadows.','Sign up today','#')
		U = Slide.objects.filter(heading = 'Zed').get()
		self.assertEqual(u2, U)
	
	
class FeaturesTest(TestCase):
	def testFeaturesRawCreation(self):
		f1 = Feature(heading = 'Fiddlesticks',
                    subheading = 'The Harbinger of Doom',
                    description = 'For nearly twenty years, Fiddlesticks has stood alone in the easternmost summoning chamber of the Institute of War. Only the burning emerald light of his unearthly gaze pierces the musty darkness of his dust-covered home. It is here that the Harbinger of Doom keeps a silent vigil. His is a cautionary tale of power run amok, taught to all summoners within the League.',
                    image = 'static/img/fiddleSquare.png')
		f2 = Feature(heading = 'Ziggs',
                    subheading = 'The Hexplosives Expert',
                    description = 'Ziggs was born with a talent for tinkering, but his chaotic, hyperactive nature was unusual among yordle scientists. Aspiring to be a revered inventor like  Heimerdinger, he rattled through ambitious projects with manic zeal, emboldened by both his explosive failures and his unprecedented discoveries. Word of Ziggs volatile experimentation reached the famed Yordle Academy in Piltover and its esteemed professors invited him to demonstrate his craft.',
                    image = 'static/img/ziggsSquare.png')
		f1.save()
		F1 = Feature.objects.filter(heading = 'Fiddlesticks').get();
		self.assertEqual(f1.heading, F1.heading)
		
		self.assertNotEqual(f2.heading, F1.heading)
		F2 = Feature.objects.filter(heading = 'Ziggs');
		self.assertEqual(0, F2.count())
		f2.save()
		F2 = Feature.objects.filter(heading = 'Ziggs');
		self.assertEqual(1, F2.count())
	
			
	def testFeaturesCreation(self):
		u = Feature.add('Fiddlesticks', 'The Harbinger of Doom','For nearly twenty years, Fiddlesticks has stood alone in the easternmost summoning chamber of the Institute of War. Only the burning emerald light of his unearthly gaze pierces the musty darkness of his dust-covered home. It is here that the Harbinger of Doom keeps a silent vigil. His is a cautionary tale of power run amok, taught to all summoners within the League.','static/img/fiddleSquare.png')
		U = Feature.objects.filter(heading = 'Fiddlesticks').get()
		self.assertEqual(u, U)
		u2 = Feature.add('Ziggs','The Hexplosives Expert','Ziggs was born with a talent for tinkering, but his chaotic, hyperactive nature was unusual among yordle scientists. Aspiring to be a revered inventor like  Heimerdinger, he rattled through ambitious projects with manic zeal, emboldened by both his explosive failures and his unprecedented discoveries. Word of Ziggs volatile experimentation reached the famed Yordle Academy in Piltover and its esteemed professors invited him to demonstrate his craft.','static/img/ziggsSquare.png')
		U = Feature.objects.filter(heading = 'Ziggs').get()
		self.assertEqual(u2, U)

