
from flask import Flask,render_template,request
from utils.function import cancer


app=Flask(__name__)

@app.route('/')
def index ():
    return render_template('prediction.html')

@app.route('/predict',methods=['GET','POST'])
def predict():

    if request.method=='POST':
        data=request.form
        gender=int(data['gender'])
        age=float(data['age'])
        hypertension=int(data['hypertension'])
        heart_disease=int(data['heart_disease'])
        ever_married=int(data['ever_married'])
        work_type=data['work_type']
        Residence_type=int(data['Residence_type'])
        avg_glucose_level=float(data['avg_glucose_level'])
        bmi=float(data['bmi'])
        smoking_status=int(data['smoking_status'])

    class_obj=cancer(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status)
    result=class_obj.predict()

    return render_template('prediction.html',pred=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)