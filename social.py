import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image

gray = cv2.imread('1.png')
resize=cv2.resize(gray,(800,700))

# Convert into grayscale
#gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
#img = cv2.imread('1.png')
#resize=cv2.resize(gray,(400,300))


# Detect faces
#faces = face_cascade.detectMultiScale(gray, 1.1, 4)
faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces1=faces.detectMultiScale(resize,scaleFactor=1.2,minNeighbors=5,minSize=(20,20))
print(faces1)

# Draw rectangle around the faces
l=[]
i=1
lf=[]

for (x, y, w, h) in faces1:
    cv2.rectangle(resize, (x, y), (x + w, y + h), (255, 0, 0), 2)
    s=str(i)
    cv2.putText(resize,s,(x,y),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),2)
    i=i+1
    l=[]
    l.append(x)
    l.append(y)
    lf.append(l)
    print(l)
    #print(lf)
print(lf) 

close_person=""
import math
for i in range(len(lf)):
    print(lf[i])
    for j in range(i+1,len(lf)):
        print(lf[j])
        #d=math.sqrt((lf[j][1]-lf[i][1])**2)+((lf[j][0]-lf[i][0]**2))
        d=math.sqrt( ((lf[j][1]-lf[i][1])**2)+((lf[j][0]-lf[i][0])**2) )
        print(d)
        if d<300: 
            close_person=close_person+ "Person" +str(i+1) +  "and Person"+str(j+1)+"not following social distancing"+";  "   
close_person+="are not following social distancing" 
print(close_person)       

# Display the output
#cv2.imshow('img', img)
#resize=cv2.resize(gray,(400,300))
cv2.imshow("priyanka",resize)
#cv2.imshow("priyanka",gray)
cv2.waitKey()
