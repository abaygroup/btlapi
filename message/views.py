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
            Вам пришел заказ от нового пользователя. Подробная информация заказчика представлена ниже:

            Имя: {}
            Email адрес: {}
            Телефон: {}
            Фрукты: {}
            Масса: {} (т)
        """.format(full_name, email, phone, fruits, weight)

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['Btlfood2@gmail.com',]

        send_mail( subject, message, email_from, recipient_list )
        return Response({"message" : "Success"})

