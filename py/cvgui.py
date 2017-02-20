import cv2
import numpy as np

def draw_keypoints(keypoints, im, color=(255,0,0)):

    for k in keypoints:
        radius = 3 #int(k.size / 2)
        center = (int(k[0]), int(k[1]))

        #Draw circle
        cv2.circle(im, center, radius, color)

def get_click(im, title='get_click'):
    global click_pos
    click_pos = None

    cv2.namedWindow(title)
    cv2.moveWindow(title, 100, 100)

    def onMouse(event, x, y, flags, param):
        global click_pos

        if flags & cv2.EVENT_FLAG_LBUTTON:
            click_pos = (x,y)

    cv2.setMouseCallback(title, onMouse)

    cv2.imshow(title,im)

    #Preview
    while click_pos is None:
        cv2.waitKey(10)

    cv2.destroyWindow(title)

    return click_pos

def select_pts(im, title='select_points'):

    cv2.namedWindow(title)
    cv2.moveWindow(title, 100, 100)

    pts = []

    scale = 1

    def draw():
        im_draw = cv2.resize(im, (0,0), fx=scale, fy=scale)
        scaled_pts = [(scale*a,scale*b) for (a,b) in pts]

        draw_keypoints(scaled_pts, im_draw)

        cv2.imshow(title, im_draw)


    def onMouse(event, x, y, flags, param):


        if event == cv2.EVENT_LBUTTONUP:
            pts.append((x/scale,y/scale))
            draw()


    cv2.setMouseCallback(title, onMouse)
    cv2.imshow(title, im)

    #Preview
    while True:
        key = cv2.waitKey(10)
        key = chr(key & 255)

        if key == 'q':
            break

        if key == 'd':
            pts.pop()
            draw()
        if key == '+':
            scale *= 2
            draw()
        if key == '-':
            scale /= 2
            draw()

    cv2.destroyWindow(title)

    return pts

def get_rect(im, title='get_rect', square = False):

    global tl
    global br

    tl = None
    br = None

    cv2.namedWindow(title)
    cv2.moveWindow(title, 100, 100)

    def onMouse(event, x, y, flags, param):

        global tl
        global br

        if square and tl is not None:
            #Check for square constraint
            x = max(x, tl[0] + (y - tl[1]))
            y = max(y, tl[1] + (x - tl[0]))

        current_pos = (x,y)

        if event == cv2.EVENT_LBUTTONUP and tl is None:
            tl = current_pos

        elif event == cv2.EVENT_LBUTTONUP and br is None:
            br = current_pos

        if tl is not None:
            im_draw = np.copy(im)
            cv2.rectangle(im_draw, tl, current_pos, (255,0,0))
            cv2.imshow(title, im_draw)

    cv2.setMouseCallback(title, onMouse)
    cv2.imshow(title,im)

    while br is None:

        cv2.waitKey(10)

    cv2.destroyWindow(title)

    #Make sure tl < br

    tl_final = (min(tl[0],br[0]), min(tl[1],br[1]))
    br_final = (max(tl[0],br[0]), max(tl[1],br[1]))

    return (tl_final,br_final)

