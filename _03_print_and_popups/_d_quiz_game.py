from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
 window = Tk()
    # Hide the window using the window's .withdraw() method
 window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
 score =0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
 userinput=simpledialog.askstring("Office Quiz","What’s the name of the company The Office employees work for?")
    #      // 3.  Use an if statement to check if their answer is correct
 if userinput=="dunder mifflin":
    #      // 4.  if the user's answer was correct, add one to their score
    score+=1
    messagebox.showinfo(message="corect")
 else:
     score-=1
     messagebox.showinfo(message="incorect, dunder mifflin")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 userinput = simpledialog.askstring("Office Quiz","What’s the company's annual award ceremony called?")
 if userinput== "the dundies":
    score+=1
    messagebox.showinfo(message="corect")
 else:
    score-=1
    messagebox.showinfo(message="incorect, the dundies")
 userinput = simpledialog.askstring("Office Quiz","Which character does tons of crosswords during the many meetings?")
 if userinput== "stanley hudson":
    score+=1
    messagebox.showinfo(message="corect")
 else:
     score-=1
     messagebox.showinfo(message="incorect, stanley hudson")
userinput = simpledialog.askstring("Office Quiz", "Who are the three main heads of the party planing commity?")
if userinput=="pam angela phylis":
    score+=1
    messagebox.showinfo(message="correct")
else:
    score-=1
    messagebox.showinfo(message="incorect, pam angela phylis")
if score>2:
    messagebox.showinfo(message="congrats, you passed!")
else:
    messagebox.showinfo(message="you failed:( try agin next time")


    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
window.mainloop()