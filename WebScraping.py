#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame
from pygame.locals import *
import sys
import time
import random
from tkinter import *
from bs4 import BeautifulSoup
import requests
import csv
import ssl
from urllib.request import urlopen
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 750 x 500

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class WebScarping:
    def write_category(cat):
        category = cat
        url = 'https://www.dawn.com/{cat}'.format(cat=category)
        html = urlopen(url, context=ctx).read()
        fetch_soup = BeautifulSoup(html,'html.parser')

        fetch_headlines = fetch_soup.find_all("article", class_="story")
        fetch_array = [];

        for f in fetch_headlines:
            cur_soup = f
            cur_head = cur_soup.find("div", class_="story__excerpt")
            if cur_head:
                value = cur_head.text
                fetch_array.append([value.strip()])

#         print(*fetch_array, sep='\n')
#         print("Headlines_Fetched : "+str(len(fetch_array)))
        with open("sentences.txt", "w",encoding='utf-8') as txt_file:
            for i in fetch_array:
                txt_file.write(''.join(i)+"\n")

class Register:
    def __init__(self, root):
        self.Initial_Page()
        
    def Initial_Page(self):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("1350x700")
        
        #main window frame
        frame1 = Frame(root, bg="white")
        frame1.place(x=480, y=100, width=500, height=500)
        
        title = Label(frame1, text="Choose any one option", font="Times 25 bold", fg="black").place(x=50, y=30)
        
        button1 = tk.Button(frame1, text="Register Yourself", command=self.register_window, font="Times 15", cursor="hand2",
                            bg="black", fg="white").place(x=50, y=400, width=180)
        button2 = tk.Button(frame1, text="Proceed as Guest", command= self.proceed, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=250, y=400, width=180)
        button3 = tk.Button(frame1, text="Quit", command=self.close_window, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=390, y=450, width=100)
    
    def proceed(self):
        root.destroy()
        WebScarping.write_category('latest-news')
        Game().run()
        
    def register_window(self):    
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700")

        # Registraion Frame
        frame1 = Frame(root, bg="white")
        frame1.place(x=480, y=100, width=500, height=500)

        title = Label(frame1, text="REGISTRATION", font="Times 25 bold", bg="white", fg="black").place(x=50, y=30)

        f_name = Label(frame1, text="User Name", font="Times 15").place(x=50, y=100)  # gap between labels 70
        self.txt_fname = Entry(frame1, font="Times 20", bg="gray")
        self.txt_fname.place(x=50, y=130, width=250)  # gap between text entry 70

        password = Label(frame1, text="Password", font="Times 15").place(x=50, y=170)
        self.txt_password = Entry(frame1, font="Times 20", bg="gray")
        self.txt_password.place(x=50, y=200, width=250)

        contact = Label(frame1, text="Contact Number", font="Times 15").place(x=50, y=240)
        self.txt_contact = Entry(frame1, font="Times 20", bg="gray")
        self.txt_contact.place(x=50, y=270, width=250)

        button1 = tk.Button(frame1, text="Register", command=self.register_data, font="Times 15", cursor="hand2",
                            bg="black", fg="white").place(x=50, y=400, width=100)
        button2 = tk.Button(frame1, text="Sign In", command=self.signup, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=250, y=400, width=100)
        button4 = tk.Button(frame1, text="Back", command=self.Initial_Page, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=280, y=450, width=100)
        button3 = tk.Button(frame1, text="Quit", command=self.close_window, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=390, y=450, width=100)

    def close_window(self):
        print("Close")
        root.destroy()

        
    def signup(self):
        self.root = root
        self.root.title("Sign In Window")
        self.root.geometry("1350x700")

        # Registraion Frame
        frame1 = Frame(root, bg="white")
        frame1.place(x=480, y=100, width=500, height=500)

        title = Label(frame1, text="SIGN IN", font="Times 30 bold", bg="white", fg="green").place(x=50, y=30)

        u_name = Label(frame1, text="User Name", font="Times 15").place(x=50, y=100)  # gap between labels 70
        self.txt_uname = Entry(frame1, font="Times 20", bg="gray")
        self.txt_uname.place(x=50, y=130, width=250)  # gap between text entry 70

        pwd = Label(frame1, text="Password", font="Times 15").place(x=50, y=170)
        self.txt_pwd = Entry(frame1, font="Times 20", bg="gray")
        self.txt_pwd.place(x=50, y=200, width=250)

        cont = Label(frame1, text="Contact Number", font="Times 15").place(x=50, y=240)
        self.txt_cont = Entry(frame1, font="Times 20", bg="gray")
        self.txt_cont.place(x=50, y=270, width=250)
        
        button6 = tk.Button(frame1, text = "Registration Window", command=self.register_data, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=250, y=400, width=100)
        button4 = tk.Button(frame1, text="Sign In", command=self.signin, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=250, y=400, width=100)
        button7 = tk.Button(frame1, text="Back", command=self.Initial_Page, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=300, y=450, width=100)
        button5 = tk.Button(frame1, text="Quit", command=self.close_window, font="Times 15", cursor="hand2", bg="black",
                            fg="white").place(x=390, y=450, width=100)

    def signin(self):
        signinflag = True
        print(self.txt_uname.get(), self.txt_pwd.get(), self.txt_cont.get())
        print(self.txt_fname.get(), self.txt_password.get(), self.txt_contact.get())
        if (self.txt_uname.get() == "" or self.txt_pwd.get() == "" or self.txt_cont.get() == ""):
            messagebox.showerror("Error", "All fields are required!",
                                 parent=self.root)  # parent: messagebox is for root window
        else:
            print("text")
            if ((self.txt_uname.get()).format() == (self.txt_fname.get()).format() and (
            self.txt_pwd.get()).format() == (self.txt_password.get()).format() and (self.txt_cont.get()).format() == (
            self.txt_contact.get()).format()):
                messagebox.showinfo("Login Success", "Login Successful!", parent=self.root)
