from tkinter import * 


root = Tk()
root.title("Blackjack")
root.geometry("900x500")
root.configure(background="Green")

main_frame = Frame(root, bg="green")
main_frame.pack(pady=20)

dealer_frame = LabelFrame(main_frame, text="Dealer",)
dealer_frame.grid(row=0,column=0,padx=20,ipadx=20)


root.mainloop()