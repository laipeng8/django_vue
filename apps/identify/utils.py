# 银行卡验证  流程，传入照片，得到银行卡号

class Identify_bank:
    def __init__(self):
        # 初始化卷积核
        rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
        sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

        digits = {}  # 定义一个字典来存储数字模板
        locs = []  # 存储轮廓
    def template(self):
        template = cv2.imread('image/template1.png')
        # cv2.imshow('template', template)

        template_Gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('gray', template_Gray)

        # 二值图
        template_binary = cv2.threshold(template_Gray, 177, 255, cv2.THRESH_BINARY_INV)[1]
        # cv2.imshow('binary', template_binary)
        # 提取轮廓
        # cv2.findContours的参数是二值图  ，cv2.RETR_EXTERNAL检测外轮廓（外轮廓计算外界矩形），cv2.CHAIN_APPROX_SIMPLE保留终点坐标
        refCnts, his = cv2.findContours(template_binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(template, refCnts, -1, (0, 0, 255), 2)  # -1表示所有轮廓
        # cv2.imshow('contour', template)  # 轮廓图
        # print(len(refCnts))  # 打印轮廓数量
        # 遍历每一个轮廓
        for (i, c) in enumerate(refCnts):
            # 计算外接矩形并且resize成合适大小
            (x, y, w, h) = cv2.boundingRect(c)  # 外接矩形
            roi = template[y:y + h, x:x + w]
            roi = cv2.resize(roi, (57, 88))
            # 每一个数字对应每一个模板
            digits[i] = roi
        return digits#

    def resize(self,image, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]  # 获取图像的高度和宽度
        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))
        resized = cv2.resize(image, dim, interpolation=inter)  # 使用cv库的resize函数
        return resized
    def indentiy_bank(self,image):
        image = resize(image, width=300)
        # 转化为灰度图
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('gray',gray)
        # 礼帽操作，突出更明亮的区域
        tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
        # cv2.imshow('tophat_card',tophat)
        # 梯度运算：边缘检测，计算出轮廓
        gradx = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
        grady = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
        gradx = np.absolute(gradx)
        minVal = np.min(gradx)
        maxVal = np.max(gradx)
        # 保证值的范围在0-255之间
        gradx = (255 * ((gradx - minVal) / (maxVal - minVal)))
        gradx = gradx.astype("uint8")
        # cv2.imshow('gray_crad',grady)

        # print(np.array(gradx).shape)
        # 闭操作：通过闭操作（先膨胀，再腐蚀）将数字连在一起,便于后面求矩形框
        gradx = cv2.morphologyEx(gradx, cv2.MORPH_TOPHAT, rectKernel)
        # cv2.imshow('gray_crad', grady)

        # 阈值分割：利用阈值对图片进行二值化处理, 聚焦处理部分
        # THRESH_OTSU会自动寻找合适的阈值，适合双峰，需要把阈值设置为0
        thresh = cv2.threshold(gradx, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # cv2.imshow('thresh_card',thresh)

        # 再进行闭操作
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
        # cv2.imshow("thresh2_card",thresh)
        # 计算轮廓  检测外轮廓，保留终点坐标
        threshCnts, his = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = threshCnts
        cur_img = image.copy()
        cv2.drawContours(cur_img, cnts, -1, (0, 0, 255), 2)  # -1表示所有的轮廓
        cv2.imshow('contour_card', cur_img)
