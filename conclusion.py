from tkinter import *
from PIL import Image as Image_k
from PIL import ImageTk
from tkinter.simpledialog import *
import CallAPI
import random

def show_image():
    window = Tk()
    window.title("미세먼지 측정기")
    window.geometry("700x500")

    
    img_path_good = ["C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_03.jpg",
                "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_06.jpg",
                "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_13.jpg",
                "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_15.jpg",
                "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_17.jpg",
                "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_20.jpg",
                ]
    img_path_soso = ["C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_02.jpg",
                     "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_08.jpg",
                     "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_11.jpg",
                     "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_18.jpg",
                     ]
    img_path_bad = ["C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_01.jpg",
                    "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_04.jpg",
                    "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_07.jpg",
                    "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_09.jpg",
                    "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_16.jpg",]
    img_path_too_bad = ["C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_05.jpg",
                        "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_10.jpg",
                        "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_12.jpg",
                        "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_14.jpg",
                        "C:\\Users\\sinmi\\OneDrive\\바탕 화면\\파이썬 teamproject\\images\\KakaoTalk_20250525_094734829_19.jpg",]
    selected_img_path1 = random.choice(img_path_good)
    selected_img_path2 = random.choice(img_path_soso)
    selected_img_path3 = random.choice(img_path_bad)
    selected_img_path4 = random.choice(img_path_too_bad)
    
    image1 = Image_k.open(selected_img_path1)    
    image2 = Image_k.open(selected_img_path2)
    image3 = Image_k.open(selected_img_path3)
    image4 = Image_k.open(selected_img_path4)

    
    

    desired_width = 500
    desired_height = 300
    if CallAPI.c == 1:  
        try:
            resample_filter = Image_k.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image_k.LANCZOS 
        resized_image = image1.resize((desired_width, desired_height), resample_filter)
        
        label2 = Label(window, text="오늘의 미세먼지는 좋음입니다")
        label2.pack(side="top", pady=20)
        photo = ImageTk.PhotoImage(resized_image)




        label1 = Label(window, image=photo)
        label1.pack(side= "bottom",pady=20)
        window.mainloop()
    elif CallAPI.c == 2:

        try:
            resample_filter = Image_k.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image_k.LANCZOS 
        resized_image = image2.resize((desired_width, desired_height), resample_filter)
        
        label2 = Label(window, text="오늘의 미세먼지는 보통입니다")
        label2.pack(side="top", pady=20)
        photo = ImageTk.PhotoImage(resized_image)




        label1 = Label(window, image=photo)
        label1.pack(side= "bottom",pady=20)
        window.mainloop()
    elif CallAPI.c == 3:
        try:
            resample_filter = Image_k.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image_k.LANCZOS 
        resized_image = image3.resize((desired_width, desired_height), resample_filter)
        
        label2 = Label(window, text="오늘의 미세먼지는 나쁨입니다")
        label2.pack(side="top", pady=20)
        photo = ImageTk.PhotoImage(resized_image)




        label1 = Label(window, image=photo)
        label1.pack(side= "bottom",pady=20)
        window.mainloop()
    elif CallAPI.c == 4:
        try:
            resample_filter = Image_k.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image_k.LANCZOS 
        resized_image = image4.resize((desired_width, desired_height), resample_filter)
        
        label2 = Label(window, text="오늘의 미세먼지는 매우나쁨입니다")
        label2.pack(side="top", pady=20)
        photo = ImageTk.PhotoImage(resized_image)




        label1 = Label(window, image=photo)
        label1.pack(side= "bottom",pady=20)
        window.mainloop()