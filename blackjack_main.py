from tkinter import * 
from PIL import Image, ImageTk
import random
import math

global player, player_spot, dealer, dealer_spot
#players hand 
player = []
player_value = 0
player_spot = 0
#dealers hand 
dealer = []
dealer_value = 0
dealer_spot = 0

#give the starting hand for the player 
def start_hand_player():
    global player_spot,player_image_1, player_image_2, player_value
    if player_spot < 2:
        if player_spot == 0:
            player_card = random.choice(deck)
            deck.remove(player_card)
            used_cards.append(player_card)
            player.append(player_card)
            player_image_1 = resize_card(f"cards/{player_card}.png")
            player_label_1.config(image=player_image_1)
            # get value of cards 
            value_of_card = int(player_card.split("_", 1)[0])
            if value_of_card == 1:
                player_value += 11
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                player_value += 10
            else:
                player_value += value_of_card
            
            player_spot += 1

        else:
            pass
        if player_spot == 1:
            player_card = random.choice(deck)
            deck.remove(player_card)
            used_cards.append(player_card)
            player.append(player_card)
            player_image_2 = resize_card(f"cards/{player_card}.png")
            player_label_2.config(image=player_image_2)
            # get value of cards 
            value_of_card = int(player_card.split("_", 1)[0])
            if value_of_card == 1:
                if player_value >= 11:
                    player_value += value_of_card
                else:  
                    player_value += 11
                
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                player_value += 10
            else:
                player_value += value_of_card
            print(f"player value:{player_value}")
            player_spot += 1 

        else:
            pass
#give the starting hand for the dealer
def start_hand_dealer():
    global dealer_spot, dealer_image_1, dealer_image_2, dealer_card, dealer_value
    if dealer_spot < 2:
        if dealer_spot == 0: 
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            used_cards.append(dealer_card)
            dealer.append(dealer_card)
            dealer_image_1 = resize_card(f"cards/{dealer_card}.png")
            dealer_label_1.config(image=dealer_image_1)
            # get value of cards 
            value_of_card = int(dealer_card.split("_", 1)[0])
            if value_of_card == 1:
                dealer_value += 11
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                dealer_value += 10
            else:
                dealer_value += value_of_card

            dealer_spot += 1
        else:
            pass
        if dealer_spot == 1:
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            used_cards.append(dealer_card)
            dealer.append(dealer_card)
            dealer_image_2 = resize_card(f"cards/{dealer_card}.png")
            dealer_label_2.config(image=dealer_image_2)
            # get value of cards 
            value_of_card = int(dealer_card.split("_", 1)[0])
            if value_of_card == 1:
                if dealer_value >= 11:
                    dealer_value += value_of_card
                else:  
                    dealer_value += 11
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                dealer_value += 10
            else:
                dealer_value += value_of_card
            print(f"dealer value:{dealer_value}")
            dealer_spot += 1



def hit_player():
    global player_spot, player_image_1, player_image_2, player_image_3, player_image_4, player_image_5,player_value
    if player_spot <= 5:
        if player_spot == 2:
            player_card = random.choice(deck)
            deck.remove(player_card)
            used_cards.append(player_card)
            player.append(player_card)
            player_image_3 = resize_card(f"cards/{player_card}.png")
            player_label_3.config(image=player_image_3)
            # get value of cards 
            value_of_card = int(player_card.split("_", 1)[0])
            if value_of_card == 1:
                if player_value >= 11:
                    player_value += value_of_card
                else:  
                    player_value += 11
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                player_value += 10
            else:
                player_value += value_of_card
            
            print(f"player value:{player_value}")
            player_spot += 1

        elif player_spot == 3:
            player_card = random.choice(deck)
            deck.remove(player_card)
            used_cards.append(player_card)
            player.append(player_card)
            player_image_4 = resize_card(f"cards/{player_card}.png")
            player_label_4.config(image=player_image_4)
            # get value of cards 
            value_of_card = int(player_card.split("_", 1)[0])
            if value_of_card == 1:
                if player_value >= 11:
                    player_value += value_of_card
                else:  
                    player_value += 11
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                player_value += 10
            else:
                player_value += value_of_card

            print(f"player value:{player_value}")
            player_spot += 1

        elif player_spot == 4:
            player_card = random.choice(deck)
            deck.remove(player_card)
            used_cards.append(player_card)
            player.append(player_card)
            player_image_5 = resize_card(f"cards/{player_card}.png")
            player_label_5.config(image= player_image_5)
            # get value of cards 
            value_of_card = int(player_card.split("_", 1)[0])
            if value_of_card == 1:
                if player_value >= 11:
                    player_value += value_of_card
                else:  
                    player_value += 11
            elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                player_value += 10
            else:
                player_value += value_of_card

            player_spot += 1
            print(f"player value:{player_value}")
            print(used_cards)
    else:
        pass
    #splearen has max med kort 

