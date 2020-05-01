
from tkinter import *
import serial, time
import os
import ast
import json
from tkinter import ttk
import serial.tools.list_ports

#######Possibilitar Ângulos negativos
####### Guardar posição geral num txt
####### Possibilitar zeramento
####### Guardar filtros txt


FONT = ("Verdana" , 10)




def load_Memory():
        #global Sensor_Dict
        memory = {}
        if os.stat('./memory.txt').st_size == 0:
            memory = {}
        else:
            f = open('./memory.txt','r').read()
            memory = ast.literal_eval(f)
            ##Sensor_Dict = json.load(f)    
            print(memory)

        return memory



def save_Memory(memory):
    with open('./memory.txt','w') as file:
        file.write(json.dumps(memory))
    file.close()
    




class Application(Frame):

    def __init__(self,master):

        Frame.__init__(self,master)
        self.grid()
        self.Memory = load_Memory()
        self.Pos = self.Memory['Pos']
        self.create_widgets()

        self.value = 1
        
        

        
    def create_widgets(self):
        #Address Label
        #self.instruction = ttk.Label(self,text = "Enviar para posição:", font = FONT)
        #self.instruction.grid(row = 1, column =7, columnspan = 1, sticky = W)


        #Communication button
        self.send_button = ttk.Button(self, text = "Conectar" ,command = self.Establish_COM)
        self.send_button.grid(row = 1, column = 0, sticky = W)

        self.label1 = ttk.Label(self, text = "Info:", font = 'Helvetica 12 bold'). grid(row = 3, column = 0, sticky =W)
        
        
        #COM Label 
        self.COMLabel = ttk.Label (self, text = "Controlador para Focador Automático", font = "Helvetica 16 bold")
        self.COMLabel.grid(row = 0, column =0, columnspan =5, sticky = W)


        self.autolabel = ttk.Label(self, text = "Atuação Automática", font = 'helvetica 10 bold').grid(row = 8, column = 3, sticky = W)
        #Auto Label 
        self.AutoLabel = ttk.Label (self, text = "Ir para:", font = FONT)
        self.AutoLabel.grid(row = 9, column =3, columnspan = 1, sticky = W)        

        self.address = ttk.Entry(self)
        self.address.grid(row = 10, column = 3, columnspan = 2 ,sticky = W)

         #Send button
        self.send_button = ttk.Button(self, text = "Rodar", state = 'disabled' , command = self.Arduino_COM)
        self.send_button.grid(row = 11, column = 3, sticky = W)


        #Go to zero
        self.gotozero = ttk.Button(self, text = "Zerar", state = 'disabled' ,command = self.Go_to_zero)
        self.gotozero.grid(row = 11, column = 3, sticky = E)

        

        #Val Label
        self.Var1Label = ttk.Label (self, text = "Incremento: ", font = FONT)
        self.Var1Label.grid(row = 4, column =3, columnspan = 2, sticky = W)

        #Val Label
        self.VarLabel = ttk.Label (self, text = "1", font = ('Helvetica 10 bold '))
        self.VarLabel.grid(row = 4, column =3, columnspan = 1, sticky = E)
        
        #COM Entry
        #self.COM = ttk.Entry(self)
        #self.COM.grid(row = 1, column = 0, sticky = W)
        #Address Entry
        

        
        

    

        
        #COM Label 
        self.IncLabel = ttk.Label (self, text = "Atuação manual", font = 'helvetica 10 bold')
        self.IncLabel.grid(row = 2, column =3, columnspan = 2, sticky = W)

        #COM Label 
##        self.ManLabel = ttk.Label (self, text = "Modo Manual:", font = FONT)
##        self.ManLabel.grid(row = 0, column =3, columnspan = 2, sticky = W)
            
        ####################SEPARADORES 
        for i in range(15):
            self.blkLabel = ttk.Label (self, text = "  |  ", font = FONT)
            self.blkLabel.grid(row = i+1, column =2, columnspan = 1, sticky = E)

        for i in range(8):
            self.blkLabel = ttk.Label (self, text = "    ", font = FONT)
            self.blkLabel.grid(row = i, column =6, columnspan = 1, sticky = W)

        


        ###############################################

        #Continuous spin
        self.RightBtnLbl = ttk.Label (self, text = "Rotação contínua: ", font = ('Helvetica 10'))
        self.RightBtnLbl.grid(row = 6, column =3, columnspan = 3, sticky = W)

        self.right_button = ttk.Button(self, text = "--->",  state = 'disabled')
        self.right_button.grid(row = 7, column = 3, sticky = E)

        self.left_button = ttk.Button(self, text = "<---",  state = 'disabled')
        self.left_button.grid(row = 7, column = 3, sticky = W)

        self.right_button.bind("<ButtonPress>",  self.spin_right)
        self.right_button.bind("<ButtonRelease>", self.stop_spin)

        self.left_button.bind("<ButtonPress>", self.spin_left)
        self.left_button.bind("<ButtonRelease>", self.stop_spin)


        #Inc button
        self.inc_button = ttk.Button(self, text = "->",  state = 'disabled',command = self.Arduino_COM_inc)
        self.inc_button.grid(row = 3, column = 3, sticky = E)

        #Dec button
        self.dec_button = ttk.Button(self, text = "<-", state = 'disabled', command = self.Arduino_COM_dec)
        self.dec_button.grid(row = 3, column = 3, sticky = W)
        

        #IncVar button
        self.incvar_button = ttk.Button(self, text = "+", state = 'disabled', command = self.inc_var)
        self.incvar_button.grid(row = 5, column = 3, sticky = E)

        #DecVar button
        self.decvar_button = ttk.Button(self, text = "-", state = 'disabled', command = self.dec_var)
        self.decvar_button.grid(row = 5, column = 3, sticky = W)        

       

        #s1 = StringVar()
        #s1.set(str(self.Pos))

        self.VarposLabel = ttk.Label (self, text = "Posição: ", font = ('Helvetica 10'))
        self.VarposLabel.grid(row = 6, column =0, columnspan = 3, sticky = W)

        self.ConnLabel = ttk.Label (self, text= "Conexão: False" , font = FONT)
        self.ConnLabel.grid(row = 4, column = 0, columnspan = 2,sticky = W)

        self.VarposLabel = ttk.Label (self, text = str(self.Pos) + 'º', font = ("Verdana", 12))
        self.VarposLabel.grid(row = 6, column =1, columnspan = 1, sticky = W)
        
