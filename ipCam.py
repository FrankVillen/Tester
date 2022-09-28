import cv2

# Test
cap = cv2.VideoCapture('rtsp://rtsp.stream/pattern')

# Congelados de Navarra
# cap = cv2.VideoCapture('rtsp://admin:camara123@172.16.17.99:554')
ret, frame = cap.read()
cv2.imwrite('newImage.png', frame)

# while True:
    # ret, frame = cap.read()
    # Run stream
    # cv2.imshow('frame', frame)

    # Take a snapshot
    # cv2.imwrite('opencv.png', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break

# cap.release()
# cv2.destroyAllWindows()
