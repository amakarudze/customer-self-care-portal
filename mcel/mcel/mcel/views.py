"""
Routes and views for the flask application.
"""

import mysql.connector, datetime, re, os



from datetime import datetime
from flask import (render_template, redirect, request, get_flashed_messages, 
                   flash, Flask, url_for, session)
from flask_bcrypt import generate_password_hash, check_password_hash, Bcrypt
from flask_login import (current_user, login_required, login_user, logout_user, 
                         LoginManager, UserMixin)
from flask_mail import Mail, Message
from flask_wtf import CsrfProtect
from peewee import *
from itsdangerous import URLSafeTimedSerializer
from mcel import app
from mcel import forms, models 



bcrypt = Bcrypt(app)
csrf = CsrfProtect(app)


app.secret_key = 'hwiehoiefbvfepjocwnev,hifeuoipef.ceuefug!bdcuioefbfeifvboefgoefvfekef$%&^*#@shgjkfiogbjghuirh'



login_manager = LoginManager()
login_manager.login_view = 'signin'
login_manager.session_protection = "strong"
login_manager.setup_app(app)
login_serializer = URLSafeTimedSerializer(app.secret_key)



app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'anntelebiz@gmail.com'
app.config["MAIL_PASSWORD"] = 'T@wana03'
 

mail = Mail()
mail.init_app(app)


conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
mycursor=conn.cursor()


