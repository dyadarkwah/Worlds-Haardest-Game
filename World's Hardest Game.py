import graphics
##def is_point_in_rectangle(point_x, point_y, rectangle_center_x, rectangle_center_y, rectangle_width, rectangle_height):
##    x = point_x
##    y = point_y
##    width = rectangle_width / 2
##    height = rectangle_height / 2
##    left_x = rectangle_center_x - width
##    right_x = x <= rectangle_center_x + width
##    bottom_y = y <= rectangle_center_y + height
##    top_y = y >= rectangle_center_y - height
##    return x >= left_x and right_x and bottom_y and top_y


def rectangle_overlaps(x1, y1, width1, height1, x2, y2, width2, height2):
    if ((x1 - width1 / 2) > (x2 + width2 / 2)) or ((x1 + width1 / 2) < (x2 - width2 / 2)):
        return False

    else:
        if ((y1 - height1 / 2) > (y2 + height2 / 2)) or ((y1 + height1 / 2) < (y2 - height2 / 2)):
            return False
        else:
            return True




graphics.window_size(1320,840)
graphics.window_title('Project')
graphics.window_background_color(color='lavender')


player_x = 1100
player_y = 300


enemy1and3_x = 390
enemy2and4_x = 930

enemy1_y = 330
enemy2_y = 390
enemy3_y = 450
enemy4_y = 510

e1and3speed = 10
e2and4speed = 10

list1 = [enemy1_y, enemy2_y, enemy3_y, enemy4_y]

safe0 = 0
deaths1 = 0


