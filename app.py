from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "gizli_anahtar"

# Örnek kullanıcı veritabanı
users = {
    "admin": {"password": "1234", "role": "admin"},
    "ali": {"password": "4321", "role": "user"}
}

# Ana sayfa (Giriş yapmamış kullanıcılar için)
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

# Kullanıcı giriş yaptıktan sonra göreceği ana sayfa/dashboard
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    return redirect(url_for("login"))

# Giriş sayfası
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
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Hatalı kullanıcı adı veya şifre!")
    return render_template("login.html")

# Kayıt sayfası
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return render_template("register.html", error="Bu kullanıcı adı zaten mevcut!")
        
        users[username] = {"password": password, "role": "user"}
        
        return redirect(url_for("login"))

    return render_template("register.html")

# Admin paneli
@app.route("/admin")
def admin_panel():
    if "username" in session and session["role"] == "admin":
        return render_template("admin.html", username=session["username"])
    return "Yetkisiz giriş!"

# Çıkış yapma
@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("role", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)