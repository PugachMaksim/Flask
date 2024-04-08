"""
Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".

"""

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = '123456788'  # ключ для адреса


@app.route('/', methods=['GET', 'POST'])
def prov():
    if request.method == 'POST':
        name = request.form.get("name")
        flash(f'Hello {name}', 'success')  # Флэш сообщение
        return redirect(url_for('prov'))  # создание адреса

    return render_template('form_name_8.html')


if __name__ == "__main__":
    app.run(debug=True)
