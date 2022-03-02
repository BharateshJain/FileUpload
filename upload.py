from flask import Flask, render_template, request

import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename

s3 = boto3.resource('s3',
        aws_access_key_id = "",
        aws_secret_access_key = ""
        )

@app.route('/')
def home():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                data = open(filename,'rb')
                s3.Bucket('s3-assingment-uploads').put_object(Key=filename, Body=data)
                msg = "Upload Done ! "

    return render_template("file_upload_to_s3.html",msg =msg)

if __name__ == "__main__":

    app.run(host='0.0.0.0',port=8080)
