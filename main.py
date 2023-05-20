from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from predict_parkinsons import predict_image
import os


app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['UPLOAD_FOLDER']='static/images'


waveModel = os.path.join("models/", "random_forest_wave_model.pkl")
spiralModel = os.path.join("models/", "random_forest_spiral_model.pkl")


class UploadFileForm(FlaskForm):
    file=FileField("File",validators=[InputRequired()])
    submit=SubmitField("Upload File")

@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file=form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename('PatientImage.png')))
        pred=predict_image('static/images/PatientImage.png', spiralModel)
        print("the output from the model is", pred)
        if pred == "Healthy":
            return "The patient is healthy"
        else:
            return "The patient is affected with parkinsons"
    return render_template('index.html',form=form)



if __name__=='__main__':
    app.run(debug=True)