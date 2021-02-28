import tkinter as tk
import tkinter.font as font

"""Principal of my calcurator was putting everything in the list(called counter) and then executing all operations.
since this is my first project I didn't know what to do right and came to it in process of creating"""

def wtc_ari(self): #I've created wtc_ari to add every arithmetical operation to the counter
    s = str(self)
    wtd = (s.split())
    if wtd[0] == '<KeyPress': # I used it to recognise whether button was pressed on keyboard or by mouse
        wtd = wtd[4]
        wtd = wtd.split('=')[1]
        wtd = wtd[1]
    else:
        wtd = s
    global counter
    global element
    global result
    if element != '':
        counter += [element]
        element = ''
        counter += wtd
        result.insert(tk.END, wtd) #I decided to use tkinter.Text as input and output
    elif counter != []:
        counter[-1] = wtd
        result.delete('end-2c', tk.END)
        result.insert(tk.END, wtd)

def wtc_elem(self): #wtc_elem was created to put numbers inside the counter
    s=str(self)
    wtd = (s.split())
    if wtd[0] == '<KeyPress':
        wtd = wtd[4]
        wtd = wtd.split('=')[1]
        wtd = wtd[1]
    else:
        wtd = s
    global element
    global result
    result.insert(tk.END, wtd)
    element += wtd

def wtc_poi(self): # I had to create separate function for points in order two omit double points etc.
    global element
    global result
    if element != '' and '.' not in element:
        element +='.'
        result.insert(tk.END, '.')

def resulting(self): #resulting takes everything from the counter and just doing operations
    global element
    global counter
    global result
    if element != '':
        counter += [element]
        while '/' in counter or '*' in counter:
            if '/' in counter and '*' in counter:
                divider = counter.index('/')
                multip = counter.index('*')
                if divider < multip:
                    ans = float(counter[divider - 1])/ float(counter[divider + 1])
                    for i in range(3):
                        counter.pop(divider - 1)
                    counter.insert(divider-1,ans)
                else:
                    ans = float(counter[multip - 1])/ float(counter[multip + 1])
                    for i in range(3):
                        counter.pop(multip - 1)
                    counter.insert(multip-1,ans)
            elif '/' in counter and '*' not in counter:
                divider = counter.index('/')
                ans = float(counter[divider - 1]) / float(counter[divider + 1])
                for i in range(3):
                    counter.pop(divider - 1)
                counter.insert(divider - 1, ans)
            elif '*' in counter and '/' not in counter:
                multip = counter.index('*')
                ans = float(counter[multip - 1]) * float(counter[multip + 1])
                for i in range(3):
                    counter.pop(multip - 1)
                counter.insert(multip - 1, ans)
        while '+' in counter:
            sum_in = counter.index('+')
            ans = float(counter[sum_in - 1]) + float(counter[sum_in + 1])
            for i in range(3):
                counter.pop(sum_in - 1)
            counter.insert(sum_in -1,ans)
        while '-' in counter:
            dec_in = counter.index('-')
            ans = float(counter[dec_in - 1]) - float(counter[dec_in + 1])
            for i in range(3):
                counter.pop(dec_in - 1)
            counter.insert(dec_in -1,ans)
        result.delete('1.0', tk.END)
        result.insert(tk.END, float(counter[-1]))
        element=str(counter[-1])
        counter.pop()

def cancel(self): #separate function for removing elements from the tkinter.Text and counter
    global counter
    global element
    global result
    if element != '':
        element = element[:-1]
        result.delete('end-2c', tk.END)
    elif counter != []:
        if counter[-1] == '+' or counter[-1] == '-' or counter[-1] == '/' or counter[-1] == '*':
            counter.pop()
        else:
            to_stay = str(counter[-1])
            counter.insert(-1,to_stay[:-1])
            counter.pop(-1)
            if counter[-1] == '':
                counter.pop()
            else:
                element = counter[-1]
                counter.pop

#I've created graphical interface called win to work with
win = tk.Tk()
win.geometry(f"400x500")
win.title("Calculator")
win.config(bg = 'black')
element=""
counter=[]

#long and boring part of creating buttons, selecting colors putting them on the right places and giving commands
#code was lagging when I added enter to output and I decided to leave = only
win.bind_all('1',wtc_elem)
win.bind_all('2',wtc_elem)
win.bind_all('3',wtc_elem)
win.bind_all('4',wtc_elem)
win.bind_all('5',wtc_elem)
win.bind_all('6',wtc_elem)
win.bind_all('7',wtc_elem)
win.bind_all('8',wtc_elem)
win.bind_all('9',wtc_elem)
win.bind_all('0',wtc_elem)
win.bind_all('.',wtc_poi)
win.bind_all('+',wtc_ari)
win.bind_all('-',wtc_ari)
win.bind_all('/',wtc_ari)
win.bind_all('*',wtc_ari)
win.bind_all('<BackSpace>',cancel)
win.bind_all('=',resulting)

