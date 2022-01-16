import time
import cv2
from grabscreen import grab_screen

time.sleep(2)
screen = grab_screen(region=(500,500,1200,800))
screen = cv2.resize(screen, (350, 150))
cv2.imshow('a',screen)
cv2.waitKey(0)
cv2.destroyAllWindows()