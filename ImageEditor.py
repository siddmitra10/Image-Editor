#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
This program takes the input of an image and manually creates a grayscale version, rotates it by a certain number of degrees, or box filters it.

Assignment Information
	Assignment:     Python Project
	Author:         Kate Wilson, wils1061
                    Emme Longman, elongman
                    Siddharth Mitra, mitra30
                    Jeff Huang, huan1399
                    
	Team ID:        002-17 (e.g. 001-14 for section 1 team 14)
	
Contributor:                    
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import cv2 #imports Open CV to be later used in the file
import numpy as np #imports numpy to help with array interpretation

image = str(input("Enter the filename of your image: ")) #prompts the user to input the file name of the image
while image:
    if image.endswith('.jpg')==True: #If the image ends with a .jpg, the image will run effectively and continue with the code
        break
    elif image.endswith('.jpg')==False: #If the image is not a .jpg, it will ask for another
        image=str(input('Image is not a .jpg, please enter another: '))
    

processing = input("Enter the type of processing wanted on image [grayscale, rotation, or box filtering]: ")

while processing:
    if processing in ['rotation', 'box filtering', 'grayscale', 'mirror' ,'show me everything you can do']:
        break
    else:
        processing=str(input('Program cannot do that type of processing; please enter grayscale, rotation, or box filtering: '))
    
if processing == 'grayscale':
    def Grayscale(image):
        import cv2 #imports Open CV to be later used in the file
        import numpy as np #imports numpy to help with array interpretation
            
        image = cv2.imread(f'{image}') #reads the image
        l = np.array(image) #makes the image array into a new variable to be later referenced
            
        def Make_Zero_Array(image): 
            shape = np.shape(image) #finds the shape (rows, columns, depth) of the image
            A = np.zeros(shape) #creates an array full of zeros with that same image shape
            return A #returns the zeros array for later referencing
        
        A = Make_Zero_Array(image) #runs the above UDF
        
        def Make_Grayscale(l,A):
            for i in range(len(l)): #iterates through rows
                for j in range(len(l[0])): #iterates through columns
                    A[i][j]=np.sum((l[i][j])/3) #sets a specific i and j coordinate spot in the zero array equal to the grayscale value at that point in the image, which is just an average of the red, green, and blue values
            return A #returns the new array, which has filled-in values for grayscale
        
        A = Make_Grayscale(l,A) #runs the above UDF
            
        def Make_Grayscale_Image(A):
            cv2.imwrite('grayscaleimg.jpg',A) #writes/creates the new image from the array A, saves it in Downloads on a computer for later access
            GrayscaleImage = cv2.imread('grayscaleimg.jpg') #reads the image file from the computer
            cv2.imshow('GrayscaleImage',GrayscaleImage) #creates a new window within Spyder for the image to load and show in
            cv2.waitKey(0) #waits for user to close out
            cv2.destroyAllWindows() #closes window when user hits the close button
            
        Make_Grayscale_Image(A) #runs the above UDF
        
    Grayscale(image)
        
if processing == 'rotation':
    
#    x=input('Enter name of image you want to edit: ') #this takes the name of the image as input from the user
    action=input('Enter one of the following [rotate 90 degrees, rotate 180 degrees, rotate 270 degrees, or mirror]: ') #this takes the required action as an input from the user
    while action:
        if action in ['rotate 90 degrees', 'rotate 180 degrees', 'rotate 270 degrees', 'mirror', 'show me everything you can do']: #If the angle is not one of the ones entered, it will prompt for another.
            break
        else: 
            action=input('Please enter a correct angle: ') #This will prompt the user for another input.

    img=cv2.imread(image)

    def mirror(img): #defines the user-defined function: mirror
        h,w,c = img.shape #assigns height, width and channels of the original image to variables h,w,and c 
        empty_img = np.zeros([h,w,c], dtype=np.uint8) #creates an empty array that has the same h,w,and c as the original imgage 
        for origCol1 in range(w): #it starts a for-loop in the range (o,width of the image) and assigns a new value to variable origCol1 everytime it runs
            newCol1 = int(w-origCol1 - 1) #this uses the values of origCol1 and w to assign newCol1 new value everytime the for-loop runs
            for origRow1 in range(h): #this starts a nested for-loop inside the previous for-loop and assigns origRow1 new value in the range(o,height of the image) everytime the for-loop runs
                newRow1 = int(origRow1) #it uses value of origRow1 to assign new value to newRow1 everytime the for loop runs
                empty_img[newRow1, newCol1] = img[origRow1, origCol1] #uses value of newRow1,newCol1,origRow1 and origCol1 to assign them as coordinates for the new image
        cv2.imwrite("mirrored.jpg", empty_img) #takes data from empty_img and writes it onto a new file "mirrrored.jpg" 
        cv2.imshow("mirrored.jpg", empty_img) #display the data in empty_image as an image in a new window named mirrored.jpg
        cv2.waitKey(50000)
        cv2.destroyAllWindows()
