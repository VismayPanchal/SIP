from django.shortcuts import render
from .models import *
# Create your views here.
def register(request):
	if request.method == "POST":
		user_obj = user.objects.create(
			user_name=request.POST.get('uname'),
			user_email=request.POST.get('email'),
			password=request.POST.get('pass'))
		user_obj.save()
		
	return render(request,'register.html')

def products(request):
	if request.method != 'POST':
		prod_obj=product.objects.all()
		datalist = []
		for x in prod_obj:
			datalist.append(
				{
				'pname':x.product_name, 'image':x.image, 'price':x.price,'pid':x.product_id
				})

		
        #print('DataList => ', datalist)
	return render(request,'products.html', {'Data': datalist})

def home(request):
	return render(request,'index.html')

def admin_index(request):
	return render(request,'ad_index.html')

def products_detail(request, pid):
	prod_obj= product.objects.get(product_id=pid)
	print("id++++",pid)
	datalist=[]
	datalist.append(
			{
			'stock':prod_obj.stock,'pname':prod_obj.product_name,'cname':prod_obj.cat_name,
			'image':prod_obj.image,'description':prod_obj.description,'price':prod_obj.price
			})
	print("Whole data :",datalist[0])
	return render(request,'product_detail.html',{'Data':datalist[0]})

def contact_us(request):
	return render(request,'contact.html')

def cart(request):
	return render(request,'cart.html')
