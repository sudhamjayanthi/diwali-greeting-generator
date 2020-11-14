from flask import Flask, render_template, request, redirect, url_for
from gen import generate_image


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html', image_url=generate_image("Sudham"))

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['hero-field']
    return render_template('home.html', image_url=generate_image(name))

@app.route('/feedback', methods=['GET','POST'])
def feedback():
    name = request.form['name2'] 
    email = request.form['email'] 
    message = request.form['message']
    print(name, email, message)
    file = open('other/feedbacks.csv', 'a')
    file.write(f'{name}, {email}, {message}')
    file.close()
    return redirect(url_for('/', image_url= generate_image("Sudham")))

if __name__ == "__main__":
   app.run(debug=True) 