#mirror(img)
        
    def rotate180(img): #defines the user-defined function: rotate180
        h,w,c = img.shape #assigns height, width and channels of the original image to variables h,w,and c 
        empty_img = np.zeros([h,w,c], dtype=np.uint8) #creates an empty array that has the same h,w,and c as the original imgage 
        for i in range(h): #it starts a for loop in the range (o,height of the image) and assigns a new value to the variable i every time the loop runs
            for j in range(w): #it starts a for loop in the range (o,width of the image) and assigns a new value to variable j every time the loop runs
                empty_img[i,j] = img[h-i-1,w-j-1] #uses values of i,j in every loop to assign new coordinate value to data in empty_img
        cv2.imwrite("rotated_180.jpg", empty_img) #takes data from empty_img and writes it onto a new file "rotated_180.jpg" 
        cv2.imshow("rotated_180.jpg", empty_img) #display the data in empty_image as an image in a new window named rotated_180.jpg 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#rotate180(img)
    
    def rotate270(img): #defines the user-defined function: rotate270
        h,w,c = img.shape #assigns height, width and channels of the original image to variables h,w,and c 
        empty_img = np.zeros([w,h,c], dtype=np.uint8) #creates an empty array that has the same height as w(width) and same width as h(height) and same c as that of the original imgage 
        for origRow1 in range(h): #it starts a for loop in the range (o,height of the image) and assigns a new value to variable origRow1 everytime it the loop runs
            newCol1 = int(h-origRow1 - 1) #this uses the values of origRow1 and h to assign newCol1 new value everytime the for loop runs
            for origCol1 in range(w): #this starts a nested for-loop inside the previous for-loop and assigns origCol1 new value in the range(o,width of the image) everytime the for-loop runs
                newRow1 = int(origCol1) #it uses value of origCol1 to assign new value to newRow1 everytime the for loop runs
                empty_img[newRow1, newCol1] = img[origRow1, origCol1] #uses value of newRow1,newCol1,origRow1 and origCol1 to assign them as coordinates for the new image
        cv2.imwrite("rotated_270.jpg", empty_img) #takes data from empty_img and writes it onto a new file "rotated_270.jpg" 
        cv2.imshow("rotated_270.jpg", empty_img) #display the data in empty_image as an image in a new window named rotated_270.jpg 
        cv2.waitKey(0)
        cv2.destroyAllWindows()    
#rotate270(img)
    
    def rotate90(img): #defines the user-defined function: rotate270
        h,w,c = img.shape #assigns height, width and channels of the original image to variables h,w,and c 
        empty_img = np.zeros([w,h,c], dtype=np.uint8) #creates an empty array that has the same height as w(width) and same width as h(height) and same c as that of the original imgage 
        for origCol1 in range(w): #it starts a for-loop in the range (o,width of the image) and assigns a new value to variable origCol1 everytime it runs
            newRow1 = int(w - origCol1 - 1) #this uses the values of origCol1 and w to assign newRow1 new value everytime the for-loop runs
            for origRow1 in range(h): #this starts a nested for-loop inside the previous for-loop and assigns origRow1 new value in the range(o,height of the image) everytime the for-loop runs
                newCol1 = int(origRow1) #it uses value of origRow1 to assign new value to newCol1 everytime the for loop runs
                empty_img[newRow1, newCol1] = img[origRow1, origCol1] #uses value of newRow1,newCol1,origRow1 and origCol1 to assign them as coordinates for the new image
        cv2.imwrite("rotated_90.jpg", empty_img) #takes data from empty_img and writes it onto a new file "rotated_90.jpg" 
        cv2.imshow("rotated_90.jpg", empty_img) #display the data in empty_image as an image in a new window named rotated_90.jpg 
        cv2.waitKey(0)
        cv2.destroyAllWindows()    
#rotate90(img)
        
    if action=="mirror":
        mirror(img)
    elif action=="rotate 90 degrees":
        rotate90(img)
    elif action=="rotate 180 degrees":
        rotate180(img)
    elif action=="rotate 270 degrees":
        rotate270(img)
    elif action=="show me everything you can do":
        mirror(img)
        rotate90(img)
        rotate180(img)
        rotate270(img)
    
if processing == 'box filtering':
    
   def boxfilter():
          imagename=image
          from PIL import Image, ImageDraw    
    #Open image 
          imfile = Image.open(imagename)    

    #Load image pixel data into Pixel Access Object
          inputfile = imfile.load()
    
    #Define kernel values
          box_kernel = [[1 / 9, 1 / 9, 1 / 9],
                         [1 / 9, 1 / 9, 1 / 9],
                         [1 / 9, 1 / 9, 1 / 9]]
           
           #Find center of kernel
          boxcenter = len(box_kernel) // 2
           
          outfile = Image.new("RGB", imfile.size) 
           
           #Function for output image
          def displayoutput():
               outfile.save("output.jpg")
               outfile.show()
            
           #Function for translating the new filtered values onto the output Pixel Access Object
          filter = ImageDraw.Draw(outfile)
           
           #function that calculates RGB values for new pixels, by multiplying pixels by box filter
          def findnewpixels(rgb):
               finalpixels[rgb] += pixel[rgb] * box_kernel[kernelxvalue][kernelyvalue]
           
           #For loop that iterates for each row between the center of the box filter
           #and the edges of the image on the x-axis. 
          for imagex in range(boxcenter, imfile.width - boxcenter):
               
               #For loop that iterates for each row between the center of the box filter
               #and the edges of the image on the y-axis.
              for imagey in range(boxcenter, imfile.height - boxcenter):
                  
                   #Empty matrix that will eventually become the final pixel values
                  finalpixels = [0, 0, 0]
                   
                   #For loop that iterates for each x-value of the box filter
                  for kernelxvalue in range(len(box_kernel)):
                       
                       #For loop that iterates for each y-value of the box filter
                      for kernelyvalue in range(len(box_kernel)):
                         
                           #Define where the pixels land on the 3x3 box filter
                          xo = imagex + kernelxvalue - boxcenter
                          yo = imagey + kernelyvalue - boxcenter
                          pixel = inputfile[xo, yo]
                           
                           #call "findnewpixels" function
                          findnewpixels(0)
                          findnewpixels(1)
                          findnewpixels(2)
                   
                   #Calls "filter" function
                  filter.point((imagex, imagey), (int(finalpixels[0]), int(finalpixels[1]), int(finalpixels[2])))

           #Calls "display image" function
          displayoutput()
   boxfilter()
    