from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE) # if user is deleted, delete all associated
  image = models.ImageField(default = 'profile_pics/empty.jpg', upload_to = 'profile_pics')
  title = models.CharField(max_length = 255)
  location = models.CharField(max_length = 255)
  about = models.TextField()
  
  def __str__(self):
    return f'{self.user.username} - {self.title}';

class Profiles_on_db(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE) # if user is deleted, delete all associated
  search_score = models.FloatField(null = True, blank = True)
  about_me = models.TextField(null = True, blank = True)
  ask_me_about = models.TextField(null = True, blank = True)
  business_Unit = models.TextField(null = True, blank = True)
  certifications_Accreditations = models.TextField(null = True, blank = True)
  company_Name_1 = models.TextField(null = True, blank = True)
  company_Name_2 = models.TextField(null = True, blank = True)
  company_Name_3 = models.TextField(null = True, blank = True)
  company_Name_4 = models.TextField(null = True, blank = True)
  company_Name_5 = models.TextField(null = True, blank = True)
  company_Name_6 = models.TextField(null = True, blank = True)
  company_Name_7 = models.TextField(null = True, blank = True)
  department = models.TextField(null = True, blank = True)
  discipline = models.TextField(null = True, blank = True)
  education = models.TextField(null = True, blank = True)
  function = models.TextField(null = True, blank = True)
  job_Title = models.TextField(null = True, blank = True)
  last_Updated = models.TextField(null = True, blank = True) # could be date field if you have 
  location_1 = models.TextField(null = True, blank = True)
  location_2 = models.TextField(null = True, blank = True)
  location_3 = models.TextField(null = True, blank = True)
  location_4 = models.TextField(null = True, blank = True)
  location_5 = models.TextField(null = True, blank = True)
  location_6 = models.TextField(null = True, blank = True)
  location_7 = models.TextField(null = True, blank = True)
  name = models.TextField(null = True, blank = True)
  professional_Memberships = models.TextField(null = True, blank = True)
  profile_Complete = models.TextField(null = True, blank = True)
  publications = models.TextField(null = True, blank = True)
  ref_Indicator = models.TextField(null = True, blank = True)
  job_Title = models.TextField(null = True, blank = True)
  role_1 = models.TextField(null = True, blank = True)
  role_2 = models.TextField(null = True, blank = True)
  role_3 = models.TextField(null = True, blank = True)
  role_4 = models.TextField(null = True, blank = True)
  role_5 = models.TextField(null = True, blank = True)
  role_6 = models.TextField(null = True, blank = True)
  role_7 = models.TextField(null = True, blank = True)
  role_Description_1 = models.TextField(null = True, blank = True)
  role_Description_2 = models.TextField(null = True, blank = True)
  role_Description_3 = models.TextField(null = True, blank = True)
  role_Description_4 = models.TextField(null = True, blank = True)
  role_Description_5 = models.TextField(null = True, blank = True)
  role_Description_6 = models.TextField(null = True, blank = True)
  role_Description_7 = models.TextField(null = True, blank = True)
  shell_Business = models.TextField(null = True, blank = True)
  skills = models.TextField(null = True, blank = True)
  timespan_1 = models.TextField(null = True, blank = True)
  timespan_2 = models.TextField(null = True, blank = True)
  timespan_3 = models.TextField(null = True, blank = True)
  timespan_4 = models.TextField(null = True, blank = True)
  timespan_5 = models.TextField(null = True, blank = True)
  timespan_6 = models.TextField(null = True, blank = True)
  timespan_7 = models.TextField(null = True, blank = True)
  unique_id = models.TextField(null = True, blank = True, unique = True) # might run into naming stuff as: unique_id != id

  '''
  dict_keys(['@search.score', 'About_me', 'Ask_me_about', 'Business_Unit', 'Certifications_Accreditations', 'Company_Name_1', 'Company_Name_2', 'Company_Name_3', 'Company_Name_4', 'Company_Name_5', 'Company_Name_6', 'Company_Name_7', 'Department', 'Discipline', 'Education', 'Function', 'Job_Title', 'Last_Updated', 'Location_1', 'Location_2', 'Location_3', 'Location_4', 'Location_5', 'Location_6', 'Location_7', 'Name', 'Professional_Memberships', 'Profile_Complete', 'Publications', 'Ref_Indicator', 'Role_1', 'Role_2', 'Role_3', 'Role_4', 'Role_5', 'Role_6', 'Role_7', 'Role_Description_1', 'Role_Description_2', 'Role_Description_3', 'Role_Description_4', 'Role_Description_5', 'Role_Description_6', 'Role_Description_7', 'Shell_Business', 'Skills', 'Timespan_1', 'Timespan_2', 'Timespan_3', 'Timespan_4', 'Timespan_5', 'Timespan_6', 'Timespan_7', 'id'])
  '''
  
  def __str__(self):
    return f'{self.unique_id}';
