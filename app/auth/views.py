# -*- coding:utf-8 -*-

from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm
from ..models import User
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next and next.startswitch('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invaild username or password.')
    return render_template('auth/login.html', form=form)
