from gamelib import *

game = Game(800,600,"Rules of Rosetta",60)

bk = Image("start.jpg",game)
bk.resizeTo(game.width,game.height)


bk2 = Image("wall.jpg",game)
bk2.resizeTo(game.width,game.height)

Ungifted = Image("Ungifted.jpg",game, False)
Ungifted.resizeBy(-90)
Ungifted.moveTo(450,550)

rules = Image("rules.png",game)
rules.y -= 100

f = Font(white, 15, black, "Oswald")
fo = Font(white, 25, black, "Times New Roman")

start = Image("startup.png",game)
start.y += 100

continu = Image("continue.png",game)
continu.y += 150

gs = Animation("gs.png",40,game,466/10,192/4, 10)


while not game.over:
    game.processInput()
    bk.draw()
    rules.draw()
    start.draw()
    Ungifted.draw()
    gs.draw()
    game.drawText("Co. Ungifted    Sebastian Aguilar, Adolfo Juarez, John Lam",500, 550,f)
    if start.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
    
    
game.over = False
game.clearBackground()
while not game.over:
    game.processInput()
    bk2.draw()
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
game.over = False
game.update(30)
game.quit()
