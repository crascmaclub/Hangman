import pygame
from time import sleep as sl
import random

pygame.init()
width, height = 1380, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
cras_logo = pygame.image.load("graphics/logo.jpg")
pygame.display.set_icon(cras_logo)
pygame.display.set_caption("Hangman")
game_active = True

# Font
font = pygame.font.SysFont("comicsans", 60)
font_start = pygame.font.SysFont("comicsans", 50)
font_title = pygame.font.SysFont("comicsans", 25,italic = False)
font_topic = pygame.font.SysFont("comicsans", 35)
font_small = pygame.font.SysFont("comicsans", 42)

# Letters
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

def var():
    global guess, choosed, count, limit, topic, topic_choosed
    global already_guessed, lost, won, word,hint
    global word_tp

    guess = ""
    choosed = False
    count = 0
    limit = 4
    topic = ["Technology", "Sports", "Foods", "Movies", "Mental Health", "Social issues"]
    topic_choosed = ""
    already_guessed = []
    hint = 3

    word_tp = {
        "Technology": ["programmer", "developer", "wire", "automatic", "machine", "circuit", "router", "cpu", "terminal", "microprocessor", "processor"],
        "Sports": ["skiing", "sportmanship", "hockey", "rugby", "handball", "offside", "racket", "archery", "wrestling", "hurdling", "polo", "regatta", "dodgeball"],
        "Foods": ["lolipop", "pudding", "macaroons", "pasta", "olive", "raspberry", "baguette", "salami", "smoothies", "ham", "oysters", "croissants"],
        "Movies": ["inception", "interstellar", "avatar", "gladiator", "parasite", "avengers", "joker", "titanic", "frozen"],
        "Mental Health": ["anxiety", "therapy", "depression", "stress","meditation", "mindfulness", "bipolar", "resilience"],
        "Social issues": ["poverty", "racism", "education", "equality", "corruption", "bullying", "violence", "homelessness"]
    }

    lost = False
    won = False
    word = ""

var()
clicked = -1
draw = True

