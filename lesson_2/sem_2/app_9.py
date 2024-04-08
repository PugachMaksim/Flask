"""
Задание №9
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

"""

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = '123456788'

@app.route('/', methods=['GET', 'POST'])
def prov():
    if request.method == 'POST':
        name = request.form.get("name")
        flash(f'Hello {name}', 'success')
        return redirect(url_for('prov'))

    return render_template('form_name_8.html')


if __name__ == "__main__":
    app.run(debug=True)