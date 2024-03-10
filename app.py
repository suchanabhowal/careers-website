from flask import Flask,render_template,jsonify
app = Flask(__name__)  #app is the name odf the actual variable that contains the flask application that u want to run.  for production,inside start command write 'gunicorn app:app'  
#instead of python write gunicorn, gunicorn is for deployment, python for production. first 'app' is name of the python file i wan to run.second 'app' is is th ename of the flaskapplication
jobs=[
    {
        'id': 1,
        'title':'Data Analyst',
        'location':'Bangalore,india',
        'salary':'Rs 10,00,000'
    },
     {
        'id': 2,
        'title':'System Design',
        'location':'Delhi,india',
        'salary':'Rs 1,00,000'
    },
     {
        'id': 3,
        'title':'Supply Chain manager',
        'location':'Bangalore,india',
        'salary':'Rs 40,00,000'
    },
]
@app.route('/') #info is stored in html format
def home():
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs') #here we have created an api route, info in stored in json format, we can change it as necessary.
def find_jobs():    #don't use function name same as  name of return variable
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
    




#WSGI accepts many requests from client, each workers takes up one request and completes it and then proceeds to the next request. Next request is handled only after one request is completed.
#ASGI is asynchronous gateway interface, which can handle many more number of requests persecond compared to WSGI. it handles requests asynchronously, meaning it will strt executing a second request, even before first request completion, if therre is a large code in first request.