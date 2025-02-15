from django.db import models
from django.contrib.auth.models import User

# Create your models here.


###############  FARMER FIELD  #######################

# Choices for gender, land ownership, selling options, etc.
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

LAND_OWNERSHIP_CHOICES = [
    ('Owner', 'Owner'),
    ('Tenant', 'Tenant'),
]

SELLING_OPTIONS = [
    ('Direct Sale To Consumer/Retailer/Food_Processor', 'Direct Sale To Consumer//Retailer/Food_Processor'),
    ('Direct Sale To farmRule', 'Direct Sale To farmRule'),
]

LANGUAGE_CHOICES = [
    ('Telugu', 'Telugu'),
    ('Hindi', 'Hindi'),
    ('English', 'English'),
]

YES_NO_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]



class Farmer(models.Model):

    # 1️ Basic Information
    user = models.OneToOneField(User,default=True, on_delete=models.CASCADE )  # Link Farmer to User
    full_name = models.CharField(max_length=255, default=True)
    mobile_number = models.CharField(max_length=20, unique=True, default=True)  # OTP verification needed
    aadhaar_number = models.CharField(max_length=20, unique=True, default=True)  # Aadhaar for verification
    date_of_birth = models.DateField(default=True, auto_created=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, default=True)
    email=models.CharField(max_length=100,default=True)

    # 2️ Location & Land Details
    state = models.CharField(max_length=100, default="Unknown")
    district = models.CharField(max_length=100, default="Unknown")
    village_town = models.CharField(max_length=100, default="Unknown")
    pincode = models.CharField(max_length=6, default="000000")
    land_ownership = models.CharField(max_length=10, choices=LAND_OWNERSHIP_CHOICES, default="Owner")
    land_area = models.FloatField(default=0.0, help_text="Land area in acres or hectares")

    # 3️ Banking & Payment Details
    bank_account_number = models.CharField(max_length=20, default="0000000000")
    ifsc_code = models.CharField(max_length=11, default="00000000000")
    upi_id = models.CharField(max_length=50, blank=True, null=True)  # Optional field

    # 4️ Crop & Market Preferences
    main_crops_grown = models.TextField(default="None", help_text="Comma-separated crop names")
    selling_option = models.CharField(max_length=50, choices=SELLING_OPTIONS, default="Direct Sale")
    expected_harvest_season = models.CharField(max_length=100, default="Unknown")

    # 5️ Document Uploads (Optional in Phase-1)
    aadhaar_card = models.FileField(upload_to='documents/farmer/aadhaar/', blank=True, null=True)
    land_ownership_certificate = models.FileField(upload_to='documents/farmer/land/', blank=True, null=True)
    bank_passbook = models.FileField(upload_to='documents/farmer/bank/', blank=True, null=True)

    # 6️ Additional Features
    preferred_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default="English")
    ai_chatbot_assistance = models.CharField(max_length=3, choices=YES_NO_CHOICES, default="No")
    weather_market_alerts = models.CharField(max_length=3, choices=YES_NO_CHOICES, default="No")
    terms_and_conditions = models.BooleanField(default=False)  # Check box for terms and conditions

    def __str__(self):
        return self.full_name










##################  CONSUMER FIELD  #########################


class ConsumerType(models.TextChoices):
    CONSUMER='Consumer', 'Consumer'
    RETAILER='Rteailer', 'Retailer'
    FOOD_PROCESSOR='Food Processor', 'Food Processor'
    OTHER='Other','Other'

class PurchaseMethod(models.TextChoices):
    DIRECT_FROM_FARMER='Direct From Farmer','Direct From Farmer'
    DIRECT_FROM_COMPANY='Direct From Company','Direct From Company'


    

class Consumer(models.Model):
    # 1️ Basic Information
    full_name=models.CharField(max_length=200)
    business_name=models.CharField(max_length=200, blank=True, null=True) #optional field
    mobile_number=models.CharField(max_length=15,unique=True) #must be unique
    email=models.CharField(unique=True)#must be unique
    consumer_type=models.CharField(max_length=50, choices=ConsumerType.choices, default=ConsumerType.CONSUMER)

    # 2️ Business & Location Details (If Not Consumer)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)  # PAN number is optional for consumers
    address = models.TextField(blank=True, null=True)
    warehouse_location = models.TextField(blank=True, null=True)

    # 3️ Banking & Payment Details
    bank_account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    upi_id = models.CharField(max_length=50, blank=True, null=True)  # Optional 

    # 4️ Purchase Preferences
    crops_intrested_in=models.TextField()
    prefered_buying_method=models.CharField(max_length=20, choices=PurchaseMethod.choices, default=PurchaseMethod.DIRECT_FROM_FARMER)
    average_buying_quantity=models.PositiveIntegerField() #monthly purchase quantity in ton or kg

    # 5️ Documents Upload (For Verification, If Not Consumer)
    gst_certificate=models.FileField(upload_to='documents/consumer/', blank=True, null=True)
    pan_card=models.FileField(upload_to='documents/consumer/', blank=True, null=True)
    business_license=models.FileField(upload_to='documents/consumer/', blank=True, null=True)



    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name if self.consumer_type == 'Consumer' else self.business_name or self.full_name