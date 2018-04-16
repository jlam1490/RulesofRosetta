from gamelib import *

game = Game(800, 800, "RoR")
#Player Controls
def controls():
    rightward.moveTo(main.x,main.y)
    rightward.visible = False
    leftward.moveTo(main.x,main.y)
    leftward.visible = False
    backward.moveTo(main.x,main.y)
    backward.visible = False
    foward.moveTo(main.x,main.y)
    foward.visible = False
        
    if keys.Pressed[K_d] and not main.collidedWith(girl):
        walk.play()
        rightward.visible = True
        rightward.draw()
        rightward.x += 4
        main.visible = False
        main.moveTo(rightward.x, rightward.y)
    if keys.Pressed[K_s] and not main.collidedWith(girl):
        walk.play()
        backward.visible = True
        backward.draw()
        backward.y += 4
        main.visible = False
        main.moveTo(backward.x, backward.y)

    if keys.Pressed[K_w] and not main.collidedWith(girl):
        walk.play()
        foward.visible = True
        foward.draw()
        foward.y -= 4
        main.visible = False
        main.moveTo(foward.x, foward.y)
    if keys.Pressed[K_a] and not main.collidedWith(girl):
        walk.play()
        leftward.visible = True
        leftward.draw()
        leftward.x -= 4
        main.visible = False
        main.moveTo(leftward.x, leftward.y)
    

    if not keys.Pressed[K_d] and not keys.Pressed[K_s] and not keys.Pressed[K_w] and not keys.Pressed[K_a]:
        main.visible = True

    
#Backgrounds
bk = Image("room3.jpg",game , False)
bk.resizeTo(game.width, game.height)

bk2 = Image("room2.jpg", game, False)
bk2.resizeTo(game.width, game.height)

bk3 = Image("room1b.png", game)
bk3.resizeTo(game.width, game.height)

bk4 = Image("room.png", game)
bk4.resizeTo(game.width, game.height)

bk5 = Image("start.jpg",game)
bk5.resizeTo(game.width,game.height)

bk6 = Image("wall.jpg",game, False)
bk6.resizeTo(game.width,game.height)

bk7 = Image("outside.jpg", game, False)
bk7.resizeTo(game.width, game.height)

bk8 = Image("woodbk.jpg",game)
bk8.resizeTo(800,800)

bk9= Image("wall2.jpg",game)
bk9.resizeTo(800,800)

#Sounds
door = Sound("door.wav", 1)
walk = Sound("walk.wav", 2)
web = Sound("web.wav", 3)
coins = Sound("coins.wav", 4)

#Fonts
f = Font(white, 14, black , "Comic Sans MS")
f2 = Font(white, 15, black, "Oswald")
f3 = Font(red, 35, black, "chiller")
f4 = Font(red, 20, black, "chiller")
fo = Font(white, 25, black, "Times New Roman")

#Graphics
main = Image("Main.png",game,False)
foward = Animation("Forwarrds.png",4,game, 196/4,60,5,False)
rightward = Animation("Rightwards.png",4, game, 197/4, 68,5,False)
backward = Animation("backwards.png",4, game, 197/4, 62,5,False) 
leftward = Animation("Leftwards.png",4, game, 197/4, 64,5,False)

Ungifted = Image("Ungifted.jpg",game, False)
Ungifted.resizeBy(-90)
Ungifted.moveTo(600,750)

rules = Image("rules.png",game)
rules.y -= 100

start = Image("startup.png",game)
start.y += 100

continu = Image("continue.png",game)
continu.y += 150

gs = Animation("gs.png",40,game,466/10,192/4, 10)

man = Image("man.png", game, False)
man.resizeBy(-80)
man.moveTo(250, 100)

man2 = Image("Man 2.jpg", game, False)
man2.resizeBy(-40)
man2.moveTo(150, 600)

man3 = Image("man 3.png", game ,False)
man3.resizeBy(-75)
man3.moveTo(680, 630)

ghost = Image("Ghost.png", game, False)
ghost.resizeBy(-85)
ghost.setSpeed(25, 0)

jumpscare1 = Image("jumpscare1.png", game)

girl = Image("finished-girl-pixilart.png", game)
girl.resizeBy(70)
girl.visible = False

tbox = Image("pixil-frame-1.png",game)
tbox.resizeTo(game.width, 200)
tbox.moveTo( 400, 700)

