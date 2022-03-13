import serial, numpy, time, cv2, time
from PIL import Image



roadX = 385
skyX = 400
offRoadX = 10
midLineX = 245
rightEdgeX = 520


roadY = 340
skyY = 10
offRoadY = 160
midLineY = 300
rightEdgeY = 300

count = 0

while count < 2000:
    time.sleep(0)
    count += 1

    sourcePath  =   'C:\\Users\\ekhad\\Desktop\\rawvid_backup\\frame' + str(count+15000) + '.png'

    offRoadPath =   'C:\\Users\\ekhad\\Desktop\\training data\\btrain\\offroad\\offroad' + str(count) + '.png'
    roadPath =      'C:\\Users\\ekhad\\Desktop\\training data\\btrain\\road\\road' + str(count) + '.png'
    midLinePath =   'C:\\Users\\ekhad\\Desktop\\training data\\btrain\\road\\midline' + str(count) + '.png'
    skyPath =       'C:\\Users\\ekhad\\Desktop\\training data\\btrain\\offroad\\sky' + str(count) + '.png'
    rightEdgePath = 'C:\\Users\\ekhad\\Desktop\\training data\\btrain\\road\\rightedge' + str(count) + '.png'
    offRoadPath =   'C:\\Users\\ekhad\\Desktop\\training data\\btrain\\offroad\\offroad' + str(count) + '.png'

    frame = cv2.imread(sourcePath)
    pframe = Image.open('C:\\Users\\ekhad\\Desktop\\rawvid_backup\\frame' + str(count+15000) + '.png')

    road = numpy.array(pframe.crop((roadX, roadY, roadX + 40, roadY + 40)))
    sky = numpy.array(pframe.crop((skyX, skyY, skyX + 40, skyY + 40)))
    midLine = numpy.array(pframe.crop((midLineX, midLineY, midLineX + 40, midLineY + 40)))
    offRoad = numpy.array(pframe.crop((offRoadX, offRoadY, offRoadX + 40, offRoadY + 40)))
    rightEdge = numpy.array(pframe.crop((rightEdgeX, rightEdgeY, rightEdgeX + 40, rightEdgeY + 40)))

  
    for i in range(roadY, roadY+40):
        for j in range(roadX, roadX+40):
            frame[i][j][1] = 130
    for i in range(skyY, skyY+40):
        for j in range(skyX, skyX+40):
            frame[i][j][1] = 130
    for i in range(midLineY, midLineY+40):
        for j in range(midLineX, midLineX+40):
            frame[i][j][1] = 130
    for i in range(offRoadY, offRoadY+40):
        for j in range(offRoadX, offRoadX+40):
            frame[i][j][1] = 130
    for i in range(rightEdgeY, rightEdgeY+40):
        for j in range(rightEdgeX, rightEdgeX+40):
            frame[i][j][1] = 130

    '''



    cv2.imwrite(skyPath, sky)
    cv2.imwrite(offRoadPath, offRoad)
    cv2.imwrite(roadPath, road)
    cv2.imwrite(rightEdgePath, rightEdge)

    '''
    cv2.imwrite(midLinePath, midLine)


    for i in range(len(midLine)):
        for j in range(len(midLine)):
            midLine[i][j][0] = midLine[i][j][0]
            midLine[i][j][1] = midLine[i][j][1]
            midLine[i][j][2] = midLine[i][j][2]


    cv2.imshow('midline', midLine)
    cv2.imshow('sky', sky)
    cv2.imshow('rightEdge', rightEdge)
    cv2.imshow('offRoad', offRoad)
    cv2.imshow('road', road)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        1

    '''
    if count == 2000:
        count = 0


    '''

















