sum_but = tk.Button(win, text = '+',
                    command = lambda : wtc_ari('+'),
                    bg = '#696969',fg = '#3CB371'
                    )
sum_but.place(x=340,y=335)
subs_but = tk.Button(win,text = '-',
                     command = lambda : wtc_ari('-'),
                     bg = '#696969',fg = '#3CB371'
                     )
subs_but.place(x = 340,y = 255)
div_but = tk.Button(win,text = '/',
                     command = lambda : wtc_ari('/'),
                    bg = '#696969',fg = '#3CB371'
                    )
div_but.place(x = 340,y = 175)
mul_but = tk.Button(win,text = '*',
                    command = lambda : wtc_ari('*'),
                    bg = '#696969',fg = '#3CB371'
                    )
mul_but.place(x = 340,y = 95)
one_but = tk.Button(win,text = '1',
                    command = lambda : wtc_ari('1'),
                    bg = '#696969',fg = 'white',
                    border = 0
                    )
one_but.place(x = 20, y = 330)
two_but = tk.Button(win,text = '2',
                    command = lambda : wtc_elem('2'),
                    bg = '#696969',fg = 'white',
                    border = 0
                    )
two_but.place(x = 130, y = 330)
three_but = tk.Button(win,text = '3',
                      command = lambda : wtc_elem('3'),
                      bg = '#696969',fg = 'white',
                      border = 0
                      )
three_but.place(x = 240, y = 330)
four_but = tk.Button(win,text = '4',
                     command = lambda : wtc_elem('4'),
                     bg = '#696969',fg = 'white',
                     border = 0
                     )
four_but.place(x = 20, y = 245)
five_but = tk.Button(win,text = '5',
                     command = lambda : wtc_elem('5'),
                     bg = '#696969',fg = 'white',
                     border = 0
                     )
five_but.place(x= 130, y = 245)
six_but = tk.Button(win,text = '6',
                    command = lambda : wtc_elem('6'),
                    bg = '#696969',fg = 'white',
                    border = 0
                    )
six_but.place(x = 240, y = 245)
seven_but = tk.Button(win,text = '7',
                      command = lambda : wtc_elem('7'),
                      bg = '#696969',fg = 'white',
                      border = 0
                      )
seven_but.place(x = 20, y = 160)
eight_but = tk.Button(win,text = '8',
                      command = lambda : wtc_elem('8'),
                      bg = '#696969',fg = 'white',
                      border = 0
                      )
eight_but.place(x = 130, y = 160)
nine_but = tk.Button(win,text = '9',
                     command = lambda : wtc_elem('9'),
                     bg = '#696969',fg = 'white',
                     border = 0
                     )
nine_but.place(x = 240, y = 160)
zero_but = tk.Button(win,text = '0',
                     command = lambda : wtc_elem('0'),
                     bg = '#696969',fg = 'white',
                     border = 0
                     )
zero_but.place(x = 130, y = 415)
poi_but = tk.Button(win,text = '.',
                    command = lambda : wtc_poi(''),
                    bg = '#696969',fg = 'white',
                    border = 0
                    )
poi_but.place(x=240, y =415)
res_but = tk.Button(win, text = '=',
                    command = lambda : resulting(''),
                    bg = '#3CB371',fg = 'black',
                    )
res_but.place(x=340,y= 415)
can_but = tk.Button(win, text = 'C',
                    command = lambda : cancel(''),
                    fg = '#DC143C',bg = '#696969'
                    )
can_but.place(x = 340,y = 10)

can_but.config(height = 5,width = 7)
sum_but.config( height = 5, width = 7)
res_but.config(height = 5, width = 7)
subs_but.config(height = 5, width = 7)
mul_but.config(height = 5, width = 7)
div_but.config(height = 5, width = 7)
one_but.config(height = 5, width = 10)
two_but.config(height = 5, width = 10)
three_but.config(height = 5, width = 10)
four_but.config(height = 5, width = 10)
five_but.config(height = 5, width = 10)
six_but.config(height = 5, width = 10)
seven_but.config(height = 5, width = 10)
eight_but.config(height = 5, width = 10)
nine_but.config(height = 5, width = 10)
zero_but.config(height = 5, width = 10)
poi_but.config(height = 5, width = 10)

result = tk.Text(win,width = 35, height = 4, font = 50, bg = 'black',fg = 'white', border = 0)
result.place(x=15, y = 20)
element = ''

win.mainloop()

