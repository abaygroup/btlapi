from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

class MainView(APIView):

    def post(self, request):
        full_name = request.data['full_name']
        email = request.data['email']
        phone = request.data['phone']
        fruits = request.data['fruits']
        weight = request.data['weight']

        subject = 'Новая заказ'
        message = """
            Если у Вас на экране появилась ошибка "Fatal error: Call to undefined function: mail()", 
            это значит, что либо PHP собран без поддержки функции mail, либо она запрещена настройками 
            сервера. 

            Имя: {}
            Email адрес: {}
            Телефон: {}
            Фрукты: {}
            Масса: {} (т)
        """.format(full_name, email, phone, fruits, weight)

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mukhagaliaryn@gmail.com',]

        send_mail( subject, message, email_from, recipient_list )
        return Response({"message" : "Success"})