while graphics.window_open() and safe0 == 0:
    graphics.clear()

    if player_x < 280:
        safe0 = 1

    graphics.draw_line(120, 240, 300, 240, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(360, 300, 900, 300, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(900, 240, 1200, 240, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(960, 300, 1020, 300, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(300, 537, 360, 537, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(420, 540, 960, 540, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(120, 600, 420, 600, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(1020, 600, 1200, 600, fill='black', thickness = 5)
    ##graphics.wait(0.5)


    graphics.draw_line(120, 240, 120, 600, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(300, 240, 300, 539, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(360, 300, 360, 539, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(420, 540, 420, 600, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(900, 240, 900, 300, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(960, 300, 960, 540, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(1020, 300, 1020, 600, fill='black', thickness = 5)
    ##graphics.wait(0.5)
    graphics.draw_line(1200, 240, 1200, 600, fill='black', thickness = 5)
    ##graphics.wait(0.5)


    #Safe Zones
    graphics.draw_rectangle(210, 420, 175, 353.5, fill="#99ff99", thickness=0)
    graphics.draw_rectangle(1110, 420, 175, 353.5, fill="#99ff99", thickness=0)

    #Main arena
    graphics.draw_image('rfinal2.gif', 660, 420)
    graphics.draw_rectangle(660, 30, 1320, 60, fill="Black", thickness = 0)
    graphics.draw_rectangle(660, 810, 1320, 60, fill="Black", thickness = 0)
    graphics.draw_text("Level 1", 100, 30, color="White", size=44)
    graphics.draw_text("Deaths: " + str(deaths1), 1150, 30, color="White", size=44)


    #Drawing of enemies
    enemy1 = graphics.draw_oval(enemy1and3_x, enemy1_y, 24, 24, outline='black', fill='Blue', thickness=7)
    enemy2 = graphics.draw_oval(enemy2and4_x, enemy2_y, 24, 24, outline='black', fill='Blue', thickness=7)
    enemy3 = graphics.draw_oval(enemy1and3_x, enemy3_y, 24, 24, outline='black', fill='Blue', thickness=7)
    enemy4 = graphics.draw_oval(enemy2and4_x, enemy4_y, 24, 24, outline='black', fill='Blue', thickness=7)

    #Animation of enemies
    enemy1and3_x = enemy1and3_x + e1and3speed
    enemy2and4_x = enemy2and4_x - e2and4speed

        #Ball 1 and 3
    if enemy1and3_x > 942:
        e1and3speed = e1and3speed * -1
    if enemy1and3_x < 390:
        e1and3speed = e1and3speed * -1

        #Ball 2 and 4
    if enemy2and4_x < 390:
        e2and4speed = e2and4speed * -1
    if enemy2and4_x > 942:
        e2and4speed = e2and4speed * -1


    # Death by touch

    for i in range(len(list1)):
        if i % 2 == 1:
            if rectangle_overlaps(enemy2and4_x, list1[i], 24, 24, player_x, player_y, 40, 40):
                player_x = 1100
                player_y = 300
                deaths1 += 1
                print('even')
            
        else:
            if rectangle_overlaps(enemy1and3_x, list1[i], 24, 24, player_x, player_y, 40, 40):
                player_x = 1100
                player_y = 300
                deaths1 += 1
                print('odd')

                


    

    
    #Change the location of the player based on what key the user is pressing
    if graphics.key_down('Right'):
        if player_x + 20 < 1200:
            if player_y - 20 < 539 and player_x + 20 < 300:
                player_x += 5
            if player_y - 20 > 539 and player_x + 20 < 420:
                player_x += 5
            if (player_y + 20 < 545 and player_y + 20 > 239) and (player_x - 20 > 350 and player_x + 20 < 960):
                player_x += 5
            if player_y + 20 < 302  and player_x + 20 > 900:
                player_x += 5
            if player_y + 20 > 302 and player_x > 1020:
                player_x += 5
            if player_y - 20 < 540 and player_x + 20 < 419 and player_x - 20 > 300:
                player_x += 5
    
            
    if graphics.key_down('Left'):
        if player_x - 20 > 125:
            if player_x - 20 > 1020:
                player_x -= 5
            if player_y + 20 < 305 and player_x - 20 > 900:
                player_x -= 5
            if player_x + 20 < 1020 and player_x - 20 > 900:
                player_x -= 5
            if player_y - 20 > 299 and player_x + 20 < 1000 and player_x - 20 > 360:
                player_x -=5
            if player_y - 20 > 539 and player_x - 20 < 420:
                player_x -= 5
            if player_y - 20 < 539 and player_x < 350:
                player_x -= 5

        
    if graphics.key_down('Down'):
        if player_y + 20 < 600:
            if player_x + 20 < 425 or player_x - 20 > 1020:
                player_y += 5
            elif player_x + 20 > 420 and player_x + 20 < 965 and player_y + 20 < 540:
                player_y += 5
            elif player_x + 20 > 960 and player_y + 20 < 300:
                player_y += 5

        
    if graphics.key_down('Up'):
        if player_y - 20 > 245:
            if (player_x - 20 > 359 and player_y - 20 > 302) or (player_x - 20 > 900) or (player_x + 20 < 305):
                player_y -= 5
            elif player_x + 20 > 300 and player_y - 20 > 541:
                player_y -=5


    
    # Draw the player, and at the new location
    player = graphics.draw_rectangle(player_x, player_y, 40, 40, fill="red", outline = "black", thickness=4)


    graphics.wait(0.03333333)
##################################################################################################################################


graphics.window_size(1188, 840)
graphics.window_background_color('lavender')


player_x = 150
player_y = 420

eodd_y = 570
eeven_y = 270

enemy1_x = 231
enemy2_x = 297
enemy3_x = 363
enemy4_x = 429
enemy5_x = 495
enemy6_x = 561
enemy7_x = 627
enemy8_x = 696
enemy9_x = 762
enemy10_x = 828
enemy11_x = 894
enemy12_x = 960

eodd_speed = 1
eeven_speed = 1

deaths = 0
eaten = 0

liste = [enemy1_x, enemy2_x, enemy3_x, enemy4_x, enemy5_x, enemy6_x, enemy7_x, enemy8_x, enemy9_x, enemy10_x, enemy11_x, enemy12_x]
oddliste = [enemy1_x, enemy3_x, enemy5_x, enemy7_x, enemy9_x, enemy11_x]
evenliste = [enemy2_x, enemy4_x, enemy6_x, enemy8_x, enemy10_x, enemy12_x]

safe = False

while graphics.window_open() and safe == False:
    if player_x - 30 > 990 and (player_y  - 20 >= 360 and player_y + 20 <= 480) and eaten == 1:
        safe = True

    graphics.clear()

    graphics.draw_line(198, 240, 990, 240, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(66, 360, 198, 360, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(990, 360, 1122, 360, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(66, 480, 198, 480, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(990, 480, 1122, 480, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(198, 600, 990, 600, fill="black", thickness = 5)
    ##graphics.wait(1)

    graphics.draw_line(198, 240, 198, 360, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(990, 240, 990, 360, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(66, 360, 66, 480, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(1122, 360, 1122, 480, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(198, 480, 198, 600, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_line(990, 480, 990, 600, fill="black", thickness = 5)
    ##graphics.wait(1)
    graphics.draw_rectangle(134, 420, 132, 118, fill="pale green", thickness = 0)
    ##graphics.wait(1)
    graphics.draw_rectangle(1054, 420, 132, 118, fill="pale green", thickness = 0)


    #Main game area
    graphics.draw_image('/Users/davidadarkwah/Desktop/Worlds Hardest Game/Project Pics/main2.gif', 594, 420)
    graphics.draw_rectangle(594, 30, 1188, 60, fill="Black", thickness = 0)
    graphics.draw_rectangle(594, 810, 1188, 60, fill="Black", thickness = 0)
    graphics.draw_text("Level 2", 100, 30, color="White", size=44)
    graphics.draw_text("Deaths: " + str(deaths), 1000, 30, color="White", size=44)




    #Yellow circle
    if eaten == 0:
        food = graphics.draw_oval(594, 420, 24, 24, outline='black', fill='Yellow', thickness=7)


    for i in range(len(evenliste)):
        enemies = graphics.draw_oval(evenliste[i], eeven_y, 24, 24, outline="Black", fill="Blue", thickness=7)
        enemies = graphics.draw_oval(oddliste[i], eodd_y, 24, 24, outline="Black", fill="Blue", thickness=7)


    #Animation of enemies
    eodd_y = eodd_y - eodd_speed
    eeven_y = eeven_y + eeven_speed

        #Odd Balls
    if eodd_y < 255:
        eodd_speed = eodd_speed * -1
    if eodd_y > 585:
        eodd_speed = eodd_speed * -1

        #Even Balls
    if eeven_y > 585:
        eeven_speed = eeven_speed * -1
    if eeven_y < 255:
        eeven_speed = eeven_speed * -1

    
    #deaths by touch
    for i in range(len(liste) - 1):
        if i % 2 == 1:
            if rectangle_overlaps(liste[i], eeven_y, 24, 24, player_x, player_y, 40, 40):
                player_x = 132
                player_y = 410
                eaten = 0
                deaths += 1
                print('even')
        else:
            if rectangle_overlaps(liste[i], eodd_y, 24, 24, player_x, player_y, 40, 40):
                player_x = 132
                player_y = 410
                eaten = 0
                deaths += 1
                print('odd')
                



    #Change the location of the player based on what key the user is pressing
    if graphics.key_down('Right'):
        if player_x + 20 < 1120:
            if player_x + 20 < 990:
                player_x +=10
            elif player_y + 20 < 480 and player_y - 20 > 359:
                player_x += 10
                
    if graphics.key_down('Left'):
        if player_x - 20 > 70:
            if player_x - 20 > 200:
                player_x -=10
            elif player_y + 20 < 481 and player_y - 20 > 359:
                player_x -= 10
            
    if graphics.key_down('Down'):
        if player_x - 20 > 198 and player_x + 20 < 991:
            if player_y + 20 != 600:
                player_y += 10
                
        elif player_y + 20 != 480:
            player_y += 10
        
    if graphics.key_down('Up'):
        if player_x -20 > 198 and player_x + 20 < 991:
            if player_y - 20 != 240:
                player_y -= 10
                
        elif player_y - 20 != 360:
            player_y -= 10


    # Draw the player, and at the new location
    player = graphics.draw_rectangle(player_x, player_y, 40, 40, fill="red", outline = "black", thickness=4)
    if (player_x > 550 and player_x < 638) and (player_y  > 376 and player_y < 464):
        eaten = 1

    graphics.wait(0.000000165)




##########################################################################################################################

graphics.mainloop()


