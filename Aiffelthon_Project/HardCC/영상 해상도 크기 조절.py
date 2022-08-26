#전처리 코드

#영상 해상도 크기 조절

root = "D:/cctv/data_process/download"
change = "D:/cctv/data_process/downsize"

for dic in os.listdir(root):
    dic = "D:/cctv/data_process/download/" + dic
    dic2 = root + "/downsize"
    
    for di in os.listdir(dic):
        temp = di
        di = dic + "/" + di
        di2 = dic2 + "/" + temp
        
        for d in os.listdir(di):
            temp = d
            path ,exe = os.path.splitext(temp)
            d = di + "/" + d
            temp2 = di2 + "/" +temp
            
            if exe == '.mp4':
                command = "ffmpeg -i " + d +" -vf " + "scale=960*540 " + temp
                os.system(command)
    
    