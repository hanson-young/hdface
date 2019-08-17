#encoding=utf-8
__author__ = "hanson"
import cv2
from hdface.hdface import hdface_detector
import glob,os

if __name__ == '__main__':

    test_image_root = r'/media/yj_backup/hanson/safe_mao/ori_safemao/Images/03'
    factor = 1.0
    det = hdface_detector(use_cuda=True)

    total_num = 0
    path_list = glob.glob(os.path.join(test_image_root,"*.jpg"))

    for path in path_list:
        img = cv2.imread(path)

        img_bg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_bg = cv2.resize(img_bg,(int(img_bg.shape[1] * factor),int(img_bg.shape[0] * factor)))
        # img_bg = cv2.copyMakeBorder(img_bg, 100, 100, 100, 100,cv2.BORDER_CONSTANT)

        result = det.detect_face(img_bg)

        for i in range(len(result)):
            box = result[i]['box']
            cls = result[i]['cls']
            pts = result[i]['pts']
            cv2.rectangle(img_bg, (box[0], box[1]), (box[2], box[3]),(0, 255, 0), 2)

            cv2.circle(img_bg, (pts['leye'][0], pts['leye'][1]), 2, (0, 255, 0),2)
            cv2.circle(img_bg, (pts['reye'][0], pts['reye'][1]), 2, (0, 0, 255), 2)
            cv2.circle(img_bg, (pts['nose'][0], pts['nose'][1]), 2, (0, 255, 255), 2)
            cv2.circle(img_bg, (pts['lmouse'][0], pts['lmouse'][1]), 2, (0, 255, 0), 2)
            cv2.circle(img_bg, (pts['rmouse'][0], pts['rmouse'][1]), 2, (0, 0, 255), 2)

        cv2.imshow("img", cv2.cvtColor(img_bg,cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
