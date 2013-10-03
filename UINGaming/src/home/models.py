from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

def loadTestDataSlides():
	slide = Slide(image = 'static/img/leesin.jpg',
			  heading = 'Best Lee Sin LAS',
			  caption = 'Torneo 1vs1 top. Sos el mejor Lee Sin del server latinoamerica?',
			  linkText = 'Inscribirse',
			  linkRef = '#')
	slide.save()
	slide = Slide(image = 'static/img/zed.jpg',
			  heading = 'Zed',
			  caption = 'The master of shadows.',
			  linkText = 'Sign up today',
			  linkRef = '#')
	slide.save()
	slide = Slide(image = 'static/img/thresh.jpg',
			  heading = 'Thresh',
			  caption = 'The chain warden.',
			  linkText = 'Sign up today',
			  linkRef = '#')
	slide.save()

class Slide(models.Model):
	image = models.CharField(max_length=256)
	heading = models.CharField(max_length=256)
	caption = models.CharField(max_length=256)
	linkText = models.CharField(max_length=256)
	linkRef = models.CharField(max_length=256)
	created = models.DateField(auto_now_add=True)
	
	@classmethod
	def getSlides(self, quantity):
		if (Slide.objects.count() == 0):
			loadTestDataSlides()
			
		try:
			slides = Slide.objects.all().order_by('-created')[0:quantity];
		except ObjectDoesNotExist:
			return None;
		
		return slides
		
	# Debemos agregar aqui la informacion adicional del slide
	# para poder inicializarlo correctamente
	@classmethod
	def add(self, image, heading, caption, linkText, linkRef):
		#checkeo unicidad con head a falta de ideas
		if Slide.objects.filter(heading=heading).count() != 0:
			return None
		s = Slide(image=image, heading=heading, caption=caption, linkText=linkText, linkRef=linkRef)
		s.save()
		return s
		
	def getDictionary(self):
		return dict(image = self.image,
                  heading = self.heading,
                  caption = self.caption,
                  linkText = self.linkText,
                  linkRef = self.linkRef
    )

def loadTestDataFeatures():
	feature = Feature(heading = 'Fiddlesticks',
                    subheading = 'The Harbinger of Doom',
                    description = 'For nearly twenty years, Fiddlesticks has stood alone in the easternmost summoning chamber of the Institute of War. Only the burning emerald light of his unearthly gaze pierces the musty darkness of his dust-covered home. It is here that the Harbinger of Doom keeps a silent vigil. His is a cautionary tale of power run amok, taught to all summoners within the League.',
                    image = 'static/img/fiddleSquare.png')
	feature.save()
	feature = Feature(heading = 'Ziggs',
                    subheading = 'The Hexplosives Expert',
                    description = 'Ziggs was born with a talent for tinkering, but his chaotic, hyperactive nature was unusual among yordle scientists. Aspiring to be a revered inventor like  Heimerdinger, he rattled through ambitious projects with manic zeal, emboldened by both his explosive failures and his unprecedented discoveries. Word of Ziggs volatile experimentation reached the famed Yordle Academy in Piltover and its esteemed professors invited him to demonstrate his craft.',
                    image = 'static/img/ziggsSquare.png')
	feature.save()
	feature = Feature(heading = 'Brand',
                    subheading = 'The Burning Vengeance',
                    description = 'In a faraway place known as Lokfar there was a seafaring marauder called Kegan Rodhe. As was his people\'s way, Kegan sailed far and wide with his fellows, stealing treasures from those unlucky enough to catch their attention. To some, he was a monster; to others, just a man. One night, as they sailed through the arctic waters, strange lights danced over the frozen wastes.',
                    image = 'static/img/brandSquare.png')
	feature.save()

class Feature(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	description = models.CharField(max_length=2000)
	image = models.CharField(max_length=256)
	created = models.DateField(auto_now_add=True)
	
	@classmethod
	def getFeatures(self, quantity):
		if (Feature.objects.count() == 0):
			loadTestDataFeatures()
			
		try:
			features = Feature.objects.all().order_by('-created')[0:quantity];
		except ObjectDoesNotExist:
			return None;
		
		return features
		
	# Debemos agregar aqui la informacion adicional del feature
	# para poder inicializarlo correctamente
	@classmethod
	def add(self, heading, subheading, description, image):
		#checkeo unicidad con head a falta de ideas
		if Feature.objects.filter(heading=heading).count() != 0:
			return None
		f = Feature(heading=heading, subheading=subheading, description=description, image=image)
		f.save()
		return f
		
	def getDictionary(self):
		return dict(heading = self.heading,
                  subheading = self.subheading,
                  description = self.description,
                  image = self.image
    )

class New(models.Model):
	header = models.CharField(max_length=256)
	subheader = models.CharField(max_length=256)
	body = models.CharField(max_length=256)
	image = models.CharField(max_length=256)
	created = models.DateTimeField(auto_now_add=True)
	
	
	@classmethod
	def add(self, header, subheader, body, image):
		if header == '' or image == '':
			return None
		n = New(header=header, subheader=subheader, body=body, image=image)
		n.save()
		return n
	
	@classmethod
	def getList(self, begin=0,end=1,):
		try:
			news = New.objects.all().order_by('-created')[begin:end];
		except ObjectDoesNotExist:
			return None;
		
		return news
	
	@classmethod
	def remove(self, pk):
		try:
			n = New.objects.filter(pk = pk).get()
		except ObjectDoesNotExist:
			return False
		
		n.delete()
		return True

	def updateHeader(self, header):
		self.header = header
	
	def updateSubHeader(self, subheader):
		self.subheader = subheader
		
	def updateBody(self, body):
		self.body = body
		
	def updateImage(self, image):
		self.image = image
	
	def toDic(self):
		dic = {}
		dic['pk'] = self.pk
		dic['header'] = self.header
		dic['subheader'] = self.subheader
		dic['body'] = self.body
		dic['image'] = self.image
		return dic