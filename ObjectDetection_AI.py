import os
import cv2
from imageai.Detection import ObjectDetection

exu_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(exu_path, "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectCustomObjectsFromImage(input_image='my_class.jpg',output_image_path='my_class_detection.jpg')
print(type(detections))
