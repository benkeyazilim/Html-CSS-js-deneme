from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "gizli_anahtar"

# Örnek kullanıcı veritabanı
users = {
    "admin": {"password": "1234", "role": "admin"},
    "ali": {"password": "4321", "role": "user"}
}

@app.route("/")
def home():
    if "username" in session:
        return f"Hoş geldin {session['username']}! <br><a href='/logout'>Çıkış Yap</a>"
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["username"] = username
            session["role"] = users[username]["role"]
            if users[username]["role"] == "admin":
                return redirect(url_for("admin_panel"))
            return redirect(url_for("home"))
        return "Hatalı kullanıcı adı veya şifre!"
    return render_template("login.html")

@app.route("/admin")
def admin_panel():
    if "username" in session and session["role"] == "admin":
        return "Admin Paneli: Buradan her şeyi kontrol edebilirsin! <br><a href='/logout'>Çıkış Yap</a>"
    return "Yetkisiz giriş!"

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("role", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
