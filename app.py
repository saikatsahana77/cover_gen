from flask import Flask, render_template, request, redirect, session
from flask.helpers import url_for
import os
import shutil
app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/download')
def download():
    name = request.args['name']
    institute = request.args['institute']
    locality = request.args['locality']
    city = request.args['city']
    zip_code = request.args['zip_code']
    subject = request.args['subject']
    topic = request.args['topic']
    class_name = request.args['class_name']
    roll = request.args['roll']
    teacher = request.args['teacher']
    filename = request.args['filename']
    desc = request.args['desc']
    return render_template('result.html', name=name, institute=institute, locality=locality, city=city, zip_code=zip_code, subject=subject, topic=topic, class_name=class_name, roll=roll, teacher=teacher, filename=filename, desc=desc)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, 'static/')
        if not os.path.isdir(target):
            os.mkdir(target)
        image = request.files['image']
        img_name = image.filename
        destination = "/".join([target, img_name])
        image.save(destination)

        name = request.form['name']
        institute = request.form['institute']
        locality = request.form['locality']
        city = request.form['city']
        zip_code = request.form['zip']
        subject = request.form['subject']
        topic = request.form['topic']
        class_name = request.form['class']
        roll = request.form['roll']
        teacher = request.form['teacher']
        desc = request.form['desc']
        return redirect(url_for("download", name=name, institute=institute, locality=locality, city=city, zip_code=zip_code, subject=subject, topic=topic, class_name=class_name, roll=roll, teacher=teacher, filename=img_name, desc=desc))
    else:
        try:
            dir_name = "static"
            test = os.listdir(dir_name)
            for item in test:
                if item.endswith(".png") or item.endswith(".jpg") or item.endswith(".gif") or item.endswith(".jpeg") or item.endswith(".bmp"):
                    os.remove(os.path.join(dir_name, item))
        except OSError:
            pass
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
