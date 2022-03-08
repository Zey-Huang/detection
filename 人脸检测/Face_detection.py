import cv2 as cv

def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.resize(gray, None, fx=1, fy=1)
    gray = cv.equalizeHist(gray)
    # face_detector = cv.CascadeClassifier("D:/pyproject/cv_renlianjiance/haarcascades/haarcascade_frontalface_alt_tree.xml")
    face_detector = cv.CascadeClassifier("C:/Users/16426/Desktop/py/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray, 1.10, 5)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
    cv.imshow("result", image)

# capture = cv.VideoCapture(0)#其中的0表示电脑中的第一个相机
capture = cv.VideoCapture("C:/Users/16426/Desktop/py/demo.mp4")
capture.set(cv.CAP_PROP_FRAME_WIDTH,1920)
capture.set(cv.CAP_PROP_FRAME_HEIGHT,1080)
capture.set(cv.CAP_PROP_FPS, 144)
cv.namedWindow("result", cv.WINDOW_NORMAL)
while (True):
    #按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
    ret, frame = capture.read()
    # cv.flip函数表示图像翻转，沿y轴翻转, 0: 沿x轴翻转, <0: x、y轴同时翻转
    frame = cv.flip(frame, 1)
    face_detect_demo(frame)
    #waitKey（）方法本身表示等待键盘输入，参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
    c = cv.waitKey(1)
    if c == 27:#当键盘按下‘ESC’退出程序
        break
capture.release()
#cv.waitKey(0)参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停,；
cv.waitKey(0)
cv.destroyAllWindows()#作用是能正常关闭绘图窗口