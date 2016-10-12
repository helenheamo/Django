from django.db import models

class Tag(models.Model):
	name=models.CharField(max_legth=31,unique=True)
	slug=models.SlugField(max_legth=31,unique=True,help_text='A label for URL config')
	def _str_(self):
		return self.name

class Startup(models.Model):
	name=models.CharField(max_legth=31,db_index=True)
	slug=models.SlugField(max_legth=31,unique=True,help_text='A label for URL config')
	description=models.TextField()
	founded_date=models.DateField('date founded')
	contact=models.EmailField()
	website=models.URLField(max_legth=255)
	tags=models.ManyToManyField(Tag)
	def __str__(self):
		return self.name


class NewLink(models.Model):
	title=models.CharField(max_legth=63)
	pub_date=models.DateField('date published')
	link=models.URLField(max_legth=255)
	startup=models.ForeignKey(Startup)
	def __str__(self):
		return"{}:{}".format(self.startup,self.title)

