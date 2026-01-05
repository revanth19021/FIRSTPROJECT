from flask import Flask,render_template, request


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/submit',methods=["post"])
def submit():
    email=request.form['email']
    message=request.form['message']
    return f"email :{email},message {message}"

if __name__=="__main__":
    app.run(debug=True)