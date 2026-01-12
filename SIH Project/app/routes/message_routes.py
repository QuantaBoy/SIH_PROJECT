from flask import Blueprint, render_template, request, redirect, url_for

message_bp = Blueprint("message",__name__)

@message_bp.route("/",methods=['GET','POST'])
def message():
    if request.method == "POST":
        user_message = request.form.get("message")

        print(user_message)
        return redirect(url_for("message.message"))

    return render_template("message.html")