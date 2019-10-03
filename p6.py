import pandas as pd
msg=pd.read_csv('text6.txt',names=['message','label'])
print('The dimensions of the dataset',msg.shape)
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
X=msg.message
y=msg.labelnum
print(X)
print(y)


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)


from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
xtrain_dtm=count_vect.fit_transform(xtrain)
xtest_dtm=count_vect.transform(xtest)
print(count_vect.get_feature_names())


df=pd.DataFrame(xtrain_dtm.toarray(),columns=count_vect.get_feature_names())
print(df)
print(xtrain_dtm)

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(xtrain_dtm,ytrain)
predicted=clf.predict(xtest_dtm)

from sklearn import metrics
print('Accuracy metrics')
print('Accuracy of the classifier is',metrics.accuracy_score(ytest,predicted))
print('Confusion metrics')
print(metrics.confusion_matrix(ytest,predicted))
print('Recall and precision')
print(metrics.recall_score(ytest,predicted))
print(metrics.precision_score(ytest,predicted))


docs_new=['I like this place','My boss is not my saviour']
X_new_counts=count_vect.transform(docs_new)
predictednew=clf.predict(X_new_counts)
for doc,category in zip(docs_new,predictednew):
	print('%s->%s'%(doc,msg.labelnum[category]))
