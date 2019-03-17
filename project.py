#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense


# In[2]:


dataset=pd.read_csv("heart.csv")
final=dataset["target"]


# In[3]:


mdataset=dataset.drop("target",1)
mdataset.replace("?",9999999,inplace=True)
target=dataset["target"]
mdataset.head()


# In[4]:


result=[]
for i in target:
    if i==1:
        result.append([1,0])
    elif i==0:
        result.append([0,1])


# In[5]:


modified=np.array(mdataset)
result=np.array(result)


# In[6]:


x_train,x_test,y_train,y_test=train_test_split(modified,result,test_size=0.21,random_state=35)
print(x_train.shape)
print(x_test.shape)


# In[7]:


model=Sequential()
model.add(Dense(700,input_dim=13,activation='sigmoid'))
model.add(Dense(100,activation='tanh'))
model.add(Dense(2,activation='softmax'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(x_train,y_train, epochs=1000, batch_size=50, validation_data=(x_test,y_test))


# In[9]:



from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Heart Diseases")
window.geometry("735x400+150+50")
window.resizable(height=False,width=False)

########################functions and class################################
def labels(text,i,j=0):
 label=Label(window,text=text)
 label.grid(row=i,column=j,sticky=E)

def optionboxs(list,i,j=1):
  fopt=StringVar()
  fopt.set(list[0])
  OptionMenu(window,fopt,*list).grid(row=i,column=j,sticky=W)
  return fopt

def entrys(i,j=1):
 result=IntVar()
 entry=Entry(window,textvariable=result)
 entry.grid(row=i,column=j,sticky=W)
 return result

#############################entrys########################################## 
 
labels(" ",0)

labels("Age",1)
age=entrys(1)

labels("Resting Blood Pressure:",2)
trestbps=entrys(2)

labels("Cholesterol:",3)
chol=entrys(3)

labels("Max Heartrate:",4)
thalach=entrys(4)

labels("St Depression:",5)
oldpeak=entrys(5)

#####################optionboxs###############################

labels("Slope:",6)
slope=optionboxs(["unsloping","flat","downsloping"],6)

labels("Thal:",7)
thal=optionboxs(["normal","fixed defect","reversible"],7)

labels("Sex:",1,4)
sex=optionboxs(["Male","Female"],1,5)

labels("Chest Pain:",2,4)
cp=optionboxs([ "typical angina" ,"atypical angina","non-anginal pain","asymptomatic" ],2,5)

labels("Fasting Blood Sugar:",3,4)
fbs=optionboxs([">120mg/dl","<120mg/dl"],3,5)

labels("Resting ECG:",6,4)
restecg=optionboxs(["adequate","having ST-T wave"," showing probable left ventricular hypertrophy "],6,5)

labels("Exercise Induced Angina:",5,4)
eia=optionboxs(["yes","no"],5,5)

labels("Number of major vessels:",4,4)
nmv=optionboxs(["zero","one","two","three"],4,5)

############################predict###################################

def predict():  
 print(age.get(),sex.get(),cp.get(),trestbps.get(),chol.get(),fbs.get(),restecg.get(),thalach.get(),eia.get(),slope.get(),nmv.get(),thal.get())
 inp=[]
 inp.append(age.get())#age
 if sex.get()=="Male":#sex
   inp.append(1)
 elif sex.get()=="Female":
   inp.append(0)
 if cp.get()=="typical angina":#chest pain
   inp.append(0)
 elif cp.get()=="atypical angina":
   inp.append(1)
 elif cp.get()=="non-anginal pain":
   inp.append(2)
 elif cp.get()=="asymptomatic":
   inp.append(3)
 inp.append(trestbps.get())#trestbps
 inp.append(chol.get())#chol
 if fbs.get()==">120mg/dl":#fasting blood sugar
    inp.append(1)
 elif fbs.get()=="<120mg/dl":
    inp.append(0)
 if restecg.get()=="adequate":#resting ECG
    inp.append(0)
 elif restecg.get()=="having ST-T wave":
    inp.append(1)
 elif restecg.get()=="showing probable left ventricular hypertrophy":
    inp.append(2)	
 inp.append(thalach.get())#thalach
 if eia.get()=="yes":#exercise induced angina
    inp.append(1)
 elif eia.get()=="no":
    inp.append(0)
 inp.append(oldpeak.get())#oldpeak
 if slope.get()=="unsloping":#slope
   inp.append(0)
 elif slope.get()=="flat":
    inp.append(1)
 elif slope.get()=="downsloping":
    inp.append(2)	
 if nmv.get()=="zero":#number of major vessels
    inp.append(0)
 elif nmv.get()=="one":
    inp.append(1)
 elif nmv.get()=="two":
    inp.append(2)	
 elif nmv.get()=="three":
    inp.append(3)
 if thal.get()=="normal":#thal
    inp.append(0)
 elif thal.get()=="fixed defect":
    inp.append(1)
 elif thal.get()=="reversible":
    inp.append(2)	
 re=model.predict_classes([[inp]])
 if re==0:
    messagebox.showinfo("prediction","Greater than 50% of diameter narrowing")
 elif re==1:
    messagebox.showwarning("prediction","Less than 50% of diameter narrowing")
 print(inp,"\n",len(inp)) 
 
#################################predict button#################################
labels("  ",8)
labels("  ",9)
labels("  ",10)
labels("  ",10,1)

try:
 button1=Button(window,text="      Predict      ",command=predict)
 button1.grid(row=10,columnspan=2,column=2)
except:
 messagebox.showerror("prediction","something went wrong")
window.mainloop()


# In[ ]:




