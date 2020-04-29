import tkinter as tk
import tkinter.font as tkFont

result=''
aux=''
porcent=False

screenSize = { 'width': 480, 'height': 480 }

root = tk.Tk()
root.title('Calculator')
root.minsize(screenSize['width'], screenSize['height'])
root.resizable(False, False)

themePalette = {
    "Primary":"#230444",
    "Secondary":"#ed8240",
    'Numbers':"#3b6978"
}

themeFonts = {
    "Display": tkFont.Font(family = 'Calibri', size=48),
    "Numpad": tkFont.Font(family="Calibri", size=24)
}

def redondear(numero):
    numStr=str(numero)
    if '.' in numStr:
        punto=numStr.index('.')
        entero=numStr[:punto]
        decimal=numStr[punto+1:]
        espaciosRestante=12-len(entero)
        if espaciosRestante>0:
            decimal=round(float('0.'+decimal), espaciosRestante)
        return entero+'.'+str(decimal)[2:]
    else:
        return numero

def clear():
    global result
    result=''
    text.set('')

def masMenos():
    global result
    igual()
    result=-float(result)
    redondear(result)
    text.set(result)
    result=str(result)

def porcentaje(i):
    global result
    num=float(i)*1/100
    result=result+str(num)
    text.set(result)

def igual():
    global result
    text.set('')
    if '/0' in result and result[-2:]=='/0':
        result=''
    else:
        aux=result
        result=eval(result)
        result=redondear(result)
        text.set(result)
        result=str(result)
        aux=''
    

def appendAsString(i):
    operadores=['+','-','*','/']
    numeros=['0','1','2','3','4','5','6','7','8','9']
    global result
    if '%'==i:
        myvar=result[::-1]
        misOperadores=[]
        indicesOperadores=[]
        contador=0
        for k in myvar:
            if k in operadores:
                misOperadores.append(k)
                indicesOperadores.append(myvar.index(k))   
                contador+=1
            if contador>=2:
                break
        if len(misOperadores)<2:
            if len(misOperadores)==0:
                result=''
            else:
                result=result[:len(result)-indicesOperadores[0]]
                porcentaje(myvar[:indicesOperadores[0]][::-1])
            
        else:
            numeroPorcent= myvar[:indicesOperadores[0]][::-1]
            numeroOriginal=myvar[indicesOperadores[0]+1:][:indicesOperadores[1]-indicesOperadores[0]-1][::-1]
            result=result[:len(result)-indicesOperadores[0]]
            porcentaje(numeroPorcent)
        
    else:
        result=result+i
        text.set(result)
    

seccionDisplay = tk.Frame(root, bg=themePalette['Primary'])
seccionDisplay.place( anchor = tk.NW, relwidth=1.0, relheight = 0.2 )
seccionDisplay.place_configure(relx=0, rely=0)

text=tk.StringVar()

labelDisplay= tk.Label(seccionDisplay, bg=themePalette['Primary'],
fg='white', textvariable=text, font=themeFonts['Display'])
labelDisplay.place(anchor=tk.CENTER, rely=0.5)
labelDisplay.place_configure(anchor=tk.E, relx=0.9)

seccionNumpad = tk.Frame(root, bg = themePalette['Secondary'])
seccionNumpad.place(anchor=tk.NW, relwidth = 1.0, relheight=0.8)
seccionNumpad.place_configure(relx=0, rely=0.2)

calcButtons={}
buttonFunction=['C','+/-','%','/','7','8','9','*','4','5','6','-','1','2','3','+','0','.','=']

for item in buttonFunction:
    if (item!='C' and item!='+/-' and item!='%' and item!='='):
        calcButtons[item]=tk.Button(seccionNumpad, 
            text=item,
            font = themeFonts['Numpad'],
            bg=themePalette['Secondary'],
            command=lambda x=item:appendAsString(x)
        )
    elif item=='C':
        calcButtons[item]=tk.Button(seccionNumpad, 
            text=item,
            font = themeFonts['Numpad'],
            bg=themePalette['Secondary'],
            command=lambda:clear()
        )
    elif item=='+/-':
        calcButtons[item]=tk.Button(seccionNumpad, 
            text=item,
            font = themeFonts['Numpad'],
            bg=themePalette['Secondary'],
            command=lambda:masMenos()
        )
    elif item=='%':
       calcButtons[item]=tk.Button(seccionNumpad, 
            text=item,
            font = themeFonts['Numpad'],
            bg=themePalette['Secondary'],
            command=lambda x=item:appendAsString(x)
        )
    elif item=='=':
        calcButtons[item]=tk.Button(seccionNumpad, 
            text=item,
            font = themeFonts['Numpad'],
            bg=themePalette['Secondary'],
            command=lambda:igual()
        )

    calcButtons[item].place(anchor=tk.NW, relwidth=0.25, relheight=0.2)
    if item=="0":
        calcButtons[item].place(anchor=tk.NW, relwidth=0.5, relheight=0.2)

x=0.0
y=0.0
contador=0
for item in buttonFunction:
    calcButtons[item].place_configure(relx=x, rely=y)
    x+=0.25
    contador+=1
    if contador>3:
        contador=0
        x=0.0
        y+=0.2


calcButtons['.'].place_configure( relx=0.5,rely=0.8)
calcButtons['='].place_configure( relx=.75,rely=0.8)
root.mainloop()