UPLOAD_FOLDER = '/uploads/'
ALLOWED_EXTENSIONS = set(['doc', 'pdf', 'docx', 'jpg', 'jpeg', 'gif', 'png'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == "__main__":   
    app.config["REMEMBER_COOKIE_DURATION"] = datetime.timedelta(days=7)
   



@csrf.error_handler
def csrf_error(reason):
    return render_template('csrf_error.html', reason=reason), 400

  

class User(UserMixin):
   idUser = IntegerField(primary_key=True)
   fname = CharField(max_length=100), 
   lname = CharField(max_length=100),
   email = CharField(unique=True),
   password = CharField(max_length=100),
   membersince = DateTimeField(default=datetime.now)


   def __init__(self, email, password):
       self.id = email
       self.password = password

   def get_auth_token(self):
        data = [str(self.id), self.password]
        return login_serializer.dumps(data)
 
   @staticmethod
   def get(email):
        conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
        mycursor=conn.cursor()
        mycursor.execute("SELECT email, password from user where email = email")
        users = mycursor.fetchall()
        for user in users:
            if user[0] == email:
                return User(user[0], user[1])
        return None

   def get_id(self):
        return str(self.id)

   def is_active(self):
        return True

   def is_anonymous(self):
        return False

   def is_authenticated(self):
        return True
 
      
   
@login_manager.user_loader
def load_user(email):
    return User.get(email)
    


@login_manager.token_loader
def load_token(token):
    max_age = app.config["REMEMBER_COOKIE_DURATION"].total_seconds()
 
    data = login_serializer.loads(token, max_age=max_age)
 
    user = User.get(data[0])
 
    if user: 
        return user
    return None


   
    
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    user_id = (current_user.get_id() or "No User Logged In")
    return render_template('index.html', title='Home Page', year=datetime.now().year, user_id=user_id)



@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    """Renders the contact page."""
    form = forms.ContactForm()
    user_id = (current_user.get_id() or "No User Logged In")
     
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            return render_template('contact.html', title='Contact', 
                           year=datetime.now().year, message='mcel Contact Details', form=form)
        else:
            msg = Message(form.subject.data, sender='anntelebiz@gmail.com', recipients=['amakarudze@gmail.com'])
            msg.body = """
            From: %s <%s>
            
            Phone: %s 
            Subject: %s 
            Message: %s""" % (form.name.data, form.email.data, form.phone.data, form.subject.data, form.messagem.data)
            mail.send(msg)
 
            flash("Message sent.", "success")

    if request.method == 'GET':
        return render_template('contact.html', title='Contact', 
                           year=datetime.now().year, message='mcel Contact Details', form=form, user_id=user_id)



@app.route('/about')
def about():
    """Renders the about page."""
    user_id = (current_user.get_id() or "No User Logged In")
    return render_template('about.html', title='About', year=datetime.now().year,
        message='About mcel', user_id=user_id)



@app.route('/packages', methods=['GET', 'POST'])
def packages():
    """Renders the about page."""
    user_id = (current_user.get_id() or "No User Logged In")
    form = forms.SelectPackage()

    if request.method == 'GET':
        acceptedfee = 10000.00
        p_query = ("select pname, pdescription, ptype, category, minutes, " 
                    "datamb, sms, monthlyfee, gadget, gadgettype from package")
        conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
        mycursor=conn.cursor()
        mycursor.execute(p_query)
        
        packages_available = [dict(pname=row[0], pdescription=row[1], ptype=row[2], category=row[3],
                                   minutes=row[4], datamb=row[5], sms=row[6], monthlyfee=row[7],
                                   gadget=row[8], gadgettype=row[9]) for row in mycursor.fetchall()]
        return render_template('packages.html', title='Packages', year=datetime.now().year,
                    message='Packages:', form=form, packages_available=packages_available, acceptedfee=acceptedfee, user_id=user_id)
        
        mycursor.close()
        conn.close() 

        
    if request.method == 'POST':
        if form.validate_on_submit == False:
            flash("Please enter your monthly income.")
            return render_template('packages.html', title='Packages', year=datetime.now().year,
                    message='Packages:', form=form, packages_available=packages_available, acceptedfee=acceptedfee, user_id=user_id)
        else:
            monthlyincome = int(form.monthlyincome.data)
            num = 9
            
            acceptedfee = monthlyincome / num
            acceptedmonthlyfee = int(acceptedfee)
            p_query = ("select pname, pdescription, ptype, category, minutes, " 
                    "datamb, sms, monthlyfee, gadget, gadgettype from package")
                   
            conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
            mycursor=conn.cursor()
            mycursor.execute(p_query)
        
            packages_available = [dict(pname=row[0], pdescription=row[1], ptype=row[2], category=row[3],
                                   minutes=row[4], datamb=row[5], sms=row[6], monthlyfee=row[7],
                                   gadget=row[8], gadgettype=row[9]) for row in mycursor.fetchall()]
               
            mycursor.close()
            conn.close() 
            
            return render_template('packages.html', title='Packages', message='Packages:', acceptedmonthlyfee=acceptedmonthlyfee, 
                                   acceptedfee=acceptedfee, packages_available=packages_available, form=form, user_id=user_id)

    
     

@app.route('/applyindividual',  methods=['GET', 'POST'])
@login_required
def applyindividual():
    """Renders the apply page."""
    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
    form = forms.ApplicationForm()

    form.package.choices = [('1', 'Ola 30'), ('2', 'Ola 60'), ('3', 'Ola 120'), ('4', 'Ola 500'), ('5', 'Net Giro')]
    form.category.choices = [('Prepaid', 'Prepaid'), ('Postpaid', 'Postpaid'), ('NTDUO', 'NTDUO')]
    form.gadgettype.choices = [('Blackbery', 'Blackbery'), ('iPhone', 'iPhone'), ('Samsung', 'Samsung'), ('Nokia', 'Nokia')]
    form.billemail.choices = [('Yes', 'Yes'), ('No', 'No')]
    form.receivepromos.choices = [('Yes', 'Yes'), ('No', 'No')]
    form.promoby.choices = [('Email', 'Email'), ('SMS', 'SMS'), ('Phone', 'Phone')]

    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]
    else:
        flash("Please create your profile.", "error")


    if request.method == 'POST':
        if form.validate_on_submit == False:
            return render_template('applyindividual.html', title='Individual Application',  message='Individual Package Application',
        year=datetime.now().year, form=form, user_id=user_id)

        else:
            try:
                add_app = ("INSERT INTO application "
                "(idCustomer, idPackage, category, numlines, numgadgets, gadgettype, "
                "appstatus, billemail, receivepromos, promoby, dateapplied) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                
                idPackage = int(form.package.data)
                category = form.category.data
                numlines = form.numlines.data
                numgadgets = form.numgadgets.data
                gadgettype = form.gadgettype.data
                appstatus = "Pending"
                billemail = form.billemail.data
                receivepromos = form.receivepromos.data
                promoby = form.promoby.data
                dateapplied = datetime.now()
            
                app_data = (idCustomer, idPackage, category, numlines, numgadgets, gadgettype, 
                            appstatus, billemail, receivepromos, promoby, dateapplied)
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(add_app, app_data)
                conn.commit()
                idApp = mycursor.lastrowid
                mycursor.close()
                conn.close() 
                flash("Thank you. Please upload required documents to complete your application. "
                      "The reference number for your application is {}.". format(idApp), "success")
                return redirect(url_for('billinginfo'))
                  
            except models.IntegrityError:
                raise ValueError("User already has open applications.", "error")
                return render_template('applyindividual.html', title='Individual Application',  message='Individual Package Application',
                                        year=datetime.now().year, form=form, user_id=user_id)
    if request.method == 'GET':
                   
        id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
        conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
        mycursor=conn.cursor()
        mycursor.execute(id_query, (user_id, ))
        customer_id = mycursor.fetchall()
        if customer_id:
            for cust_id in customer_id:
                if cust_id[0] == user_id:
                    idCustomer = cust_id[1]
                    return render_template('applyindividual.html', title='Individual Application', message='Individual Package Application',
                                            year=datetime.now().year, form=form, user_id=user_id)
        else:
            flash("You need to create your profile before you can apply for packages on offer.", "error")
            return redirect(url_for('createprofile', user_id=user_id))



@app.route('/uploaddocs',  methods=['GET', 'POST'])
#@login_required
def uploaddocs():
    """Renders the apply page."""
    user_id = (current_user.get_id() or "No User Logged In")
    form = forms.UploadDocuments()

    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]
    else:
        flash("You have no open applications.", "error")

    if request.method == 'POST':
        if form.validate_on_submit == False:
            return render_template('uploaddocs.html', title='Upload Documents', message='Upload Required Documents',
        year=datetime.now().year, form=form)

        else:
            try:
                upload_docs = ("""UPDATE application SET proofid=%s, proofres=%s, bankstatement=%s, ddform=%s, appstatus=%s WHERE idCustomer=%s""")
                
                proofid = form.proofid.data
                proofres = form.proofres.data
                bankstatement = form.bankstatement.data
                ddform = form.ddform.data
                appstatus = "Submitted"
                            
                docs_data = (proofid, proofres, bankstatement, ddform, appstatus, idCustomer)
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(upload_docs, docs_data)
                conn.commit()
                mycursor.close()
                conn.close() 
                flash("Thank you. Please enter your bank details to complete your application. ", "success")
                return redirect(url_for('index'))
                  
            except models.IntegrityError:
                raise ValueError("User already exists.", "error")
                return render_template('uploaddocs.html', title='Upload Documents', message='Upload Required Documents',
                                        year=datetime.now().year, form=form, user_id=user_id)
    if request.method == 'GET':
        return render_template('uploaddocs.html', title='Upload Documents', message='Upload Required Documents',
            year=datetime.now().year, form=form, user_id=user_id)
       




@app.route('/trackapplication')
@login_required
def trackapplication():
    """Renders the about page."""
    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]
    else:
        flash("You have no open applications.", "success")
                   
    if request.method == 'GET':
        t_query = ("""SELECT p1.idApp, p1.idPackage, p1.gadgettype, p1.appstatus, p1.dateapplied, p2.monthlyfee, p2.pname 
                    FROM application AS p1, package AS p2 where idCustomer=%s AND p2.idPackage=p1.idPackage""")
        mycursor.execute(t_query, (idCustomer, ))
        open_app = [dict(idApp=row[0], idPackage=row[1], gadgettype=row[2], appstatus=row[3], dateapplied=row[4],
                    monthlyfee=row[5], pname=row[6]) for row in mycursor.fetchall()]
        mycursor.close()
        conn.close() 
        return render_template('trackapplication.html', title='Track Application', 
           year=datetime.now().year, message='Open Applications', open_app=open_app, user_id=user_id)

            
            
