## Final Project for Computer Programming for CS
## Authors: Oswald Fiifi Amissah & Yaw Darfour Botwe

## This program aims to make the voting process in the Ashesi Community
## easier, faster and greener.

## In this program, classes are used to represent the various frames
##  in the app


# Import modules to be used in program
from tkinter import*
from random import random

#This is to set the font style of the Labels drawn in tkinter windows
fontStyle = ("Avenir", 18,"Roman")

# A function to return the second item in a tuple comprising a word
# Retrieved from Dr. Ayorkor Korsah's program for finding the word frequency of a text file
def byFreq(pair):
     return pair[1]


class StartPage(Frame):

     #A frame containing widgets is created in the constructor of this class
     #pseudoPar and passPar are variables we would use in storing
     # specific numbers based on the user's input and passing it to another class
     
     def __init__(self, parent, controller, pseudoPar, passPar):
          
          #The class inherents the frame class from the tkinter module
          ''' We inhereted the frame class so that the StartPage frame (and other frames)
               can exist as an independent frame object without opening another tkinter window '''
          #A frame with width and height of 600 pixels and a white background is created
          
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Label with ashesi logo
          self.img = PhotoImage(file = "rsz_1ashesi.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.13, anchor="center")

          #Label with heading "Ashesi Votes"
          heading = Label(self, text="Ashesi Votes", bg = 'white', fg = 'maroon', font=(fontStyle, 25))
          heading.place(relx=.5, rely=.251, anchor="center")

          #Label describing the use of the entry field
          label = Label(self, text= "Please enter the number of candidates (Limit of 10 candidates)",
                      bg = 'white',fg = 'maroon')
          label.place(relx=.5, rely=.5, anchor="center")

          #Entry field for user's input
          canInput = Entry(self, bg = "grey", fg = "black", 
                             selectbackground = "white", selectforeground = "maroon")
          canInput.place(relx=.5, rely=.6, anchor="center")
          
          #Button to show the next frame
          button1 = Button(self, text="Next", bg = 'white',
                            command=lambda: controller.show_frame1("enterCandidates", canInput))
          button1.place(relx=0.5, rely=0.7 ,anchor="center")


          
class enterCandidates(Frame):
     
     def __init__(self, parent, controller, pseudoPar, passPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Empty list to contain the user's input (candidate names)
          self.entryLst = []

          #Create a variable and assign it a sting value
          m ="a"

          #Label describing the use of the entry fields
          label = Label(self, text="Enter the names of candidates", bg = 'white',
                      fg = 'maroon',font=(fontStyle, 15))
          label.place(relx=.5, rely=.08, anchor="center")

          #The pseudo variable is passed to the entry class in
          #the show_frame1 method in the VotingApp class

          #Loop to create a list of entry objects that are distinct
          ''' This would help us to get the different candidate names
               when we use the .get() method of the entry widget '''
          #The entry objects are then created on the frame separated
          # 50 pixels from each other
          for i in range(pseudoPar):
               self.entryLst.append(m+str(i))
               self.entryLst[i] = Entry(self, bg= 'grey', fg = 'black', width = 30, 
                      selectbackground = "white", selectforeground = "maroon")
               self.entryLst[i].place(x = 200, y = 70 + (i * 50))
          
          #Button to show the next frame                    
          button = Button(self, text="Next",
                           command=lambda: controller.show_frame2("passCodeFrame", self.entryLst))
          button.place(relx=0.5, rely=0.94 ,anchor="center")


class passCodeFrame(Frame):
     
     def __init__(self, parent, controller, pseudoPar, passPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Randomly generate passcode
          self.passcode = int(random() * 10000)

          #Label describing what passcode would be used for
          label = Label(self,
                        text="Here is your passcode. \nPlease write it down so you do not forget. \nInput this in the pass code entry field to terminate voting:",
                        bg = 'white',fg = 'maroon',font=(fontStyle, 15))
          label.place(relx=.5, rely=.4, anchor="center")

          #Label of the user's passcode
          usercode = Label(self,text= str(self.passcode),
                        bg = 'white',fg = 'maroon',font=(fontStyle, 30))
          usercode.place(relx=.5, rely=.6, anchor="center")

               
          #Button to show the next frame                   
          button = Button(self, text="Next", command = lambda: controller.show_frame3("SignIn",self.passcode))
          button.place(relx=0.5, rely=0.94 ,anchor="center")

          
          
class SignIn(Frame):

     def __init__(self, parent, controller,pseudoPar, passPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Label with ashesi logo
          self.img = PhotoImage(file = "rsz_1ashesi.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.13, anchor="center")

          #Label with heading "Sign In"
          heading = Label(self, text = "Sign In", font = (fontStyle, 40),
                             fg = 'maroon', bg = 'white')
          heading.place(relx=.5, rely=.267, anchor="center")

          #Label describing entry field for the student's  name
          namelabel = Label( self, text = "Full Name: ",
                                     fg = 'maroon', bg = 'white')
          namelabel.place(relx=.1, rely=.55, anchor="center")

          #Label describing entry field for student's id
          idlabel = Label( self, text = "School ID: ",fg = 'maroon', bg = 'white')
          idlabel.place(relx=.1, rely=.65, anchor="center")
          
          #Entry field for the student's name
          username = Entry(self, bg = "grey", fg = "black", width = 40,
                                  selectbackground = "white", selectforeground = "maroon")
          username.place(relx=.55, rely=.55, anchor="center")
        
          #Entry field for the student's id
          userid = Entry(self, bg = "grey", fg = "black", width = 20,
                                 selectbackground = "white", selectforeground = "maroon")
          userid.place(relx=.45, rely=.65, anchor="center")

          #Label describing entry field for the passcode
          passlabel = Label(self, text = "Pass Code: ",
                            fg = 'maroon', bg = 'white')
          passlabel.place(relx=.7, rely=.95, anchor="center")

          #Entry field for the passcode
          passcode = Entry(self, bg = "grey", fg = "black", width = 10,
                                 selectbackground = "white", selectforeground = "maroon")
          passcode.place(relx=.85, rely=0.95, anchor="center")         

          #Button to show the next frame 
          button = Button(self, text="Sign In!",
                           command=lambda: controller.show_frame4("votingPage", passPar, username, userid, passcode))
          button.place(relx=.5, rely=.8, anchor="center")

class votingPage(Frame):
     
     def __init__(self, parent, controller, pseudoPar, passPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Label with heading "Make your Choice"
          heading = Label(self, text = "Make your Choice", font = (fontStyle, 30),
                        fg = 'maroon', bg = 'white')
          heading.place(relx=.5, rely=.1, anchor="center")

          #Label describing entry field for voter's choice
          choicelabel = Label(self, text = "I choose: ", font = (fontStyle, 15),
                        fg = 'maroon', bg = 'white')
          choicelabel.place(relx=.26, rely=.7, anchor="center")

          #Entry field for voter's choice
          choice = Entry(self, bg = "grey", fg = "black", width = 20,
                                 selectbackground = "white", selectforeground = "maroon")
          choice.place(relx=.5, rely=.7, anchor="center")

          #Button to show the next frame 
          button = Button(self, text="Done",
                           command=lambda: controller.show_frame5("SignIn", choice))
          button.place(relx=.5, rely=.8, anchor="center")

class votingResults(Frame):

     def __init__(self, parent, controller,pseudoPar, passPar):
          #A frame with width and height of 600 pixels and a white background is created
          Frame.__init__(self, parent, bg = 'white', height = 600, width = 600)
          self.controller = controller

          #Label with ashesi logo
          self.img = PhotoImage(file = "rsz_1ashesi.gif")
          logo = Label(self, image=self.img)
          logo.place(relx=.5, rely=.13, anchor="center")

          #Label with heading "Voting Results"
          heading = Label(self, text = "Voting Results", font = (fontStyle, 40),
                             fg = 'maroon', bg = 'white')
          heading.place(relx=.5, rely=.267, anchor="center")
          

          #Button to show the next frame 
          button = Button(self, text="Exit", command = lambda: controller.exitCommand())
          button.place(relx=.5, rely=.95, anchor="center")

        
#This is the main class we created
#This class opens a tkinter window with a frame, container.
#This frame holds all other frames and loops through them when buttons are clicked


class VotingApp:
     
     def __init__(self, master):
          ''' The container is a frame for stacking other frames.
               when we wanta frame to be visible we raise that frame above others'''
          self.master = master
          self.container = Frame(self.master)
          self.container.pack(side="top", fill="both", expand=True)
          self.container.grid_rowconfigure(0, weight=1)
          self.container.grid_columnconfigure(0, weight=1)

          #List containing the names of people who have voted
          self.alreadyVoted = ['']

          #List containing the names of candidates 
          self.candidates=[]

          #List containing the users' choices
          self.votes = []

          #A dictionary containing the tally of votes
          self.tally = {}

          #A dictionary containing objects of the frames(classes) created above
          self.frames = {}

          #Loop to place all the pages in the self.frame dictionary
          # one on the top of the stacking order would be visible
          for F in (StartPage, enterCandidates, passCodeFrame, SignIn, votingPage, votingResults):

               page_name = F.__name__
               frame = F(parent=self.container, controller=self,pseudoPar= 0, passPar = 0)
               self.frames[page_name] = frame
               frame.grid(row=0, column=0, sticky="nsew")

          #Call method for placing page at the top of the stacking order
          self.show_frame("StartPage")



     '''The following methods are used as commands for the buttons
          in the frames above'''

     
     #Method for placing page at the top of the stacking order
     def show_frame(self, page_name):
          #Show a frame for the given page name
          frame = self.frames[page_name]
          frame.tkraise()

     #Method for going to the 'enterCandidates' page
     def show_frame1(self, page_name, entry):
          
          #Checks if there is an input in the entry field
          if entry.get() != '':
               x = int(entry.get())
               
               #Limits the number of candidates to 10
               if x < 11:
                    
                    #Selects the 'enterCandidates' frame from the self.frames dictionary
                    #and raises that frame to be visible
                    frame = self.frames[page_name]
                    frame.tkraise()

                    page_name = enterCandidates.__name__
                    
                    # Passes the number of candidates to the enterCandidates frame
                    # by setting pseudoPar to x
                    frame = enterCandidates(parent=self.container, controller=self, pseudoPar = x,
                                       passPar = 0)
                    self.frames[page_name] = frame
                    frame.grid(row=0, column=0, sticky="nsew")

     
     #Method for going to the 'passCodeFrame' page
     def show_frame2(self, page_name, lst):
          # Iterates through the entry objects in the self.entryLst
          #l ist in the enterCandidates frame,
          # gets input of each entry field and adds it to a list
          for entries in lst:
               if entries.get() != '':
                    self.candidates.append(entries.get())
          frame = self.frames[page_name]
          frame.tkraise()

     #Method for going to the 'SignIn' page
          ''' Sends the passcode to the SignIn frame as the value of the variable passPar'''
     def show_frame3(self, page_name, passcode):
          frame = self.frames[page_name]
          frame.tkraise()

          
          
          page_name = SignIn.__name__
          frame = SignIn(parent=self.container, controller=self, pseudoPar = 0, passPar = passcode)
          self.frames[page_name] = frame
          frame.grid(row=0, column=0, sticky="nsew")
               

     #Method for going to the 'votingPage' page
     def show_frame4(self, page_name, code, entry1, entry2, entry3):

          #Opens a file containing the students' names and their respective IDs
          dataFile = open('StudentDatabase.txt', 'r')
          data = dataFile.read()
          #Make a list of students' names and their respective IDs
          database = data.split('\n')

          #Join entries in the two entry fields together
          name = entry1.get()
          stuId = entry2.get()
          passcode = entry3.get()
          person = name +'\t' + stuId


          #Check if the users details is in the database,
          #whether the user has not already voted
          #and if the passcode is correct
          if (person in database) and (person not in self.alreadyVoted) and passcode != str(code):

               #Show votingPage frame
               frame = self.frames[page_name]
               frame.tkraise()
               page_name = votingPage.__name__
               frame = votingPage(parent=self.container, controller=self, pseudoPar = 0, passPar = 0)
               self.frames[page_name] = frame
               frame.grid(row=0, column=0, sticky="nsew")

               #Create loop to draw labels of the names of election candidates
               #on the 'votingPage' frame
               i = 0
               for candidates in self.candidates:
                    names = Label(self.container, text= str(candidates), font = (fontStyle, 14),
                        fg = 'maroon', bg = 'white')
                    names.place(relx=0.2, rely=(0.2+i), anchor="center")
                    i += 0.05
               self.alreadyVoted.append(person)

          #When passcode is correct
          elif passcode == str(code):
               #Show 'votingResults' frame
               frame = self.frames[page_name]
               frame.tkraise()
               page_name = votingResults.__name__
               frame = votingResults(parent=self.container, controller=self, pseudoPar = 0, passPar = 0)
               self.frames[page_name] = frame
               frame.grid(row=0, column=0, sticky="nsew")

               #Loop for counting the number of votes for each candidate
               for v in self.votes:
                    if v not in self.tally:
                         self.tally[v] = 1
                    else:
                         self.tally[v] = self.tally.get(v) + 1

               #To take care of instances where a candidate gets no vote
               for non in self.candidates:
                    if non not in self.votes:
                         self.tally[non] = 0

               #To arrange names of candidates in alphabetical order
               # on the 'votingResults' frame
               self.candidates.sort()

               #Create sorted list of self.tally dictionary
               tally = sorted(self.tally)


               i , j= 0, 0
               #Iterate through the sorted list of candidates and create labels on the frame
               for candidates in self.candidates:
                    names = Label(self.container, text= str(candidates), font = (fontStyle, 14),
                        fg = 'maroon', bg = 'white')
                    names.place(relx=0.2, rely=(0.4+i), anchor="center")
                    i += 0.04

                    
               #Iterate through the sorted list of the keys in the tally list
               #and get the value of these keys to create labels on the frame
               for results in tally:
                    score =  Label(self.container, text= str(self.tally.get(results)), font = (fontStyle, 14),
                                  fg = 'maroon', bg = 'white')
                    score.place(relx=0.6, rely=(0.4+j), anchor="center")
                    j += 0.04

               # Reverse form of sorting a list of items
               # Retrieved from Dr. Ayorkor Korsah's program
               # for finding the word frequency of a text file
               items = list(self.tally.items())
               items.sort()
               items.sort(key=byFreq, reverse=True)

               #Create label of the first item on the list as the winner of the election
               winner = Label(self.container, text = "The winner is " + (items[0])[0],
                              font = (fontStyle, 20), fg = 'maroon', bg = 'white')
               winner.place(relx=0.5, rely=0.85, anchor="center")

          else:
               #Create error label
               error = Label(self.container, text = "Invalid Input", font = (fontStyle, 16),
                             fg = 'red', bg = 'white')
               error.place(relx=.5, rely=.73, anchor="center")

     #Method for going back to the SignIn Frame after voting
     def show_frame5(self, page_name, entry):
          frame = self.frames[page_name]
          frame.tkraise()

          #Add users entry to self.votes list
          if entry.get() in self.candidates:
               self.votes.append(entry.get())

     #Method to close tkinter window
     def exitCommand(self):
          self.master.destroy()
            


def main():
     #Create tkinter window with dimension 600x600
     # and title 'Computerized Voting System'
     root = Tk()
     root.title('Computerized Voting System')
     root.geometry('600x600+300+100')
     
     app = VotingApp(root)

     #To keep the tkinter window running
     root.mainloop()

if __name__ == "__main__":
     main()
