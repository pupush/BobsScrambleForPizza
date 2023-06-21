from tkinter import *
import random
import json
import os
from dataclasses import dataclass
from conflict_CZECH_REPUBLIC import *
import time
# these are modules

root = Tk()
# basically the place i work in

@dataclass
class Jeremih:
    treugolnik_telo: int
    speedX: int
    speedY: int
    vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228 : int
    stoIt: bool
# this is jeremy, he can move, we will use him later

def levelы(uroven_nazvanie): #levels
    global c, absolut_vodka, pizza_png, boboprobivaemiy, list_fotochkov, pizza, bob, vspomoGosha, vspomoGosha_v2_0, vspomoGosha_v3_0, vspomoGosha_v4_0, vspomoGosha_v5_0, pressed_a, pressed_d, pressed_s, end_flag, speedX, speedY, tick_duration, stoIt, jeremy_stoIt, gravity, FRICKtion_FUCKtor, X, Y, john_list, TOZHOS, platform_list, jeremy_list, jump_list, invis_list, key_list
    # globallin da shit (the things we will need later) outta here

    f = open(os.path.join("levelы", uroven_nazvanie)) #the path to the level yo wanna play
    coord_dacha = json.load(f) #loadin it up
    f.close() #we dont need the module os anymore
    john_data = coord_dacha["john_list"]
    platform_data = coord_dacha.get("platform_list", [])
    jump_data = coord_dacha.get("jumpy_list", [])
    jeremy_data = coord_dacha.get("jeremy_list", [])
    invis_data = coord_dacha.get("invis_list", [])
    key_data = coord_dacha.get("key_list", [])
    end_data = coord_dacha["end"]
    #the objects' json data

    c = Canvas(root, width=400, height=400)
    c.pack()
    #the canvas

    absolut_vodka = c.create_rectangle(0,0,1,1, outline="", tags="vse_fignjuliny")
    #absolute zero point, dont question it, its for the camera physics basically

    klyuchi = []
    for klucz in os.listdir(path="klyuchi"):
        klyuchi.append(klucz)
    #adding the images of all da keys into here, then im gonna take one o' those brave boys randomly to use in the level, if there are any in the level
    
    NUZHNIE_klyuchi = random.sample(klyuchi, k=len(key_data)) #here it is

    pizza_png = PhotoImage(file = "zhrachka.png") #bob's pizza's photo
    boboprobivaemiy = PhotoImage(file = "platformichulechka.png") #fake platform
    pizza = c.create_image(end_data["x"], end_data["y"], image=pizza_png, anchor="nw", tags="vse_fignjuliny") #THE bob's pizza
    bob = c.create_rectangle(135, 220, 165, 250, outline="#000", fill="#7d3", tags="vse_fignjuliny") #THE MAIN PROTAGONIST, THE ONE AND ONLY, BOB THE THIRD OF BRITTANY-BURGUNDIA THE SON OF THe GOD OF WAR OF ROME ARES HIMSELF!!!!
    vspomoGosha = c.create_rectangle(end_data["x"], end_data["y"], end_data["x"] + pizza_png.width(), end_data["y"] + pizza_png.height(), outline="", tags="vse_fignjuliny") # pizza's hitbox
    vspomoGosha_v2_0 = c.create_rectangle(250,0,460,9999999, outline="") #left end of camera, it starts to go lefter
    vspomoGosha_v3_0 = c.create_rectangle(-460,0,130,9999999, outline="") #right end of camera, it starts to go righter
    vspomoGosha_v4_0 = c.create_rectangle(-2**68,-9999999999999,2**68,100) #bottom end of camera
    vspomoGosha_v5_0 = c.create_rectangle(-2**68,9999999999999,2**68,300) #top end of camera, it starts to go top

    pressed_a = False
    pressed_s = False
    pressed_d = False
    # for detecting when to move
    end_flag = False
    # for end text

    speedX = 0 # pixels per second on the horizontal axis (default setting)
    speedY = 5 # pixels er second on the vertical axis (default setting)
    jeremy_speedX = 75 #speed of jeremy to the player in pixels per second
    jeremy_speedY = 0 # this will be not 0 only whe jeremy falls
    tick_duration = 0.01 # one in-game tick in seconds
    stoIt = False # is the player standing on something or not (by default)
    jeremy_stoIt = False #same for jeremy (by default)
    gravity = 300
    FRICKtion_FUCKtor = 300 #friction
    X = float(c.coords(bob)[0]) #bob's horizontal coordinate
    Y = float(c.coords(bob)[1]) #bob's vertical coordinate

    john_list = [] 
    TOZHOS = [] #Tebe Ostalos' ZHyt' Odnu Sekundu        aka camera regulator, this is the point of doom, where it is 150 units lower than the upper side of the lowest john. There is bo escape from there, only suffer.
    platform_list = []
    jump_list = []
    jeremy_list = []
    invis_list = [] #fake platform list
    key_list = []
    list_fotochkov = [] #basically the list of the photos of da keys or smth like that

    def iz_levela():
        global TOZHOS
        for john in john_data:
            if john["random"]:
                rand_x1, rand_y1, rand_x2, rand_y2 = john["rand_x1"], john["rand_y1"], john["rand_x2"], john["rand_y2"]
                x = random.randint(rand_x1, rand_x2)
                y = random.randint(rand_y1, rand_y2)
                x1 = x
                y1 = y
                x2 = x+60
                y2 = y+60
            else:
                x1 = john["x1"]
                x2 = john["x2"]
                y1 = john["y1"]
                y2 = john["y2"]

            predatel_amogus = c.create_rectangle(x1, y1, x2, y2, outline="#000", fill="#a00", tags=("vse_fignjuliny"))
            john_list.append(predatel_amogus)
            TOZHOS.append(y1)

        for platform in platform_data:
            if platform["random"]:
                rand_x1, rand_y1, rand_x2, rand_y2 = platform["rand_x1"], platform["rand_y1"], platform["rand_x2"], platform["rand_y2"]
                x = random.randint(rand_x1, rand_x2)
                y = random.randint(rand_y1, rand_y2)
                x1 = x
                y1 = y
                x2 = x+100
                y2 = y+10
            else:
                x1 = platform["x1"]
                x2 = platform["x2"]
                y1 = platform["y1"]
                y2 = platform["y2"]

            zheleznskiy_amogus = c.create_rectangle(x1, y1, x2, y2, outline="#000", fill="#F5F5DC", tags=("vse_fignjuliny")) 
            platform_list.append(zheleznskiy_amogus)

        for ZHUMP in jump_data:
            if ZHUMP["random"]:
                rand_x1, rand_y1, rand_x2, rand_y2 = ZHUMP["rand_x1"], ZHUMP["rand_y1"], ZHUMP["rand_x2"], ZHUMP["rand_y2"]
                x = random.randint(rand_x1, rand_x2)
                y = random.randint(rand_y1, rand_y2)
                x1 = x
                y1 = y
                x2 = x+60
                y2 = y+60
            else:
                x1 = ZHUMP["x1"]
                x2 = ZHUMP["x2"]
                y1 = ZHUMP["y1"]
                y2 = ZHUMP["y2"]

            prygus = c.create_rectangle(x1, y1, x2, y2, outline="#000", fill="#dd0", tags=("vse_fignjuliny"))
            jump_list.append(prygus)

        for jeremy in jeremy_data:
            x1 = jeremy["x1"]
            y1 = jeremy["y1"]
            x2 = x1-15
            y2 = y1+30
            x3 = x1+15
            y3 = y1+30
            trёugolnik = c.create_polygon(x1,y1,x2,y2,x3,y3,outline="#000", fill="#0000ff", tags="vse_fignjuliny")
            VOVAN228 = c.create_rectangle(x1-(x1-x2)/2,y1/2,x1+(x3-x1)/2,y2, outline="#000", tags="vse_fignjuliny")
            jeremy_list.append(Jeremih(treugolnik_telo=trёugolnik, speedX=jeremy_speedX, speedY=jeremy_speedY, vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228=VOVAN228, stoIt=jeremy_stoIt))

        for invis in invis_data:
            x = invis["x"]
            y = invis["y"]
            obmanSCHTSCHikoviy_amogus = c.create_image(x, y, image=boboprobivaemiy, anchor="nw", tags="vse_fignjuliny")
            invis_list.append(obmanSCHTSCHikoviy_amogus)
        
        for id, key in enumerate(key_data):
            key_x = key["key_x"]
            key_y = key["key_y"]
            vassal_x1 = key["vassal_x1"]
            vassal_y1 = key["vassal_y1"]
            vassal_x2 = key["vassal_x2"]
            vassal_y2 = key["vassal_y2"]
            fotochka = PhotoImage(file=f"klyuchi\\{NUZHNIE_klyuchi[id]}")
            klucz_kasatel = c.create_rectangle(key_x, key_y, key_x + fotochka.width(), key_y + fotochka.height(), outline="", fill="", tags="vse_fignjuliny")
            otkrivatelniy_amogus = c.create_image(key_x, key_y, image=fotochka, anchor="nw", tags="vse_fignjuliny")
            vasSALOviy_sugoma = c.create_rectangle(vassal_x1, vassal_y1, vassal_x2, vassal_y2, outline="#000", fill="#F5F5DC", tags="vse_fignjuliny")
            key_list.append([otkrivatelniy_amogus, vasSALOviy_sugoma, klucz_kasatel])
            list_fotochkov.append(fotochka)

    iz_levela() #this function gets all the data of all the objects in the level.

    TOZHOS = max(TOZHOS) #lowest john point

    pressed_a = False
    pressed_s = False
    pressed_d = False
    end_flag = False # a flag which says did the level end or not
    # wasd flags

    speedX = 0 # player's speed on the X axis in pixels per second
    speedY = 5 # same shit but on the Y axis
    tick_duration = 0.01 # in seconds
    stoIt = False #determines if the player's standing on a platform or an another thing that i might add in the future idk 
    gravity = 300  # how strong the gravity is
    FRICKtion_FUCKtor = 300 # how strong the friction is
    X = float(c.coords(bob)[0]) # X position
    Y = float(c.coords(bob)[1]) # Y position

    def move_left(event):
        global pressed_a
        pressed_a = True
        go_czechker()
    def stop_left(event):
        global pressed_a, speedX
        pressed_a = False

    def move_right(event):
        global pressed_d
        pressed_d = True
        go_czechker()
    def stop_right(event):
        global pressed_d
        pressed_d = False

    def move_down(event):
        global pressed_s
        pressed_s = True
        go_czechker()
    def stop_down(event):
        global pressed_s
        pressed_s = False
    #things that say OMG THIS KEY IS PUSHED ON THE KEYBOARD

    def no_gravity(event): #you don't know about this...
        global gravity
        gravity = 0

    def yes_gravity(event): #and about this...
        global gravity
        gravity = 300

    root.bind("<KeyPress-s>", move_down)
    root.bind("<KeyRelease-s>", stop_down)

    root.bind("<KeyPress-d>", move_right)
    root.bind("<KeyRelease-d>", stop_right)

    root.bind("<KeyPress-a>", move_left)
    root.bind("<KeyRelease-a>", stop_left)

    root.bind("<KeyPress-n>", no_gravity)
    root.bind("<KeyPress-y>", yes_gravity)

    root.bind("<KeyPress-k>", lambda event: root.destroy())
    root.bind("<KeyPress-space>", jump)
    # if the things that say about OMG THE GUY PUSHED A KEY are the guys who told the jokes, these guys are the guys who told the joke louder
    
    fizika_czech() # it goes down...
    zagolovchik.destroy() #fuck the title, lets kick it out
    for knopochk in list_knopochek:
        knopochk.destroy() # yeah and also fuck the buttons, they're stupid
    nenuzhniy_dibil.destroy() # 1. why did i call him that way? 2. he's not useless, he's actually useful, he helps the level buttons arrange correctly

