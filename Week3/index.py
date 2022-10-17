import cv2 
import pafy
from rich.console import Console
from rich.theme import Theme 
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)
url = "https://www.youtube.com/watch?v=4zbehnz-8QU"
	
video = pafy.new(url)
best = video.getbest(preftype="mp4")

source = cv2.VideoCapture(best.url)
def Main(id):
	console.print("Çıkmak için CTRL+C",style="error")
	try:
		while True:
			ret, img = source.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray, (5, 5), 0)
			canny = cv2.Canny(blur, 10, 70)
			ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
			if id == "1":
				cv2.imshow("Live", gray)
			elif id == "2":
				cv2.imshow("Live", blur)
			elif id == "3":
				cv2.imshow("Live", canny)
			elif id == "4":
				cv2.imshow("Live", mask)

			key = cv2.waitKey(1)
			if key == ord("q"):
				break
			
		cv2.destroyAllWindows()
		source.release()
	except KeyboardInterrupt:
		console.print("Script Sonlandırıldı!",style="success")
def GrayScale():
	console.print("Çıkmak için CTRL+C",style="error")
	try:
		while True:
			ret, img = source.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			cv2.imshow("Live", gray)
   
			key = cv2.waitKey(1)
			if key == ord("q"):
				break
			
		cv2.destroyAllWindows()
		source.release()
	except KeyboardInterrupt:
		console.print("Script Sonlandırıldı!",style="success")

def Blur():
	
	console.print("Çıkmak için CTRL+C",style="error")
	try:
		while True:
			ret, img = source.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray, (5, 5), 0)
			cv2.imshow("Live", blur)

			key = cv2.waitKey(1)
			if key == ord("q"):
				break
			
		cv2.destroyAllWindows()
		source.release()
	except KeyboardInterrupt:
		console.print("Script Sonlandırıldı!",style="success")
def Canny():
	
	console.print("Çıkmak için CTRL+C",style="error")
	try:
		while True:
			ret, img = source.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray, (5, 5), 0)
			canny = cv2.Canny(blur, 10, 70)
			cv2.imshow("Live", canny)

			key = cv2.waitKey(1)
			if key == ord("q"):
				break
			
		cv2.destroyAllWindows()
		source.release()
	except KeyboardInterrupt:
		console.print("Script Sonlandırıldı!",style="success")
def EdgeDetection():
	
	console.print("Çıkmak için CTRL+C",style="error")
	try:
		while True:
			ret, img = source.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray, (5, 5), 0)
			canny = cv2.Canny(blur, 10, 70)
			ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
			cv2.imshow("Live", mask)

			key = cv2.waitKey(1)
			if key == ord("q"):
				break
			
		cv2.destroyAllWindows()
		source.release()
	except KeyboardInterrupt:
		console.print("Script Sonlandırıldı!",style="success")