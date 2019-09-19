import csv
import math
import random
def loadCsv(filename):
	lines=csv.reader(open(filename,"r"))
	dataset=list(lines)
	for i in range(len(dataset)):
		dataset[i]=[float(x) for x in dataset[i]]
	return dataset
def splitDataset(dataset,splitRatio):
	trainSize=int(len(dataset)*splitRatio)
	trainSet=[]
	copy=list(dataset)
	while len(trainSet)<trainSize:
		index=random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return[trainSet,copy]

def seperatedByClass(dataset):
	seperated={}
	for i in range(len(dataset)):
		vector=dataset[i]
		if(vector[-1] not in seperated):
			seperated[vector[-1]]=[]
		seperated[vector[-1]].append(vector)
	return seperated
def mean(numbers):
	return sum(numbers)/float(len(numbers))
def stdev(numbers):
	avg=mean(numbers)
	variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def summarize(dataset):
	summaries=[(mean(attribute),stdev(attribute)) for attributes in zip(*dataset)]
	del summaries[-1]
	return summaries

def summariesByClass(dataset):
	seperated=seperatedByClass(dataset)
	summaries={}
	for classValue,instances in seperated.items():
		summaries[classValue]=summarize(instances)
	return summaries

def calculateProbability(x,mean,stdev):
	exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return summaries

def calculateClassProbablities(summaries,inputVector):
	probabilities={}
	for classValue,classsummaries in summaries.items():
		probabilities[classValue]=1
		for i in range(len(classsummaries)):
			mean,stdev=classsummaries[i]
			x=inputVector[i]
			probabilities[classValue]*=calculateProbability(x,mean,stdev)
	return probabilities

def predict(summaries,inputVector):
	probabilities=calculateClassProbabilities(summaries,inputVector)
	bestLabel,bestProb=None,-1
	for vlassValue,probability in probabilities.items():
		if bestLabel is None or probability>bestProb:
			bestProb=probability
			bestLabel=classValue
	return bestLabel

def getpredictions(summaries,testset):
	predictions=[]
	for i in range(len(testset)):
		result=predict(summaries,testset(i))
		predictions.append(result)
	return predictions

def getAccuracy(testSet,predictions):
	correct=0
	for i in range(len(testSet)):
		if testSet[i][-1]==predictions[i]:
			correct+=1
	return (correct/float(len(testSet)))*100.0

def main():
	filename="5data.csv"
	splitRatio=0.67
	dataset=loadCsv(filename)
	trainingSet,testSet=splitDataset(dataset,splitRatio)
	print('split{0} rows into train{1} and test={2} rows'.format(len(dataset),len(trainingSet),len(testSet)))
	summaries=summariesByClass(trainingSet)
	predictions=getPredictions(summaries,testSet)
	accuracy=getAccuracy(testset,predictions)
	print('accuracy of the classifier is:{0}%'.format(accuracy))

main()


