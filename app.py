from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = 'f3de790ee9c9a9f68f11c45e5d4c9bc4'  # Needed for flashing messages

# Hardcoded username and password
USERNAME = 'md.bluechip@admin'
PASSWORD = 'Bluechip@1234'



# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change to your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'brudra95mech@gmail.com'  # Change to your email
app.config['MAIL_PASSWORD'] = 'xfdkoxbkcholfnbr'  # Change to your email password
app.config['MAIL_DEFAULT_SENDER'] = 'brudra95mech@gmail.com'  # Change to your email

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/mbbs_pg')
def mbbs_pg():
    return render_template('mbbs_pg.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        select1 = request.form['select1']
        message = request.form['message']
        
        # Create the email message
        msg = Message('New lead From Websites',
                      recipients=['rudra95mech@gmail.com'])  # Change to the recipient's email
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSelection: {select1}\nMessage: {message}"
        
        try:
            mail.send(msg)
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email: {str(e)}', 'danger')
        
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/mbbs')
def mbbs():
    return render_template('mbbs.html')

@app.route('/pg')
def pg():
    return render_template('pg.html')

@app.route('/usa')
def usa():
    return render_template('usa.html')

@app.route('/mipr')
def mipr():
    return render_template('mipr.html')

@app.route('/tsampi')
def tsampi():
    return render_template('tsampi.html')

@app.route('/fmiph')
def fmiph():
    return render_template('fmiph.html')

@app.route('/ieu')
def ieu():
    return render_template('ieu.html')

@app.route('/log_sign')
def log_sign():
    return render_template('log_sign.html')

@app.route('/bc_admin')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('bc_admin.html')

@app.route('/adm_student')
def adm_student():
    return render_template('adm_student.html')

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the credentials match
        if username == USERNAME and password == PASSWORD:
            session['username'] = username  # Save user in session
            return redirect(url_for('dashboard'))
        else:
           return render_template('log.html', error="Invalid credentials, please try again!")
    
    return render_template('log.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')



@app.route('/pass_rest')
def pass_reset():
    return render_template('pass_reset.html')

@app.route('/st_details')
def st_details():
    return render_template('st_details.html')

@app.route('/st_documents')
def st_documents():
    return render_template('st_documents.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True,port=8004)
