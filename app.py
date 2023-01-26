from flask import Flask,request,render_template
import pickle


with open('model.pkl', 'rb') as file:
    model = pickle.load(file)



app=Flask(__name__)

@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        output= request.get_json()
        print(output)
        y=model.predict([[int(output['open']),int(output['high']),int(output['low']),int(output['volume'])]])
        print(str(y))


        return {'message':str(y[0])}


    return render_template('home.html')



if __name__=='__main__':
    app.run(debug=True)