from flask import Flask, render_template # llamamos flask y lo inicialisamos

app = Flask(__name__) #llamamos al objeto con nombre app
#el objeto (app)  es importante


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)