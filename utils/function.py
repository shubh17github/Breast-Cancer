
import config
import pickle
import json
import numpy as np

class cancer():

    def __init__(self,gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status):
        """ init function ar used for accepting input from users"""
        self.gender=gender
        self.age=age
        self.hypertension=hypertension
        self.heart_disease=heart_disease
        self.ever_married=ever_married
        self.work_type=work_type
        self.Residence_type=Residence_type
        self.avg_glucose_level=avg_glucose_level
        self.bmi=bmi
        self.smoking_status=smoking_status

    def load_model(self):

        with open(config.model_file_path,'rb') as file:
            self.model=pickle.load(file)

        with open(config.col_list_path,'r') as file:
            self.col_dict=json.load(file)

    def predict(self):

        self.load_model()

        array=np.zeros(len(self.col_dict['column']))

        array[0]=self.gender
        array[1]=self.age
        array[2]=self.hypertension
        array[3]=self.heart_disease
        array[4]=self.ever_married
        array[5]=self.Residence_type
        array[6]=self.avg_glucose_level
        array[7]=self.bmi
        array[8]=self.smoking_status

        work_type_value='work_type_'+self.work_type
        work_type_index=self.col_dict['column'].index(work_type_value)
        array[work_type_index]=1

        res=self.model.predict([array])
        return res[0]



        

        

