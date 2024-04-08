"""
Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет
отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
пользователя и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, render_template, redirect, url_for, request, make_response, session

app = Flask(__name__)
app.secret_key = '12345678'


@app.route('/')
def index():
    if 'name' in session:
        return f' Привет, {session["name"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get('name') or 'NoName'
        # session['password'] = request.form.get('mail')
        return redirect(url_for('index'))
    return render_template('enter.html')


@app.route('/logout/')
def logout():
    session.pop('name', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
