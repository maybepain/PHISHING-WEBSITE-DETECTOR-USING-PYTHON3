import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv('phishing_url_dataset.csv')
x= df.drop("target", axis=1)  # inputs
y = df["target"]   

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()
model.fit(x_test,y_test)

y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

