import cv2

# Video Capture from a store camera
cap = cv2.VideoCapture('store_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Process the frame for analytics
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Customer Movement', gray)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
