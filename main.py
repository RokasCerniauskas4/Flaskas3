"""
-flask sqlalchemy
-flask migrate
"""
from flask import Flask, render_template, request, redirect, url_for
from forms import AddClientForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
app = Flask(__name__)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = "?``§=)()%``ÄLÖkhKLWDO=?)(_:;LKADHJATZQERZRuzeru3rkjsdfLJFÖSJ"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database'

db.init_app(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String)


with app.app_context():
    db.create_all()

clients = []


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    form = AddClientForm()
    if request.method == 'POST':
        name = form.name.data
        client = Client(name=name)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('show_clients'))
    return render_template('add_client.html', form=form)


@app.route('/clients')
def show_clients():
    #clients = db.session.execute(db.select(Client)).scalars()

    return render_template('clients.html', data=clients)


if __name__ == '__main__':
    app.run(debug=True)
