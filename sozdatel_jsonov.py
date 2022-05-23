import random
import json
import os

SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY = {"john_list":[{"random":False,"x1":-2**68,"y1":405,"x2":2**68,"y2":505}], "platform_list":[], "end":{"x":3020, "y":0}}
x1 = 100
x2 = 200
y1 = random.randint(225,375)
y2 = y1+10
SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"].append({"random":False, "x1":x1, "y1":y1, "x2":x2, "y2":y2})


for i in range(0,-361,-2):
    lastY = SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"][-1]["y1"]
    idkw1 = lastY-60
    idkw2 = lastY+60
    x1 = i*100
    x2 = (i-1)*100
    y1 = random.randint(idkw1,idkw2)
    y2 = y1+10
    if y1 >= 400:
        y1 -= 100
        y2 = y1 + 10
    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"].append({"random":False, "x1":x1, "y1":y1, "x2":x2, "y2":y2})

for i in range(3,361,2):
    lastY = SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"][-1]["y1"]
    if i == 3:
        lastY = SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"][0]["y1"]
    idkw1 = lastY-60
    idkw2 = lastY+60
    x1 = i*100
    x2 = (i+1)*100
    y1 = random.randint(idkw1,idkw2)
    y2 = y1+10
    if y1 >= 400:
        y1 -= 100
        y2 = y1 + 10
    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["platform_list"].append({"random":False, "x1":x1, "y1":y1, "x2":x2, "y2":y2})

    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["end"]["y"] = y1-80
    SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY["end"]["x"] = x1+20

fail = open("parkur markur.json", "w")
json.dump(SAM_JSON_NE_EVO_SOBSTVENNOY_PERSONOY, fail)
fail.close()