def hit_dealer():
    global dealer_spot,dealer_image_1,dealer_image_2,dealer_image_3,dealer_image_4,dealer_image_5,dealer_value
    if dealer_spot <= 5:
        if dealer_spot == 2:
                if dealer_value <= 17:
                    dealer_card = random.choice(deck)
                    deck.remove(dealer_card)
                    used_cards.append(dealer_card)
                    dealer.append(dealer_card)
                    dealer_image_3 = resize_card(f"cards/{dealer_card}.png")
                    dealer_label_3.config(image=dealer_image_3)
                # get value of cards 
                    value_of_card = int(dealer_card.split("_", 1)[0])
                    if value_of_card == 1:
                        if dealer_value >= 11:
                            dealer_value += value_of_card
                        else:  
                            dealer_value += 11
                    elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                        dealer_value += 10
                    else:
                        dealer_value += value_of_card
                    print(f"dealer value:{dealer_value}")
                    dealer_spot += 1
                else:
                    pass
        if dealer_spot == 3:
                if dealer_value <= 17:
                    dealer_card = random.choice(deck)
                    deck.remove(dealer_card)
                    used_cards.append(dealer_card)
                    dealer.append(dealer_card)
                    dealer_image_4 = resize_card(f"cards/{dealer_card}.png")
                    dealer_label_4.config(image=dealer_image_4)
                # get value of cards 
                    value_of_card = int(dealer_card.split("_", 1)[0])
                    if value_of_card == 1:
                        if dealer_value >= 11:
                            dealer_value += value_of_card
                        else:  
                            dealer_value += 11
                    elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                        dealer_value += 10
                    else:
                        dealer_value += value_of_card
                    print(f"dealer value:{dealer_value}")
                    dealer_spot += 1
                else:
                    pass
        if dealer_spot == 4:
                if dealer_value <= 17:
                    dealer_card = random.choice(deck)
                    deck.remove(dealer_card)
                    used_cards.append(dealer_card)
                    dealer.append(dealer_card)
                    dealer_image_5 = resize_card(f"cards/{dealer_card}.png")
                    dealer_label_5.config(image=dealer_image_5)
                # get value of cards 
                    value_of_card = int(dealer_card.split("_", 1)[0])
                    if value_of_card == 1:
                        if dealer_value >= 11:
                            dealer_value += value_of_card
                        else:  
                            dealer_value += 11
                    elif value_of_card == 11 or value_of_card == 12 or value_of_card == 13:
                        dealer_value += 10
                    else:
                        dealer_value += value_of_card
                    print(f"dealer value:{dealer_value}")
                    dealer_spot += 1
                else:
                    pass

def resize_card(dealer_card):
    global card_image
    card_image = Image.open(dealer_card)
    card_resized_img = card_image.resize((80,120))
    card_image = ImageTk.PhotoImage(card_resized_img)
    return card_image

