from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR_DB_URI'


db = SQLAlchemy(app)


class Esoteric(db.Model):
    __tablename__ = 'connect'  # Set the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)


@app.route("/org", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:  # Check if email exists
            entry = Esoteric(email=email)
            db.session.add(entry)
            db.session.commit()
            return "Data inserted successfully.."
        else:
            return "Email not returned.."  # Debugging message for empty email
    return render_template("home.html")


@app.route("/show_data")
def show_data():
    data = Esoteric.query.all()
    return render_template("show_data.html", data=data)


app.run(debug=True)