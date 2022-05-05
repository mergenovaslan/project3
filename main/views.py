from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import OrderForm, AddPostForm,EmailForm
from .utils import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings



def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'main/dashboard.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'main/products.html', {'products':products})

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'main/customer.html',context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'main/order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'main/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'main/delete.html', context)

def show_post(request,post_slug):
	post=get_object_or_404(Posts,slug=post_slug)
	context={'post':post}
	return render(request, 'main/post.html', context=context)


def index(request):
	return render(request,'main/index.html')


def list(request):
	return render(request,'main/list_categories.html')


def login(request):
    return HttpResponse("Авторизация")


def registration(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'main/register.html',{'form': form,'name': 'registration'})


class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'main/susccessfull.html'

    def get(self, request):
        form = self.form_class()
        return render(request,'main/successfull.html',{'email_form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, 'main/successfull.html',
                              {'email_form': form, 'error_message': 'Электрондық пошта мекенжайына жіберілді %s' % email})
            except:
                return render(request, 'main/successfull.html',
                              {'email_form': form, 'error_message': 'Не тіркеме тым үлкен немесе бүлінген'})

        return render(request, 'main/successfull.html',
                      {'email_form': form, 'error_message': 'Электрондық поштаны жіберу мүмкін емес. Тағы жасауды сәл кейінірек көріңізді өтінеміз'})
