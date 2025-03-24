from django.db import models

# Create your models here.

class Duration(models.Model):

    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value

class Batch(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value
class Gender(models.Model):
    value = models.CharField(max_length=6)

    def __str__(self):
        return self.value

class courses(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    def __str__(self):
        return self.Name   

    


class students(models.Model):
    Name = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    Mobile_no = models.IntegerField()
    Address = models.CharField(max_length=50)
    Selected_course = models.ForeignKey(courses, on_delete=models.SET_NULL,null=True,default='Select One')
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE, null=True)
    Fees = models.IntegerField(null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,null=True)
    Total = models.IntegerField(default=00)
    blnc_amount = models.IntegerField(null=True)
    
    def save(self, *args, **kwargs):
        # Automatically set the price based on the selected course
        if self.blnc_amount == None:
            self.blnc_amount = self.Fees 
        if self.Selected_course:
            self.Fees = self.Selected_course.Price       
            super().save(*args, **kwargs)
        
    def __str__(self):
        return self.Name
    

class admission(models.Model):
    Stu_id = models.IntegerField()
    Course_id = models.IntegerField()
    Price = models.IntegerField()
    Batch = models.CharField(max_length=50)
    Duration = models.IntegerField()


class billing(models.Model):
    bill_no = models.CharField(max_length=5)
    stu_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, null = True)
    paid_date = models.DateField(auto_now_add=True) 
    total_paid = models.IntegerField(default=0)
    current_paid = models.IntegerField(default=0)
    balance_amount = models.IntegerField(null =True)
    def generate_bill_no(self):
        # Get the latest bill number
        last_invoice = billing.objects.all().order_by('id').last()

        # Start with a default number if no invoices exist
        if last_invoice:
            last_number = int(last_invoice.bill_no.split('-')[-1])
            new_number = last_number + 1
        else:
            # Starting from BILL-0001 if no invoices exist
            new_number = 1

        # Generate the new bill number with leading zeros (e.g., BILL-0002)
        return f"TS-{new_number:04d}"

    def save(self, *args, **kwargs):
        if self.total_paid == 0 :
            self.total_paid = self.current_paid
        if not self.bill_no:
            self.bill_no = self.generate_bill_no()
        super(billing, self).save(*args, **kwargs)

class accounts(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    total_collection = models.IntegerField()
    pending_amount = models.IntegerField()
    expences = models.IntegerField()
class expences(models.Model):
    c_date = models.DateTimeField(auto_now_add=True,null = True)
    date = models.DateField(auto_now_add=False,null=True)
    Expence_detail = models.CharField(max_length=50,null = True)
    Expence_Amount = models.IntegerField(null = True)
    closing_balance = models.FloatField(null = True)
    opening_balance = models.FloatField(null = True)
    Total_Expences = models.FloatField(null = True)

