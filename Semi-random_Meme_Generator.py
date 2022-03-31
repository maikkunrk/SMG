# we import the following libraries to: open & show images with cv2
import cv2 as cv #open & show images with cv2
import random as rd # to create random numbers
import glob #The glob module finds all the pathnames matching a specified pattern

i = rd.randint(1, 11) #we set i as a random number so we can then influence the frequency of the images that will appear

images = glob.glob('*.png' or '*.jpg')# finds all images and shoves them to a list
# this in the end will influence the probability of different types of images from a template
if i<=5:
    n = rd.randint(0,7)
elif i>5 and i<=8:
    n = rd.randint(8,14)
elif i>8 and i<=11:
    n = rd.randint(15,19)

openedImage = images[n]# parses the image to the 'openedImage' variable
image = cv.imread(cv.samples.findFile(openedImage)) #loads the image
cv.imshow("Display Window", image) #displays the image
k = cv.waitKey(0) # keeps the window open until you press a key
# the number of images will change and many more templates will be added, also changes will be made to the probability of the program showing certain images
#in the end we want that part of the code to go randomly from template to template and for there to be a higher chance for the user to see an image we found on the internet,
#less chance for an image we created and lesser for a completely random one



#under development for checpoint 2
# we import the following libraries to: open & show images with cv2
import cv2 as cv #open & show images with cv2
import random as rd # to create random numbers
import glob #The glob module finds all the pathnames matching a specified pattern

j = rd.randint(0, 11) #we set j as a random number so we can then influence the chosen template
i = rd.randint(1, 11) #we set i as a random number so we can then influence the frequency of the images that will appear

images = glob.glob('numberz/*.png' or 'numberz/*.jpg') #finds all images and shoves them to a list
memes = glob.glob('memerz/*.png' or 'memerz/*.jpg')

# this in the end will influence the probability of different types of images from a template
if i<=5:
    n = rd.randint(0,7)
elif i>5 and i<=8:
    n = rd.randint(8,14)
elif i>8 and i<=11:
    n = rd.randint(15,19)

if j<=1:
    openedImage = images[n]#parses the image to the 'openedImage' variable
elif j>=2:
    openedImage = memes[n]
image = cv.imread(cv.samples.findFile(openedImage)) #loads the image
k = cv.waitKey(0) & 0xFF
if k == 27: # wait for ESC key to exit
    cv.destroyAllWindows()
cv.imshow("Display Window", image) #displays the image
k = cv.waitKey(0) # keeps the window open until you press a key
# the number of images will change and many more templates will be added, also changes will be made to the probability of the program showing certain images
#in the end we want that part of the code to go randomly from template to template and for there to be a higher chance for the user to see an image we found on the internet,
#less chance for an image we created and lesser for a completely random one
