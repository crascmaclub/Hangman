# Import lib
import pygame
from time import sleep as sl
import random

# Setup pygame 
pygame.init()
width, height = 1380, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
cras_logo = pygame.image.load("graphics/logo.jpg")
icon = pygame.display.set_icon(cras_logo)
caption = pygame.display.set_caption("Hangman")
game_active = True

#Font
font = pygame.font.SysFont("comicsans", 80)
font_start = pygame.font.SysFont("comicsans", 55)
font_small = pygame.font.SysFont("comicsans", 42)


#Letters
rad = 30
gap = 10
letters = []
startx = round((950 - (rad * 2 + gap) * 13) / 2 )
starty = 540
A = 65
for i in range(26):
    x = startx + gap * 2 + (rad * 2 + gap) * (i % 13)
    y = starty + ((i // 13) * (gap + rad * 2))
    letters.append([x, y, chr(A + i), True])

# Variables
def var():
    global guess
    global choosed
    global count
    global limit
    global topic
    global topic_choosed
    global already_guessed
    global word_tp1
    global word_tp2
    global word_tp3
    global lost
    global won
    guess = ""
    choosed = False
    count = 0
    limit = 4
    topic = ["Technology", "Sports", "Foods"]
    topic_choosed = ""
    already_guessed = []
    word_tp1 = [ "programmer", "developer", "wire", "automatic", "machine", "circuit", "router", "cpu", "terminal", "microprocessor", "processor"]
    word_tp2 = [ "skiing", "sportmanship", "hockey", "rugby", "handball", "offside", "racket", "archery", "wrestling", "hurdling", "polo", "regatta", "dodgeball"]
    word_tp3 = [ "lolipop", "pudding", "macaroons", "pasta", "olive", "raspberry", "baguette", "salami", "smoothies", "ham", "oysters", "croissants"]
    lost = False
    won = False

# Starting
var()
clicked = -1
draw = True
while True:
    pos = pygame.mouse.get_pos() # Mouse pos
    # Turn off
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
            
        #Replay
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == False:
                var()
                for i in range(26):
                    x = startx + gap * 2 + (rad * 2 + gap) * (i % 13)
                    y = starty + ((i // 13) * (gap + rad * 2))
                    letters.append([x, y, chr(A + i), True])
                draw = True
                game_active = True

        # Click on letters
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible and draw == True:
                    dis = ((x - m_x)**2 + (y - m_y)**2) ** 0.5
                    if dis < rad:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
                        letter[3] = False
                        already_guessed.append(ltr)
                        if ltr.lower() not in word:
                            count += 1  
            


    # Bg color
    screen.fill("white")

    # Hints/ logo
    img = pygame.transform.scale(cras_logo, (70, 70))
    hint_box = screen.blit(img, (10, 11))

    text = font_small.render("1K/ SLOT", True, "BLACK")
    screen.blit(text, (100, 11))

    # Pressed
    if hint_box.collidepoint(pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[1] == True:
                clicked += 1
                print("Hints")
                if clicked == 0:
                    for letter in word: 
                        letter = letter.upper()
                        if letter not in already_guessed:
                            already_guessed.append(letter)
                            break
        
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = -1

                    
    if game_active:
        # Pick topic
        if topic_choosed == "" :

            text = font_start.render("Which topic do you want to choose ?", True, "BLACK")
            screen.blit(text, (230, 100))

            tp1 = font_start.render(topic[0], True, "WHITE")
            tp2 = font_start.render(topic[1], True, "WHITE")
            tp3 = font_start.render(topic[2], True, "WHITE")

            # Topic 1 
            tp1_rect = pygame.Rect(190, 250, 10, 82)
            screen.blit(tp1, (tp1_rect.x + 10, tp1_rect.y))
            tp1_rect.w = max(100, tp1.get_width() + 20)
            pygame.draw.rect(screen, "#475F77", tp1_rect, 0, border_radius= 10)
            screen.blit(tp1, (tp1_rect.x + 10, tp1_rect.y))

            if tp1_rect.collidepoint(pos): 
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)         
                if event.type == pygame.MOUSEBUTTONDOWN :   
                    screen.blit(tp1, (tp1_rect.x + 10, tp1_rect.y))
                    tp1_rect.w = max(100, tp1.get_width() + 20)
                    pygame.draw.rect(screen, "#222D37", tp1_rect, 0, border_radius= 10)
                    screen.blit(tp1, (tp1_rect.x + 10, tp1_rect.y))
                    tp2_rect = pygame.Rect(630, 250, 10, 82)
                    screen.blit(tp2, (tp2_rect.x + 10, tp2_rect.y))
                    tp2_rect.w = max(100, tp2.get_width() + 20)
                    pygame.draw.rect(screen, "#475F77", tp2_rect, 0, border_radius= 10)
                    screen.blit(tp2, (tp2_rect.x + 10, tp2_rect.y))
                    tp3_rect = pygame.Rect(970, 250, 10, 82)
                    screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
                    tp3_rect.w = max(100, tp3.get_width() + 20)
                    pygame.draw.rect(screen, "#475F77", tp3_rect, 0, border_radius= 10)
                    screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pygame.display.flip()
                    sl(0.15)
                    topic_choosed = topic[0]

            
                

            # Topic 2    
            tp2_rect = pygame.Rect(630, 250, 10, 82)
            screen.blit(tp2, (tp2_rect.x + 10, tp2_rect.y))
            tp2_rect.w = max(100, tp2.get_width() + 20)
            pygame.draw.rect(screen, "#475F77", tp2_rect, 0, border_radius= 10)
            screen.blit(tp2, (tp2_rect.x + 10, tp2_rect.y))
            
            if tp2_rect.collidepoint(pos):  
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if event.type == pygame.MOUSEBUTTONDOWN :   
                    screen.blit(tp2, (tp2_rect.x + 10, tp2_rect.y))
                    tp2_rect.w = max(100, tp2.get_width() + 20)
                    pygame.draw.rect(screen, "#222D37", tp2_rect, 0, border_radius= 10)
                    screen.blit(tp2, (tp2_rect.x + 10, tp2_rect.y))
                    tp3_rect = pygame.Rect(970, 250, 10, 82)
                    screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
                    tp3_rect.w = max(100, tp3.get_width() + 20)
                    pygame.draw.rect(screen, "#475F77", tp3_rect, 0, border_radius= 10)
                    screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pygame.display.flip()
                    sl(0.15)
                    topic_choosed = topic[1]



            # Topic 3
            tp3_rect = pygame.Rect(970, 250, 10, 82)
            screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
            tp3_rect.w = max(100, tp3.get_width() + 20)
            pygame.draw.rect(screen, "#475F77", tp3_rect, 0, border_radius= 10)
            screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))

            if tp3_rect.collidepoint(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
                if event.type == pygame.MOUSEBUTTONDOWN :
                    screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
                    tp3_rect.w = max(100, tp3.get_width() + 20)
                    pygame.draw.rect(screen, "#222D37", tp3_rect, 0, border_radius= 10)
                    screen.blit(tp3, (tp3_rect.x + 10, tp3_rect.y))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    pygame.display.flip()
                    sl(0.15)
                    topic_choosed = topic[2]
            
            if tp1_rect.collidepoint(pos) == False and tp2_rect.collidepoint(pos) == False and tp3_rect.collidepoint(pos) == False:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                


        # Start
        else: 
            if choosed == False:
                # Random words based on topic
                if topic_choosed == topic[0]: 
                    word = random.choice(word_tp1)
                
                elif topic_choosed == topic[1]:
                    word = random.choice(word_tp2)

                elif topic_choosed == topic[2]:
                    word = random.choice(word_tp3)

            word_display = ""
            choosed = True

            

            #Topic
            dp_topic = font.render("Topic: " + topic_choosed, True, "BLACK")
            screen.blit(dp_topic, (14, 80))


            # Gallows
            pygame.draw.rect(screen, (0, 0, 0), [1030, 650, 350, 25], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1192.5, 100, 25, 575], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1030, 100, 162.5, 10], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1030, 108, 10, 110], 0)


            #Draw letters
            for letter in letters:
                x, y, ltr, visible = letter
                ltr = ltr.lower() #Lowercase
                
                if visible and draw == True:
                    pygame.draw.circle(screen, "BLACK", (x, y), rad, 3)
                    text = font_small.render(ltr, 1, "BLACK")
                    screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2)) 
                
                
                elif visible == False and ltr in word:
                    pygame.draw.circle(screen, "GREEN", (x, y), rad, 0)
                    


                elif visible == False and ltr not in word:
                    pygame.draw.circle(screen, "RED", (x, y), rad, 0)    
                

            # Word to guess
            for letter in word:
                letter = letter.upper()
                if letter in already_guessed:
                    word_display += letter.lower()
                else:
                    word_display += "_ "
            dp_word = font.render(word_display, True, "BLACK")
            screen.blit(dp_word, (85, 310))

            # Turns left
            screen.blit(font_start.render("Turn(s) left: "+ str(limit - count), True, "BLACK"), (880, 10))


            # Draw hangman
            if count == 1: 
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) # Head
                pygame.draw.circle(screen, (0, 0, 0), [1020, 255], 5, 0) # Eyes
                pygame.draw.circle(screen, (0, 0, 0), [1050, 255], 5, 0) #

            elif count == 2:
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) # Head
                pygame.draw.circle(screen, (0, 0, 0), [1020, 255], 5, 0) # Eyes
                pygame.draw.circle(screen, (0, 0, 0), [1050, 255], 5, 0) #
                pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100]) # Body

            elif count == 3:
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) # Head
                pygame.draw.circle(screen, (0, 0, 0), [1020, 255], 5, 0) # Eyes
                pygame.draw.circle(screen, (0, 0, 0), [1050, 255], 5, 0) #
                pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100]) # Body
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (1092, 362), 7) # Left hand
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (971, 362), 7) # Right hand
            

            elif count == limit: 
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) # Head
                pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100]) # Body
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (1092, 362), 7) # Left hand
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (971, 362), 7) # Right hand
                pygame.draw.line(screen, (0, 0, 0), (1034, 400), (1092, 491), 7) # Left leg
                pygame.draw.line(screen, (0, 0, 0), (1034, 400), (971, 491), 7) # Right leg
                dead = font_small.render("x x", True, "BLACK")
                screen.blit(dead, (1004, 220))

                # LOST
                lost = True
                draw = False
                game_active = False
            
            # Win
            if word_display == word:    
                won = True
                draw = False
                game_active = False
    else:
        letters.clear()
        if lost:
            pygame.draw.rect(screen, (0, 0, 0), [1030, 650, 350, 25], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1192.5, 100, 25, 575], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1030, 100, 162.5, 10], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1030, 108, 10, 110], 0)
            pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) # Head
            pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100]) # Body
            pygame.draw.line(screen, (0, 0, 0), (1034, 319), (1092, 362), 7) # Left hand
            pygame.draw.line(screen, (0, 0, 0), (1034, 319), (971, 362), 7) # Right hand
            pygame.draw.line(screen, (0, 0, 0), (1034, 400), (1092, 491), 7) # Left leg
            pygame.draw.line(screen, (0, 0, 0), (1034, 400), (971, 491), 7) # Right leg
            dead = font_small.render("x x", True, "BLACK")
            screen.blit(dead, (1004, 220))
            text = font_start.render("You've lost, the word is: " + word, True, "RED")
            screen.blit(text, (68, 210))

        if won:
            text = font_start.render("You've won", True, "GREEN")
            screen.blit(text, (570, 210))

        text = font_start.render("Wanna play again ? Press space", True, "Black")
        screen.blit(text, (68, 280))                    

                    

                    
    # Last part
    pygame.display.update()
    clock.tick(60)
