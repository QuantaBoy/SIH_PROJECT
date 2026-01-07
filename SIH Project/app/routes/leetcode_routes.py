from flask import Blueprint, render_template, redirect, url_for
from app.services.excel_service import update_leetcode_excel
import pandas as pd

leetcode_bp = Blueprint("leetcode", __name__)

@leetcode_bp.route("/", methods=["GET"])
def home():
    try:
        df = pd.read_excel("data/leetcode_data.xlsx")
        table = df.to_html(index=False)
    except:
        table = None
    return render_template("home.html", table=table)


@leetcode_bp.route("/fetch", methods=["POST"])
def fetch():
    update_leetcode_excel()
    return redirect(url_for("leetcode.home"))
