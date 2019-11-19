import csv
import os
import cv2
counter = 0
corrupted = 0
with open('vggface2_disk1-09') as csvfile:
    for line in csvfile:
        print(counter)
        counter += 1
        print(line)
        line_split = line.split(',')
        try:
            file_line = line_split[0]
        except:
            continue
        file_name = '/mnt/nfs/scratch1/cmanjesh/data/VGGFaces2'+file_line.split('vggface2')[1]
        cropped_file_name = '/mnt/nfs/scratch1/cmanjesh/data/VGGFaces2Cropped2'+file_line.split('vggface2')[1]
        #print(file_name, cropped_file_name)
        img = cv2.imread(file_name)
        y = int(round(float(line_split[3])))
        x = int(round(float(line_split[2])))
        w = int(round(float(line_split[4])))
        h = int(round(float(line_split[5])))
        #print(cropped_file_name)
        try:
            #print('/mnt/nfs/scratch1/cmanjesh/data/VGGFaces2Cropped/train/'+cropped_file_name.split('/')[8]+'/')
            os.mkdir('/mnt/nfs/scratch1/cmanjesh/data/VGGFaces2Cropped2/train/'+cropped_file_name.split('/')[8]+'/')
        except Exception as e:
            pass
        try:
            img = img[y:y+h, x:x+w]
            if(img.size > 0):
                cv2.imwrite(cropped_file_name, img)
            else:
                continue
                corrupted += 1
        except Exception as e:
            corrupted += 1
            print('num corrupted = ',e)
