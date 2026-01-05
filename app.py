from flask import Flask,render_template, request,pymongo


app=Flask(__name__)

client=pymongo.MongoClient("mongodb+srv://revanth200319:revanth200319@cluster0.zrtypbn.mongodb.net/")

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)