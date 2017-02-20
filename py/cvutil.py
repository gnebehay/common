import cv2
import math
import numpy as np

class FileVideoCapture(object):

    def __init__(self, path):
        self.path = path
        self.frame = 1

    def isOpened(self):
        im = cv2.imread(self.path.format(self.frame))
        return im != None

    def read(self):
        im = cv2.imread(self.path.format(self.frame))
        status = im != None
        if status:
            self.frame += 1
        return status, im

def squeeze_pts(X):
    X = X.squeeze()
    if len(X.shape) == 1:
        X = np.array([X])
    return X

def array_to_int_tuple(X):
    return (int(X[0]),int(X[1]))

def in_rect(keypoints, tl, br):
    if type(keypoints) is list:
        keypoints = keypoints_cv_to_np(keypoints)

    x = keypoints[:,0]
    y = keypoints[:,1]

    C1 = x >= tl[0]
    C2 = y >= tl[1]
    C3 = x <= br[0]
    C4 = y <= br[1]

    result = C1 & C2 & C3 & C4

    return result

def keypoints_cv_to_np(keypoints_cv):
    keypoints = np.array([k.pt for k in keypoints_cv])
    return keypoints

def keypoints_np_to_cv(keypoints):
    keypoints_cv = []
    for k in keypoints:
        keypoints_cv.append((k[0], k[1]))

    return keypoints_cv

def find_nearest_keypoints(keypoints, pos, number = 1):
    if type(pos) is tuple:
        pos = np.array(pos)
    if type(keypoints) is list:
        keypoints = keypoints_cv_to_np(keypoints)

    #TODO: Use L2norm here?
    pos_to_keypoints = np.sqrt(np.power(keypoints - pos,2).sum(axis=1))
    ind = np.argsort(pos_to_keypoints)
    return ind[:number]

def rotate(pt, rad):
    pt_rot = np.empty(pt.shape)

    s, c = [f(rad) for f in (math.sin, math.cos)]

    pt_rot[:,0] = c*pt[:,0] - s*pt[:,1]
    pt_rot[:,1] = s*pt[:,0] + c*pt[:,1]

    return pt_rot
