import cv2
import os


from os.path import splitext

path = "Images"  
images = []  
for file in os.listdir(path):
    filename, extension = splitext(file)  
    if extension == ".jpg":  
        file_name = os.path.join(path, file)  
        print(file_name)  
        images.append(file_name)  

count = len(images)  
frame = cv2.imread(images[0])  
height, width, channels = frame.shape  
size = (width, height)  
print(size)  

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)  


for i in range(count):
    img = cv2.imread(images[i])  
    out.write(img)  
    print(f"Imagem {i+1}/{count} adicionada ao vídeo.")

print("Concluído") 

out.release()  

