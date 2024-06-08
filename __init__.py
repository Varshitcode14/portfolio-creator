from flask import Flask, render_template, request,session
import uuid
import os


app = Flask(__name__)
app.secret_key = "SecretKey"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/form/<string:design>',methods = ['POST','GET'])
def form(design):
    session["design_sess"] = design
    return render_template('form.html')

@app.route('/upload', methods=['POST'])
def upload():
    desging_upload = session.get("design_sess")
    if desging_upload == "design1":
        design_name = "design1.html"
    elif desging_upload == "design2":
        design_name = "design2.html"
    elif desging_upload == "design3":
        design_name = "design3.html"
    elif desging_upload == "design4":
        design_name = "design4.html"
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        school = request.form.get('school')
        college = request.form.get('college')
        phone = request.form.get('phone')
        email = request.form.get('email')
        about = request.form.get('about')
        skill1 = request.form.get('skill1')
        skill2 = request.form.get('skill2')
        skill3 = request.form.get('skill3')
        skill4 = request.form.get('skill4')

        # Image upload
        img = request.files.get('dp')
        if img:
            key = uuid.uuid4().hex  # Use uuid4 for better uniqueness
            img_filename = f"{key}_{img.filename}"
            img_path = os.path.join('static', 'images_pf', img_filename)
            
            # Ensure the static/images_pf directory exists
            os.makedirs(os.path.dirname(img_path), exist_ok=True)
            
            img.save(img_path)
        else:
            img_filename = None  # Handle the case where no image is uploaded

        return render_template(design_name, firstname=firstname, lastname=lastname, school=school,
                               img=img_filename, college=college, phone=phone, email=email, about=about,
                               skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4)
    else:
        return render_template('form.html')     

if __name__ == '__main__':
    app.run(debug=True)