def parkurchek(): # same thing as levelы, but with the help of sozdatel jsonov, if there's something diffferent i'll say it
    import sozdatel_jsonov #another file in the same folder, go look it up you lazy dum dum
    global c, absolut_vodka, pizza_png, boboprobivaemiy, list_fotochkov, pizza, bob, vspomoGosha, vspomoGosha_v2_0, vspomoGosha_v3_0, vspomoGosha_v4_0, vspomoGosha_v5_0, pressed_a, pressed_d, pressed_s, end_flag, speedX, speedY, tick_duration, stoIt, jeremy_stoIt, gravity, FRICKtion_FUCKtor, X, Y, john_list, TOZHOS, platform_list, jeremy_list, jump_list, invis_list, key_list
    c = Canvas(root, width=400, height=400)
    c.pack()
    absolut_vodka = c.create_rectangle(0,0,0,0, outline="", tags="vse_fignjuliny")

    f = open("parkur markur.json") # don't look at this file, your eyes are gonna bleed, i explain this in sozdatel jsonov
    coord_dacha = json.load(f)
    f.close()
    john_data = coord_dacha["john_list"]
    platform_data = coord_dacha["platform_list"] #this thing is HUGE
    end_data = coord_dacha["end"]

    img = PhotoImage(file = "zhrachka.png")
    pizza = c.create_image(end_data["x"], end_data["y"], image=img, anchor="nw", tags="vse_fignjuliny")
    bob = c.create_rectangle(150, 220, 180, 250, outline="#000", fill="#7d3", tags="vse_fignjuliny") 
    vspomoGosha = c.create_rectangle(end_data["x"], end_data["y"], end_data["x"] + img.width(), end_data["y"] + img.height(), outline="", tags="vse_fignjuliny")
    vspomoGosha_v2_0 = c.create_rectangle(250,0,460,9999999, outline="") 
    vspomoGosha_v3_0 = c.create_rectangle(-460,0,130,9999999, outline="") 
    vspomoGosha_v4_0 = c.create_rectangle(-2**68,-9999999999999,2**68,100)
    vspomoGosha_v5_0 = c.create_rectangle(-2**68,300,2**68,999999999999, outline="#653")  

    john_list = []
    TOZHOS = [] #Tebe Ostalos' ZHyt' Odnu Sekundu
    platform_list = []
    jump_list = []
    jeremy_list = []
    invis_list = []
    key_list = []
    list_fotochkov = []

    def parkurist():
        global TOZHOS
        for john in john_data:
            if john["random"]:
                rand_x1, rand_y1, rand_x2, rand_y2 = john["rand_x1"], john["rand_y1"], john["rand_x2"], john["rand_y2"]
                x = random.randint(rand_x1, rand_x2)
                y = random.randint(rand_y1, rand_y2)
                x1 = x
                y1 = y
                x2 = x+60
                y2 = y+60
            else:
                x1 = john["x1"]
                x2 = john["x2"]
                y1 = john["y1"]
                y2 = john["y2"]

            krasniy_amogus = c.create_rectangle(x1, y1, x2, y2, outline="#000", fill="#a00", tags=("vse_fignjuliny"))
            john_list.append(krasniy_amogus)
            TOZHOS.append(y1)

        for platform in platform_data:
            if platform["random"]:
                rand_x1, rand_y1, rand_x2, rand_y2 = platform["rand_x1"], platform["rand_y1"], platform["rand_x2"], platform["rand_y2"]
                x = random.randint(rand_x1, rand_x2)
                y = random.randint(rand_y1, rand_y2)
                x1 = x
                y1 = y
                x2 = x+60
                y2 = y+60
            else:
                x1 = platform["x1"]
                x2 = platform["x2"] 
                y1 = platform["y1"]
                y2 = platform["y2"]
            zheleznskiy_amogus = c.create_rectangle(x1, y1, x2, y2, outline="#000", fill="#F5F5DC", tags=("vse_fignjuliny")) 
            platform_list.append(zheleznskiy_amogus)
    parkurist()

    TOZHOS = max(TOZHOS)

    pressed_a = False
    pressed_s = False
    pressed_d = False
    end_flag = False

    speedX = 0 # це пиксели въ секунду
    speedY = 5 # це тоже
    tick_duration = 0.01 # це въ секундахъ
    stoIt = False
    gravity = 300
    FRICKtion_FUCKtor = 300
    X = float(c.coords(bob)[0])
    Y = float(c.coords(bob)[1])
    jump_speed = 10 # wtf is this?! this ain't used nowhere!

    def move_left(event):
        global pressed_a
        pressed_a = True
        go_czechker()
    def stop_left(event):
        global pressed_a, speedX
        pressed_a = False

    def move_right(event):
        global pressed_d
        pressed_d = True
        go_czechker()
    def stop_right(event):
        global pressed_d
        pressed_d = False

    def move_down(event):
        global pressed_s
        pressed_s = True
        go_czechker()
    def stop_down(event):
        global pressed_s
        pressed_s = False

    def no_gravity(event):
        global gravity
        gravity = 0

    def yes_gravity(event):
        global gravity
        gravity = 300

    root.bind("<KeyPress-s>", move_down)
    root.bind("<KeyRelease-s>", stop_down)

    root.bind("<KeyPress-d>", move_right)
    root.bind("<KeyRelease-d>", stop_right)

    root.bind("<KeyPress-a>", move_left)
    root.bind("<KeyRelease-a>", stop_left)

    root.bind("<KeyPress-n>", no_gravity)
    root.bind("<KeyPress-y>", yes_gravity)

    root.bind("<KeyPress-k>", lambda event: root.destroy())
    root.bind("<KeyPress-space>", jump)
    
    fizika_czech()
    zagolovchik.destroy()
    parkOURCZECH.destroy()
    play.destroy()

