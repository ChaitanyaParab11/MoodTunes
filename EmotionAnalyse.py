
import cv2
from deepface import DeepFace

#while(True):
vid = cv2.VideoCapture(0)
while(True):
    
    ret, frame = vid.read()
    break


result = DeepFace.analyze(frame,actions=['emotion'])

dom_emo=result[0]['dominant_emotion']
print(dom_emo)

vid.release()
cv2.destroyAllWindows()