@app.route('/profile')
@login_required
def profile():
    """Renders the about page."""
    
    user_id = (current_user.get_id() or "No User Logged In")
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]

    query = ("""select firstname, lastname, gender, dateofbirth, nationality, idtype, 
                idnum, phonenum, mobilenum, emailaddress, address1, address2, towncity, country, 
                prefchannel, existingcustomer, msisdns from customer where emailaddress=%s""")
    
    mycursor.execute(query, (user_id, ))
    user_profile = [dict(firstname=row[0], lastname=row[1], gender=row[2], dateofbirth=row[3],
                         nationality=row[4], idtype=row[5], idnum=row[6], phonenum=row[7],
                         mobilenum=row[8], emailaddress=row[9], address1=row[10], address2=row[11], towncity=row[12], country=row[13],
                         prefchannel=row[14], existingcustomer=row[15], msisdns=row[16]) for row in mycursor.fetchall()]
    if user_profile ==[]:
        return redirect(url_for('createprofile', user_id=user_id))

    emp_query = ("""select employment, employer, position, companysize, employmenttenure, 
                    monthlyincome from customer where emailaddress=%s""")
    mycursor.execute(emp_query, (user_id, ))
    emp_profile = [dict(employment=row[0], employer=row[1], position=row[2], companysize=row[3], employmenttenure=row[4],
                         monthlyincome=row[5]) for row in mycursor.fetchall()]
    
    t_query = ("""SELECT p1.idApp, p1.idPackage, p1.gadgettype, p1.appstatus, p1.dateapplied, p2.monthlyfee, p2.pname 
                FROM application AS p1, package AS p2 where idCustomer=%s AND p2.idPackage=p1.idPackage""")
      
    mycursor.execute(t_query, (idCustomer, ))
    open_app = [dict(idApp=row[0], idPackage=row[1], gadgettype=row[2], appstatus=row[3], dateapplied=row[4],
                monthlyfee=row[5], pname=row[6]) for row in mycursor.fetchall()]
    

    return render_template('profile.html', title='Profile', year=datetime.now().year,
                    message='Personal Details', user_id=user_id, user_profile=user_profile, emp_profile=emp_profile, open_app=open_app)
     
    mycursor.close()
    conn.close() 
           
             

 
