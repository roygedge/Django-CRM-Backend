from django.db import models

class LandingPageField():
    field_name = models.CharField(max_length=100)
    input_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)

class Campaign(models.Model):
    # Settings
    client_name = models.CharField(max_length=100)
    campaign_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    encoding_type = models.CharField(max_length=100)
    # All the landing page fields.
    landing_page_fields = models.ManyToManyField(LandingPageField)
    email = models.EmailField()
    send_leads_to_mail = models.BooleanField(default=False)
    send_phone_leads_to_mail = models.BooleanField(default=False)
    show_new_phone_lead_to_all_managers = models.BooleanField(default=False)
    fixed_cost_per_lead = models.IntegerField() # In dollars.
    distribute_leads_equally_among_all_sales = models.BooleanField(default=False)
    #TODO: Add remarks and sales representative.

    # Time and Budget
    start_date = models.DateField()
    end_date = models.DateField()
    general_budget = models.IntegerField() # In dollars.
    monthly_budget = models.IntegerField() # In dollars.
    daily_budget = models.IntegerField() # In dollars.
    status = models.CharField(max_length=100)
    number_of_days_for_lead_activity =  models.IntegerField()

    # More settings
    ministe_number = models.CharField(max_length=100)
    account_manager = models.CharField(max_length=100)
    media_manager = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    advertising_agency = models.CharField(max_length=100)
    
    # Whatsapp 
    country_code = models.CharField(max_length=100) # Used for marketing Whatsapp calls.
    default_message = models.CharField() # For Whatsapp.


    # Feedback
    is_send_sms = models.BooleanField(default=False)
    is_send_email = models.BooleanField(default=False)
    sms_message_content = models.CharField(max_length=200)
    sms_name = models.CharField(max_length=100)
    sms_number = models.CharField(max_length=100)
    sms_start_hour =  models.CharField(max_length=100) # HH:MM format
    sms_end_hour =  models.CharField(max_length=100) # HH:MM format
    email_sender_name =  models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100)
    email_subject = models.CharField(max_length=100)
    email_body = models.CharField() #TODO: Support in font and size and color etc...

    # Data boradcast
    broadcast_method = models.CharField(max_length=100)
    boradcast_format = models.CharField(max_length=100)
    link = models.CharField()
    post_fields_only = models.CharField()
    data_field = models.CharField(max_length=100)
    is_repeated_broadcast = models.BooleanField(default=False)
    successful_broadcast_string =  models.CharField(max_length=100)
    braodcast_internet_lead = models.BooleanField(default=False)
    broeadcast_phone_lead = models.BooleanField(default=False)
    time_to_broadcast_phone_lead = models.CharField(max_length=100)
    is_broadcast_phone_lead_same = models.BooleanField(default=True)
    broadcast_phone_lead = models.CharField(max_length=100)




    


