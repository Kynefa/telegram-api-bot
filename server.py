from flask import Flask, request

app = Flask(__name__)

users = {
    "Solo#skayt1": {
        "last_name": "Соловйова",
        "first_name": "Катерина",
        "course": "2",
        "group": "ІС-31"
    }
}

@app.route('/')
def home():
    login = request.args.get('login')
    if login in users:
        user = users[login]
        return f"""
        <h2>Дані користувача</h2>
        <p>Прізвище: {user['last_name']}</p>
        <p>Ім’я: {user['first_name']}</p>
        <p>Курс: {user['course']}</p>
        <p>Група: {user['group']}</p>
        """
    else:
        return "Користувача не знайдено або не передано login."

if __name__ == '__main__':
    app.run(debug=True, port=3000)