def resize_card(player_card):
    global card_image
    card_image = Image.open(player_card)
    card_resized_img = card_image.resize((80,120))
    card_image = ImageTk.PhotoImage(card_resized_img)
    return card_image

def new_game():
    global player_spot, dealer_spot,dealer_value,player_value
    # clearing last game
    dealer_label_1.config(image="")
    dealer_label_2.config(image="")
    dealer_label_3.config(image="")
    dealer_label_4.config(image="")
    dealer_label_5.config(image="")

    player_label_1.config(image="")
    player_label_2.config(image="")
    player_label_3.config(image="")
    player_label_4.config(image="")
    player_label_5.config(image="")

    #reset scores and spots
    player_spot = player_spot - player_spot 
    dealer_spot = dealer_spot - dealer_spot
    
    dealer_value = dealer_value - dealer_value
    player_value = player_value - player_value

    deck.extend(used_cards)
    used_cards.clear()

    start_hand_player()                           
    start_hand_dealer()



    
suits = ["hearts","spades","diamonds","clubs"]
cards = range(1, 14)

used_cards = []
deck = []

for suits in suits:
    for card in cards:
        deck.append(f"{card}_of_{suits}")
   

root = Tk()
root.title("Blackjack")
root.geometry("1080x630")
root.configure(background="green")

main_frame = Frame(root, bg="green")
main_frame.pack(pady=20)

dealer_frame = LabelFrame(main_frame, text="Dealer",font=("Roman", 15, "bold"),bg="green")
dealer_frame.grid(sticky="", pady=50)

player_frame = LabelFrame(main_frame, text="Player",font=("Roman", 15, "bold"),bg="green")
player_frame.grid(sticky="")

player_score_frame = Frame(main_frame)

# label for dealer cards
dealer_label_1 = Label(dealer_frame,text=" ",bg="green")
dealer_label_1.grid(row=0,column=0, pady= 20, padx=20)

dealer_label_2 = Label(dealer_frame,text=" ",bg="green")
dealer_label_2.grid(row=0,column=1, pady= 20, padx=20)

dealer_label_3 = Label(dealer_frame,text=" ",bg="green")
dealer_label_3.grid(row=0,column=2, pady= 20, padx=20)

dealer_label_4 = Label(dealer_frame,text=" ",bg="green")
dealer_label_4.grid(row=0,column=3, pady= 20, padx=20)

dealer_label_5 = Label(dealer_frame,text=" ",bg="green")
dealer_label_5.grid(row=0,column=4, pady= 20, padx=20)


# label for players cards
player_label_1 = Label(player_frame,text="",bg="green")
player_label_1.grid(row=1,column=0, pady= 20, padx=20)

player_label_2 = Label(player_frame,text="",bg="green")
player_label_2.grid(row=1,column=1, pady= 20, padx=20)

player_label_3 = Label(player_frame,text="",bg="green")
player_label_3.grid(row=1,column=2, pady= 20, padx=20)

player_label_4 = Label(player_frame,text="",bg="green")
player_label_4.grid(row=1,column=3, pady= 20, padx=20)

player_label_5 = Label(player_frame,text="",bg="green")
player_label_5.grid(row=1,column=4, pady= 20, padx=20)

button_frame = Frame(root, bg="green")
button_frame.pack(pady= 20)

new_game_button = Button(button_frame,padx= 20, pady=20, text= "New game",font=("Roman", 10),command=new_game)
new_game_button.grid(row= 0, column= 2, padx= 20)

stand_button = Button(button_frame,padx= 20, pady=20, text= "Stand",font=("Roman", 10), command=hit_dealer)
stand_button.grid(row= 0, column= 1, padx= 20)

hit_button = Button(button_frame,padx= 20, pady=20, text= "Hit",font=("Roman", 10),bg="red",command=hit_player)
hit_button.grid(row= 0, column= 0, padx= 20)

score_frame = Frame(root, bg="green")




start_hand_player()

start_hand_dealer()

print(used_cards)










root.mainloop()