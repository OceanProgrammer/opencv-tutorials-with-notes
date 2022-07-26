import cv2
## READING IMAGES
cards = cv2.imread('img/cards.jpg') # matrix of the image
print(type(cards))
# cv2.imshow("Cards001", cards)
cv2.waitKey(0) # 1000ms = 1 sec

## READING VIDEOS
video = cv2.VideoCapture('videos/travelling_large.mp4')
print(video)
while True:
    completed, frame = video.read()
    cv2.imshow("Travelling", frame)

    if cv2.waitKey(10) & 0xFF==ord('i'):
        break
video.release()

cv2.destroyAllWindows()