gameover = Image("Gameover1.png",game)

skull = Image("New Piskel.gif",game)
skull.resizeBy(500)
skull.moveTo(400,250)

#List
rings = []

for times in range(50):
    rings.append( Animation("coin.png", 21, game, 2048/16  , 256/2))

for times in range(50):
    rings[times].moveTo(randint(1,800), randint(1,800))
    s = randint(5, 10)
    a = randint(0,360)
    rings[times].setSpeed(s, a)

#Coin setup
coin = []
for index in range(50):
    coin.append(Animation("coin.png",21,game, 2048/16, 256/2,2))
    coin[index].resizeBy(-75)
for index in range(50):
    coin[index].moveTo(randint(1,800), randint(1,800))
    s = randint(5,10)

    a = randint(0,360)
    coin[index].setSpeed(s,a)
    
#Roses setup
roses = []
for index in range(5):
    roses.append(Image("pixelroses.jpg",game,False))
    roses[index].resizeBy(-90)
for index in range(5):
    roses[index].moveTo(randint(1,800), randint(1,800))
    s = randint(5,10)
    a = randint(0,360)
    roses[index].setSpeed(s,a)
    roses[index].moveTo(200,200)

#Start Screen
while not game.over:
    game.processInput()
    bk5.draw()
    rules.draw()
    start.draw()
    Ungifted.draw()
    gs.draw()
    game.drawText("Co. Ungifted",Ungifted.x+ 40, Ungifted.y - 20 ,f2)
    game.drawText("Sebastian Aguilar",Ungifted.x+ 40, Ungifted.y - 10 ,f2)
    game.drawText("Adolfo Juarez",Ungifted.x+ 40, Ungifted.y,f2)
    game.drawText("John Lam",Ungifted.x+ 40, Ungifted.y+10,f2)
    if start.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
    
#Intro
game.over = False
game.clearBackground()
while not game.over:
    game.processInput()
    game.setBackground(bk6)
    game.drawBackground()
    continu.draw()
    game.drawText("You are a lost spirit with no knowledge of your past", 150, 200,fo)
    game.drawText("You wake up what seems to be a manshion",150,225,fo)
    game.drawText("You're able to move using the WASD keys",150,250,fo)
    game.drawText("Entering corriders you wander this mysterious place", 150, 275,fo)
    game.drawText("By solving puzzles you get closer knowing the reason",150,300,fo)
    game.drawText("of this place", 150, 325, fo)
    if continu.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)

