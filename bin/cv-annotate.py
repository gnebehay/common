#!/usr/bin/env python

import cv2
import numpy as np
import os
import sys
import cvbb
import cvseq
import cvutil

def prop_annotate(seq, prop):

    #Create path to annotation folder
    annot_folder = os.path.join('annotations', seq.identifier)

    #Create folder if it doesn't exist
    if not os.path.exists(annot_folder):
        os.mkdir(annot_folder)

    annotation_file = os.path.join(annot_folder, prop + '.label')
    if os.path.exists(annotation_file):
        annot = np.genfromtxt(annotation_file).astype(np.bool)
        if annot.shape[0] != seq.num_frames:
            raise Exception("Number of frames in annotation file differs from number of frames in sequence.")
    else:
        annot = np.zeros((seq.num_frames,1), dtype = np.bool)

    frame = 0

    start_frame = None
    gt = cvbb.poly2bb(seq.gt)
    while True:

        #Read image
        im_path = seq.im_list[frame]
        if not os.path.exists(im_path):
            raise Exception(im_path + ' does not exist')
        im = cv2.imread(im_path)

        #Display annotations
        im_text = str(frame+1)
        if annot[frame] == True:
            im_text += ' ' + prop

#        #Draw groundtruth
        gt_frame = gt[frame]
        if not np.any(np.isnan(gt_frame)):
            tl = cvutil.array_to_int_tuple(gt_frame[:2])
            br = cvutil.array_to_int_tuple(gt_frame[:2] + gt_frame[2:4])
            cv2.rectangle(im, tl, br, (255,0,0))

        cv2.putText(im, im_text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)

        #Show image, wait for key
        cv2.imshow(seq.identifier, im)
        key = cv2.waitKey(0)
        key = chr(key & 255)

        #Handle key
        if key == 's':
            print 'Start frame of annotation set.'
            start_frame = frame
        if key == 'e':
            if start_frame is not None:
                end_frame = frame+1
                annot[start_frame:end_frame] = True
                start_frame = None
                print 'End frame of annotation set.'
            else:
                print 'No start frame set for end frame'
        if key == 'd':
            print 'Deleting continuous annotation'
            if annot[frame]:
                #Delete forward
                frame_forward = frame
                while frame_forward < seq.num_frames and annot[frame_forward] == True:
                    annot[frame_forward] = False
                    frame_forward += 1

                frame_backward = frame-1
                while frame_backward >= 0 and annot[frame_backward] == True:
                    annot[frame_backward] = False
                    frame_backward -= 1
        if key == 'x':
            print 'Deleting single annotation'
            annot[frame] = False
        #Standard movement
        if key == 'S' or key == ' ':
            frame += 1
        if key == 'Q':
            frame -= 1 #Go back one frame
        if key == 'P':
            frame = 0
        if key == 'W':
            frame = seq.num_frames-1
        if key == 'm':
            frame = seq.num_frames / 2
        if key == 'V':
            frame += seq.num_frames / 100
        if key == 'U':
            frame -= seq.num_frames / 100
        if key == 'q':
            break

        #Don't go out of bounds
        frame = max(frame, 0)
        frame = min(frame, seq.num_frames-1)

    #When loop was exited, save file
    annotation_file = os.path.join(annot_folder, prop + '.label')
    np.savetxt(annotation_file, annot, fmt = '%d')

if __name__ == "__main__":
    top_dir = sys.argv[1]
    seq_name = sys.argv[2]
    seqs = cvseq.load_sequences(top_dir)
    seq = seqs[seq_name]
    seq.load()
    prop = sys.argv[3]

    #Create annotations folder
    if not os.path.exists('annotations'):
        os.mkdir('annotations')

    prop_annotate(seq, prop)
