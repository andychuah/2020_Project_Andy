
# dict, clear(dict), help(dataframe)
import tkinter as tk
import os
import atexit
from tkinter.filedialog import asksaveasfile
from collections import defaultdict
from tkinter import *
import pandas as pd

window = tk.Tk()
window.title("Welcome to my window")
window.geometry('1000x1000')

lbl = Label(window, text="Text Area", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

txt = Text(window, height=12, width=100)
txt.grid(column=0, row=1)
btn = Button(window, text="Run")

classlist = []
funclist = []
output = []
global cnt
line=6.0
global cplus
global cdef
global flagclass
global flagdefine
global defintmain
global detectdc
global callvalue
cplus = ""

thisdict = defaultdict(list)

def runclicked():
    
    txt1.delete('1.0', END)
    output.clear()
    
    global line
    cnt=0
    cdef=0
    flagclass = 0
    flagdefine = 0
    defintmain=0
    detectdc=0
    callvalue=1
    text = txt.get('1.0', END).splitlines()
    for word in text:
        cnt += 1
        r = re.match("run", word)
        if(r):
            output.append("#include <iostream>\n\nusing namespace std; \n")
        
        hp = re.search("help",word)
        if(hp): #frame
            top = Toplevel()
            top.title("Command that you can use")
            top.geometry('900x300')
            
            helptext = """
            These are some keywords you can try to use:\n 
            Commands              |  Definition
            ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            define                     |  Define a function
            function                  |  There are some functions that already provided for users,such as add,sub,multiply,divide,factorial,fibonacci...
                                              Ex : i want an add function/ i want a fibonacci function
            class                       |  Define a class
            print                        |  Print something, Ex : print hello world, cout << "hello world";
            calculate and print |  Print the result of an simple calculation, Ex : calculate and print 5+5, cout << "5+5" << 5+5;
            declare                   |  Declare any variables
            call                         |  Call back the function, Ex : call add(5,5)
            clear                       |  Clear all the contents in both areas
            """
            lbltop = Label(top, text=helptext ,font=("Arial Bold", 10), justify=LEFT)
            lbltop.pack()

            button = Button(top, text="Close", command=top.destroy)
            button.pack()
        
        c = re.search("class",word)
        if(c):
            if(flagclass == 1):
                output.append("\n\n}")
                flagclass = 0
            if(flagdefine == 1):
                output.append("\n\n}")
                flagdefine = 0
            cdef += 1
            flagclass = 1
            detectdc=1
            cList = word.split(" ")
            idxclass = cList.index("class")
            clasdic = " ".join(word.split(' ') [idxclass+1:])
            cls = " ".join(word.split(' ')[idxclass:])
            output.append("\n" + cls + "\n{") 
            thisdict["class"].append([clasdic])
            
        func = re.search("function", word)
        if(func):
            funlist = word.split(" ")
            idxfunc = funlist.index("function")
            fun =  "".join(word.split(' ')[idxfunc-1])
            funclist.append(fun)
            print(fun)
            if (fun == "add"):
                thisdict["function"].append(["\nint add(int a, int b) //add function to add two integer a and b\n{\n\treturn a+b; //return result of a+b\n}"])
                output.append("\nint add(int a, int b) //add function to add two integer a and b\n{\n\treturn a+b; //return result of a+b\n}")
            if (fun == "sub"):
                thisdict["function"].append(["\nint sub(int a, int b) //sub function to sub two integer a and b\n{\n\treturn a-b; //return result of a-b\n}"])
                output.append("\nint sub(int a, int b) //sub function to sub two integer a and b\n{\n\treturn a-b; //return result of a-b\n}")
            if (fun == "multiply"):
                thisdict["function"].append(["\nint mul(int a, int b) //multiply function to multiply two integer a and b\n{\n\treturn a*b; //return result of a*b\n}"])
                output.append("\nint mul(int a, int b) //multiply function to multiply two integer a and b\n{\n\treturn a*b; //return result of a*b\n}")
            if (fun == "divide"):
                thisdict["function"].append(["\nint div(int a, int b) //divide function to divide two integer a and b\n{\n\treturn a/b; //return result of a/b\n}"])
                output.append("\nint div(int a, int b) //divide function to divide two integer a and b\n{\n\treturn a/b; //return result of a/b\n}")
            if (fun == "factorial"):
                thisdict["function"].append(["\nint factorial(int n) //factorial of integer n\n{\n\tif(n>1)\n\t\treturn n*factorial(n - 1);\n\telse\n\t\treturn 1;\n}"])
                output.append("\nint factorial(int n) //factorial of integer n\n{\n\tif(n>1)\n\t\treturn n*factorial(n - 1);\n\telse\n\t\treturn 1;\n}")
            if (fun == "fibonacci"):
                thisdict["function"].append(["\nint fibonacci(int n) // 0 1 1 2 3 5 8 ....\n{\n\tif(n==0 || n==1)\n\t\treturn n;\n\treturn fibonacci(n-1)+fibonacci(n-2);// F(n) = F(n-1) + F(n-2)\n}"])
                output.append("\nint fibonacci(int n) // 0 1 1 2 3 5 8 ....\n{\n\tif(n==0 || n==1)\n\t\treturn n;\n\treturn fibonacci(n-1)+fibonacci(n-2);// F(n) = F(n-1) + F(n-2)\n}")
                
        define = re.match("define",word)
        if(define):
            if(flagclass == 1):
                output.append("\n\n}")
                flagclass = 0
            if(flagdefine == 1):
                output.append("\n\n}")
                flagdefine = 0
            flagdefine = 1
            detectdc=1
            cdef += 1
            deList = word.split(" ")
            idxde = deList.index("define")
            de =  " ".join(word.split(' ')[idxde+1:])
            funclist.append(de)
            output.append("\n" + de + "()\n{")
            thisdict["define"].append([de])
               
        infunc = re.match("in", word)
        if(infunc):
            print(word)
            inList = word.split(" ")
            print(inList)
            idxin = inList.index("in")
            infunction = "".join(word.split(' ')[idxin+1])
            inf = " ".join(word.split(' ')[idxin+2:])
            thisdict[infunction].append([inf])
            #inf1 = " ".join(word.split(' ')[idxin+2:])
            print(infunction)
            if(inf == "print"):
                print("yes")
                
                #output.append("\n\tvalue"+ str(callvalue) + "=" + call + ";")
        
        declare = re.match("declare", word)
        if(declare):
            declareList = word.split(" ")
            idxdec = declareList.index("declare")
            declare = " ".join(word.split(' ')[idxdec+1:])
            output.append("\n\t" + declare + ";")
            thisdict["declare"].append([declare])
            
        initialize = re.search("initialize", word)
        if(initialize):
            initializeList = word.split(" ")
            idxini =initializeList.index("initialize")
            initialize = " ".join(word.split(' ')[idxini+1:])
            output.append("\n\t" + initialize + ";")
            thisdict["initialize"].append([initialize])
        
        assign = re.search("assign", word)
        if(assign):
            assignList = word.split(" ")
            idxass = assignList.index("assign")
            assign = " ".join(word.split(' ')[idxass+1:])
            output.append("\n\t" + assign + ";")
            thisdict["assign"].append([assign]) 
            
        call = re.search("call", word)
        if(call):
            callList = word.split(" ")
            idxcall = callList.index("call")
            call =  " ".join(word.split(' ')[idxcall+1:])
            output.append("\n\tvalue"+ str(callvalue) + "=" + call + ";")
            thisdict["call"].append(["\n\tvalue"+ str(callvalue) + "=" + call + ";"])
            callvalue += 1
        
        calprint = re.search("print" and "calculate",word)
        p = re.search("print",word)
        if(calprint):
            cpList = word.split(" ")
            idxcp = cpList.index("print")
            cp = " ".join(word.split(' ')[idxcp+1:])
            output.append("\n\tcout << \"" + cp + "=\"<<" + cp +";")
            thisdict["calculatePrint"].append(["\n\tcout << \"" + cp + "=\"<<" + cp +";"])
            line += 1
            
        elif(p and not infunc):
            pList = word.split(" ")
            idx = pList.index("print")
            p = " ".join(word.split(' ')[idx+1:])
            output.append("\n\tcout << \"" + p + "\";")
            thisdict["print"].append(["\n\tcout << \"" + p + "\";"])
            line += 1
        #'''
        if(cnt == len(text)):
            if(detectdc == 1):
                output.append("\n}")
            cplus = ""
            for i in output:
                cplus = cplus + i;
            txt1.insert(line,cplus)
        #'''
        clear = re.search("clear",word)
        if(clear):
            line=6.0
            output.clear()
            txt1.delete('1.0', END)
            txt.delete('1.0',END)
        
        print(thisdict)

btn = Button(window, text="Run", command=runclicked)
btn.grid(column=2, row=0)

def clearclicked():
    line=6.0
    output.clear()
    txt.delete('1.0',END)
    txt1.delete('1.0',END)

btnclr = Button(window, text='Clear', command=clearclicked)
btnclr.grid(column=4, row=0)

lbl = Label(window, text="Code Area", font=("Arial Bold", 20))
lbl.grid(column=0, row=4)

txt1 = Text(window, height=16, width=100)
txt1.grid(column=0, row=5)
btn = Button(window, text="Compile")

def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 
    code =  txt1.get('1.0', END)
    if file:
        file.write(code)
        file.close()
    
btn = Button(window, text = 'Save', command = lambda : save())
btn.grid(column=2, row=4)

lbl = Label(window, text="Compile Area", font=("Arial Bold", 20))
lbl.grid(column=0, row=6)

txt2 = Text(window, height=12, width=100)
txt2.grid(column=0, row=7)

window.mainloop()