#                 self.signin
                signinflag = True
                self.redirect()
            else:
                messagebox.showerror("Error", "Invalid values entered", parent=self.root)
                signinflag = False
        

        #self.close_window
        
    def redirect(self):
        """if required registration is true then enter into typing speed test module"""
        self.close_window
        Game().run()

    def register_data(self):
        print(self.txt_fname.get(), self.txt_password.get(), self.txt_contact.get())
        if (self.txt_fname.get() == "" or self.txt_password.get() == "" or self.txt_contact.get() == ""):
            messagebox.showerror("Error", "All fields are required!",
                                 parent=self.root)  # parent: messagebox is for root window
        else:
            messagebox.showinfo("Success", "Registered Successfully!")
            self.signup()


class Game:

    Result_Accuracy = [];
    Result_Time = [];
    Result_WPS = [];
    
    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (750,500))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Type Speed test')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def draw_Sentencetext(self, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        pos = (50,200)
        words = [word.split(' ') for word in msg.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = screen.get_size()
       
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 1, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
#                 text_rect = word_surface.get_rect(center=(x, y))
                screen.blit(word_surface, (x, y))
#                 screen.blit(word_surface,text_rect)
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        pygame.display.update() 
    
    def get_sentence(self):
        f = open('sentences.txt',encoding='utf-8').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_Graph(self):
        print("Here")
        print(self.Result_Accuracy)

        data1 = {'Time': self.Result_Time,
         'Accuracy': self.Result_Accuracy
                }
        df1 = DataFrame(data1,columns=['Time','Accuracy'])

        root= tk.Tk() 
        root.title("Graph")
        figure1 = plt.Figure(figsize=(6,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[['Time','Accuracy']].groupby('Time').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Time Vs. Accuracy')


        root.mainloop()

    def show_results(self, screen):
        if (not self.end):
            # Calculate time
            self.total_time = time.time() - self.time_start
#             self.total_time = "{:.2f}".format(self.total_time)
            # Calculate accuracy
            #formula for accuracy is
            #correct words * 100 / total characters in sentence
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100
            
            self.Result_Accuracy.append(round(self.accuracy))
            # Calculate words per minute
            #avaerage word consists of 5 characters
            #divide toatl words with 5
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)
            self.Result_Time.append(round(self.total_time))
            self.Result_WPS.append(round(self.wpm))
            self.results = 'Time:' + str(round(self.total_time)) + " secs   Accuracy:" + str(
                round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('images.png')
            self.time_img = pygame.transform.scale(self.time_img, (100, 100))
            # screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
#             self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))

            self.graph_img = pygame.image.load('Graph.png')
            self.graph_img = pygame.transform.scale(self.graph_img, (100, 100))
            # screen.blit(self.time_img, (80,320))
            screen.blit(self.graph_img, (600, self.h - 140))
#             self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))
            
            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()

        self.running = True
        while (self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # position of input box
                    if (x >= 50 and x <= 650 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                        # position of reset box
                    if (x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()
                    if (x >= 600 and x <= 750 and y >= 390 and self.end):
                        self.show_Graph()
                        x, y = pygame.mouse.get_pos()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True

                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))

        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        # drawing heading
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)

        # draw the sentence string
        self.draw_Sentencetext(self.screen, self.word, 200, 28, self.TEXT_C)
        
        pygame.display.update()

root = Tk()
obj = Register(root)
root.mainloop()


# In[ ]:




