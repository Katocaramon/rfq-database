from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select
from db import SessionLocal
from models import User

auth_bp = Blueprint("auth", __name__)
login_manager = LoginManager()
login_manager.login_view = "auth.login"

class UserSession(UserMixin):
    def __init__(self, orm_user):
        self.id = orm_user.id
        self.username = orm_user.username

@login_manager.user_loader
def load_user(user_id):
    with SessionLocal() as db:
        u = db.get(User, int(user_id))
        return UserSession(u) if u else None

@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username","").strip()
        password = request.form.get("password","")
        with SessionLocal() as db:
            u = db.execute(select(User).where(User.username==username)).scalar_one_or_none()
            if u and check_password_hash(u.password_hash, password):
                login_user(UserSession(u))
                return redirect(url_for("dashboard"))
        flash("Credenziali non valide", "danger")
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth_bp.route("/settings/password", methods=["GET","POST"])
@login_required
def change_password():
    if request.method == "POST":
        old = request.form.get("old","")
        new = request.form.get("new","")
        with SessionLocal() as db:
            u = db.get(User, int(current_user.id))
            if not u or not check_password_hash(u.password_hash, old):
                flash("Password attuale errata", "danger")
                return redirect(url_for("auth.change_password"))
            u.password_hash = generate_password_hash(new)
            db.commit()
            flash("Password aggiornata", "success")
            return redirect(url_for("dashboard"))
    return render_template("change_password.html")