zagolovchik = Label(root, text="BOB'S SCRAMBLE \nFOR PIZZA", anchor="nw", font="Open_Sans 20") #title
zagolovchik.pack()

def vыbiratelь(): #buttonz
    global list_knopochek, nenuzhniy_dibil
    vse_uROVni = os.listdir(path="levelы") #list of levels' files
    list_knopochek = []  # button list
    list_levelov = [] #level list
    nenuzhniy_dibil = Frame(root) #explained him at the end of levelы
    nenuzhniy_dibil.pack()

    for i, lvl in enumerate(vse_uROVni):
        def ya_zadobalsya_pridumyvat_nazvaniya(lvl): #level launcher
            return lambda : levelы(lvl)
        
        if i%4 == 0: #creates new row if the current one has more than 4 levels
            novaya_rota = Frame(nenuzhniy_dibil) # the new row
            novaya_rota.pack(fill="x")
        
        knopocheka = Button(novaya_rota, text=f"{i+1}", padx=10, pady=10, command=ya_zadobalsya_pridumyvat_nazvaniya(lvl)) # a level button 
        knopocheka.pack(side="left", padx=(21.5,0), pady=15)
        list_knopochek.append(knopocheka)
        list_levelov.append(lvl)
    
    play.destroy()
    parkOURCZECH.destroy()