@app.route('/createprofile', methods=['GET', 'POST'])
@login_required
def createprofile():
    """Renders the Create Profile Page"""
    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
    form = forms.CreateProfile()
    form.gender.choices = [('F', 'Female'), ('M', 'Male')]
    form.idtype.choices = [('Moz ID', 'Moz ID'), ('Moz Passport', 'Moz Passport'), ('Passport', 'Passport')]
    form.nationality.choices = [('Malawian', 'Malawian'), ('Mozambican', 'Mozambican'), ('South African', 'South African'), ('Zimbabwean', 'Zimbabwean')]   
    
    if request.method == 'POST':
        if form.validate_on_submit == False:
            return render_template('createprofile.html', title='Create Your Profile', form=form, user_id=user_id)
        else:
            try:
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                gender = request.form['gender']
                dateofbirth = request.form['dateofbirth']
                nationality = request.form['nationality']
                idtype = request.form['idtype']
                idnum = request.form['idnum']
                emailaddress = user_id
                
                add_customer = ("INSERT INTO customer "
                "(firstname, lastname, gender, dateofbirth, nationality, idtype, idnum, emailaddress) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                 
                customer_data = (firstname, lastname, gender, dateofbirth, nationality, idtype, idnum, emailaddress)
                
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(add_customer, customer_data)
                conn.commit()
                idCustomer = mycursor.lastrowid
                mycursor.close()
                conn.close() 
                flash("Thank you. Your profile has been created. Keep going.", "success")

                return redirect(url_for('contactdetails'))
                  
            except models.IntegrityError:
                raise ValueError("User already exists.", "error")
                return render_template('createprofile.html', title='Create Your Profile', form=form, user_id=user_id)

    if request.method == 'GET':
        if request.method == 'GET':
            cust_query = ("select firstname, lastname from customer where emailaddress=%s")
            conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
            mycursor=conn.cursor()
            mycursor.execute(cust_query, (user_id, ))
            customer = [dict(firstname=row[0], lastname=row[1]) for row in mycursor.fetchall()]
        
            if customer:
                for r in customer:
                    form.firstname.data = r.firstname
                    form.lastname.data = r.lastname
        
        mycursor.close()
        conn.close()   
        return render_template('createprofile.html', title='Create Your Profile', form=form, user_id=user_id)




@app.route('/contactdetails', methods=['GET', 'POST'])
@login_required
def contactdetails():
    """Renders the Contact Details Page"""
    user_id = (current_user.get_id() or "No User Logged In")
    form = forms.ContactDetails()
        
    form.towncity.choices = [('Beira', 'Beira'), ('Chimoio', 'Chimoio'), ('Maputo', 'Maputo'), 
                             ('Nampula', 'Nampula'), ('Sofala', 'Sofala'), ('Tete', 'Tete'), ('Other', 'Other')]
    form.country.choices = [('Mozambique', 'Mozambique'), ('Other', 'Other')]
    form.prefchannel.choices = [('Phone', 'Phone'), ('SMS', 'SMS'), ('Email', 'Email')]

    if request.method == 'POST':
        if form.validate_on_submit == False:
            return render_template('contactdetails.html', title='Contact Details', form=form, user_id=user_id)
        else:
            try:
                phonenum = request.form['phonenum']
                mobilenum = request.form['mobilenum']
                emailaddress = request.form['emailaddress']
                address1 = request.form['address1']
                address2 = request.form['address2']
                towncity = request.form['towncity']
                country = request.form['country']
                prefchannel = request.form['prefchannel']
                
                update_customer = ("""UPDATE customer SET 
                phonenum=%s, mobilenum=%s, emailaddress=%s, address1=%s, address2=%s, 
                towncity=%s, country=%s, prefchannel=%s WHERE emailaddress=%s""")
                
                customer_data = (phonenum, mobilenum, emailaddress, address1, address2, towncity, country, prefchannel, user_id)
                
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(update_customer, customer_data)
                conn.commit()
                mycursor.close()
                conn.close() 
                flash("Thank you. Your profile has been created. Keep going.", "success")
                return redirect(url_for('subscriberdetails', user_id=user_id))
                  
            except models.IntegrityError:
                raise ValueError("User already exists.", "error")
                return render_template('contactdetails.html', title='Contact Details', form=form, user_id=user_id)

    if request.method == 'GET':
        if request.method == 'GET':
            return render_template('contactdetails.html', title='Contact Details', form=form, user_id=user_id)

    


@app.route('/subscriberdetails', methods=['GET', 'POST'])
@login_required
def subscriberdetails():
    """Renders the Subscriber Details Page"""
    user_id = (current_user.get_id() or "No User Logged In")
    form = forms.SubscriberDetails()
         
    form.existingcustomer.choices = [('Yes', 'Yes'), ('No', 'No')]
    form.category.choices = [('Prepaid', 'Prepaid'), ('Postpaid', 'Postpaid'), ('NTDUO', 'NTDUO')]
    form.package.choices = [('1', 'Ola 30'), ('2', 'Ola 60'), ('3', 'Ola 120'), ('4', 'Ola 500'), ('5', 'Net Giro')]

    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]
    else:
        flash("The given profile does not exist.", "error")

    if request.method == 'POST':
        if form.validate_on_submit == False:
            return render_template('subscriberdetails.html', title='Subscriber Details', form=form, user_id=user_id)
        else:
            try:
                package = request.form['package']
                existingcustomer = request.form['existingcustomer']
                msisdn = request.form['msisdn']
                category = request.form['category']
                
                update_customer = ("""UPDATE customer SET msisdns=%s, existingcustomer=%s 
                WHERE emailaddress=%s""")

                add_package = ("""INSERT INTO customerpackage 
                		(idCustomer, idPackage, MSISDN, category) 
                		VALUES (%s, %s, %s, %s)""")
                
                customer_data = (msisdn, existingcustomer, user_id)
                customer_package = (idCustomer, package, msisdn, category)
                
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(update_customer, customer_data)
                conn.commit()
                mycursor.execute(add_package, customer_package)
                conn.commit()
                mycursor.close()
                conn.close() 
                flash("Thank you. Your profile has been created. Keep going.", "success")
                return redirect(url_for('employmentdetails'))
                  
            except models.IntegrityError:
                raise ValueError("User already exists.", "error")
                return render_template('subscriberdetails.html', title='Subscriber Details', form=form, user_id=user_id)

    if request.method == 'GET':
        return render_template('subscriberdetails.html', title='Subscriber Details', form=form, user_id=user_id)

