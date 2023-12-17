#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<Card {self.id}>'
#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST','GET'])
def process_form():
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')
        text = request.form.get('text')
        email = request.form.get('email')

        new_user = User(text=text, email=email)
        db.session.add(new_user)
        db.session.commit()
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_html=button_html,button_db=button_db,text=text,email=email)


if __name__ == "__main__":
    app.run(debug=True)