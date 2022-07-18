from __future__ import absolute_import
from tkinter import *
import random
import json
import os
from dataclasses import dataclass

root = Tk()

@dataclass
class Jeremih:
    treugolnik_telo: int
    speedX: int
    speedY: int
    vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228 : int
    stoIt: bool

def levelы(uroven_nazvanie):
    global c, absolut_vodka, pizza_png, boboprobivaemiy, pizza, bob, vspomoGosha, vspomoGosha_v2_0, vspomoGosha_v3_0, vspomoGosha_v4_0, vspomoGosha_v5_0, pressed_a, pressed_d, pressed_s, end_flag, speedX, speedY, tick_duration, stoIt, Jeremiah_stoIt, gravity, FRICKtion_FUCKtor, X, Y, john_list, TOZHOS, platform_list, jeremiah_list, jump_list, invis_list
    f = open(os.path.join("levelы", uroven_nazvanie))
    coord_dacha = json.load(f)
    f.close()
    john_data = coord_dacha["john_list"]
    platform_data = coord_dacha["platform_list"]
    jump_data = coord_dacha["jumpy_list"]
    jeremiah_data = coord_dacha["jeremiah_list"]
    invis_data = coord_dacha["invis_list"]
    end_data = coord_dacha["end"]

    c = Canvas(root, width=400, height=400)
    c.pack()

    absolut_vodka = c.create_rectangle(0,0,1,1, outline="", tags="vse_fignjuliny")

    pizza_png = PhotoImage(file = "zhrachka.png")
    boboprobivaemiy = PhotoImage(file = "platformichulechka.png")
    pizza = c.create_image(end_data["x"], end_data["y"], image=pizza_png, anchor="nw", tags="vse_fignjuliny")
    bob = c.create_rectangle(135, 220, 165, 250, outline="#000", fill="#7d3", tags="vse_fignjuliny") 
    vspomoGosha = c.create_rectangle(end_data["x"], end_data["y"], end_data["x"] + pizza_png.width(), end_data["y"] + pizza_png.height(), outline="", tags="vse_fignjuliny")
    vspomoGosha_v2_0 = c.create_rectangle(250,0,460,9999999, outline="") 
    vspomoGosha_v3_0 = c.create_rectangle(-460,0,130,9999999, outline="") 
    vspomoGosha_v4_0 = c.create_rectangle(-2**68,-9999999999999,2**68,100) 
    vspomoGosha_v5_0 = c.create_rectangle(-2**68,9999999999999,2**68,300)

    pressed_a = False
    pressed_s = False
    pressed_d = False
    end_flag = False

    speedX = 0 # це пиксели въ секунду
    speedY = 5 # це тоже
    Jeremiah_speedX = 75
    Jeremiah_speedY = 0
    tick_duration = 0.01 # це въ секундахъ
    stoIt = False
    Jeremiah_stoIt = False
    gravity = 300
    FRICKtion_FUCKtor = 300
    X = float(c.coords(bob)[0])
    Y = float(c.coords(bob)[1])

    john_list = []
    TOZHOS = [] #Tebe Ostalos' ZHyt' Odnu Sekundu
    platform_list = []
    jump_list = []
    jeremiah_list = []
    invis_list = []

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

        for jeremiah in jeremiah_data:
            x1 = jeremiah["x1"]
            y1 = jeremiah["y1"]
            x2 = x1-15
            y2 = y1+30
            x3 = x1+15
            y3 = y1+30
            trёugolnik = c.create_polygon(x1,y1,x2,y2,x3,y3,outline="#000", fill="#00f", tags="vse_fignjuliny")
            VOVAN228 = c.create_rectangle(x1-(x1-x2)/2,y1,x1+(x3-x1)/2,y2, outline="", tags="vse_fignjuliny")
            jeremiah_list.append(Jeremih(treugolnik_telo=trёugolnik, speedX=Jeremiah_speedX, speedY=Jeremiah_speedY, vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228=VOVAN228, stoIt=Jeremiah_stoIt))

        for invis in invis_data:
            x = invis["x"]
            y = invis["y"]
            obmanSCHTSCHikoviy_amogus = c.create_image(x, y, image=boboprobivaemiy, anchor="nw", tags="vse_fignjuliny")
            invis_list.append(obmanSCHTSCHikoviy_amogus)

    iz_levela()

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
    play.destroy()
    zagolovchik.destroy()
    parkOURCZECH.destroy()
    for knopochk in list_knopochek:
        knopochk.destroy()

