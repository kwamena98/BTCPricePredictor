from flask import Flask,request,render_template
import json


app=Flask(__name__)

@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        open_= request.get_json()
        print(open_)

        return {'message':'ok'}


    return render_template('home.html')



if __name__=='__main__':
    app.run(debug=True)