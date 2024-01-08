import cv2

cap = cv2.VideoCapture(0) # (0) to find 1st camera access

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    _, frame = cap.read()
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 2, 2)
    for x, y, w, h, in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        face_roi = frame[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
    cv2.imshow('show frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
