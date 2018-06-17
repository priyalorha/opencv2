import cv2

def main():
	k=cv2.imread('4.1.01.tiff')
	cv2.imshow('image',k)
	cv2.waitKey(0)
	#cv2.show()
	cv2.destroyAllWindows();
	
    
	
	
	
	
	#print(cv2.__version__)
main()