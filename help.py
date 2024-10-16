from flask import Flask, render_template, request, send_file
from steganography import encode_message, decode_message
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/image/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        image = request.files['file']
        message = request.form['message']
        
        # salvam imaginea
        filename = secure_filename(image.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(upload_path)
        
        # facem mesajul in imagine
        encoded_image_path = encode_message(upload_path, message)
        
        # imaginea pentru download
        return send_file(encoded_image_path, as_attachment=True)
    
    return render_template('encode.html')


@app.route('/image/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        encoded_image = request.files['file']
        
        # salvam imaginea
        filename = secure_filename(encoded_image.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        encoded_image.save(upload_path)
        
        # o decodam
        message = decode_message(upload_path)
        
        return render_template('decode.html', message=message)
    
    return render_template('decode.html')


if __name__ == '__main__':
    app.run(debug=True)
