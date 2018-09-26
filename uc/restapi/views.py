from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Users
from . serializers import usersSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string


# Get all user List
class userList(generics.ListCreateAPIView):
	queryset = Users.objects.all()
	serializer_class = usersSerializer


# Get selected user List
class userDetail(generics.RetrieveDestroyAPIView):
	queryset = Users.objects.all()
	serializer_class = usersSerializer


# check all validations for user
class checkUser():
	@api_view(['GET', 'POST'])
	def kaaroFunction(request,format=None):
        # check email exist
		if request.method == 'POST':
			emailee = request.POST.get('email')
			if Users.objects.filter(email = emailee).exists():
				return Response('already exists',status=200)
			return Response('not exist',status=200)

		elif request.method == 'GET':
			return Response('Get not allow',status=404)

class registerUser():
	@api_view(['Get','POST'])
	def register(request,fromat=None):
		email = request.POST.get('email')
		password = request.POST.get('password')
		deviceToken = request.POST.get('deviceToken')
		deviceType = request.POST.get('deviceType')
		dummyId = request.POST.get('dummyId')
		deleteFlag = request.POST.get('deleteFlag')
		connectSherpaFlag = request.POST.get('connectSherpaFlag')
		data = {'email': email, 'password': password, 'deviceToken': deviceToken,
		'deviceType': deviceType,'deleteflag': deleteFlag,'connectsherpaflag':connectSherpaFlag }

		if Users.objects.filter(email = email).exists():
				return Response('already exists',status=200)
		else:
			serializer = usersSerializer(data=data)
			if serializer.is_valid():
				instance = serializer.save()
				instance_id = instance.userid
				return Response(instance,status=201)
			else:
				err = serializer.errors
				return Response(err,status=200)
			return Response('registered',status=200)

class mailCheck():
	@api_view(['GET','POST'])
# send normal email
	def send_email(request):
		subject = 'testing'
		message = 'test for email'
		from_email = 'prabhat.singh@rsvrtech.com'
		if subject and message and from_email:
			try:
				send_mail(subject, message, from_email, ['prabhat.singh@rsvrtech.com'])
			except BadHeaderError:
				return Response('Invalid header found',status=200)
			return Response('Greate thanks' , status= 200)
		else:
			# In reality we'd use a form class
			# to get proper validation errors.
			return Response('Something Went Wrong',status= 200)

# send mail with template
	def send_mail_template():
		ctx = {
				'name': 'prabhat'
			}
		message = render_to_string('email.html', ctx)
		subject, from_email = 'hello', 'from@example.com'
		msg = EmailMessage(subject, message, from_email=from_email, to=['prabhat.singh@rsvrtech.com'])
		msg.content_subtype = 'html'
		msg.send(fail_silently=True)
		return Response('mail', status=200)

# send mail with attachment
	def mail_attachment():
		ctx = {
                'name': 'prabhat'
            }
		message = render_to_string('email.html', ctx)
		image2 = request.FILES['image2']
		subject, from_email = 'hello', 'from@example.com'
		msg = EmailMessage(subject, message, from_email=from_email, to=['prabhat.singh@rsvrtech.com'])
		msg.attach(image2.name, image2.read(), image2.content_type)
		msg.content_subtype = 'html'
		msg.send(fail_silently=True)
		return Response('mail', status=200)


# Lets play with data
class dataplay():
	@api_view(['GET','POST'])
	# write custom query
	def getusersdata(request):
		queryset = Users.objects.raw('SELECT * FROM users')
		dict = {}
		list = []
		for p in queryset:
			dict['email'] = p.email
			dict['name']= p.firstname
			dict['app'] = 'prabhat'
			list.append(dict.copy())
			dict = {}
		return Response(list,status=200)