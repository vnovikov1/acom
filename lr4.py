import cv2
import time
import numpy as np

video = cv2.VideoCapture("images/lr4_main.mov", cv2.CAP_ANY)   #чтение видео из файла

# video = cv2.VideoCapture(0)

ok, frame = video.read()   #первое значение true/false содержит ли video кадр для чтения, второе - фактический кадр						
old_frame_1 = frame   #первый кадр

w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))   #c помощью get получаем высоту и ширину исходного видео
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')   #видеокодек, способ сжатия видеопотока, для mp4 xvid 
video_writer = cv2.VideoWriter("images/output4.mov", fourcc, 25, (w, h))   #создаем объект класса videowriter для записи видео 

countr = 0   #переменная для дальнейшего сравнения площадей контуров

while (True):   #пока нет break
	ok, frame_2 = video.read()   #читаем кадр 
	if ok == False:   #если кадр не прочитался, выходим 
		break
	frame_1 = frame_2   #frame_1 - текущий кадр 
	old_frame = cv2.GaussianBlur(cv2.cvtColor(old_frame_1, cv2.COLOR_BGR2GRAY), (11,11), 0)   #переводим самый первый кадр в чб и блюр
	frame = cv2.GaussianBlur(cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY), (11,11), 0)   #переводим текущий кадр в чб и блюр
	frame_diff = cv2.absdiff(frame, old_frame)   #находим разницу между самым первым и текущим кадром и записываем в переменную 
	# нахождение разницы двух кадров, которая проявляется лишь при изменении одного из них, т.е. с этого момента наша программа реагирует на любое движение
	rt, frame_diff = cv2.threshold(frame_diff, 10, 255, cv2.THRESH_BINARY)   #операция двоичного разделения фрейма
	contours, hierarchy  = cv2.findContours(frame_diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   #находим контуры объектов для фрейма frame_diff 
	# cv2.imshow("Difference Frame", frame_diff)


	if contours != ():
		countr_now = cv2.contourArea(contours[0])
		# print(countr_now)
		if countr_now >= countr:
			video_writer.write(frame_1)
		countr = countr_now

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	old_frame_1 = frame_1.copy()

video.release()
video_writer.release()

cap = cv2.VideoCapture("images/output4.mov",cv2.CAP_ANY)
while (True):
	ok, frame = cap.read()
	if not ok:
		break
	time.sleep(0.04)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()