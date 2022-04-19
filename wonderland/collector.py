import requests, cv2, numpy

coords = [('39.4784593', '-88.1739754'), ('39.4784593', '-88.1739754')]
imgsize = '2000'
heading = '0'
pitch = '0'
fov = '40'

urls = []
for i in coords:
    urls.append("https://maps.googleapis.com/maps/api/streetview?size="+
                imgsize+"x"+imgsize+"&location="+i[0]+","+i[1]+"&fov="+fov+"&heading="+heading+"&pitch="+pitch
                +"&key=AIzaSyC4CFILOjXwmKqd7ehYgUwA9SkjE0D9HlA")

print(urls[1])

for i in range(len(urls)):
    img = requests.get(urls[i], stream=True).content

    with open("D:\\wonderland\\test\\"+str(i)+".png", "wb") as f:
        f.write(img)

imgs = []
for i in range(2):
    print(i)
    imgs.append(numpy.array(cv2.imread("D:\\wonderland\\test\\"+str(i)+".png")))

while 1:
    for i in range(len(imgs)):
        cv2.imshow(str(i), imgs[i])

    cv2.waitKey(1)