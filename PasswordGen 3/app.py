from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "", "Weak"

    password = ''.join(random.choice(characters) for _ in range(length))

    strength = "Weak"
    if use_uppercase + use_lowercase + use_numbers + use_symbols >= 3 and length >= 12:
        strength = "Strong"
    elif length >= 8:
        strength = "Moderate"

    return password, strength

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    strength = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        uppercase = bool(request.form.get('uppercase'))
        lowercase = bool(request.form.get('lowercase'))
        numbers = bool(request.form.get('numbers'))
        symbols = bool(request.form.get('symbols'))

        password, strength = generate_password(length, uppercase, lowercase, numbers, symbols)

    return render_template('index.html', password=password, strength=strength)

if __name__ == '__main__':
    app.run(debug=True)