@app.route('/employmentdetails', methods=['GET', 'POST'])
@login_required
def employmentdetails():
    """Renders the Employment Profile Page"""
    user_id = (current_user.get_id() or "No User Logged In")
    
    form = forms.EmploymentDetails()
    form.employmenttype.choices = [('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')] 
    form.companysize.choices = [('0-10', '0-10 employees'), ('11-50', '10-50 employees'), 
                                ('51-250', '51-250 employees'), ('Over 250', 'Over 250 employees')]
    form.employmenttenure.choices = [('0-2', '0-2 years'), ('3-6', '3-6 years'), ('7-10', '7-10 years'), ('Over 10', 'Over 10 years')] 

    
    if request.method == 'POST':
         if form.validate_on_submit == False:
             return render_template('employmentdetails.html', title='Employment Details', form=form, user_id=user_id)
         else:
             try:
                update_emp = ("""UPDATE customer SET
                employment=%s, employer=%s, position=%s, companysize=%s, 
                employmenttenure=%s, monthlyincome=%s
                WHERE emailaddress=%s""")
             
                employment = form.employmenttype.data
                company = form.company.data
                position = form.position.data
                companysize = form.companysize.data
                employmenttenure = form.employmenttenure.data
                monthlyincome = form.monthlyincome.data
                
                emp_data = (employment, company, position, companysize, employmenttenure, monthlyincome, user_id)
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(update_emp, emp_data)
                conn.commit()
                mycursor.close()
                conn.close() 
                flash("Thank you. Your profile has been updated.", "success")
                return redirect(url_for('profile', user_id=user_id))

             except models.IntegrityError:
                raise ValueError("User already exists.", "error")
                return render_template('createprofile.html', title='Create Your Profile', form=form, user_id=user_id)

    if request.method == 'GET':
        return render_template('employmentdetails.html', title='Employment Details', form=form, user_id=user_id)


    
