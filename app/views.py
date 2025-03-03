from app import app , mail
from flask import render_template, request, redirect, url_for,flash
from .forms import Contact_Form
from flask_mail import Message

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact_Form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        msg = Message(
            subject=f"New Contact Form Submission: {subject} <{email}>",
            sender=(name, email), 
            recipients= ["to@example.com"]
        )
        msg.body = f"From: {name} \n\n{message}"
        try:
            mail.send(msg)
            flash('Your message has been sent', 'success')
            return redirect(url_for('home'))     
        except Exception as e:
            flash(f'Error sending email: {str(e)} ', 'danger')
    return render_template('contact.html', form=form)
