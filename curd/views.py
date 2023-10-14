from django.shortcuts import render,redirect
from django.http import JsonResponse
from curd.models import Employees


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        employee = Employees.objects.create(name=name, email=email, address=address, phone=phone)
        return redirect('/')     
    emp = Employees.objects.all()
    context = {
        'emp':emp
    }
    return render(request,'main.html',context)


def singleEmpData(request,emp_id):
    employee = Employees.objects.get(id=emp_id)
    data = {
        'name':employee.name,
        'email':employee.email,
        'address':employee.address,
        'phone':employee.phone    
        }
    return JsonResponse(data)


def updateEmp(request,emp_id):
    employee = Employees.objects.get(id=emp_id)
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    employee.name = name
    employee.email = email
    employee.address = address
    employee.phone = phone
    employee.save()
    return redirect('/')

def deleteEmp(request,emp_id):
    Employees.objects.get(id=emp_id).delete()
    return redirect('/')
        