while True:
    pos = pygame.mouse.get_pos() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == False:
                var()
                letters.clear()
                for i in range(26):
                    x = startx + gap * 2 + (rad * 2 + gap) * (i % 13)
                    y = starty + ((i // 13) * (gap + rad * 2))
                    letters.append([x, y, chr(A + i), True])
                draw = True
                game_active = True
            #thả hint if player stuck
            if event.key == pygame.K_h and game_active and topic_choosed != "" and hint > 0:
                r_letter = [c.upper() for c in word if c.upper() not in already_guessed]
                if r_letter:
                    hint_letter = random.choice(r_letter)
                    already_guessed.append(hint_letter)
                    hint -= 1

        if event.type == pygame.MOUSEBUTTONDOWN and topic_choosed != "":
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible and draw == True:
                    dis = ((x - m_x) ** 2 + (y - m_y) ** 2) ** 0.5
                    if dis < rad:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        letter[3] = False
                        already_guessed.append(ltr)
                        if ltr.lower() not in word:
                            count += 1

    screen.fill("white")

    img = pygame.transform.scale(cras_logo, (70, 70))
    hint_box = screen.blit(img, (10, 11))

    text = font_small.render("1K/ SLOT", True, "BLACK")
    screen.blit(text, (100, 11))

    if hint_box.collidepoint(pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[1] == True:
                clicked += 1
                if clicked == 0:
                    for letter in word:
                        letter = letter.upper()
                        if letter not in already_guessed:
                            already_guessed.append(letter)
                            break
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = -1

    if game_active:
        # chọn topic
        if topic_choosed == "":
            text = font_start.render("Which topic do you want to choose ?", True, "BLACK")
            screen.blit(text, (230, 100))

            topic_rects = []
            rows, cols = 2, 3
            button_w, button_h = 250, 82
            start_x = (width - (cols * button_w + (cols - 1) * 50)) // 2
            start_y = 250
            gap_x, gap_y = 50, 150

            for i, t in enumerate(topic):
                row = i // cols
                col = i % cols
                x = start_x + col * (button_w + gap_x)
                y = start_y + row * gap_y

                text_surface = font_topic.render(t, True, "WHITE")
                rect = pygame.Rect(x, y, button_w, button_h)
                pygame.draw.rect(screen, "#475F77", rect, 0, border_radius=10)
                screen.blit(text_surface, (
                    rect.x + (button_w - text_surface.get_width()) // 2,
                    rect.y + (button_h - text_surface.get_height()) // 2
                ))

                topic_rects.append((rect, t))

            # Event click chọn topic
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, t in topic_rects:
                    if rect.collidepoint(pos):
                        topic_choosed = t
                        pygame.display.flip()
                        sl(0.15)

            # Đổi cursor khi hover
            hovered = False
            for rect, _ in topic_rects:
                if rect.collidepoint(pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    hovered = True
                    break
            if not hovered:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Start
        else:
            if choosed == False:
                word = random.choice(word_tp[topic_choosed])
                choosed = True

            word_display = ""

            dp_topic = font.render("Topic: " + topic_choosed, True, "BLACK")
            screen.blit(dp_topic, (14, 80))

            pygame.draw.rect(screen, (0, 0, 0), [1030, 650, 350, 25], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1192.5, 100, 25, 575], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1030, 100, 162.5, 10], 0)
            pygame.draw.rect(screen, (0, 0, 0), [1030, 108, 10, 110], 0)

            for letter in letters:
                x, y, ltr, visible = letter
                ltr = ltr.lower()
                if visible and draw == True:
                    pygame.draw.circle(screen, "BLACK", (x, y), rad, 3)
                    text = font_small.render(ltr, 1, "BLACK")
                    screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
                elif visible == False and ltr in word:
                    pygame.draw.circle(screen, "GREEN", (x, y), rad, 0)
                elif visible == False and ltr not in word:
                    pygame.draw.circle(screen, "RED", (x, y), rad, 0)

            for letter in word:
                letter = letter.upper()
                if letter in already_guessed:
                    word_display += letter.lower()
                else:
                    word_display += "_ "
            dp_word = font.render(word_display, True, "BLACK")
            screen.blit(dp_word, (85, 310))

            screen.blit(font_title.render("Turn(s) left: "+ str(limit - count), True, "BLACK"), (880, 10))
            screen.blit(font_title.render("Hints left: " + str(hint), True, "BLACK"), (880, 60))
            screen.blit(font_title.render("press H if u want to open hint:D ", True, "BLACK"), (600, 100))            

            if count == 1: 
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) 
                pygame.draw.circle(screen, (0, 0, 0), [1020, 255], 5, 0) 
                pygame.draw.circle(screen, (0, 0, 0), [1050, 255], 5, 0)
            elif count == 2:
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7) 
                pygame.draw.circle(screen, (0, 0, 0), [1020, 255], 5, 0)
                pygame.draw.circle(screen, (0, 0, 0), [1050, 255], 5, 0)
                pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100])
            elif count == 3:
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7)
                pygame.draw.circle(screen, (0, 0, 0), [1020, 255], 5, 0)
                pygame.draw.circle(screen, (0, 0, 0), [1050, 255], 5, 0)
                pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100])
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (1092, 362), 7)
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (971, 362), 7)
            elif count == limit: 
                pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7)
                pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100])
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (1092, 362), 7)
                pygame.draw.line(screen, (0, 0, 0), (1034, 319), (971, 362), 7)
                pygame.draw.line(screen, (0, 0, 0), (1034, 400), (1092, 491), 7)
                pygame.draw.line(screen, (0, 0, 0), (1034, 400), (971, 491), 7)
                dead = font_small.render("x x", True, "BLACK")
                screen.blit(dead, (1004, 220))

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
            pygame.draw.circle(screen, (0, 0, 0), [1035, 261], 43, 7)
            pygame.draw.rect(screen, (0, 0, 0), [1031.5, 303, 7, 100])
            pygame.draw.line(screen, (0, 0, 0), (1034, 319), (1092, 362), 7)
            pygame.draw.line(screen, (0, 0, 0), (1034, 319), (971, 362), 7)
            pygame.draw.line(screen, (0, 0, 0), (1034, 400), (1092, 491), 7)
            pygame.draw.line(screen, (0, 0, 0), (1034, 400), (971, 491), 7)
            dead = font_small.render("x x", True, "BLACK")
            screen.blit(dead, (1004, 220))
            text = font_start.render("You've lost, the word is: " + word, True, "RED")
            screen.blit(text, (68, 210))

        if won:
            text = font_start.render("You've won", True, "GREEN")
            screen.blit(text, (570, 210))

        text = font_start.render("Wanna play again ? Press space", True, "Black")
        if lost:
            screen.blit(text, (80, 280))
        if won:
            screen.blit(text, (345, 280))

    pygame.display.update()
    clock.tick(60)
