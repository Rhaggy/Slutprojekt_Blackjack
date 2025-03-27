from tkinter import * 
from PIL import Image, ImageTk
import random

#append a card to palyer list
def hit_player():
    f
#append a card to dealer list
def hit_dealer():
    f

def shuffle_cards():
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
    value = math.ceil(card/4)
    if value == 1:
        return 11
    elif value > 10:
        return 10
    else:
        return value
    

deck = [x for x in range(1,53)]

root = Tk()
root.title("Blackjack")
root.geometry("1600x1080")
root.configure(background="Green")

main_frame = Frame(root, bg="green")
main_frame.pack(pady=20)

dealer_frame = LabelFrame(main_frame, text="Dealer")
dealer_frame.grid(row=0,column=0,pady=100,ipadx=50)

player_frame = LabelFrame(main_frame, text="Player")
player_frame.grid(row=1,column=0,ipadx=20)

# label for dealer cards
dealer_label_1 = Label(dealer_frame,text=" ")
dealer_label_1.grid(row=0,column=0, pady= 20, padx=20)

dealer_label_2 = Label(dealer_frame,text=" ")
dealer_label_2.grid(row=0,column=1, pady= 20, padx=20)

dealer_label_3 = Label(dealer_frame,text=" ")
dealer_label_3.grid(row=0,column=2, pady= 20, padx=20)

dealer_label_4 = Label(dealer_frame,text=" ")
dealer_label_4.grid(row=0,column=3, pady= 20, padx=20)

dealer_label_5 = Label(dealer_frame,text=" ")
dealer_label_5.grid(row=0,column=4, pady= 20, padx=20)


# label for players cards
player_label_1 = Label(player_frame,text="")
player_label_1.grid(row=1,column=0, pady= 20, padx=20)

player_label_2 = Label(player_frame,text="")
player_label_2.grid(row=1,column=1, pady= 20, padx=20)

player_label_3 = Label(player_frame,text="")
player_label_3.grid(row=1,column=2, pady= 20, padx=20)

player_label_4 = Label(player_frame,text="")
player_label_4.grid(row=1,column=3, pady= 20, padx=20)

player_label_5 = Label(player_frame,text="")
player_label_5.grid(row=1,column=4, pady= 20, padx=20)



#players hand 
player = []

#dealers hans 
dealer = []






root.mainloop()