@app.route('/billinginfo', methods=['GET', 'POST'])
@login_required
def billinginfo():
    """Renders the Billing Details Page"""
    user_id = (current_user.get_id() or "No User Logged In")

    form = forms.BillingInfo()                                   
    form.accounttype.choices = [('Current', 'Current'), ('Savings', 'Savings')]
    form.bankname.choices = [('BancABC', 'BancABC'), ('Barclays', 'Barclays'), ('FNB', 'FNB'), ('Moza de Banco', 'Moza de Banco'), 
                             ('Standard Bank', 'Standard Bank'), ('BIM', 'BIM')]
    form.currency.choices = [('EUR', 'Euro'), ('MZN', 'MZN'), ('USD', 'USD'), ('ZAR', 'ZAR')]

    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]
    else:
        flash("You have no open applications.", "error")

    if request.method == 'POST':
         if form.validate_on_submit == False:
             return render_template('billinginfo.html', title='Billing Information', form=form, user_id=user_id)
         else:
             try:
                add_bill = ("""UPDATE customer SET
                accounttype=%s, accountnum=%s, bankname=%s, branch=%s, currency=%s, yearsopen=%s, monthsopen=%s, 
                bankcertname=%s, bankcertpos=%s WHERE idCustomer=%s""")
                accounttype = form.accounttype.data
                accountnum = form.accountnum.data
                bankname = form.bankname.data
                branch = form.branch.data
                currency = form.currency.data
                yearsopen = form.yearsopen.data
                monthsopen = form.monthsopen.data
                bankcertname = form.bankcertname.data
                bankcertpos = form.bankcertpos.data
                               

                bill_data = (accounttype, accountnum, bankname, branch, currency, yearsopen, monthsopen, bankcertname, 
                            bankcertpos, idCustomer)
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(add_bill, bill_data)
                conn.commit()
                mycursor.close()
                conn.close() 
                flash("Thank you. Your bank details have been saved. Keep going.", "success")
                return redirect(url_for('uploaddocs'))
                  
             except models.IntegrityError:
                raise ValueError("User already exists.", "error")
                return render_template('billinginfo.html', title='Billing Information', form=form, user_id=user_id)


    if request.method == 'GET':
      return render_template('billinginfo.html', title='Billing Information', form=form, user_id=user_id)




