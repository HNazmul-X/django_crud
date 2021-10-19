from django.shortcuts import redirect, render
from .models import EmployeeModel, Position

# Create your views here.
def employee_list(request):
    allEmployee = EmployeeModel.objects.all()
    return render(request, "employe/employee_list.html",{"allEmployee":allEmployee})
        
def employee_form(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        empCode = request.POST["empCode"]
        mobile = request.POST["mobile"]
        position = request.POST["position"]
        x = Position.objects.get(pk = position)
        EmployeeModel(fullname=fullname, empCode=empCode,mobile=mobile, position=x).save()
        return redirect("employee_list")
    else:
        allPositions = Position.objects.all()
        return render(request, "employe/employee_form.html", {"all_positions": allPositions})



def employee_update(request,id):
    employee = EmployeeModel.objects.get(pk=id)
    positions = Position.objects.all()
    if request.method =="POST":
            newName = request.POST["fullname"] if request.POST["fullname"] != None else employee["fullname"]
            newPosition = Position.objects.get(title=request.POST["position"]) or employee["position"]
            newEmpCode = request.POST["empCode"] or employee["empCode"]
            newMobile = request.POST["mobile"] or employee["mobile"]
            print(newPosition)
            EmployeeModel.objects.filter(pk=id).update(fullname=newName,position=newPosition,empCode=newEmpCode,mobile=newMobile)
            return redirect("employee_list")
    return render(request,"employe/employee_update.html",{"exitingData":employee,"all_positions":positions})


def deleteEmployee(request,id):
    EmployeeModel.objects.get(pk=id).delete()
    return redirect("employee_list")