play = Button(root, text="Play", padx=20, pady=10, command=vыbiratelь) # basically summons a list of level buttons
parkOURCZECH = Button(root, text="Parkour practice", padx=20, pady=10, command=parkurchek) # parkour arena button
play.pack()
parkOURCZECH.pack()

def fizika_czech(): # i think i'm gonna vomit... this is the physics machine of this game. and it's awful.
    global X, Y, speedX, speedY, stoIt, jeremy_stoIt, end_flag, absoluteY
    root.after(int(tick_duration*1000), fizika_czech) # this says after tick_duration milliseconds (a second is 1000 milliseconds, and tick_duration is in seconds, that's why i multiplied tick_duration by 1000) do this function (so it's just a while True but with a timer)
    absoluteY = c.coords(bob)[1] - c.coords(absolut_vodka)[1] # Y, but better
    oldX, oldY = X, Y # X and Y of the old iteraiton
    X += speedX * tick_duration # S = Vt so the new X is the old X but player's x speed * 0.01 seconds more
    Y += speedY * tick_duration # same thing but with Y
    if not stoIt:
        speedY += gravity * tick_duration # if the player doesn't stand on a surface, his vertical speed must increase by gravity * 0.01 seconds
    
    for ZHIRIMI in jeremy_list: 
        jeremy_oldX, jeremy_oldY = c.coords(ZHIRIMI.treugolnik_telo)[0], c.coords(ZHIRIMI.treugolnik_telo)[1] # jeremy's X and Y of the old iteration
        jeremy_X, jeremy_Y = c.coords(ZHIRIMI.treugolnik_telo)[0], c.coords(ZHIRIMI.treugolnik_telo)[1] #jeremy's X and Y position
        jeremy_X += ZHIRIMI.speedX * tick_duration # same thing as 429 and 430 but for jeremy
        jeremy_Y += ZHIRIMI.speedY * tick_duration
        if not ZHIRIMI.stoIt: # if jeremy doesn't stand on a surface, his vertical speed must increase by gravity * 0.01 seconds
            ZHIRIMI.speedY += gravity*tick_duration
        
        c.coords(ZHIRIMI.treugolnik_telo, jeremy_X, jeremy_Y, jeremy_X-15, jeremy_Y+30, jeremy_X+15, jeremy_Y+30) #this draws a jeremy
        c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, jeremy_X-(jeremy_X-15)/2, jeremy_Y, jeremy_X+(jeremy_X+15)/2, jeremy_Y+30) #jeremy's hitbox
        
        for platform in platform_list:
            KOLYAsion_v2_0 = collision_czech(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, platform) #collision bool set
            Иеремий_collisionX_left, Иеремий_collisionX_right, Иеремий_collisionY_top, Иеремий_collisionY_bottom = KOLYAsion_v2_0.collisions
            Иеремий_collisionX = KOLYAsion_v2_0.collisionX
            
            if Иеремий_collisionX_left or Иеремий_collisionX_right:
                jeremy_X = jeremy_oldX 
                c.coords(ZHIRIMI, jeremy_X, jeremy_Y, jeremy_X-15, jeremy_Y+30, jeremy_X+15, jeremy_Y+30)
            
            if Иеремий_collisionY_top or Иеремий_collisionY_bottom:
                ZHIRIMI.speedY = 0
                jeremy_Y = jeremy_oldY
                c.coords(ZHIRIMI, jeremy_X, jeremy_Y, jeremy_Y, jeremy_X-15,jeremy_Y+30, jeremy_X+15, jeremy_Y+30)
                if Иеремий_collisionY_top:
                    ZHIRIMI.stoIt = platform
            
            elif not Иеремий_collisionX and ZHIRIMI.stoIt == platform:
                ZHIRIMI.stoIt = False
        
        if any(collision_czech(bob, ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228).collisions):
            root.destroy()
        
        if c.coords(bob)[2] < c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228)[0]:
            ZHIRIMI.speedX = -75
        
        if c.coords(bob)[0] > c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228)[2]:
            ZHIRIMI.speedX = 75
        
        c.coords(ZHIRIMI.treugolnik_telo, jeremy_X, jeremy_Y, jeremy_X-15, jeremy_Y+30, jeremy_X+15, jeremy_Y+30)
        c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, jeremy_X-(jeremy_X-(jeremy_X-15))/2,jeremy_Y,jeremy_X+((jeremy_X+15)-jeremy_X)/2,jeremy_Y+30)
    
    FRICKtion(tick_duration)
    
    c.coords(bob, X, Y, X+30, Y+30)

    if any(any(collision_czech(bob, john).collisions) for john in john_list):
        root.destroy()
    
    if not end_flag and any(collision_czech(bob,vspomoGosha).collisions):
        end_flag = True
        c.create_text(200,50,text="Поздравляю, ты дошел до просто стоящей и никак не \nдвигающейся pizzы! Даже собака с моего двора \nэто не смогла сделать!")
        root.after(5000, root.destroy)
    
    for platform in platform_list:
        KOLYAsion = collision_czech(bob,platform)
        collisionX_left, collisionX_right, collisionY_top, collisionY_bottom = KOLYAsion.collisions
        collisionX = KOLYAsion.collisionX
        
        if collisionX_left or collisionX_right:
            speedX = 0
            X = oldX
            c.coords(bob, X, Y, X+30, Y+30)
        
        if collisionY_top or collisionY_bottom:
            speedY = 0
            Y = oldY
            c.coords(bob, X, Y, X+30, Y+30)
            if collisionY_top:
                stoIt = platform
        
        if not collisionX and stoIt == platform:
            stoIt = False
    
    if any(collision_czech(bob, jump).collisions[2] for jump in jump_list):
        speedY = -300
    
    elif any(collision_czech(bob, jump).collisions[0] for jump in jump_list) or any(collision_czech(bob, jump).collisions[1] for jump in jump_list):
        speedX = 0
    
    elif any(collision_czech(bob, jump).collisions[3] for jump in jump_list):
        speedY = 0
    
    for l in key_list:
        klucz, vassal, kasalka = l
        try:
            if any(collision_czech(bob, vassal).collisions):
                X = oldX
                Y = oldY
                speedX = 0
                speedY = 0
            if any(collision_czech(bob, kasalka).collisions):
                c.delete(kasalka)
        except:
            try:
                if not any(collision_czech(bob, vassal).collisions):
                    c.coords(klucz, c.coords(bob)[0]-110, c.coords(bob)[1]-15)
                elif any(collision_czech(bob, vassal).collisions):
                    c.delete(vassal)
                    c.delete(klucz)
            except:
                pass

    if collision_czech(bob, vspomoGosha_v2_0).any():
        X -= speedX*tick_duration + 0.0625
        c.move("vse_fignjuliny", -speedX*tick_duration, 0)
    
    if collision_czech(bob, vspomoGosha_v3_0).any():
        X -= speedX*tick_duration - 0.0625
        c.move("vse_fignjuliny", -speedX*tick_duration, 0)
    
    if speedY < 0:
        if any(collision_czech(bob, vspomoGosha_v4_0).collisions):
            Y -= speedY*tick_duration - 0.0625
            c.move("vse_fignjuliny", 0, -speedY*tick_duration)
    
    if absoluteY < TOZHOS-150:
        if any(collision_czech(bob,vspomoGosha_v5_0).collisions):
            Y -= speedY*tick_duration + 0.0625
            c.move("vse_fignjuliny", 0, -speedY*tick_duration)

def FRICKtion(timer_thing):
    global pressed_a, pressed_d, stoIt, speedX, FRICKtion_FUCKtor
    if not pressed_a and stoIt:
        if speedX > 0:
            speedX -= FRICKtion_FUCKtor * timer_thing
    
    if not pressed_d and stoIt:
        if speedX < 0:
            speedX += FRICKtion_FUCKtor * timer_thing
    
def go_czechker(): # before fizika_czech became a thing, this thing was glorius lmfao now he's this
    global speedX,speedY
    if pressed_a:
        speedX -= 150
        if speedX < -150:
            speedX = -150
    
    if pressed_s:
        speedY += 1
    
    if pressed_d:
        speedX += 150
        if speedX >= 150:
            speedX = 150

def jump(event=None):
    global stoIt
    global speedY
    if stoIt:
        stoIt = False
        speedY = -200

def collision_czech(someone1, someone2):
    pos1 = c.coords(someone1)
    pos2 = c.coords(someone2)
    return conflict_czechk(pos1, pos2)

root.mainloop()

print("UwU")
# ꙮ this is an actual letter lmfao