@app.route('/pay', methods=['GET', 'POST'])
@login_required
def pay():
    """Renders the Billing Details Page"""
    user_id = (current_user.get_id() or "No User Logged In")

    form = forms.PaymentInfo()                                   
    form.billingtype.choices = [('VISA', 'VISA'), ('MasterCard', 'MasterCard'), ('Maestro', 'Maestro'), ('Paypal', 'Paypal'), ('mkesh', 'mkesh')]
    
    user_id = (current_user.get_id() or "No User Logged In")
    idCustomer = None
            
    id_query = ("select emailaddress, idCustomer from customer where emailaddress=%s")
    conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
    mycursor=conn.cursor()
    mycursor.execute(id_query, (user_id, ))
    customer_id = mycursor.fetchall()
    if customer_id:
        for cust_id in customer_id:
            if cust_id[0] == user_id:
               idCustomer = cust_id[1]
    else:
        flash("Your shopping cart is empty.", "error")

    if request.method == 'POST':
         if form.validate_on_submit == False:
             return render_template('pay.html', title='Make Payment', form=form, user_id=user_id)
         else:
             try:
                add_payment = ("""INSERT INTO payment VALUES (idCustomer, billingtype, billingaccount, securitynum, 
				cardholder, expirydate, dateofpayment) 
                		VALUES (%s, %s, %s, %s, %s, %s, %s))
                
                billingtype = form.billingtype.data
                billingaccount = form.billingaccount.data
                securitynum = form.securitynum.data
                cardholder = form.cardholder.data
		expirydate = form.expirydate.data
                dateofpayment = datetime.now()
               

                pay_data = (idCustomer, billingtype, billingaccount, securitynum, cardholder, expirydate, dateofpayment)
                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                mycursor.execute(add_payment, pay_data)
                conn.commit()
                mycursor.close()
                conn.close() 
                flash("Thank you. The transaction was successful.", "success")
                return redirect(url_for('index'))
                  
             except models.DoesNotExist:
                raise ValueError("The transaction was declined by your bank.", "error")
                return render_template('pay.html', title='Make Payment', form=form, user_id=user_id)


    if request.method == 'GET':
      return render_template('pay.html', title='Make Payment', form=form, user_id=user_id)





@app.route('/signin', methods=['GET', 'POST'])
def signin():
    """Renders the Sign In Page"""
    form = forms.SignInForm()

    if current_user.is_authenticated():
        return redirect(url_for('profile'))
   
    if request.method == 'POST':
      if form.validate_on_submit() == False:
          return render_template('signin.html', title='Sign In', year=datetime.now().year, form=form)
      else:
         try:
             email = form.email.data.strip()
             passwd = form.password.data

             user = User.get(email)
             conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
             mycursor=conn.cursor()
                          
             if user:
                password_query = ("select password from user where email = email")
                mycursor.execute(password_query)
                dbpassword = mycursor.fetchall()
                pwhash = ''.join(dbpassword[0])
                password = pwhash
                                             
                if check_password_hash(pwhash, passwd):
                    user = User(email, password)
                    login_user(user, remember=True)
                    flash("You're now logged in!")
                    user_id = (current_user.get_id() or "No User Logged In") 
                    return redirect(url_for('home', user_id=user_id)) 
                    mycursor.close()
                    
                else:
                    flash("No user with that email/password combo")
         except models.DoesNotExist:
              flash("No user with that email/password combo")
              return render_template('signin.html', title='Sign In', year=datetime.now().year, form=form)
    
    if request.method == 'GET':
      return render_template('signin.html', title='Sign In', year=datetime.now().year, form=form) 

                   

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Renders the Sign Up Page"""
    form = forms.SignUpForm()
        
    if request.method == 'POST':
        if form.validate_on_submit():
             try:
                fname = form.fname.data
                lname = form.lname.data
                email = form.email.data
                password = generate_password_hash(form.password.data)
                membersince = datetime.now()

                conn = mysql.connector.connect(user="root", password="T@wana03", database="customers", host="localhost")
                mycursor=conn.cursor()
                user_query = ("select email from user where email = %s")
                mycursor.execute(user_query, (email, ))
                user_details = mycursor.fetchall()
                
                if user_details:
                    flash("User with that email already exists!", "error")
                    return render_template('signup.html', title='Sign Up', year=datetime.now().year, form=form)

                else:
                    add_user = ("INSERT INTO user "
                    "(fname, lname, email, password, membersince) "
                    "VALUES (%s, %s, %s, %s, %s)")
                
                    user_data = (fname, lname, email, password, membersince)
                    mycursor.execute(add_user, (user_data))
                    conn.commit()

                    """add_customer = ("INSERT INTO customer "
                    "(firstname, lastname, emailaddress) "
                    "VALUES (%s, %s, %s)")
                    customer_data = (fname, lname, email)
                    mycursor.execute(add_customer, customer_data)
                    conn.commit()"""
                    mycursor.close()
                    conn.close() 
                    flash("Thank you. You are registered.", "success")
                    return redirect(url_for('signin'))
                  
             except models.IntegrityError:
                raise ValueError("That email address is taken. User already exists.", "error")
            
        else:
           return render_template('signup.html', title='Sign Up', year=datetime.now().year, form=form)

    if request.method == 'GET':
      return render_template('signup.html', title='Sign Up', year=datetime.now().year, form=form)

    

@app.route('/signout')
@login_required
def signout():
    """Renders the Sign Out page."""
    logout_user()
    flash("You have been logged out", "success")
    return redirect(url_for('signin'))