def parkurchek():
    import sozdatel_jsonov
    global c, absolut_vodka, img, pizza, bob, vspomoGosha, vspomoGosha_v2_0, vspomoGosha_v3_0, vspomoGosha_v4_0, vspomoGosha_v5_0, pressed_a, pressed_d, pressed_s, end_flag, speedX, speedY, tick_duration, stoIt, gravity, FRICKtion_FUCKtor, X, Y, john_list, TOZHOS, platform_list, jump_list, jeremiah_list
    c = Canvas(root, width=400, height=400)
    c.pack()
    absolut_vodka = c.create_rectangle(0,0,0,0, outline="", tags="vse_fignjuliny")

    f = open("parkur markur.json")
    coord_dacha = json.load(f)
    f.close()
    john_data = coord_dacha["john_list"]
    platform_data = coord_dacha["platform_list"]
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
    TOZHOS = [] #Tebe Osatlos' ZHyt' Odnu Sekundu
    platform_list = []
    jump_list = []
    jeremiah_list = []

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
    jump_speed = 10 # wtf is this?!

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
    play.destroy()
    zagolovchik.destroy()
    parkOURCZECH.destroy()
#for lvl, i in zip(vse_uROVni, range(0, len(vse_uROVni)))
zagolovchik = Label(root, text="BOB'S SCRAMBLE \nFOR PIZZA", anchor="nw", font="Open_Sans 20")
zagolovchik.pack()
def vыbiratelь(): 
    global list_knopochek
    vse_uROVni = os.listdir(path="levelы")
    list_knopochek = []
    list_levelov = []
    for i, lvl in enumerate(vse_uROVni):
        def ya_zadobalsya_pridumyvat_nazvaniya(lvl):
            return lambda : levelы(lvl) 
        knopocheka = Button(root, text=f"{i+1}", padx=10, pady=10, command=ya_zadobalsya_pridumyvat_nazvaniya(lvl))
        knopocheka.pack()
        list_knopochek.append(knopocheka)
        list_levelov.append(lvl)
    play.destroy()
    parkOURCZECH.destroy()
play = Button(root, text="Play", padx=20, pady=10, command=vыbiratelь)
parkOURCZECH = Button(root, text="Parkour practice", padx=20, pady=10, command=parkurchek)
play.pack()
parkOURCZECH.pack()

