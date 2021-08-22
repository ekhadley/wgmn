import requests, cv2, numpy

coords = ('39.4784593', '-88.1739754')
imgsize = '2000'
heading = '0'
pitch = '0'
fov = '40'

url = "https://maps.googleapis.com/maps/api/streetview?size="+imgsize+"x"+imgsize+"&location="+coords[0]+","+coords[1]+"&fov="+fov+"&heading="+heading+"&pitch="+pitch+"&key=AIzaSyC4CFILOjXwmKqd7ehYgUwA9SkjE0D9HlA&scale=2"

img = requests.get(url, stream=True).content


with open("D:\\wonderland\\test\\1.png", "wb") as f:
    f.write(img)

imgs = []
for i in range(1, 3):
    print(i)
    imgs.append(numpy.array(cv2.imread("D:\\wonderland\\test\\"+str(i)+".png")))

while 1:
    for i in range(len(imgs)):
        cv2.imshow(i, imgs[i])