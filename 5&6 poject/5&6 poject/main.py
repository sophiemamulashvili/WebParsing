from flask import Flask, redirect, url_for, render_template, request,Response, session,flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///caars.sqlite'
db = SQLAlchemy(app)


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    url = db.Column(db.String)

    def __str__(self):
        return f' {self.text} ფასი: {self.price}'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user')
def user():
    all_cars = Cars.query.all()
    length = len(all_cars)
    return render_template('main.html',all_cars=all_cars, length=length)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        password = request.form['password']
        result = request.form['result']
        if username != '' and password != '' and result != '':
            if result == 'გამყიდველი':return redirect(url_for('cars'))
            elif result == 'მყიდველი':return redirect(url_for('user'))
            else: flash('მესამე ველში აირჩიეთ ერთ-ერთი და შეიყვანეთ ქართული შრიფტით', 'error')
        else:
            flash('შეავსეთ ყველა ველი', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')


@app.route('/cars', methods=['GET','POST'])
def cars():
    if request.method == 'POST':
        t = request.form['title']
        d = request.form['discription']
        p = request.form['price']
        if t == '' or d == '' or p == '':
            flash('შეავსეთ ყველა ველი', 'error')
        elif not p.isnumeric():
            flash('ფასის ველში შეიყვანეთ მხოლოდ რიცხვითი მონაცემი ', 'error')
        else:
            car1 = Cars(title=t, text=d, price=float(p))
            db.session.add(car1)
            db.session.commit()
            flash('მონაცემები დამატებულია', 'info')
    return render_template('add_cars.html')


if __name__ == "__main__":
    app.run(debug=True)