#Start Room
game.over = False
time = 120
while not game.over:
    game.processInput()
    game.setBackground(bk4)
    game.drawBackground()
    man.draw()
    main.draw()
    if time > 1:
        tbox.draw()
        game.drawText("Me: Ugh, my head! Where am I?? Wait...Who am I? Why can't I remember",tbox.x - 250, tbox.y, f)
        game.drawText("Why can't I remember!! Maybe that man over there can help me. ", tbox.x- 250, tbox.y+25, f)
        game.drawText("I should go talk to him", tbox.x-250, tbox.y+50, f)
        game.update(30)
        time -= 1
        continue
    
    controls()
    
    if main.collidedWith(man, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man: Hey!PSTT!! Come this way, it'll help you find your way.",tbox.x - 250, tbox.y, f)
        game.drawText("I promise, it will take you somewhere magical...HeeHee. Remember, you ", tbox.x - 250, tbox.y+25, f)
        game.drawText("only have one shot at this!!", tbox.x - 250, tbox.y+ 50, f)

    if main.y < 100 and main.x > 200 and main.x < 400:
        web.play()
        game.over = True
        
    game.update(30)

#Room 1 / Puzzle 1
game.over = False
time = 90
main.moveTo(610, 600)
while not game.over:
    game.processInput()
    game.setBackground(bk2)
    game.drawBackground()

    if time > 1:
        main.visible = True
        main.draw()
        game.drawText("*rattle* *rattle*", 200, 200, f)
        game.drawText("*click*", 530, 650, f)
        game.drawText("NoNoNo The door locked on me!!", main.x - 250, main.y, f)
        game.update(30)
        time -= 1
        continue
    main.draw()
    controls()
    
    if main.y > 530:
        game.drawText("It's useless it won't budge.", main.x, main.y, f)
        
    if main.y < 210 and main.x < 250:
        while not game.over:
            game.processInput()

            game.clearBackground()
    
            for times in range(50):
                rings[times].move(True)
                if rings[times].collidedWith(mouse) and mouse.LeftClick:
                    coin.play()
                    rings[times].visible= False
                    game.score += 1

            if game.score == 1:
                game.over = True
            
            game.displayScore()
    
            game.update(60)
        
    game.update(30)

#Room 1(2) 
game.over = False
time = 60
time2 = 60
while not game.over:
    game.processInput()
    game.setBackground(bk2)
    game.drawBackground()
    main.draw()
    if time > 1:
        main.visible = True
        main.draw()
        game.drawText("HAHAAH!! Sometimes its better to save yourself",200 ,400 , f3)
        game.drawText("than others. You can't always play hero...",200 ,425 , f3)
        game.update(30)
        time -= 1
        continue
    
    
    if time2 > 1:
        main.visible = True
        main.draw()
        tbox.draw()
        game.drawText("Me: Who was that? What does it mean?",tbox.x - 250, tbox.y , f)
        game.drawText("*click*", 530, 650, f)
        game.update(30)
        time2 -= 1
        continue
    
    main.draw()
    controls()
    
    if main.y > 620:
        web.play()
        game.over = True
        
    game.update(30)

#Start Room(2)
game.over= False
main.moveTo(400, 100)
while not game.over:
    game.processInput()
    game.setBackground(bk4)
    game.drawBackground()
    main.draw()
    man.draw()
    man2.draw()
    man3.draw()
    if main.collidedWith(man, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man: I saw that you passed the puzzle room, I will tell you something",tbox.x - 250, tbox.y, f)
        game.drawText("Your name is Rose and we are not real. Now go to the man in the Green Shirt,", tbox.x - 250, tbox.y+ 25, f)
        game.drawText(" he has a task for you",tbox.x - 250, tbox.y+50, f)

    if main.collidedWith(man2, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man 2: Hello, Rose there will be another puzzle room behind me. Good luck",tbox.x - 250, tbox.y, f)
        game.drawText("Now, on a serious note go through this way it will actually...Help you", tbox.x - 250, tbox.y+ 25, f)
        game.drawText("Remember, once you go in you cannot go in again",tbox.x - 250, tbox.y+50, f)

    if main.collidedWith(man3, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man 3: I have nothing to do with you",tbox.x - 250, tbox.y, f)
        game.drawText("",tbox.x - 250, tbox.y+ 25)
        game.drawText("",tbox.x - 250, tbox.y+50)

    if main.x < 100:
        web.play()
        game.over = True
        
    controls()
        
    game.update(30)

#Room 2 / Puzzle 2
game.over = False
main.moveTo(700, 420)
time = 60
coinscore = 0
while not game.over:
    game.processInput()
    game.setBackground(bk)
    game.drawBackground()
    main.draw()

    game.drawText("*Ding* *Ding*", 150, 400, f)


    if main.x == 200:
        main.moveTo(600,600)
        game.setBackground(bk8)
        while not game.over:
            game.processInput()
            game.drawBackground()
            main.draw()
            controls()
            
            for index in range(1):
                coin[index].move(True)
                if coin[index].collidedWith(main):
                    coin.play()
                    coin[index].visible = False
                    coinscore += 1
                if coin[index].collidedWith(rightward):
                    coin.play()
                    coin[index].visible = False
                    coinscore += 1
                if coin[index].collidedWith(leftward):
                    coin.play()
                    coin[index].visible = False
                    coinscore += 1
                if coin[index].collidedWith(foward):
                    coin.play()
                    coin[index].visible = False
                    coinscore += 1
                if coin[index].collidedWith(backward):
                    coin.play()
                    coin[index].visible = False
                    coinscore += 1

            if coinscore == 1:
                game.over = True
            
            for index in range(5):
                roses[index].move(True)
                if main.collidedWith(roses[index], "circle") or foward.collidedWith(roses[index], "circle") or rightward.collidedWith(roses[index], "circle") or leftward.collidedWith(roses[index], "circle") or backward.collidedWith(roses[index], "circle"):
                    while not game.over:
                        game.processInput()
                        game.clearBackground()
                        bk9.draw()
                        gameover.draw()
                        skull.draw()
                        game.update(30)    
                    game.quit()
            game.update(30)
        
    controls()
    
    game.update(30)
#Room 2(2)
game.over = False
main.moveTo(200, 400)
while not game.over:
    game.processInput()
    game.setBackground(bk)
    game.drawBackground()
    main.draw()
    controls()

    if main.x > 700:
        web.play()
        game.over = True

    game.update(30)
    

#Start Room(3)
game.over= False
main.moveTo(100, 400)
while not game.over:
    game.processInput()
    game.setBackground(bk4)
    game.drawBackground()
    main.draw()
    man.draw()
    man2.draw()
    man3.draw()
    if main.collidedWith(man, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man: Dont listen to the Green Man!! You have to trust me",tbox.x - 250, tbox.y, f)
        game.drawText("I know the man in the green shirt said not to, but please", tbox.x - 250, tbox.y+ 25, f)
        game.drawText("listen to me this once don't trust the Green Man",tbox.x - 250, tbox.y+50, f)

    if main.collidedWith(man2, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man 2: Good Job Rose!! You have completed the second puzzle room. I shall reward",tbox.x - 250, tbox.y, f)
        game.drawText("you with some information now. We are only in your head, but there ", tbox.x - 250, tbox.y + 25, f)
        game.drawText("is a great evil in this place. Beware!! Go to the Green Man",tbox.x - 250, tbox.y+50, f)

    if main.collidedWith(man3, "circle"):
        tbox.draw()
        game.drawText("Mysterious Man 3: Let us go this way... It is your LAST room Rose. ",tbox.x - 250, tbox.y, f)
        game.drawText("Remeber once you go in you cannot come out", tbox.x - 250, tbox.y + 25, f)
        game.drawText("HeHe Good Luck I'll see you in the long run.",tbox.x - 250, tbox.y+50, f)

    if main.x > 700:
        web.play()
        game.over = True
        
    controls()
        
    game.update(30)

#End Room
game.over = False
ghost.moveTo(400, 100)
main.moveTo(50, 400)
time = 60
ghostTime = 30
while not game.over:
    game.processInput()
    game.setBackground(bk3)
    game.drawBackground()
    main.draw()
    girl.moveTo(500, 650)
    girl.visible = True
    girl.draw()
    
    if time > 1:
        main.visible = True
        main.draw()
        game.drawText("AHH HELP ME PLEASE!! ITS COMING PLEASE HELP ME",girl.x - 100 ,girl.y , f4)
        game.update(30)
        time -= 1
        continue
    
    if main.collidedWith(girl):
        game.drawText("Ha...HAAHAAA, I told you...there is no such thing as a hero", girl.x-125, girl.y, f4)
        if ghostTime > 1:
            game.update(10)
            ghostTime -= 1
            continue 
        ghost.move(True)
        a = ghost.angleTo(main)
        ghost.rotateTo(a)
        
        if ghost.collidedWith(main):
            jumpscare1.draw()
    
    if main.y < 350 and main.x > 700:
        web.play()
        game.over = True
        
    controls()

    game.update(30)

    
#Outside
game.over = False
backward.moveTo(400, 500)
backward.resizeBy(-50)
backward.setSpeed(5, 0)
time = 50
big = 40
while not game.over:
    game.processInput()
    game.setBackground(bk7)
    game.drawBackground()
    backward.draw()
    backward.y += 2
        
    if big > 1:
        backward.resizeBy(5)
        backward.y += 2
        
    if time > 1:
        print(time, big)
        time -= 1
        big -= 1
        game.update(15)
        continue
    
    game.update(30)
    
    if backward.isOffScreen("bottom"):
        game.over = True
    
#End Game
game.over = False
while not game.over:
    game.processInput()
    bk5.draw()
    rules.draw()
    Ungifted.draw()
    game.drawText("Co. Ungifted",Ungifted.x+ 40, Ungifted.y - 20 ,f2)
    game.drawText("Sebastian Aguilar",Ungifted.x+ 40, Ungifted.y - 10 ,f2)
    game.drawText("Adolfo Juarez",Ungifted.x+ 40, Ungifted.y,f2)
    game.drawText("John Lam",Ungifted.x+ 40, Ungifted.y+10,f2)
    game.update(30)
game.quit()

    
    
    
