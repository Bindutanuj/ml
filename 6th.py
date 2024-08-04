import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
msg=pd.read_csv('naive.csv',header=None,names=['message','label'])
print("The dimensions of the dataset",msg.shape)
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
x=msg.message
y=msg.labelnum
xtrain,xtest,ytrain,ytest=train_test_split(x,y,random_state=1)
count_vect=CountVectorizer() xtrain_dtm=count_vect.fit_transform(xtrain)
xtest_dtm=count_vect.transform(xtest)
clf=MultinomialNB().fit(xtrain_dtm,ytrain)
predicted=clf.predict(xtest_dtm)
print("Accuracy metrics:")
print("Accuracy of the classifier is",metrics.accuracy_score(ytest,predicted))
print("Confusion matrix:")
print(metrics.confusion_matrix(ytest,predicted))
print("Recall and Precision:")
print(metrics.recall_score(ytest,predicted))
print(metrics.precision_score(ytest,predicted))
