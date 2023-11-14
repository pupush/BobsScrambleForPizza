import random
import json

SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY = {"john_list":[{"random":False,"x1":-2**68,"y1":450,"x2":2**68,"y2":525}], "platform_list":[], "jeremiah_list":[], "end":{"x":3020, "y":0}} #we're gonna turn this into a json!
x1 = 100
x2 = 200
y1 = random.randint(225,375)
y2 = y1+10
SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"].append({"random":False, "x1":x1, "y1":y1, "x2":x2, "y2":y2}) #first platform


for i in range(0,-361,-2): #left mfs
    lastY = SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"][-1]["y1"]
    idkw1 = lastY-40
    idkw2 = lastY+40 #these guys are gonna be a range
    x1 = i*125
    y1 = random.randint(idkw1,idkw2)
    x2 = (i-1)*125
    y2 = y1+10 #new platform coords
    if y1 >= 400:
        y1 -= 100
        y2 = y1 + 10 # i did this so platforms wouldn't be lower than the doom point
    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"].append({"random":False, "x1":x1, "y1":y1, "x2":x2, "y2":y2})

for i in range(3,361,2): #right mfs
    lastY = SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"][-1]["y1"]
    if i == 3:
        lastY = SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"][0]["y1"]
    idkw1 = lastY-40
    idkw2 = lastY+40
    x1 = i*125
    x2 = (i+1)*125
    y1 = random.randint(idkw1,idkw2)
    y2 = y1+10
    if y1 >= 400:
        y1 -= 100
        y2 = y1 + 10
    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"].append({"random":False, "x1":x1, "y1":y1, "x2":x2, "y2":y2})

    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["end"]["y"] = y1-80
    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["end"]["x"] = x1+20

faïl = open("parkur markur.json", "w")
json.dump(SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY, faïl) # we put our dict into a json file
faïl.close()