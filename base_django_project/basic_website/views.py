from django.http import HttpResponseRedirect
from django.shortcuts import render
import re
from .functions import email_examp

# Create your views here.

regex_mail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex_phone = re.compile(r'(^[\+]?[(]?[0-9]{2,3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$)')

# mail attributes

MY_EMAIL = 'blu.ninja.2022@gmail.com'
MY_PASSWORD = 'hnnjsgqjjdrcvqzx'

def isValid(email, error):
    if re.fullmatch(regex_mail, email):
        pass
    else:
        error.append('נא למלא מייל תקין')

def phoneIsValid(phone_num, error):
    if re.fullmatch(regex_phone, phone_num):
        pass
    else:
        error.append('נא למלא מספר טלפון תיקני')

def index(request):
    if request.method == "POST":
        error = []
        entered_username = request.POST['name']
        entered_email = request.POST['email']
        entered_phone = request.POST['phone']
        entered_image = request.FILES.get('file', False)
        print(entered_image)          
        if entered_username == "":
            error.append('לא ניתן לשלוח בלי שדה שם')
        if len(entered_username) >= 100:
            error.append("שם ארוך מדי")  
        if entered_image != False:
            file_size = entered_image.size /1024 / 1024
            if file_size > 5:
                error.append("מותר לעלות קובץ עד 5 מגהבייט")
        isValid(entered_email, error)
        phoneIsValid(entered_phone, error)  
        if len(error) >= 1:
            return render(request, 'basic_website/index-heb.html', {'errors': error
            })
        contents = {'subject': 'mail from a client', 
            'name': entered_username, 'phone': entered_phone,
            'email_sender': entered_email,
            'message': 'Mail from a client'}
        email_examp(MY_EMAIL, MY_PASSWORD, contents)
        msg = "בקשתך נתקבלה, נציג יצור איתך קשר בהקדם"
        request.session['msg'] = msg
        return HttpResponseRedirect("/")
    msg = request.session.get('msg', False)
    if (msg): del(request.session['msg'])
    return render(request, 'basic_website/index-heb.html', {'message': msg})


def about_us(request):
    if request.method == "POST":
        entered_username = request.POST['name']
        entered_email = request.POST['email']
        entered_phone = request.POST['phone']
        entered_msg = request.POST['message']
        contents = {'subject': 'mail from a client', 
                'name': entered_username, 'phone': entered_phone,
                'email_sender': entered_email,
                'message': entered_msg}
        email_examp(MY_EMAIL, MY_PASSWORD, contents)
        msg = "בקשתך נתקבלה, נציג יצור איתך קשר בהקדם"
        request.session['msg'] = msg
        return HttpResponseRedirect("about-us")
    msg = request.session.get('msg', False)
    if (msg): del(request.session['msg'])
    return render(request, 'basic_website/about-us.html', {'message': msg})


def reviews(request):
    if request.method == "POST":
        entered_username = request.POST['name']
        entered_email = request.POST['email']
        entered_phone = request.POST['phone']
        entered_msg = request.POST['message']
        contents = {'subject': 'mail from a client', 
        'name': entered_username, 'phone': entered_phone,
        'email_sender': entered_email,
        'message': entered_msg}
        email_examp(MY_EMAIL, MY_PASSWORD, contents)
        msg = "בקשתך נתקבלה, נציג יצור איתך קשר בהקדם"
        request.session['msg'] = msg
        return HttpResponseRedirect("reviews")
    msg = request.session.get('msg', False)
    if (msg): del(request.session['msg'])
    return render(request, 'basic_website/reviews.html', {'message': msg})

def sales(request):
    if request.method == "POST":
        entered_username = request.POST['name']
        entered_email = request.POST['email']
        entered_phone = request.POST['message']
        entered_msg = request.POST['phone']
        contents = {'subject': 'mail from a client', 
        'name': entered_username, 'phone': entered_phone,
        'email_sender': entered_email,
        'message': entered_msg}
        email_examp(MY_EMAIL, MY_PASSWORD, contents)
        msg = "בקשתך נתקבלה, נציג יצור איתך קשר בהקדם"
        request.session['msg'] = msg
        return HttpResponseRedirect("sales")
    msg = request.session.get('msg', False)
    if (msg): del(request.session['msg'])
    return render(request, 'basic_website/portfolio.html', {'message': msg})

def order_page(request):
    return render(request, 'basic_website/order-page.html')

def our_projects(request):
    pass



def contact_us(request):
    pass






def order_form(request):
    pass