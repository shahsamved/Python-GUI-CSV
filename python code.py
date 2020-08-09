'''
PSC Sessional Assignment
Name-Samved Shah
Roll No. - 18BCE206
Div - D
'''

# Importing necessary modules

import csv
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import cv2

from tkinter import filedialog

img_path = ""
s1=""
s2=""
s=""
lis=[]

# This is a function to select files from your device using GUI(tkinter)

def fileselector():

    name = askopenfilename(initialdir="",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file.")

    try:
        with open(name,'r') as UseFile:
            s=UseFile.read()
            lis.append(s)
    except:
        print("No file exists")

# Here we are selecting 2 files but using this code only you can select as many files as you want.

# We are appending the contents of the file to a list in the form of a string so we can use it later 
# for our other half of the program.

# Now this is a function to generate csv file.


def generate_csv():

	s1=lis[0]     # As we have chosen two files and have appended into the list, we extract it and store
	s2=lis[1]	  # them in two string variables.

	temp1=s1.split(" ")
	p1=set(temp1)

	temp2=s2.split(" ")
	p2=set(temp2)

	# For frequency count and generating statistics of the files, I have used a dictionary.

	# First I have used a set and added the whole content in it so we get all the words and charachters used unrepeated.

	# Then I have used the concept of frequency mapping to store the count of each charchter in dictionary.

	s=s1+s2
	d1={}
	d2={}
	st=set()
	for i in s:
	    st.add(i)
	s=""
	for i in st:
	    d1[i]=0
	    d2[i]=0
	for i in st:
	    s+=i

	for i in s:
	    if i in s1:
	        for i in s1:
	            if i in d1:
	                d1[i]+=1
	            else:
	                d1[i]=1
	    if i in s2:
	        for i in s2:
	            if i in d2:
	                d2[i]+=1
	            else:
	                d2[i]=1
	        
	s=s1+s2
	sam=s.split(" ")
	samved=set()
	for i in sam:
	    samved.add(i)


	for i in samved:
	    d1[i]=0
	    d2[i]=0

	for i in samved:
	    if i in p1:
	        if i in d1:
	            d1[i]+=1
	        else:
	            d1[i]=1
	    if i in p2:
	        if i in d2:
	            d2[i]+=1
	        else:
	            d2[i]=1


	l=list()

	cc1=0
	cc2=0
	wc1=0
	wc2=0

	for i in s1:
	    cc1+=1
	    
	w1=s1.split(" ")

	for i in w1:
	    wc1+=1
	    
	for i in s2:
	    cc2+=1

	w2=s2.split(" ")

	for i in w2:
	    wc2+=1
	    
	for i in d1:

	    l.append({'Data':i,'File 1':d1[i],'File 2':d2[i]})

	l.append({'Data':"Word Count",'File 1':wc1,'File 2':wc2})

	l.append({'Data':"Charachter Count",'File 1':cc1,'File 2':cc2})
	    
	fields = ['Data','File 1','File 2'] 

	# The below code is just for writing into the CSV file.

	filename = "count_frequency.csv"

	with open(filename, 'w') as csvfile: 

	    writer = csv.DictWriter(csvfile, fieldnames = fields) 
	      
	    writer.writeheader() 

	    writer.writerows(l)

	# This part onwards is for generating graph, I have used the statistics like count or words and all you'll see below

	sp1=0	
	sp2=0
	fs1=0
	fs2=0
	c1=0
	c2=0

	for i in s1:
		if i == " ":
			sp1+=1
		if i.isalpha():
			fs1+=1
		if i.isdigit():
			c1+=1

	for i in s2:
		if i == " ":
			sp2+=1
		if i.isalpha():
			fs2+=1
		if i.isdigit():
			c2+=1

	n_groups = 5
	f1 = (wc1,cc1,sp1,fs1,c1)
	f2 = (wc2,cc2,sp2,fs2,c2)

	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8

	rects1 = plt.bar(index, f1, bar_width,
	alpha=opacity,
	color='g',
	label='File 1')

	rects2 = plt.bar(index + bar_width,f2, bar_width,
	alpha=opacity,
	color='r',
	label='File 2')

	plt.xlabel('Data')
	plt.ylabel('Frequency Counts')
	plt.title('Statistics')
	plt.xticks(index + bar_width, ('Words', 'Charachters', 'Spaces', 'Alphabets', 'Digits'))
	plt.legend()

	plt.tight_layout()
	plt.show()
	plt.savefig("Picture3.png")
	    
# The main logic is over and below lines of codes are just for GUI purposes. I have created buttons to choose file and generate CSV.
    
root = Tk()
root.title("GUI")

root.geometry("880x530")

root.configure(background = 'white')
Tops = Frame(root,bg = 'blue',pady = 1, width =1750, height = 90, relief = "ridge")
Tops.grid(row=0,column=0)


Title_Label = Label(Tops,font=('Comic Sans MS',20,'bold'),text = "     PSC Assignment   ",pady=9,bg= 'white',fg='blue',justify ="center")
Title_Label.grid(row=0,column=0)
MainFrame = Frame(root,bg = 'white',pady=2,padx=2, width =1350, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)



Label_2 =Label(MainFrame, font=('arial', 15,'bold'), text="",padx=2,pady=2, bg="white",fg = "black")
Label_2.grid(row=1, column=0,sticky=W)

Label_9 =Button(MainFrame, font=('arial', 19,'bold'), text="  Select Files ",padx=2,pady=2, bg="red",fg = "white",command=fileselector)
Label_9.grid(row=2, column=0)

Label_9 =Button(MainFrame, font=('arial', 19,'bold'), text="  Generate CSV ",padx=2,pady=2, bg="red",fg = "white",command=generate_csv)
Label_9.grid(row=2, column=1,sticky=W)

Label_2 =Label(MainFrame, font=('arial', 10,'bold'), text="",padx=2,pady=2, bg="white",fg = "black")
Label_2.grid(row=3, column=0,sticky=W)

Label_3 =Label(MainFrame, font=('arial', 30,'bold'), text="          \t\t\t",padx=2,pady=2, bg="white",fg = "black")
Label_3.grid(row=4, column=0)



img = cv2.imread("./Picture3.png")
img = cv2.resize(img,(450,280))
cv2.imwrite('Picture3.png',img)
img = ImageTk.PhotoImage(Image.open("Picture3.png"))
panel = Label(MainFrame, image = img).grid(row=4,column=0,sticky=E)


Label_3 =Label(MainFrame, font=('arial', 10,'bold'), text="\t\t\t\t          ",padx=2,pady=2, bg="white",fg = "black")
Label_3.grid(row=5, column=1)

root.mainloop()


