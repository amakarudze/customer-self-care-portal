from flask_wtf import Form
from wtforms import (TextField, SubmitField, PasswordField, 
                     RadioField, SelectField, TextAreaField, StringField)
from wtforms import BooleanField, DateField, DateTimeField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length




class SignInForm(Form):
  email = StringField("Email", validators = [DataRequired(), Email()]) 
  password = PasswordField("Password", validators = [DataRequired()])
 

  
      
class SignUpForm(Form):
  fname = TextField("First Name(s)", validators = [DataRequired()])
  lname = TextField("Last Name", validators = [DataRequired()])
  email = TextField("Email Address", validators = [DataRequired(), Email(), EqualTo('confirm', message='Email addresses must match')])
  confirm = TextField("Confirm Email", validators = [DataRequired(), Email()])
  password = PasswordField("Password", validators = [DataRequired(), Length(min=8), EqualTo('confirmp', message='Passwords must match!')])
  confirmp = PasswordField("Confirm Password", validators = [DataRequired()])
  



class CreateProfile(Form):
  firstname = TextField("First Name(s)", validators = [DataRequired()])
  lastname = TextField("Last Name", validators = [DataRequired()])
  gender = SelectField("Gender", validators = [DataRequired()])
  idtype = SelectField("ID Type", validators = [DataRequired()])
  idnum = TextField("ID Number",  validators = [DataRequired()])
  dateofbirth = DateField("Date of Birth", validators = [DataRequired()])
  nationality = SelectField("Nationality", validators = [DataRequired()])




class UpdateProfile(Form):
  firstname = TextField("First Name(s)")
  lastname = TextField("Last Name")
  gender = SelectField("Gender", validators = [DataRequired()])
  idtype = SelectField("ID Type", validators = [DataRequired()])
  idnum = TextField("ID Number",  validators = [DataRequired()])
  dateofbirth = DateField("Date of Birth", validators = [DataRequired()])
  nationality = SelectField("Nationality", validators = [DataRequired()])
  
  


class ContactDetails(Form):
    phonenum = TextField("Phone Number")
    mobilenum = TextField("Mobile/Cell Number",  validators = [DataRequired()])
    emailaddress = TextField("Email Address", validators = [DataRequired(), Email()])
    address1 = TextField("Address Line 1",  validators = [DataRequired()])
    address2 = TextField("Address Line 2")
    towncity = SelectField("Town/City",  validators = [DataRequired()])
    country = SelectField("Country",  validators = [DataRequired()])
    prefchannel = SelectField("Preferred Communication Channel",  validators = [DataRequired()])




class UpdateContacts(Form):
    phonenum = TextField("Phone Number")
    mobilenum = TextField("Mobile/Cell Number",  validators = [DataRequired()])
    emailaddress = TextField("Email Address")
    address1 = TextField("Address Line 1",  validators = [DataRequired()])
    address2 = TextField("Address Line 2")
    towncity = SelectField("Town/City",  validators = [DataRequired()])
    country = SelectField("Country",  validators = [DataRequired()])
    prefchannel = SelectField("Preferred Communication Channel",  validators = [DataRequired()])




class SubscriberDetails(Form):
    existingcustomer = SelectField("Current mcel customer",  validators = [DataRequired()])
    msisdn = TextField("Current mcel number",  validators = [DataRequired()])
    category = SelectField("Category", validators = [DataRequired()])
    package = SelectField("Package", validators = [DataRequired()])
    
  


class EmploymentDetails(Form):
   employmenttype = SelectField("Employment Type", validators = [DataRequired()])
   company = TextField("Company Name", validators = [DataRequired()])
   position = TextField("Position", validators = [DataRequired()])
   companysize = SelectField("Company Size", validators = [DataRequired()])
   employmenttenure = SelectField("Years with Company", validators = [DataRequired()])
   monthlyincome = TextField("Monthly Income", validators = [DataRequired()])
   
   

   
class ApplicationForm(Form):
    package = SelectField("Packages", validators = [DataRequired()])
    category = SelectField("Type", validators = [DataRequired()])
    numlines = TextField("Number of lines", validators = [DataRequired()])
    numgadgets = TextField("Number of gadgets/phones", validators = [DataRequired()])
    gadgettype = SelectField("Gadget/Phone Type", validators = [DataRequired()])
    billemail = SelectField("Receive bill by email", validators = [DataRequired()])
    receivepromos = SelectField("Receive information on promotions", validators = [DataRequired()])
    promoby = SelectField("Receive information on promotions by", validators = [DataRequired()])
    


class UploadDocuments(Form):
    proofid = TextField("Proof of identification", validators = [DataRequired()])
    proofres = TextField("Proof of residence", validators = [DataRequired()])
    bankstatement = TextField("Bank Statement", validators = [DataRequired()])
    ddform = TextField("Direct Debit Order Form", validators = [DataRequired()])

 
       
class ContactForm(Form):
    name = TextField("Full Name", validators = [DataRequired()])
    phone = TextField("Cell/Phone Number", validators = [DataRequired()])
    email = TextField("Email Address", validators = [DataRequired(), Email()])
    subject = TextField("Subject", validators = [DataRequired()])
    messagem = TextAreaField("Message", validators = [DataRequired()])
    



class BillingInfo(Form):
    accounttype = SelectField("Account Type", validators = [DataRequired()])
    accountnum = TextField("Account Number", validators = [DataRequired()])
    bankname = SelectField("Bank Name", validators = [DataRequired()])
    branch = TextField("Branch", validators = [DataRequired()])
    currency = SelectField("Currency", validators = [DataRequired()])
    yearsopen = TextField("Years Open", validators = [DataRequired()])
    monthsopen = TextField("Months Open", validators = [DataRequired()])
    bankcertname = TextField("Bank Certification", validators = [DataRequired()])
    bankcertpos = TextField("Bank Certification Cargo", validators = [DataRequired()])


class PaymentInfo(Form):
    billingtype = SelectField("Account Type", validators = [DataRequired()]) 
    billingaccount = TextField("Card Number", validators = [DataRequired()])
    securitynum = TextField("Security Number", validators = [DataRequired()])
    cardholder = TextField("Card Holder", validators = [DataRequired()])




class SelectPackage(Form):
    monthlyincome = TextField("Monthly Income", validators = [DataRequired()])
    
   


class ChangePasswordForm():
    oldpassword = PasswordField("Old Password", validators = [DataRequired(), Length(min=8)])
    newpassword = PasswordField("New Password", validators = [DataRequired(), Length(min=8), EqualTo('confirmp', message='Passwords must match!')])
    confirmp = PasswordField("Confirm Password", validators = [DataRequired()])
    signup = SubmitField("Change Password")