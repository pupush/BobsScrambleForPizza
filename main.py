from tkinter import *
import random
import json
import os
from dataclasses import dataclass
from conflict_CZECH_REPUBLIC import *
import time

root = Tk()

@dataclass
class Jeremih:
    treugolnik_telo: int
    speedX: int
    speedY: int
    vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228 : int
    stoIt: bool

def levelы(uroven_nazvanie):
    global c, absolut_vodka, pizza_png, boboprobivaemiy, list_fotochkov, pizza, bob, vspomoGosha, vspomoGosha_v2_0, vspomoGosha_v3_0, vspomoGosha_v4_0, vspomoGosha_v5_0, pressed_a, pressed_d, pressed_s, end_flag, speedX, speedY, tick_duration, stoIt, Jeremiah_stoIt, gravity, FRICKtion_FUCKtor, X, Y, john_list, TOZHOS, platform_list, jeremiah_list, jump_list, invis_list, key_list
    f = open(os.path.join("levelы", uroven_nazvanie))
    coord_dacha = json.load(f)
    f.close()
    john_data = coord_dacha["john_list"]
    platform_data = coord_dacha.get("platform_list", [])
    jump_data = coord_dacha.get("jumpy_list", [])
    jeremiah_data = coord_dacha.get("jeremiah_list", [])
    invis_data = coord_dacha.get("invis_list", [])
    key_data = coord_dacha.get("key_list", [])
    end_data = coord_dacha["end"]

    c = Canvas(root, width=400, height=400)
    c.pack()

    absolut_vodka = c.create_rectangle(0,0,1,1, outline="", tags="vse_fignjuliny")

    klyuchi = []
    for klucz in os.listdir(path="klyuchi"):
        klyuchi.append(klucz)
    
    NUZHNIE_klyuchi = random.sample(klyuchi, k=len(key_data))
    #NUZHNIE_klyuchi = [PhotoImage(file = f"klyuchi\\{f}") for f in NUZHNIE_klyuchi]

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
    key_list = []
    list_fotochkov = []

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
    zagolovchik.destroy()
    for knopochk in list_knopochek:
        knopochk.destroy()
    nenuzhniy_dibil.destroy()

def parkurchek():
    import sozdatel_jsonov
    global c, absolut_vodka, pizza_png, boboprobivaemiy, list_fotochkov, pizza, bob, vspomoGosha, vspomoGosha_v2_0, vspomoGosha_v3_0, vspomoGosha_v4_0, vspomoGosha_v5_0, pressed_a, pressed_d, pressed_s, end_flag, speedX, speedY, tick_duration, stoIt, Jeremiah_stoIt, gravity, FRICKtion_FUCKtor, X, Y, john_list, TOZHOS, platform_list, jeremiah_list, jump_list, invis_list, key_list
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
    TOZHOS = [] #Tebe Ostalos' ZHyt' Odnu Sekundu
    platform_list = []
    jump_list = []
    jeremiah_list = []
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
    zagolovchik.destroy()
    parkOURCZECH.destroy()
    play.destroy()

zagolovchik = Label(root, text="BOB'S SCRAMBLE \nFOR PIZZA", anchor="nw", font="Open_Sans 20")
zagolovchik.pack()

def vыbiratelь(): 
    global list_knopochek, nenuzhniy_dibil
    vse_uROVni = os.listdir(path="levelы")
    list_knopochek = []
    list_levelov = []
    nenuzhniy_dibil = Frame(root)
    nenuzhniy_dibil.pack()

    for i, lvl in enumerate(vse_uROVni):
        def ya_zadobalsya_pridumyvat_nazvaniya(lvl):
            return lambda : levelы(lvl)
        
        if i%4 == 0:
            novaya_rota = Frame(nenuzhniy_dibil)
            novaya_rota.pack(fill="x")
        
        knopocheka = Button(novaya_rota, text=f"{i+1}", padx=10, pady=10, command=ya_zadobalsya_pridumyvat_nazvaniya(lvl))
        knopocheka.pack(side="left", padx=(21.5,0), pady=15)
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
            KOLYAsion_v2_0 = collision_czech(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, platform)
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
        
        if any(collision_czech(bob, ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228).collisions):
            root.destroy()
        
        if c.coords(bob)[2] < c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228)[0]:
            ZHIRIMI.speedX = -75
        
        if c.coords(bob)[0] > c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228)[2]:
            ZHIRIMI.speedX = 75
        
        c.coords(ZHIRIMI.treugolnik_telo, Jeremiah_X, Jeremiah_Y, Jeremiah_X-15, Jeremiah_Y+30, Jeremiah_X+15, Jeremiah_Y+30)
        c.coords(ZHIRIMI.vspomogatelniy_obrazovanniy_vichyslitelniy_apparat_nomer_228, Jeremiah_X-(Jeremiah_X-(Jeremiah_X-15))/2,Jeremiah_Y,Jeremiah_X+((Jeremiah_X+15)-Jeremiah_X)/2,Jeremiah_Y+30)
    
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

def collision_czech(someone1, someone2):
    pos1 = c.coords(someone1)
    pos2 = c.coords(someone2)
    return conflict_czechk(pos1, pos2)

root.mainloop()

# ꙮ