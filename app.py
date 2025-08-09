from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/topla', methods=['POST'])
def topla():
    if request.method == 'POST':
        try:
            a = float(request.form['sayi1'])
            b = float(request.form['sayi2'])
            c = a + b
            return f"Girilen sayıların toplamı: {c}"
        except ValueError:
            return "Lütfen geçerli sayılar girin."

if __name__ == '__main__':
    app.run(debug=True)