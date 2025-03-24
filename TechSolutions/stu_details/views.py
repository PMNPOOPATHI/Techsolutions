from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import *
from .forms import *
from datetime import datetime
from django.contrib import messages

#LOGIN PAGE
message = {}
user_name = None
def log_in(request):
    
    context = {'error':''}
    if request.method == 'POST':
        user = authenticate(username = request.POST['person'], password = request.POST['Passkey'] )
        global user_name
        if user is not None:
            login(request,user)
            user_name = user
            print(user_name)
            return redirect(reverse('Details_student'))
        else:
            context = {'error':'Invalid UserName or Password'}
        return render(request,'stu_details/log_inPage.html',context)
            
    return render(request,'stu_details/log_inPage.html')

#STUDENT VIEW PAGE

def students_view(request):
    a_data = students.objects.all()
    return render(request,"stu_details/students_details.html",{'item':a_data})

#VIEW DETAILS

def viewDetails(request, id):
    stu_data = students.objects.get(id = id)
    return render(request,'stu_details/view_details.html',{'i':stu_data})

#UPDATE_PAGE

def updatePage(request,id):
    st_data = students.objects.get(id = id)
    print(st_data)
    print(request.POST)
    return render(request,'stu_details/updatepage.html',{'form':students_form(),'data': st_data})


#PAY BILL PAGE


def billing_page(request,id=None):
    
    today = datetime.now()
    Response_message = None
    curent_data = None
    search_result = None
    temp = None
    if id != None:
        curent_data = students.objects.get(id = id)
        billing_detail = billing.objects.all()
        return render(request,'stu_details/pay_bill.html',{'result':curent_data,'now':today,'bill_no':billing_detail})

    if request.method == "POST":
        form_type = request.POST.get('form_type')
        
        if form_type == 'Search':
            curent_data = students.objects.get(id = request.POST['ref'])
            return render(request,'stu_details/pay_bill.html',{'result':curent_data,'now':today})
        if form_type == 'Store':
            curent_data = students.objects.get(id = request.POST['Id'])
            curent_data.Total += int(request.POST['current_paid'])
            
            total = int(request.POST["Total_paid"])+int(request.POST['current_paid'])

            blnc_amount = curent_data.Fees - total  
            if blnc_amount >=0:
                curent_data.blnc_amount = blnc_amount  
                submit_data = billing(stu_id=request.POST['Id'],course_id=request.POST['Course'],paid_date=request.POST['date'],total_paid= total,current_paid=request.POST['current_paid'],balance_amount = blnc_amount)
                submit_data.save()
                curent_data.save()
        else:
            Response_message="Student Paid their Contribution"
            return (Response_message)
    return render(request,'stu_details/pay_bill.html',{'res':Response_message})

#COURSE DETAILS

def Courses(request):
    course = courses.objects.all()
    return render(request,'stu_details/courses.html',{'data':course})

#PRINT BILL PAGE

def print_bill(request,id = None):
    value = None
    student = None 
    if id is not None:
        search_id = id
        course_data = courses.objects.all()
        value = billing.objects.get(bill_no = search_id)
        student_id = value.stu_id
        student = students.objects.get(id = student_id)
    if request.method == "POST":
        search_id = request.POST['ref']
        course_data = courses.objects.all()
        value = billing.objects.get(bill_no = search_id)
        student_id = value.stu_id
        student = students.objects.get(id = student_id)
    return render(request,'stu_details/print_bill.html',{'data': value,'course':student})

#LOGOUT PAGE

def log_out(request):
    logout(request)
    global message 
    message = {'res':'Successfully Loged out...!'}
    return redirect('LogIn')
    

#DELETE PAGE

def delete_data(request, id):
    deleted_data = students.objects.get(id = id)
    if deleted_data is not None:
        deleted_data.delete()
        return redirect('Details_student')
    


#Accounts Details Addition Page


def ac_daily(request):
    return render(request,'stu_details/add_account_data.html')
    
# ADD STUDENTS PAGE

def add_students(request):
    new_data = students_form(request.POST)
    if request.method == 'POST':
        if new_data.is_valid():
            new_data.save()
            messages.success(request, 'Your profile was updated successfully!')
    return render(request,'stu_details/add_students.html',{'form': students_form()})

#SEARCH BY ID

def search_by_id(request):
    context = {'error':''}
    search_result = []
    if request.method =="POST":
        s_id = request.POST['Search_Item']
        search_result = students.objects.get(id = s_id)

        if search_result is not None:
            context  = {'error':"Search result is found"}
        else:
            context = {'error':"Search result is not found"}
            return redirect('')
    return render(request,'stu_details/search_items.html',{'stu':search_result},context)

#SEARCH BY NAME

def search_by_name(request, name):
    search_result = students.objects.get(Name = name)
    return render(request,'',{'stu':search_result})

#SEARCH BY COURSE

def search_by_course(request, course):
    course_name = courses.objects.get(Name = course)
    search_result = students.objects.get(Selected_course = course_name.id)
    
    return render(request,'stu_details/search_items.html',{'stu':search_result})
def show_bill(request,id = None):
    current_data = None
    search_id =  None
    if id is not None:
        print('Id value is None')
        pass
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'Search':
            search_id = request.POST['ref']
            current_data = billing.objects.filter(stu_id = search_id)
    return render(request,'stu_details/show_bill.html',{'data':current_data})

def acc_summary(request):
    acc_data = expences.objects.all()
    acc_form = Accounts_Form()

    return render(request,'stu_details/summary.html',{'form':acc_form,'data':acc_data})