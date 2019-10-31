from flask import Flask, render_template, request, url_for, request, session, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()

db = client.get_database("testdb")
coll = db.get_collection("user")

db1 = client.get_database("placesdb")
cd = db1.get_collection("CDR")
wd = db1.get_collection("WDR")
ed = db1.get_collection("EDR")
mwd = db1.get_collection("MWDR")
fwd = db1.get_collection("FWDR")

db_contact = client.get_database("contactdb")
user_contact = db_contact.get_collection("user")
user_register = db_contact.get_collection("register")


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        pass

    return render_template("index.html")


@app.route("/nepal/", methods=["GET", "POST"])
def nepal():
    return render_template("nepal.html")


@app.route("/nepal/far_western/", methods=["GET", "POST"])
def far_western():
    kanc_desc, dhan_desc = None, None

    maha = fwd.find({"_id": 1}, {"Mahakali.Description": 1})

    for dta in maha:
        kanc_desc = dta["Mahakali"]["Description"]

    seti = fwd.find({"_id": 2}, {"Seti.Description": 1})

    for dta in seti:
        dhan_desc = dta["Seti"]["Description"]

    return render_template("far_western.html", maha_desc=kanc_desc, seti_desc=dhan_desc)


@app.route("/nepal/mid_western/", methods=["GET", "POST"])
def mid_western():
    nep_desc, jum_desc, rol_desc = None, None, None

    bhe = mwd.find({"_id": 1}, {"Bheri.Description": 1})

    for dta in bhe:
        nep_desc = dta["Bheri"]["Description"]

    kar = mwd.find({"_id": 2}, {"Karnali.Description": 1})

    for dta in kar:
        jum_desc = dta["Karnali"]["Description"]

    rap = mwd.find({"_id": 3}, {"Rapti.Description": 1})

    for dta in rap:
        rol_desc = dta["Rapti"]["Description"]

    return render_template("mid_western.html", bhe_desc=nep_desc, kar_desc=jum_desc, rap_desc=rol_desc)


@app.route("/nepal/western/", methods=["GET", "POST"])
def western():
    mus_desc, tri_desc, boudd_desc = None, None, None

    b = wd.find({"_id": 1}, {"Dhaulagiri.Description": 1})

    for dta in b:
        mus_desc = dta["Dhaulagiri"]["Description"]

    gan = wd.find({"_id": 2}, {"Gandaki.Description": 1})

    for dta in gan:
        tri_desc = dta["Gandaki"]["Description"]

    lumb = wd.find({"_id": 3}, {"Lumbini.Description": 1})

    for dta in lumb:
        boudd_desc = dta["Lumbini"]["Description"]

    return render_template("western.html", dha_desc=mus_desc, gan_desc=tri_desc, lum_desc=boudd_desc)


@app.route("/nepal/central/", methods=["GET", "POST"])
def central():
    b = cd.find({"_id": 2}, {"Chitwan.Description": 1})

    chi_desc, kat_desc, temp_desc = None, None, None

    for dta in b:
        chi_desc = dta["Chitwan"]["Description"]

    bag_dsc = cd.find({"_id": 1}, {"Kathmandu.Description": 1})

    for dta in bag_dsc:
        kat_desc = dta["Kathmandu"]["Description"]

    jan_desc = cd.find({"_id": 3}, {"Janakpur.Description": 1})

    for dta in jan_desc:
        temp_desc = dta["Janakpur"]["Description"]

    return render_template("central.html", nar=chi_desc, bag=kat_desc, jan=temp_desc)


@app.route("/nepal/eastern/", methods=["GET", "POST"])
def eastern():
    bri_desc, ilm_desc, eve_desc = None, None, None

    koh = ed.find({"_id": 1}, {"Koshi.Description": 1})

    for dta in koh:
        bri_desc = dta["Koshi"]["Description"]

    mec = ed.find({"_id": 2}, {"Mechi.Description": 1})

    for dta in mec:
        ilm_desc = dta["Mechi"]["Description"]

    sag = ed.find({"_id": 3}, {"Sagarmatha.Description": 1})

    for dta in sag:
        eve_desc = dta["Sagarmatha"]["Description"]

    return render_template("eastern.html", kos_desc=bri_desc, mec_desc=ilm_desc, sag_desc=eve_desc)


@app.route("/contact/", methods=["GET", "POST"])
def contact_page():
    submitted = ""

    if request.method == "POST":
        first = request.form.get("fname")
        email = request.form.get("email")
        subject = request.form.get("subject")
        text = request.form.get("desc")

        print(first + subject + email + text)

        count = user_contact.find({}).count()

        data = {
            "_id": count + 1,
            "FirstName": first,

            "EmailID": email,
            "Subject": subject,
            "Description": text
        }

        check = user_contact.insert_one(data)
        print(check.inserted_id)

        submitted = "SUBMITTED"

    return render_template("contact2.html", check1=submitted)


@app.route("/getdata/", methods=["GET", "POST"])
def trypage():
    if request.method == "POST":
        print(request.form.get("delID"))

        delete_data = user_contact.delete_one({"_id": int(request.form.get("delID"))})

        print(delete_data.deleted_count)

    a = user_contact.find({})

    fstlist = []
    mainlist = []
    for data in a:
        idvalue = data["_id"]
        Fname = data["FirstName"]
        subject = data["Subject"]
        Eid = data["EmailID"]
        Desc = data["Description"]

        fstlist.append(idvalue)
        fstlist.append(Fname)
        fstlist.append(subject)
        fstlist.append(Eid)
        fstlist.append(Desc)

        mainlist.append(fstlist)

        fstlist = []

    var = "Data Table"

    return render_template("test.html", fdata=mainlist, fdata2=var)  # desc=desca


@app.route("/signin/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        uname = request.form.get('username')
        passwo = request.form.get('passw')

        print(uname)

        if uname == "admin" and passwo == "admin123":
            return redirect("dashboard")
        else:
            return render_template("login.html")

    return render_template("login.html")

@app.route("/dashboard/", methods=["GET", "POST"])
def dashboard_page():
    if request.method == "POST":

        id = request.form.get("ID")
        des = request.form.get("email")

        up = user_contact.update({"_id": int(id)}, {"$set": {"EmailID": des}})

    a = user_contact.find({})

    fstlist = []
    mainlist = []

    for data in a:
        idvalue = data["_id"]
        Fname = data["FirstName"]
        subject = data["Subject"]
        Eid = data["EmailID"]
        Desc = data["Description"]

        fstlist.append(idvalue)
        fstlist.append(Fname)
        fstlist.append(subject)
        fstlist.append(Eid)
        fstlist.append(Desc)

        mainlist.append(fstlist)

        fstlist = []

    var = "Data Table"




    return render_template("update.html", fdata=mainlist, fdata2=var)








@app.route("/signup/", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        uname = request.form.get("name")
        password = request.form.get("pass")
        bday = request.form.get("birthday")
        gender = request.form.get("gender")
        mail = request.form.get("email")
        phone = request.form.get("phone")

        count = user_register.find({}).count()

        data = {
            "_id": count + 1,
            "Name": uname,
            "Password": password,
            "Birthday": bday,
            "Gender": gender,
            "Email": mail,
            "Phone": phone
        }
        check = user_register.insert_one(data)
        print(check.inserted_id)

    return render_template("register.html")




if __name__ == "__main__":
    app.run()