##        #Text box
##        self.text = Text(self, width = 35, height = 5, wrap = WORD)
##        self.text.grid(row = 3, column =0, columnspan = 2, sticky = W)


        ####################SEPARADORES 
       

        for i in range(14):
            self.blkLabel = ttk.Label (self, text = "  |  ", font = FONT)
            self.blkLabel.grid(row = i, column =8, columnspan = 1, sticky = W)



        FilterList= ['Alpha','OIII', 'SII','IR','R','G','B']

        self.label = ttk.Label(self, text = 'Atribuir posição atual a filtro ', font = FONT).grid(row = 11, column = 9, columnspan = 2, sticky = W)

        self.CB = ttk.Combobox(self, values = FilterList)
        self.CB.grid(row = 10, column = 9, columnspan = 1, sticky = W)


        self.label = ttk.Label(self, text = 'Gestor de Filtros:', font = ("Helvetica, 14")).grid(row = 0, column = 9, columnspan = 2, sticky = W)


        self.b1 = ttk.Button(self, text = "Ir para filtro" , state = 'disabled', command = self.Arduino_COM_filter)
        self.b1.grid(row = 10, column = 10, sticky = W)
        

        for filters in FilterList:
            
            self.label = ttk.Label(self, text = filters + ':  ' , font = "Helvetica 10 bold")

            self.label.grid(row = FilterList.index(filters)+2 , column = 9, sticky = W)
        
            self.label = ttk.Label(self, text = self.Memory[filters])
            self.label.grid(row = FilterList.index(filters)+2 , column = 10, sticky = W)
    
        self. button_filter = ttk.Button(self, text = 'Atribuir', state = 'disabled' , command = self.set_filter)
        self.button_filter.grid(row = 12, column = 9, sticky = W)

        
    def set_filter(self):
        try:
            to_change = self.CB.get()
        except:
            print("No filter selected")


        self.Memory[self.CB.get()] = self.Pos
        save_Memory(self.Memory)
        self.update()


    def stop_spin(self,event):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        msg = "Stop\n"       
        print("Sending: " + msg)
       
        self.ser.write(msg.encode())

        time.sleep(0.1)

        readOut = self.ser.readline().decode()

    
        print ("Arduino turned: "+  str(readOut)+ " degrees")
        if(str(readOut.rstrip())!=""):
            pos = float(self.Pos) + float(readOut.rstrip())
            self.Memory['Pos']= str(pos)
            save_Memory(self.Memory)
            self.update()                
        else:
            print("Arduino did not move")

    def spin_left(self,event):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()        
        msg = "Left\n"       
        print("Sending: " + msg)
       
        self.ser.write(msg.encode())

        # time.sleep(1)

        # readOut = self.ser.readline().decode()

        # time.sleep(0.1)
                      

    def spin_right(self,event):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()        
        msg = "Right\n"       
        print("Sending: " + msg)
        self.ser.write(msg.encode())
        # time.sleep(1)
        # readOut = self.ser.readline().decode()
        # time.sleep(0.1)
                 

    def Go_to_zero(self):

        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        msg = "Zero\n"       
        print("Sending: " + msg)
        self.ser.write(msg.encode())
        self.Memory['Pos']= '0'
        save_Memory(self.Memory)
        self.update()


    def inc_var(self):
        #global value
        self.value+=1
        #self.var.set(str(value))
        self.VarLabel.configure(text = str(self.value))

        
    def dec_var(self):
        #global value
        self.value-=1
        #self.var.set(str(value))
        self.VarLabel.configure(text = str(self.value))



    def Establish_COM(self):
        #COMPort = self.COM.get()
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
                print(p[0])
                print(p[1])
                if (p[1] == 'USB2.0-Serial'):
                            
                        COMPort = p[0]
        try:
            
            self.ser = serial.Serial(p[0], 9600 , timeout = 1)
            if(self.ser):
                self.inc_button['state'] = 'normal'
                self.dec_button['state'] = 'normal'
                self.incvar_button['state'] = 'normal'
                self.decvar_button['state'] = 'normal'
                self.send_button['state'] = 'normal'
                self.gotozero['state'] = 'normal'
                self. button_filter['state'] = 'normal'
                self.b1['state'] = 'normal'
                self.right_button['state'] = 'normal'
                self.left_button['state'] = 'normal'
                print("Communication Established!!")
                self.update()
                
        except:
            print("Communication Failed!!")
            pass
        

    def Arduino_COM_filter(self):
        
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        filt = self.CB.get() 
        print("Sending to position: " + self.Memory[filt] + ' para filtro: ' + filt)
        #print("FIlter value is: ", filt)
        commandToSend = str(int(self.Memory[filt]) - int(self.Pos))
        msg = commandToSend           
        self.ser.write(msg.encode())
        time.sleep(1)
        readOut = self.ser.readline().decode('ascii')
        time.sleep(0.1)
        print ("Arduino Received: ",  readOut)
        #val = int(self.Pos)+ int(readOut)
        self.Pos= str(self.Memory[filt])
        self.Memory['Pos'] = self.Pos
        #self.ser.reset_output_buffer() #flush the buffer
        save_Memory(self.Memory)
        self.update()




    def Arduino_COM(self):
        
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()      
        commandToSend = str(float(self.address.get()) - float(self.Pos))
        msg = str(commandToSend)          
        self.ser.write(msg.encode())
        time.sleep(1)
        readOut = self.ser.readline().decode('ascii')
        time.sleep(0.1)
        val = float(self.Pos)+ float(msg)
        self.Pos= str(val)
        self.Memory['Pos'] = self.Pos
        save_Memory(self.Memory)
        self.update()

        
    def Arduino_COM_inc(self):
        
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        commandToSend = self.address.get()
        msg = str(self.value)          
        self.ser.write(msg.encode())
        time.sleep(1)
        readOut = self.ser.readline().decode('ascii')
        time.sleep(0.1)
        val = float(self.Pos)+ float(msg)
        self.Pos= str(val)
        self.Memory['Pos'] = self.Pos
        save_Memory(self.Memory)
        self.update()
        
    def Arduino_COM_dec(self):
        
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()
        commandToSend = self.address.get()
        msg = str(0-self.value)          
        self.ser.write(msg.encode())
        time.sleep(1)
        readOut = self.ser.readline().decode('ascii')
        time.sleep(0.1)
        val = float(self.Pos)+ float(msg)
        self.Pos= str(val)
        self.Memory['Pos'] = self.Pos
        save_Memory(self.Memory)
        self.update()


    def update(self):

        FilterList= ['Alpha','OIII', 'SII','IR','R','G','B']
        self.Memory = load_Memory()
        self.Pos = self.Memory['Pos']
        self.VarposLabel.configure(text = str(self.Pos)  + 'º')


        for filters in FilterList:
            self.label = ttk.Label(self, text = self.Memory[filters])
            self.label.grid(row = FilterList.index(filters)+2 , column = 10, sticky = W)

        self.ConnLabel.configure(text = 'Conexão: ' + str(self.ser.isOpen()) + ' ')
#RUN

root = Tk()



root.geometry("800x350")
root.title("Focador Automático beta")
app = Application (root)

root.mainloop()
            
