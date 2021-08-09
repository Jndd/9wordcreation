import tkinter as tk
from tkinter.constants import MOVETO
import pygame
import os
import math
import random
from pygame import mouse
from tkinter.filedialog import askopenfilename, asksaveasfilename
pygame.font.init()

detective_words = ['footprints', 'secret', 'clue', 'riddle', 'detective', 'bank', 'robber', 'fingerprints', 'gold', 'traced',
 'invisible', 'cloak', 'machine', 'clock', 'mystery', 'butler', 'mansion', 'investigation', 'examined', 'searching', 'found',
  'secret', 'time', 'shadow', 'subtle', 'foggy', 'myth', 'cops']

space_words = ['dark', 'planet', 'sun', 'moon', 'black', 'star', 'rocket', 'spaceship', 'galaxy', 'universe', 'black hole',
 'alien', 'space', 'wormhole', 'gravity', 'crater', 'light year', 'astronaut', 'moon', 'meteor', 'Earth', 'time', 'telescope',
  'world', 'martian']

fantasy_words = ['princess', 'elf', 'castle', 'ogre', 'fairy', 'magic', 'magical', 'prince', 'wand', 'troll', 'king',
 'queen', 'potion', 'sparkled', 'star', 'spell', 'transformed', 'world', 'kingdom', 'palace', 'candy', 'mermaid', 'monster',
 'tower', 'colourful', 'creature']

normal_words = ['apple', 'cart',  'banana', 'dog', 'cat', 'lantern', 'torch', 'cave', 'lighthouse', 'acorn', 'umbrella',
 'blender', 'alpaca', 'moss', 'whale', 'computer', 'energy', 'champion', 'magnet', 'forest', 'birthday', 'flower', 'cupcake',
  'skyscraper', 'power', 'pillow', 'gorilla', 'hippo', 'message', 'serpent', 'glass', 'silver', 'acted', 'slippery',
 'clam', 'sticky', 'needle', 'pinecone', 'beach', 'mountain', 'pickle', 'plastic', 'treasure', 'box', 'nose', 'tree', 'stone',
 'stick', 'painting', 'crayon', 'tiny', 'humongous', 'atom', 'cute', 'amazing', 'cold', 'hot', 'alarm']

words = []

