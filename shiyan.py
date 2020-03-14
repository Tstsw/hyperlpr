from hyperlpr import  pipline as  pp
import cv2
# 自行修改文件名
image = cv2.imread("D:/jupyter-folder/picture/car.jpg")
image,res  = pp.SimpleRecognizePlate(image)
print(res)

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv_show('a',image)