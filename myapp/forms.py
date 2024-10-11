from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField()

    designation=forms.CharField()

    department=forms.CharField()

    salary=forms.IntegerField()

    contact=forms.IntegerField()

    address=forms.CharField()


    def clean(self):

        cleaned_data=super().clean()

        salary=cleaned_data.get("salary")

        if int(salary<50000):
            error_message="invaild salary"

            self.add_error("salary",error_message)

        if int(salary>100000):
            error_message="invaild salary"

            self.add_error("salary",error_message)