def fizika_czech():
    global X, Y, speedX, speedY, stoIt, Jeremiah_stoIt, end_flag, absoluteY
    root.after(int(tick_duration*1000), fizika_czech)
    absoluteY = c.coords(bob)[1] - c.coords(absolut_vodka)[1]
    oldX, oldY = X, Y
    X += speedX * tick_duration
    Y += speedY * tick_duration
    if not stoIt:
        speedY += gravity * tick_duration
    for ZHIRIMI in jeremiah_list: 
        Jeremiah_oldX, Jeremiah_oldY = c.coords(ZHIRIMI.treugolnik_telo)[0], c.coords(ZHIRIMI.treugolnik_telo)[1]
        Jeremiah_X, Jeremiah_Y = c.coords(ZHIRIMI.treugolnik_telo)[0], c.coords(ZHIRIMI.treugolnik_telo)[1]
        Jeremiah_X += ZHIRIMI.speedX * tick_duration
        Jeremiah_Y += ZHIRIMI.speedY * tick_duration
        if not ZHIRIMI.stoIt:
            ZHIRIMI.speedY += gravity*tick_duration
        c.coords(ZHIRIMI.treugolnik_telo, Jeremiah_X, Jeremiah_Y, Jeremiah_X-15, Jeremiah_Y+30, Jeremiah_X+15, Jeremiah_Y+30)
        c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, Jeremiah_X-(Jeremiah_X-(Jeremiah_X-15))/2,Jeremiah_Y,Jeremiah_X+((Jeremiah_X+15)-Jeremiah_X)/2,Jeremiah_Y+30)
        for platform in platform_list:
            KOLYAsion_v2_0 = conflict_czechk(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, platform)
            Иеремий_collisionX_left, Иеремий_collisionX_right, Иеремий_collisionY_top, Иеремий_collisionY_bottom = KOLYAsion_v2_0.collisions
            Иеремий_collisionX = KOLYAsion_v2_0.collisionX
            if Иеремий_collisionX_left or Иеремий_collisionX_right:
                Jeremiah_X = Jeremiah_oldX 
                c.coords(ZHIRIMI, Jeremiah_X, Jeremiah_Y, Jeremiah_X-15, Jeremiah_Y+30, Jeremiah_X+15, Jeremiah_Y+30)
            if Иеремий_collisionY_top or Иеремий_collisionY_bottom:
                ZHIRIMI.speedY = 0
                Jeremiah_Y = Jeremiah_oldY
                c.coords(ZHIRIMI, Jeremiah_X, Jeremiah_Y, Jeremiah_Y, Jeremiah_X-15,Jeremiah_Y+30, Jeremiah_X+15, Jeremiah_Y+30)
                if Иеремий_collisionY_top:
                    ZHIRIMI.stoIt = platform
            elif not Иеремий_collisionX and ZHIRIMI.stoIt == platform:
                ZHIRIMI.stoIt = False
        if any(conflict_czechk(bob, ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228).collisions):
            root.destroy()
        if c.coords(bob)[2] < c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228)[0]:
            ZHIRIMI.speedX = -75
        if c.coords(bob)[0] > c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228)[2]:
            ZHIRIMI.speedX = 75
        c.coords(ZHIRIMI.treugolnik_telo, Jeremiah_X, Jeremiah_Y, Jeremiah_X-15, Jeremiah_Y+30, Jeremiah_X+15, Jeremiah_Y+30)
        c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, Jeremiah_X-(Jeremiah_X-(Jeremiah_X-15))/2,Jeremiah_Y,Jeremiah_X+((Jeremiah_X+15)-Jeremiah_X)/2,Jeremiah_Y+30)
    FRICKtion(tick_duration)
    c.coords(bob, X, Y, X+30, Y+30)

    if any(any(conflict_czechk(bob, john).collisions) for john in john_list):
        root.destroy()
    if not end_flag and any(conflict_czechk(bob,vspomoGosha).collisions):
        end_flag = True
        c.create_text(200,50,text="Поздравляю, ты дошел до просто стоящей и никак не \nдвигающейся pizzы! Даже собака с моего двора \nэто не смогла сделать!")
        root.after(3500, root.destroy)
    for platform in platform_list:
        KOLYAsion = conflict_czechk(bob,platform)
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
    if any(conflict_czechk(bob, jump).collisions[2] for jump in jump_list):
        speedY = -300
    elif any(conflict_czechk(bob, jump).collisions[0] for jump in jump_list) or any(conflict_czechk(bob, jump).collisions[1] for jump in jump_list):
        speedX = 0
    elif any(conflict_czechk(bob, jump).collisions[3] for jump in jump_list):
        speedY = 0
    if conflict_czechk(bob, vspomoGosha_v2_0).any():
        X -= speedX*tick_duration + 0.0625
        c.move("vse_fignjuliny", -speedX*tick_duration, 0)
    if conflict_czechk(bob, vspomoGosha_v3_0).any():
        X -= speedX*tick_duration - 0.0625
        c.move("vse_fignjuliny", -speedX*tick_duration, 0)
    if speedY < 0:
        if any(conflict_czechk(bob, vspomoGosha_v4_0).collisions):
            Y -= speedY*tick_duration - 0.0625
            c.move("vse_fignjuliny", 0, -speedY*tick_duration)
    if absoluteY < TOZHOS-150:
        if any(conflict_czechk(bob,vspomoGosha_v5_0).collisions):
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
    
def go_czechker():
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

@dataclass
class collision_data:
    collisions: list[bool]
    collisionX: bool

    def any(self):
        return any(self.collisions) or self.collisionX

def conflict_czechk(someone1,someone2):
    pos1 = c.coords(someone1)
    pos2 = c.coords(someone2)
    collisionY = pos1[3] >= pos2[1] and pos1[1] <= pos2[3]
    collisionX = pos1[2] >= pos2[0] and pos1[0] <= pos2[2]
    collisionX_left = collisionY and pos2[2] >= pos1[2] >= pos2[0] 
    collisionX_right = collisionY and pos2[0] <= pos1[0] <= pos2[2]
    collisionY_top = collisionX and pos2[1] <= pos1[3] <= pos2[3]
    collisionY_bottom = collisionX and pos2[3] >= pos1[1] >= pos2[1]
    
    return collision_data(collisions=[collisionX_left, collisionX_right, collisionY_top, collisionY_bottom], collisionX=collisionX)

root.mainloop()