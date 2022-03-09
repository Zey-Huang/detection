import sys
import time
import cv2 as cv
from PyQt5.QtWidgets import QApplication,  QAction
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import cv2
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,  parent= None):
        QtWidgets.QMainWindow.__init__(self)
        #文件名
        self.pathx2 ="nostart"
        self.mode=0
        #
        self.resize(360,360)
        self.setWindowTitle('人脸识别')
            #设置一个按钮
        button2=QtWidgets.QPushButton("开启人脸识别")
        button2.setParent(self)
        button2.resize(150,50)
        button2.move(100,100)
        button2.clicked.connect(self.work1)
            #
            #设置一个按钮
        button3=QtWidgets.QPushButton("开启口罩人脸识别")
        button3.setParent(self)
        button3.resize(150,50)
        button3.move(100,150)
        button3.clicked.connect(self.work2)
            #
            #设置一个按钮
        button4=QtWidgets.QPushButton("开启目标追踪")
        button4.setParent(self)
        button4.resize(150,50)
        button4.move(100,200)
        button4.clicked.connect(self.work3)
        #
        exit = QAction(QIcon('icons/Blue_Flower.ico'),  'Classifier Path', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Slect Classifier')
        exit.triggered.connect(self.classifier)
        self.statusBar()
        #
        exit2 = QAction(QIcon('icons/Blue_Flower.ico'),  'Vidicon Start', self)
        exit2.setShortcut('Ctrl+W')
        exit2.setStatusTip('Use Vidicon')
        exit2.triggered.connect(self.modechose1)
        self.statusBar()
        exit3 = QAction(QIcon('icons/Blue_Flower.ico'),  'Path Choose', self)
        exit3.setShortcut('Ctrl+E')
        exit3.setStatusTip('Slect Path')
        exit3.triggered.connect(self.modechose2)
        self.statusBar()
        #设置一个菜单项，来选择分类器

        menubar = self.menuBar()
        file = menubar.addMenu('&分类器')
        file.addAction(exit)
        #
        menubar2 = self.menuBar()
        file = menubar2.addMenu('&视频模式')
        file.addAction(exit2)
        file.addAction(exit3)
        #
    def classifier(self):
        image_file,_=QFileDialog.getOpenFileName(self,'选择分类器','C:/','Image files (*.xml)')
        pathMixName = image_file,_.split('/')
        self.pathx2 = "/".join(pathMixName[0:len(pathMixName)-1])
    def modechose1(self):
        self.mode=0;
    def modechose2(self):
        image_file,_=QFileDialog.getOpenFileName(self,'选择视频','C:/','Image files (*.mp4)')
        pathMixName = image_file,_.split('/')
        self.mode = "/".join(pathMixName[0:len(pathMixName)-1])
    def face_detect_demo(self,image):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray = cv.resize(gray, None, fx=1, fy=1)
        gray = cv.equalizeHist(gray)
        face_detector = cv.CascadeClassifier(self.pathx2)
        faces = face_detector.detectMultiScale(gray, 1.10, 5)
        for x, y, w, h in faces:
            cv.rectangle(image, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
        cv.imshow("result", image)
    def work1(self):
        if self.pathx2=="nostart":
            reply = QMessageBox.critical(self,"警告","没有选择正确的分类器,是否继续？",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply!=65536:
                capture = cv.VideoCapture(self.mode)
                capture.set(cv.CAP_PROP_FRAME_WIDTH,1920)
                capture.set(cv.CAP_PROP_FRAME_HEIGHT,1080)
                capture.set(cv.CAP_PROP_FPS, 144)
                cv.namedWindow("result", cv.WINDOW_NORMAL)
                while (True):
                    #按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
                    ret, frame = capture.read()
                    # cv.flip函数表示图像翻转，沿y轴翻转, 0: 沿x轴翻转, <0: x、y轴同时翻转
                    frame = cv.flip(frame, 1)
                    self.face_detect_demo(frame)
                    #waitKey（）方法本身表示等待键盘输入，参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
                    c = cv.waitKey(1)
                    if c == 27:#当键盘按下‘ESC’退出程序
                        break
        else :
                capture = cv.VideoCapture(self.mode)
                capture.set(cv.CAP_PROP_FRAME_WIDTH,1920)
                capture.set(cv.CAP_PROP_FRAME_HEIGHT,1080)
                capture.set(cv.CAP_PROP_FPS, 144)
                cv.namedWindow("result", cv.WINDOW_NORMAL)
                while (True):
                    #按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
                    ret, frame = capture.read()
                    # cv.flip函数表示图像翻转，沿y轴翻转, 0: 沿x轴翻转, <0: x、y轴同时翻转
                    frame = cv.flip(frame, 1)
                    self.face_detect_demo(frame)
                    #waitKey（）方法本身表示等待键盘输入，参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
                    c = cv.waitKey(1)
                    if c == 27:#当键盘按下‘ESC’退出程序
                        break
    def work2(self):
        if self.pathx2=="nostart":
            reply = QMessageBox.critical(self,"警告","没有选择正确的分类器,是否继续？",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply!=65536:
                detector = cv2.CascadeClassifier(self.pathx2)
                image_file,_=QFileDialog.getOpenFileName(self,'选择口罩分类器','C:\\','Image files (*.xml)')
                pathMixName = image_file,_.split('/')
                path = "/".join(pathMixName[0:len(pathMixName)-1])
                mask_detector = cv2.CascadeClassifier(path)
                cap = cv2.VideoCapture(self.mode)
                while True:
                    ret, img = cap.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.1, 3)
                    for (x, y, w, h) in faces:
                        # 参数分别为 图片、左上角坐标，右下角坐标，颜色，厚度
                        face = img[y:y + h, x:x + w]  # 裁剪坐标为[y0:y1, x0:x1]
                        mask_face = mask_detector.detectMultiScale(gray, 1.08, 5)
                    if len(mask_face) > 0:
                        for (x2, y2, w2, h2) in mask_face:
                            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
                    else:
                        for (x2, y2, w2, h2) in faces:
                            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)

                    cv2.namedWindow("result", 0)
                    cv2.imshow("result", img)
               # waitKey（）方法本身表示等待键盘输入，参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
                    c = cv2.waitKey(1)
                    if c == 27:  # 当键盘按下‘ESC’退出程序
                        break
        else:
            detector = cv2.CascadeClassifier(self.pathx2)
            image_file,_=QFileDialog.getOpenFileName(self,'选择口罩分类器','C:\\','Image files (*.xml)')
            pathMixName = image_file,_.split('/')
            path = "/".join(pathMixName[0:len(pathMixName)-1])
            mask_detector = cv2.CascadeClassifier(path)
            cap = cv2.VideoCapture(self.mode)
            i = 0
            while True:
                i=i+1
                #mark用来标志当前的检测结果（无人脸=-1；有人脸无口罩=0；有人脸有口罩=1）
                mark = -1
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.1, 3)
                for (x, y, w, h) in faces:
                  # 参数分别为 图片、左上角坐标，右下角坐标，颜色，厚度
                    face = img[y:y + h, x:x + w]  # 裁剪坐标为[y0:y1, x0:x1]
                mask_face = mask_detector.detectMultiScale(gray, 1.1, 5)
                if len(mask_face) > 0:
                    i = 0
                    mark = 1
                else:
                    # 用i++来进行延时消抖
                    if i > 20:
                        mark = 0
                if mark == 0:
                    cv2.putText(img, "Mask: no", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 6)
                    for (x2, y2, w2, h2) in faces:
                            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
                if mark == 1:
                    cv2.putText(img, "Mask: yes", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 6)
                    for (x2, y2, w2, h2) in mask_face:
                        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
                cv2.namedWindow("result", 0)
                cv2.imshow("result", img)
               # waitKey（）方法本身表示等待键盘输入，参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
                c = cv2.waitKey(1)
                if c == 27:  # 当键盘按下‘ESC’退出程序
                    break
    def work3(self):
        if self.pathx2=="nostart":
            reply = QMessageBox.critical(self,"警告","没有选择正确的分类器,是否继续？",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply!=65536:
                tracker = cv2.TrackerKCF_create()
                # Read video
                # video = cv2.VideoCapture(0)
                video = cv2.VideoCapture(self.mode)
                video.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
                video.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
                video.set(cv2.CAP_PROP_FPS, 144)

                # Exit if video not opened.
                if not video.isOpened():
                    print("Could not open video")
                    sys.exit()

                # Read first frame.
                ok, frame = video.read()
                if not ok:
                    print("Cannot read video file")
                    sys.exit()

                # Face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray, None, fx=1, fy=1)
                gray = cv2.equalizeHist(gray)
                # Loading the face classifier
                face_detector = cv2.CascadeClassifier(self.pathx2)
                faces = face_detector.detectMultiScale(gray,1.2, 5)
                n_faces = len(faces)
                print(n_faces)
                bbox = (0, 0, 0, 0)
                bbox = faces[0]

                # Initialize tracker with first frame and bounding box
                tracker.init(frame,tuple(bbox))

                while True:
                    # Read a new frame
                    ok, frame = video.read()
                    if not ok:
                        break

                    # Start timer
                    timer = cv2.getTickCount()

                    # Update tracker
                    ok, bbox = tracker.update(frame)

                    # Calculate Frames per second (FPS)
                    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

                    # Draw bounding box
                    if ok:
                        # # Tracking success
                        p1 = (int(bbox[0]), int(bbox[1]))
                        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
                    else:
                        # Tracking failure
                        cv2.putText(frame, "Tracking failure detected", (100, 340), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 6)

                    # Display tracker type on frame
                    cv2.putText(frame, "KCF Tracker", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 170, 50), 6)

                    # Display FPS on frame
                    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 170, 50), 6)

                    # Display result
                    cv2.namedWindow("Tracking", 0)
                    cv2.imshow("Tracking", frame)

                    # Exit if ESC pressed
                    k = cv2.waitKey(1) & 0xff
                    if k == 27: break
        else:
                tracker = cv2.TrackerKCF_create()
                # Read video
                # video = cv2.VideoCapture(0)
                video = cv2.VideoCapture(self.mode)
                video.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
                video.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
                video.set(cv2.CAP_PROP_FPS, 144)

                # Exit if video not opened.
                if not video.isOpened():
                    print("Could not open video")
                    sys.exit()

                # Read first frame.
                ok, frame = video.read()
                if not ok:
                    print("Cannot read video file")
                    sys.exit()

                # Face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray, None, fx=1, fy=1)
                gray = cv2.equalizeHist(gray)
                # Loading the face classifier
                face_detector = cv2.CascadeClassifier(self.pathx2)
                faces = face_detector.detectMultiScale(gray,1.2, 5)
                n_faces = len(faces)
                print(n_faces)
                bbox = (0, 0, 0, 0)
                bbox = faces[0]

                # Initialize tracker with first frame and bounding box
                tracker.init(frame,tuple(bbox))

                while True:
                    # Read a new frame
                    ok, frame = video.read()
                    if not ok:
                        break

                    # Start timer
                    timer = cv2.getTickCount()

                    # Update tracker
                    ok, bbox = tracker.update(frame)

                    # Calculate Frames per second (FPS)
                    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

                    # Draw bounding box
                    if ok:
                        # # Tracking success
                        p1 = (int(bbox[0]), int(bbox[1]))
                        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
                    else:
                        # Tracking failure
                        cv2.putText(frame, "Tracking failure detected", (100, 340), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 6)

                    # Display tracker type on frame
                    cv2.putText(frame, "KCF Tracker", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 170, 50), 6)

                    # Display FPS on frame
                    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 170, 50), 6)

                    # Display result
                    cv2.namedWindow("Tracking", 0)
                    cv2.imshow("Tracking", frame)

                    # Exit if ESC pressed
                    k = cv2.waitKey(1) & 0xff
                    if k == 27: break

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
