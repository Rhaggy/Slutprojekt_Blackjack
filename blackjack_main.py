from tkinter import * 
from PIL import Image, ImageTk
import random
import math

#append a card to palyer list
def hit_player():
   pass 
#append a card to dealer list
def hit_dealer():
    pass

def new_game():
    # clearing last game 
    dealer_label_1.config(image=" ")
    dealer_label_2.config(image=" ")
    dealer_label_3.config(image=" ")
    dealer_label_4.config(image=" ")
    dealer_label_5.config(image=" ")

    player_label_1.config(image=" ")
    player_label_2.config(image=" ")
    player_label_3.config(image=" ")
    player_label_4.config(image=" ")
    player_label_5.config(image=" ")

# value of cards
def get_value(card): 
    value = math.ceil(card//4)
    if value == 1:
        return 11
    elif value > 10:
        return 10
    else:
        return value
    
suits = ["Hearts","Spades","Diamonds","Clubs"]
cards = range(1, 14)


deck = []

for suits in suits:
    for card in cards:
        deck.append(f"{card}_of_{suits}")
        

print(deck)
    



root = Tk()
root.title("Blackjack")
root.geometry("1600x1080")
root.configure(background="Green")

main_frame = Frame(root, bg="green")
main_frame.pack(pady=20)

dealer_frame = LabelFrame(main_frame, text="Dealer",font=("Roman", 15, "bold"))
dealer_frame.grid(row=0,column=0,pady=100,ipadx=50)

player_frame = LabelFrame(main_frame, text="Player",font=("Roman", 15, "bold"))
player_frame.grid(row=1,column=0,ipadx=50)

# label for dealer cards
dealer_label_1 = Label(dealer_frame,text=" ")
dealer_label_1.grid(row=0,column=0, pady= 100, padx=20)

dealer_label_2 = Label(dealer_frame,text=" ")
dealer_label_2.grid(row=0,column=1, pady= 100, padx=50)

dealer_label_3 = Label(dealer_frame,text=" ")
dealer_label_3.grid(row=0,column=2, pady= 100, padx=20)

dealer_label_4 = Label(dealer_frame,text=" ")
dealer_label_4.grid(row=0,column=3, pady= 100, padx=50)

dealer_label_5 = Label(dealer_frame,text=" ")
dealer_label_5.grid(row=0,column=4, pady= 100, padx=20)


# label for players cards
player_label_1 = Label(player_frame,text="")
player_label_1.grid(row=1,column=0, pady= 100, padx=20)

player_label_2 = Label(player_frame,text="")
player_label_2.grid(row=1,column=1, pady= 100, padx=50)

player_label_3 = Label(player_frame,text="")
player_label_3.grid(row=1,column=2, pady= 100, padx=20)

player_label_4 = Label(player_frame,text="")
player_label_4.grid(row=1,column=3, pady= 100, padx=50)

player_label_5 = Label(player_frame,text="")
player_label_5.grid(row=1,column=4, pady= 100, padx=20)

button_frame = Frame(root, bg="green")
button_frame.pack(pady= 20)

new_game_button = Button(button_frame,padx= 20, pady=20, text= "New game",font=("Roman", 10))#,command=new_game())
new_game_button.grid(row= 0, column= 2, padx= 20)

stand_button = Button(button_frame,padx= 20, pady=20, text= "Stand",font=("Roman", 10))
stand_button.grid(row= 0, column= 1, padx= 20)

hit_button = Button(button_frame,padx= 20, pady=20, text= "Hit",font=("Roman", 10),bg="red")
hit_button.grid(row= 0, column= 0, padx= 20)

score_frame = Frame(root, bg="green")
#use get_value def to get the score of the player/delaers hand and update a "text" in a frame
#players hand 
player = []
player_spot = 0
#dealers hans 
dealer = []
dealer_spot = 0





root.mainloop()