def write_story():
    window = tk.Tk()
    app = tk.Frame(window)
    app.pack()
    window.geometry("500x500")
    window.resizable(False, False)
    window.title("9 Word Creation")

    pink = '#fc8fed'
    blue = "#1f009a"

    window['background'] = pink

    got_words = tk.Label(window, bg=pink, fg=blue, pady=30, text="You have collected these 9 words:", font=("Helvetica italic", 20))
    got_words.pack()

    word_text = str(words)
    word_list = [char for char in word_text]
    for i in range(len(word_list)):
        if word_list[i] == "'":
            word_list[i] = ""
    word_list[0] = ""
    word_list[-1] = ""
    word_text = ''.join(word_list)

    word_text = tk.Label(window, bg=pink, fg=blue, text=word_text, font=("Helvetica italic", 15), wraplength=300).pack()
    story_time = tk.Label(window, bg=pink, fg=blue, pady=20, text="Now it's time to write a story with these 9 words!", font=("Helvetica italic", 14))
    story_time.pack()

    def text_editor():
        import tkinter as tk
        from tkinter.filedialog import askopenfilename, asksaveasfilename

        def open_file():
            filepath = askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not filepath:
                return
            txt_edit.delete(1.0, tk.END)
            with open(filepath, "r") as input_file:
                text = input_file.read()
                txt_edit.insert(tk.END, text)
            win.title(f"9 Word Creation - {filepath}")

        def save_file():
            filepath = asksaveasfilename(
                defaultextension="txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )
            if not filepath:
                return
            with open(filepath, "w") as output_file:
                text = txt_edit.get(1.0, tk.END)
                output_file.write(text)
            win.title(f"9 Word Creation - {filepath}")

        def check_words():
            new_win = tk.Tk()
            new_win.title("9 Word Creation")
            new_win.geometry("500x500")
            new_win.resizable(False, False)
            new_win.title("9 Word Creation")

            orange = '#ff9763'
            blue = "#1f009a"

            text = txt_edit.get(1.0, tk.END)

            not_found = []
            score = new_score

            check_text = text.strip()
            check_list = [char for char in check_text]
            for i in range(len(check_list)):
                if check_list[i] in ['.', '"', "'", '/', '(', ')', '!', '?', ',', ';']:
                    check_list[i] = ''
            check_text = ''.join(check_list).lower()
            check_list = check_text.split()

            for word in words:
                if word.lower() not in check_list:
                    not_found.append(word)
                else:
                    score += 20
            not_found_list = not_found
            not_found = ', '.join(not_found)
            
            if len(not_found) > 0:
                if len(not_found) == 1:
                    plural = " this "
                else:
                    plural = " these "
                found_false = tk.Label(new_win, bg=orange, fg=blue, pady=30, 
                text="You are missing" + plural + str(len(not_found_list)) + " words: " + not_found, font=("Helvetica italic", 15), wraplength=300)
                found_false.pack()
            else:
                found_false = tk.Label(new_win, bg=orange, fg=blue, pady=30, text="You have included all 9 words. Congratulations! :)", font=("Helvetica italic", 15))
                found_false.pack()
                ty = tk.Label(new_win, bg=orange, fg=blue, pady=30, text="Thank you for playing, and remember to save your story!", font=("Helvetica italic", 15))
                ty.pack()
            current_score = tk.Label(new_win, bg=orange, fg=blue, text="Your score is: " + str(score), font=("Helvetica italic", 20))
            current_score.pack()

            new_win['background'] = orange
            new_win.mainloop()

        win = tk.Tk()
        win.title("9 Word Creation")
        win.rowconfigure(0, minsize=800, weight=1)
        win.columnconfigure(1, minsize=800, weight=1)

        txt_edit = tk.Text(win)
        fr_buttons = tk.Frame(win, relief=tk.RAISED, bd=2)
        btn_score = tk.Button(fr_buttons, text="Score", command=check_words)
        btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
        btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

        btn_score.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=2, column=0, sticky="ew", padx=5)

        fr_buttons.grid(row=0, column=0, sticky="ns")
        txt_edit.grid(row=0, column=1, sticky="nsew")

        win.mainloop()

    start_writing = tk.Button(window, command=text_editor, bg=pink, fg=blue, highlightbackground=pink, text="Start Writing!", font=("Helvetica italic", 12))
    start_writing.place(x=200, y=200, width=100, height=100)

    window.mainloop()


def run_game():
    WIDTH, HEIGHT = 600, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("9 Word Creation")

    FPS = 60
    CENTER = (315, 505)
    SCORE_FONT = pygame.font.SysFont('arial', 30)
    ball_rect = pygame.Rect(CENTER[0], CENTER[1], 50, 50)

    BLACK = (0, 0, 0)

    OUT_OF_BOUNDS = pygame.USEREVENT + 1
    CLOUD_HIT = pygame.USEREVENT + 2

    ARROW = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'arrow.png')), (80, 80))
    HILLS = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'hills.png')), (WIDTH, HEIGHT))
    BALL = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ball.png')), (50, 50))

    FANTASY_CLOUD = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'fantasy_cloud.png')), (112, 80))
    SPACE_CLOUD = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space_cloud.png')), (112, 80))
    DETECTIVE_CLOUD = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'detective_cloud.png')), (112, 80))
    NORMAL_CLOUD = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_cloud.png')), (112, 80))

    cloud_pos = []

    for i in range(4):
        rand_choice = random.randint(0, 1)
        if rand_choice == 0:
            x_pos = -212
        else:
            x_pos = 712
        y_pos = random.randint(0, 270)
        cloud_pos.append((x_pos, y_pos))

    fantasy_rect = pygame.Rect(cloud_pos[0][0], cloud_pos[0][1], 112, 80)
    space_rect = pygame.Rect(cloud_pos[1][0], cloud_pos[1][1], 112, 80)
    detective_rect = pygame.Rect(cloud_pos[2][0], cloud_pos[2][1], 112, 80)
    normal_rect = pygame.Rect(cloud_pos[3][0], cloud_pos[3][1], 112, 80)

    fantasy_vel = random.randint(1, 5)
    space_vel = random.randint(1, 5)
    detective_vel = random.randint(1, 5)
    normal_vel = random.randint(1, 5)

    right = [False, False, False, False, False]
    if fantasy_rect.x == 712:
        fantasy_vel = -1 * fantasy_vel
        right[0] = True
    if space_rect.x == 712:
        space_vel = -1 * space_vel
        right[1] = True
    if detective_rect.x == 712:
        detective_vel = -1 * detective_vel
        right[2] = True
    if normal_rect.x == 712:
        normal_vel = -1 * normal_vel
        right[3] = True

    def draw_window(score):
        WIN.blit(HILLS, (0, 0))
        score_text = SCORE_FONT.render("Score: " + str(score), 1, BLACK)
        WIN.blit(score_text, (10, 10))
        if pygame.mouse.get_pressed()[0]:
            if ball_rect.x > -50 and ball_rect.x < 600 and ball_rect.y > -50 and ball_rect.y < 600:
                pos = pygame.mouse.get_pos()
                cannon_ball(pos)
                WIN.blit(BALL, (ball_rect.x, ball_rect.y))
            else:
                ball_rect.x, ball_rect.y = CENTER
                pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS))
        else:
            ball_rect.x, ball_rect.y = CENTER

        if fantasy_rect.x >= 713:
            fantasy_rect.x = -212
        elif fantasy_rect.x <= -213:
            fantasy_rect.x = 712
        
        if space_rect.x >= 713:
            space_rect.x = -212
        elif space_rect.x <= -213:
            space_rect.x = 712

        if detective_rect.x >= 713:
            detective_rect.x = -212
        elif detective_rect.x <= -213:
            detective_rect.x = 712

        if normal_rect.x >= 713:
            normal_rect.x = -212
        elif normal_rect.x <= -213:
            normal_rect.x = 712

        fantasy_rect.x += fantasy_vel
        space_rect.x += space_vel
        detective_rect.x += detective_vel
        normal_rect.x += normal_vel

        WIN.blit(FANTASY_CLOUD, (fantasy_rect.x, fantasy_rect.y))
        WIN.blit(SPACE_CLOUD, (space_rect.x, space_rect.y))
        WIN.blit(DETECTIVE_CLOUD, (detective_rect.x, detective_rect.y))
        WIN.blit(NORMAL_CLOUD, (normal_rect.x, normal_rect.y))

        arrow()
        pygame.display.update()

    def arrow():
        mouse = pygame.mouse.get_pos()
        angle = 360 - math.atan2(mouse[1] - CENTER[1],mouse[0] - CENTER[0]) * 180 / math.pi
        
        NEW_ARROW = pygame.transform.rotate(ARROW, angle + 270)
        WIN.blit(NEW_ARROW, (280, 475))

    def cannon_ball(pos):
        vel_x = (pos[0] - CENTER[0])/25
        vel_y = (pos[1] - CENTER[1])/25

        if vel_x == 0 and vel_y == 0:
            ball_rect.x += 2
            ball_rect.y += 2

        ball_rect.x += vel_x
        ball_rect.y += vel_y
        
    def collide():
        if ball_rect.colliderect(fantasy_rect):
            word = random.choice(fantasy_words)
            words.append(word)
            fantasy_words.remove(word)
            if right[0] == True:
                fantasy_rect.x = 712
            else:
                fantasy_rect.x = -212
            pygame.event.post(pygame.event.Event(CLOUD_HIT))
        elif ball_rect.colliderect(space_rect):
            word = random.choice(space_words)
            words.append(word)
            space_words.remove(word)
            if right[1] == True:
                space_rect.x = 712
            else:
                space_rect.x = -212
            pygame.event.post(pygame.event.Event(CLOUD_HIT))
        elif ball_rect.colliderect(detective_rect):
            word = random.choice(detective_words)
            words.append(word)
            detective_words.remove(word)
            if right[2] == True:
                detective_rect.x = 712
            else:
                detective_rect.x = -212
            pygame.event.post(pygame.event.Event(CLOUD_HIT))
        elif ball_rect.colliderect(normal_rect):
            word = random.choice(normal_words)
            words.append(word)
            normal_words.remove(word)
            if right[0] == True:
                normal_rect.x = 712
            else:
                normal_rect.x = -212
            pygame.event.post(pygame.event.Event(CLOUD_HIT))

    def main():
        score = 10
        word_num = 0
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or word_num == 9:
                    run = False
                    break
                if event.type == OUT_OF_BOUNDS:
                    score -= 10
                if event.type == CLOUD_HIT:
                    score += 5
                    word_num += 1
                    
            collide()
            draw_window(score)

        global new_score
        new_score = score
        pygame.quit()
        if word_num == 9:
            write_story()

    main()

window = tk.Tk()
app = tk.Frame(window)
app.pack()
window.geometry("500x500")
window.resizable(False, False)
window.title("9 Word Creation")

yellow = '#ffff33'
pink = '#fc8fed'
blue = "#1f009a"

window['background'] = yellow


def instructions():
    def start_btn():
        window.destroy()
        run_game()

    instruction_text = tk.Label(window, bg=yellow, fg=blue,
     text="First you will have to play a game in which you bump clouds with a ball to get words. There are four different types of clouds: the normal cloud, detective cloud, space cloud, and fantasy cloud. They will give you words related to the cloud name when you bump it. To move the ball press down on your mouse and don't release it. The ball will move in the direction of your mouse and will move faster if your mouse is farther away from the arrow. If the ball goes out of the screen, you will lose 10 points, but if you bump a cloud you will gain 5 points. After you collect 9 words, You will be shown the words and given a text editor to write a story (that can be as crazy as you like) that includes those 9 words. Every word you include will get you an additional 20 points! Press 'Score' to see your current score, which is located on the left hand side of the text editor. When you are done writing, you can save your story by pressing 'Save As...' which is also located on the left side of your text editor. Have fun writing your story!",
     font=("Helvetica italic", 12), wraplength=300)
    instruction_text.pack()
    start_btn = tk.Button(window, command=start_btn, bg=pink, fg=blue, highlightbackground=yellow, activebackground=pink, activeforeground=blue, text="Start Game", font=("Helvetica italic", 12))
    start_btn.place(x=200, y=450, width=100, height=30)

def instruct_btn():
    intro_text.place_forget()
    instructions_button.place_forget()
    instructions()

intro_label = tk.Label(window, bg=yellow, fg=blue, pady=30,
 text="Welcome to 9 Word Creation!", font=("Helvetica italic", 20)).pack()
intro_text = tk.Label(window, bg=yellow, fg=blue, pady=15,
 text="9 Word Creation is a game that allows kids to develop their writing skills and use their imagination to create stories that include nine interesting words!", font=("Helvetica italic", 15), wraplength=300)
instructions_button = tk.Button(window, command=instruct_btn, bg=pink, fg=blue,  highlightbackground=yellow, activebackground=pink, activeforeground=blue, text="Instructions", font=("Helvetica italic", 12))

instructions_button.place(x=200, y=200, width=100, height=100)
intro_text.place(x=100, y=70, width=300, height=100)


window.mainloop()
