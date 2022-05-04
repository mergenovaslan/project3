from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z1-10]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
	    ordering=['-name']




class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.name


class Posts(models.Model):
    title=models.CharField(max_length=255,verbose_name="Тақырып")
    is_published=models.BooleanField(default=True,verbose_name="Шығарылым")
    slug=models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")

    def get_absolute_url(self):
    	return reverse('post',kwargs={'post_slug':self.slug})

def get_number(self):
		return 7

def trueval(self):
	return False

class Meta:
	verbose_name = 'Тақырып'
	verbose_name_plural = 'Тақырыптар'
	ordering=['-order_date']




class Categories(models.Model):
	title= models.CharField(max_length=255)
	content=models.TextField(blank=True)
	picture=models.ImageField(default='default value')
	describe=models.TextField(default='DataFlair Django tutorials')

class Registration(models.Model):
    name = models.CharField(max_length=15,validators=[alphanumeric],)
    lastname = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)
    email = models.EmailField(blank=True, unique=True)
    telnumber = models.IntegerField(unique=True)
    password = models.CharField(max_length=10,validators=[MinLengthValidator(4)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'
        ordering = ['name']









