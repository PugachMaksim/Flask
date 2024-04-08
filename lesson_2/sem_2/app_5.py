"""Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        first = int(request.form.get("1_numb"))
        second = int(request.form.get("2_numb"))
        operation = request.form.get("operation")
        if operation == '+':
            res = first + second
        elif operation == '-':
            res = first - second
        elif operation == '/':
            res = first / second
        elif operation == '*':
            res = first * second
        else:
            return "неверный ввод"
        return str(res)
    return render_template('form_5.html')

if __name__ == "__main__":
    app.run(debug=True)