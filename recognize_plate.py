from hyperlpr import pipline as pp
import cv2
"""
def recognize_plate_my(image):
    '''
    调用车牌检测方法识别车牌，写此方法，供main函数调用
    :param image: 传入的图片，只需要识别出车牌即可
    :return:
    '''
    # image = cv2.imread("包含车牌图像的路径")
    # image=cv2.imread(filename)
    image, res = pp.SimpleRecognizePlate(image)
    print(res)

    return res

"""


def recognize_plate_my(image):
    '''
    调用车牌检测方法识别车牌，写此方法，供main函数调用
    :param image: 传入的图片，只需要识别出车牌即可
    :return:
    '''
    # image = cv2.imread("包含车牌图像的路径")
    # image=cv2.imread(filename)
    image, res = pp.SimpleRecognizePlateByE2E(image)
    print(res)

    return res
