from django.shortcuts import render ,redirect

from django.views.generic import View

from django.contrib import messages

from myapp.forms import EmployeeForm

from myapp.models import Employee







class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"employee_add.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance= EmployeeForm(request.POST)

        if form_instance.is_valid():
            
            data=form_instance.cleaned_data

            Employee.objects.create(**data)

            messages.success(request,"employee has been added")

            return redirect("employee-list")
    

        else:
             messages.error(request,"employee has not been added")

             return render(request,"employee_add.html",{"form":form_instance})
        


class EmployeeListView(View):

    def get(self,request,*args,**kwargs):
        
        qs=Employee.objects.all()

        return render(request,"employee_list.html",{"employee":qs})
       
       

      
class EmployeeDetailsView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)

        return render(request,"employee_details.html",{"employee":qs})
       
       
        
class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id).delete()

        messages.success(request,"employee deleted")

        return redirect("employee-list")
       
       


class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)


        dictionary={

            "name":qs.name,
            "designation":qs.designation,
            "department":qs.department,
            "salary":qs.salary,
            "contact":qs.contact,
            "address":qs.address


        }

        form_instance=EmployeeForm(initial=dictionary)

        return render(request,"employee_edit.html",{"form":form_instance})
    

       

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)
        id=kwargs.get("pk")

        if form_instance.is_valid():

            
            data=form_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)
            messages.success(request,"employee has been updated")

            return redirect("employee-list")
        
        else:

            return render(request,"employee_edit.html",{"form":form_instance})




       

                    

    


   


        
 

