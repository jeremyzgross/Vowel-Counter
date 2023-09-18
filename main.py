
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    word = request.form['word']
    Vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    vowel_count = 0
    for letter in word:
        if letter in Vowels:
            vowel_count += 1
    result = f"The word '{word}' contains {vowel_count} vowels."
    return render_template_string(open('index.html').read(), result=result)

if __name__ == '__main__':
    app.run(debug=True)

