from flask import Flask,request,render_template
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from predict_parkinsons import predict_image
import os


app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['UPLOAD_FOLDER']='static/images'


waveModel = os.path.join("models/", "random_forest_wave_model.pkl")
spiralModel = os.path.join("models/", "random_forest_spiral_model.pkl")

# route of index.html
@app.route("/",methods=["GET","POST"])
def home():
    return render_template("index.html")

# to get the about route
@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about.html")

# for testing 
# @app.route('/uploader',methods=["GET","POST"])
# def uploader():
#     if request.method=='POST':
#         f=request.files['image']
#         f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('PatientImage.png')))
#         pred=predict_image('static/images/PatientImage.png', spiralModel)
#         print("the output from the model is", pred)
#         if pred == "Healthy":    
#             return render_template('index.html',result="Parkinson Disease is detected")
#         else:
#             return "The patient is affected with parkinsons"
#     return render_template('index.html')

# route for uploading spiral images
@app.route("/uploadSpiral",methods=["GET","POST"])
def uploadSpiral():
    if request.method=='POST':
        f=request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('PatientImage.png')))
        pred=predict_image('static/images/PatientImage.png', spiralModel)
        if pred == "Healthy":
            return render_template('uploadSpiral.html',result=False)
        else:
            return render_template('uploadSpiral.html',result=True)
    return render_template('uploadSpiral.html',result="null")

# route for uploading wave images
@app.route("/uploadWave",methods=["GET","POST"])
def uploadWave():
    if request.method=='POST':
        f=request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename('PatientImage.png')))
        pred=predict_image('static/images/PatientImage.png', waveModel)
        if pred == "Healthy":
            return render_template('uploadWave.html',result=False)
        else:
            return render_template('uploadWave.html',result=True)
    return render_template('uploadWave.html',result="null")
        

    # form = UploadFileForm()
    # if form.validate_on_submit():
    #     file=form.file.data
    #     file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename('PatientImage.png')))
    #     pred=predict_image('static/images/PatientImage.png', spiralModel)
    #     print("the output from the model is", pred)
    #     if pred == "Healthy":
    #         return "The patient is healthy"
    #     else:
    #         return "The patient is affected with parkinsons"
    # return render_template('index.html',form=form)



if __name__=='__main__':
    app.run(debug=True)