from tkinter import * 
from PIL import Image, ImageTk
import random

#append a card to palyer list
#def hit_player():
    
#append a card to dealer list
#def hit_dealer():
    

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

dealer_label = Label(dealer_frame,text="")
dealer_label.pack(pady=20)

player_label = Label(player_frame,text="")
player_label.pack(pady=20)




#players hand 
player = []

#dealers hans 
dealer = []






root.mainloop()