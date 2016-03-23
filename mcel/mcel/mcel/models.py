import peewee
from peewee import *
from flask_login import UserMixin
import datetime


db = MySQLDatabase("customers", host="localhost", user="root", passwd="T@wana03", port=3306)


class MySQLModel(Model):
    class Meta:
        database = db

              
      
class Customer(MySQLModel):
    idCustomer = PrimaryKeyField(),
    firstname = CharField(max_length=100),
    lastname = CharField(max_length=100),
    gender = CharField(max_length=6),
    idtype = CharField(max_length=15)
    idnum = CharField(unique=True),
    dateofbirth = DateField(),
    nationality = CharField(max_length=100)
    phonenum = CharField(max_length=15),
    mobilenum = CharField(max_length=15),
    emailaddress = CharField(unique=True),
    address1 = CharField(max_length=100),
    address2 = CharField(max_length=100),
    towncity = CharField(max_length=45),
    country = CharField(max_length=45),
    prefchannel = CharField(max_length=15),
    existingcustomer = BooleanField(),
    msisdns = CharField(max_length=100),
    employment = CharField(max_length=45),
    employer = CharField(max_length=100),
    position = CharField(max_length=45),
    companysize = CharField(max_length=20),
    employmenttenure = CharField(max_length=15),
    monthlyincome = FloatField(),
    accounttype = CharField(max_length=15),
    accountnum = CharField(max_length=25),
    bankname = CharField(max_length=25),
    branch = CharField(max_length=25),
    currency = CharField(max_length=3),
    yearsopen = IntegerField(),
    monthsopen = IntegerField(),
    bankcertname = CharField(max_length=15),
    bankcertpos = CharField(max_length=15),
    billingtype = CharField(max_length=25),
    billingaccount = CharField(max_length=25),
    securitynum = CharField(max_length=5)
    billemail = BooleanField(),
    receivepromos = BooleanField(),
    promoby = CharField(max_length=5)
    
                          

class Package(MySQLModel):
    idPackage = PrimaryKeyField(),
    pname = CharField(max_length=45),
    pdescription = CharField(max_length=120),  
    ptype = CharField(max_length=15),
    category = CharField(max_length=15),
    minutes = IntegerField(),
    datamb = IntegerField(),
    sms = IntegerField(),
    monthlyfee = FloatField(),
    gadget = CharField(3),
    gadgettype = CharField(max_length=45)
                

    
class Application(MySQLModel):
    idApp = PrimaryKeyField(),
    idCustomer = ForeignKeyField(rel_model=Customer, related_name='application'),
    idPackage = IntegerField(),
    category = CharField(max_length=15),
    numlines = IntegerField(),
    numgadgets = IntegerField(),
    gadgettype = CharField(max_length=45),
    proofid = CharField(max_length=100),
    proofres = CharField(max_length=100),
    bankstatement = CharField(max_length=100),
    ddform = CharField(max_length=100),
    appstatus = CharField(max_length=15)
                     

db.connect()



