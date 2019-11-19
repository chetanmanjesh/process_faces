import os
for folder in os.listdir('VGGFaces2Cropped2/train'):
    count = 0
    for file_name in os.listdir('VGGFaces2Cropped2/train/'+str(folder)):
        count += 1
        try:
            os.mkdir('VGGFaces2Cropped2/val/'+folder)
        except:
            pass
        os.system('mv VGGFaces2Cropped2/train/'+str(folder)+'/'+str(file_name)+' VGGFaces2Cropped2/val/'+folder+'/'+str(file_name))
        if count == 2:
            break
