from flask import Blueprint, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if "@" not in email and len(email) < 5:
            flash("Wrong email format", category = 'error')
        elif len(firstName) < 2 and len(firstName) > 50:
            flash("Check if you typed your name correctly", category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        elif len(password1) < 4 and len(password1) > 12:
            flash("Choose another password", category='error')
        else:
            flash("Account created!", category='success')
            pass

    return render_template('sign_up.html')



