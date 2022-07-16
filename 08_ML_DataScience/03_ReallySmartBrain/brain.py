from imageai.Prediction import ImagePrediction
import os
execution_path=os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

#https://github.com/OlafenwaMoses/ImageAI