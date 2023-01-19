from tkinter import*

class program(Frame):
    def __init__(self,window):
        self.window=window
        self.window.title("calculator")
        super().__init__(self.window)
        self.grid(rows=2,columns=2)
        self.nesto()
        return

    def nesto(self):

        self.tl=StringVar()
        self.tl.set("")

        f=("calibri",25,"bold")
        self.B1=Button(self,text="1",font=f,command=self.one)
        self.B1.grid(row=1,column=1)
        
        self.B2=Button(self,text="2",font=f,command=self.two)
        self.B2.grid(row=1,column=2)

        self.B3=Button(self,text="3",font=f,command=self.three)
        self.B3.grid(row=1,column=3)

        self.B4=Button(self,text="4",font=f,command=self.four)
        self.B4.grid(row=2,column=1)

        self.B5=Button(self,text="5",font=f,command=self.five)
        self.B5.grid(row=2,column=2)

        self.B6=Button(self,text="6",font=f,command=self.six)
        self.B6.grid(row=2,column=3)

        self.B7=Button(self,text="7",font=f,command=self.seven)
        self.B7.grid(row=3,column=1)

        self.B8=Button(self,text="8",font=f,command=self.eight)
        self.B8.grid(row=3,column=2)

        self.B9=Button(self,text="9",font=f,command=self.nine)
        self.B9.grid(row=3,column=3)

        self.B0=Button(self,text="0",font=f,command=self.zero)
        self.B0.grid(row=4,column=1)

        self.B10=Button(self,text="+",font=f)
        self.B10.grid(row=4,column=2)

        self.B11=Button(self,text="-",font=f)
        self.B11.grid(row=4,column=3)

        self.B12=Button(self,text="x",font=f)
        self.B12.grid(row=5,column=1)

        self.B13=Button(self,text=":",font=f)
        self.B13.grid(row=5,column=2)

        self.B14=Button(self,text="okt",font=f,command=self.okt)
        self.B14.grid(row=5,column=3)

        self.B15=Button(self,text="bin",font=f,command=self.bin)
        self.B15.grid(row=6,column=1)

        self.B16=Button(self,text="heks",font=f,command=self.heks)
        self.B16.grid(row=6,column=2)

        self.B17=Button(self,text="dek",font=f)
        self.B17.grid(row=6,column=3)

        self.B18=Button(self,text="=",font=f)
        self.B18.grid(row=7,column=1)

        self.L1=Label(self,font=f,textvariable=self.tl)
        self.L1.grid(row=1,column=4)

        ###

        self.B19=Button(self,text="A",font=f,command=self.A)
        self.B19.grid(row=7,column=2)

        self.B20=Button(self,text="B",font=f,command=self.B)
        self.B20.grid(row=7,column=3)

        self.B21=Button(self,text="C",font=f,command=self.C)
        self.B21.grid(row=8,column=1)

        self.B22=Button(self,text="D",font=f,command=self.D)
        self.B22.grid(row=8,column=2)

        self.B23=Button(self,text="E",font=f,command=self.E)
        self.B23.grid(row=8,column=3)

        self.B24=Button(self,text="F",font=f,command=self.F)
        self.B24.grid(row=9,column=1)

        self.B25=Button(self,text="antiokt",font=f,command=self.antiokt)
        self.B25.grid(row=9,column=2)

        self.B26=Button(self,text="antibin",font=f,command=self.antibin)
        self.B26.grid(row=9,column=3)

        self.B27=Button(self,text="antiheks",font=f,command=self.antiheks)
        self.B27.grid(row=10,column=1)

        
        return

    def one(self):
        self.tl.set(self.tl.get()+"1")
        return

    def two(self):
        self.tl.set(self.tl.get()+"2")
        return

    def three(self):
        self.tl.set(self.tl.get()+"3")
        return

    
    def four(self):
        self.tl.set(self.tl.get()+"4")
        return

    def five(self):
        self.tl.set(self.tl.get()+"5")
        return

    def six(self):
        self.tl.set(self.tl.get()+"6")
        return

    def seven(self):
        self.tl.set(self.tl.get()+"7")
        return

    def eight(self):
        self.tl.set(self.tl.get()+"8")
        return

    def nine(self):
        self.tl.set(self.tl.get()+"9")
        return
    
    def zero(self):
        self.tl.set(self.tl.get()+"0")
        return
    ###

    def A(self):
        self.tl.set(self.tl.get()+"A")
        return

    def B(self):
        self.tl.set(self.tl.get()+"B")
        return

    def C(self):
        self.tl.set(self.tl.get()+"C")
        return

    def D(self):
        self.tl.set(self.tl.get()+"D")
        return

    def E(self):
        self.tl.set(self.tl.get()+"E")
        return

    def F(self):
        self.tl.set(self.tl.get()+"F")
        return

    def heks(self):
        A=hex(int(self.tl.get()))
        s=str(A)
        self.tl.set(s[2:])
        return
    
    def bin(self):
        A=bin(int(self.tl.get()))
        s=str(A)
        self.tl.set(s[2:])
        return

    def okt(self):
        A=oct(int(self.tl.get()))
        s=str(A)
        self.tl.set(s[2:])
        return
    
    def antiokt(self):
        s=self.tl.get()
        
        a=0
        
        
        for i in range(len(s)):
            
            a+=int(s[i])*8**(int(len(s)-(i+1)))
            print(a)
        self.tl.set(a)
        return


    def antibin(self):
        s=self.tl.get()
        
        a=0
        
        
        for i in range(len(s)):
            
            a+=int(s[i])*2**(int(len(s)-(i+1)))
            print(a)
        self.tl.set(a)
        return

    def antiheks(self):
        s=self.tl.get()
        
        a=0
        
        
        for i in range(len(s)):

            T=s[i]

            if T=="A":
                T=11

            if T=="B":
                T=12
                
            if T=="C":
                T=13    

            if T=="D":
                T=14
                
            if T=="E":
                T=15

            if T=="F":
                T=16
            
            a+=int(T)*16**(int(len(s)-(i+1)))
            print(a)

            
        self.tl.set(a)
        return
            
        
        




    



def main():
    p=program(Tk())
    mainloop()
    return
main()

