"""
Yeng

Yeng ile cihazınızı tarayıcınızdan kontrol edin

Github: https://github.com/kerem3338/Yeng
"""
import os
import sys
import subprocess
import threading
import getpass
import shlex

from flask import Flask,request,render_template


app=Flask(__name__)


@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/")
def index_page():
    return render_template("index.html",user=getpass.getuser())

@app.route("/",methods=["POST"])
def index_page_action():
    command_form=request.form["command"]
    subprocess.call(shlex.split(command_form),subprocess.CREATE_NEW_CONSOLE,shell=True)

    return "<script>window.location.href='/';</script>"

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host="0.0.0.0") #Yeng'e erişmek için tarayıcınızdan http://(IPv4 adresiniz):5000/