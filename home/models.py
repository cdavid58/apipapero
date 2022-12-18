from django.db import models

class Inventory(models.Model):
	code = models.CharField(unique=True, max_length=25,null = True, blank = True)
	code_int = models.CharField(unique=True, max_length=25,null = True, blank = True)
	name = models.CharField(unique = True,max_length= 80,null = True, blank = True)
	cost = models.CharField(max_length=25,null = True, blank = True)
	price_1 = models.CharField(max_length=25, null = True, blank = True)
	price_2 = models.CharField(max_length=25, null = True, blank = True)
	price_3 = models.CharField(max_length=25, null = True, blank = True)
	price_4 = models.CharField(max_length=25, null = True, blank = True)
	price_5 = models.CharField(max_length=25, null = True, blank = True)
	tax = models.CharField(max_length=3, null = True, blank = True)
	category = models.CharField(max_length = 80,null = True, blank = True)
	download = models.BooleanField(default=False)
	active = models.BooleanField(default=False)
	update = models.BooleanField(default=False)
	new_product = models.BooleanField(default=False)
	pnt_1 = models.BooleanField(default=True) #pnt_1
	pnt_2 = models.BooleanField(default=True) #pnt_2
	pnt_3 = models.BooleanField(default=True) #pnt_3
	pnt_4 = models.BooleanField(default=True) #pnt_4
	pnt_5 = models.BooleanField(default=True) #pnt_5
	pnt_6 = models.BooleanField(default=True) #pnt_6
	pnt_7 = models.BooleanField(default=True) #pnt_7
	pnt_8 = models.BooleanField(default=True) #pnt_8
	pnt_9 = models.BooleanField(default=True) #pnt_9
	pnt_10 = models.BooleanField(default=True) #pnt_10
	pnt_11 = models.BooleanField(default=True) #pnt_11
	pnt_12 = models.BooleanField(default=True) #pnt_12
	pnt_13 = models.BooleanField(default=True) #pnt_13
	pnt_14 = models.BooleanField(default=True) #pnt_14
	pnt_15 = models.BooleanField(default=True) #pnt_15

	def __str__(self):
		return self.name +' | '+self.code