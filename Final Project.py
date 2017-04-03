from tkinter import *
import sys
import serial
import time
import threading

   
# Function / Second loop that runs in the background thread to not block the UI thread
def test_loop(uiElements):
        ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	xonxoff=False,
	rtscts=False,
	dsrdtr=False
	#timeout=0
        )

        previous_sent_integer1 = 0
        previous_sent_integer2 = 0
        previous_sent_integer3 = 0
        previous_sent_integer4 = 0

        ser.flushInput() # flush the input buffer
        ser.flushOutput() # flush the output buffer

        while True:

                ### TRANSMIT MODE ###
                
                if uiElements.button1 == 1:

                        #ser.flushInput()
                        #ser.flushOutput()

                        if previous_sent_integer1 != uiElements.dataForPIC1: #write only distinct values
                                previous_sent_integer1 = uiElements.dataForPIC1

                                ser.write(bytes([0x82])) # send the START BYTE
                                ser.write(bytes([0x01])) # send the BUTTON BYTE (value = 1 for button 1)
                                ser.write(bytes([previous_sent_integer1])) # send the current VALUE BYTE
                  
                if uiElements.button2 == 1:

                        #ser.flushInput()
                        #ser.flushOutput()

                        if previous_sent_integer2 != uiElements.dataForPIC2: #write only distinct values
                                previous_sent_integer2 = uiElements.dataForPIC2

                                ser.write(bytes([0x82])) # send the START BYTE
                                ser.write(bytes([0x02])) # send the BUTTON BYTE (value = 2 for button 2)
                                ser.write(bytes([previous_sent_integer2])) # send the current VALUE BYTE
				  
                if uiElements.button3 == 1:

                        #ser.flushInput()
                        #ser.flushOutput()

                        if previous_sent_integer3 != uiElements.dataForPIC3: #write only distinct values
                                previous_sent_integer3 = uiElements.dataForPIC3

                                ser.write(bytes([0x82])) # send the START BYTE
                                ser.write(bytes([0x03])) # send the BUTTON BYTE (value = 3 for button 3)
                                ser.write(bytes([previous_sent_integer3])) # send the current VALUE BYTE
                        
                if uiElements.button4 == 1:

                        #ser.flushInput()
                        #ser.flushOutput()

                        if previous_sent_integer4 != uiElements.dataForPIC4: #write only distinct values
                                previous_sent_integer4 = uiElements.dataForPIC4

                                ser.write(bytes([0x82])) # send the START BYTE
                                ser.write(bytes([0x04])) # send the BUTTON BYTE (value = 4 for button 4)
                                ser.write(bytes([previous_sent_integer4])) # send the current VALUE BYTE




                ### RECEIVE MODE ###       

                if uiElements.button1 == 0 and uiElements.button2 == 0 and uiElements.button3 == 0 and uiElements.button4 == 0: # check that none of the sliders are in use
                        ser.flushInput()
                        ser.flushOutput()
             
                        ser.write(bytes([0x82])) # send the START BYTE
                        ser.write(bytes([0x05])) # send the BUTTON BYTE (value = 5 for button 1)
                        ser.write(bytes([previous_sent_integer1])) # send the current VALUE BYTE
                        
                        start = ser.read() # read the serial port
                        #print ("BYTE RECEIVED")
                        if start == (bytes([0x82])): # check if START BYTE is received
                                slider = ser.read() # read the serial port
                                #print ("BYTE RECEIVED")
                            
                                if slider == (bytes([0x05])): # check if BUTTON BYTE for SLIDER 1 is received
                                        pic_value1 = ser.read()
                                        #print ("BYTE RECEIVED")
                                        uiElements.selectedScaleValue1.set(int.from_bytes(pic_value1, byteorder='little'))

                        ser.flushInput()
                        ser.flushOutput()

                        ser.write(bytes([0x82])) # send the START BYTE
                        ser.write(bytes([0x06])) # send the BUTTON BYTE (value = 6 for button 2)
                        ser.write(bytes([previous_sent_integer2])) # send the current VALUE BYTE

                        start = ser.read() # read the serial port
                        #print ("BYTE RECEIVED")
                        if start == (bytes([0x82])): # check if START BYTE is received
                                slider = ser.read() # read the serial port
                                #print ("BYTE RECEIVED")
                            
                                if slider == (bytes([0x06])): # check if BUTTON BYTE for SLIDER 2 is received
                                        pic_value2 = ser.read()
                                        #print ("BYTE RECEIVED")
                                        uiElements.selectedScaleValue2.set(int.from_bytes(pic_value2, byteorder='little'))

                        ser.flushInput()
                        ser.flushOutput()

                        ser.write(bytes([0x82])) # send the START BYTE
                        ser.write(bytes([0x07])) # send the BUTTON BYTE (value = 7 for button 3)
                        ser.write(bytes([previous_sent_integer3])) # send the current VALUE BYTE

                        start = ser.read() # read the serial port
                        #print ("BYTE RECEIVED")
                        if start == (bytes([0x82])): # check if START BYTE is received
                                slider = ser.read() # read the serial port
                                #print ("BYTE RECEIVED")
                            
                                if slider == (bytes([0x07])): # check if BUTTON BYTE for SLIDER 3 is received
                                        pic_value3 = ser.read()
                                        #print ("BYTE RECEIVED")
                                        uiElements.selectedScaleValue3.set(int.from_bytes(pic_value3, byteorder='little'))

                        ser.flushInput()
                        ser.flushOutput()

                        ser.write(bytes([0x82])) # send the START BYTE
                        ser.write(bytes([0x08])) # send the BUTTON BYTE (value = 8 for button 4)
                        ser.write(bytes([previous_sent_integer4])) # send the current VALUE BYTE

                        start = ser.read() # read the serial port
                        #print ("BYTE RECEIVED")
                        if start == (bytes([0x82])): # check if START BYTE is received
                                slider = ser.read() # read the serial port
                                #print ("BYTE RECEIVED")
                            
                                if slider == (bytes([0x08])): # check if BUTTON BYTE for SLIDER 4 is received
                                        pic_value4 = ser.read()
                                        #print ("BYTE RECEIVED")
                                        uiElements.selectedScaleValue4.set(int.from_bytes(pic_value4, byteorder='little'))


class UIElements:
        def __init__(self):
                commonDefaultVar = 0
	
                self.root = Tk()
      
                self.selectedScaleValue1 = IntVar()
                self.selectedScaleValue2 = IntVar()
                self.selectedScaleValue3 = IntVar()
                self.selectedScaleValue4 = IntVar()
     
                self.root.geometry('500x500+100+0')
                self.root.title('Control Panel')
      
                # define SCALE 1
                scale = Scale(self.root, orient = HORIZONTAL, length = 400, width = 50, sliderlength = 20, from_ = 0, to = 31, tickinterval = 2, variable = self.selectedScaleValue1)
                scale.bind("<Button-1>", self.setButton1On)
                scale.bind("<ButtonRelease-1>", self.setButton1Off)
                scale.pack(anchor=CENTER)
                scale.set(commonDefaultVar)

                # define LABEL 1
                self.label = Label(self.root,fg='red',bg='yellow')
                self.label.pack()
                self.label.config(text = str(commonDefaultVar))

                self.button1 = 0
                self.dataForPIC1 = 0

                # define SCALE 2
                scale2 = Scale(self.root, orient = HORIZONTAL, length = 400, width = 50, sliderlength = 20, from_ = 0, to = 31, tickinterval = 2, variable = self.selectedScaleValue2)
                scale2.bind("<Button-1>", self.setButton2On)
                scale2.bind("<ButtonRelease-1>", self.setButton2Off)
                scale2.pack(anchor=CENTER)
                scale2.set(commonDefaultVar)

                # define LABEL 2
                self.label2 = Label(self.root,fg='red',bg='yellow')
                self.label2.pack()
                self.label2.config(text = str(commonDefaultVar))

                self.button2 = 0
                self.dataForPIC2 = 0

                # define SCALE 3
                scale3 = Scale(self.root, orient = HORIZONTAL, length = 400, width = 50, sliderlength = 20, from_ = 0, to = 31, tickinterval = 2, variable = self.selectedScaleValue3)
                scale3.bind("<Button-1>", self.setButton3On)
                scale3.bind("<ButtonRelease-1>", self.setButton3Off)
                scale3.pack(anchor=CENTER)
                scale3.set(commonDefaultVar)

                # define LABEL 3
                self.label3 = Label(self.root,fg='red',bg='yellow')
                self.label3.pack()
                self.label3.config(text = str(commonDefaultVar))

                self.button3 = 0
                self.dataForPIC3 = 0

                # define SCALE 4
                scale4 = Scale(self.root, orient = HORIZONTAL, length = 400, width = 50, sliderlength = 20, from_ = 0, to = 31, tickinterval = 2, variable = self.selectedScaleValue4)
                scale4.bind("<Button-1>", self.setButton4On)
                scale4.bind("<ButtonRelease-1>", self.setButton4Off)
                scale4.pack(anchor=CENTER)
                scale4.set(commonDefaultVar)

                # define LABEL 4
                self.label4 = Label(self.root,fg='red',bg='yellow')
                self.label4.pack()
                self.label4.config(text = str(commonDefaultVar))

                self.button4 = 0
                self.dataForPIC4 = 0

                def sendScaleValue1(a,b,c):
                        self.dataForPIC1 = self.selectedScaleValue1.get()
                        self.label.config(text = str(self.selectedScaleValue1.get()))

                self.selectedScaleValue1.trace('w', sendScaleValue1)

                def sendScaleValue2(a,b,c):
                        self.dataForPIC2 = self.selectedScaleValue2.get()
                        self.label2.config(text = str(self.selectedScaleValue2.get()))

                self.selectedScaleValue2.trace('w', sendScaleValue2)
	  
                def sendScaleValue3(a,b,c):
                        self.dataForPIC3 = self.selectedScaleValue3.get()
                        self.label3.config(text = str(self.selectedScaleValue3.get()))

                self.selectedScaleValue3.trace('w', sendScaleValue3)
	  
                def sendScaleValue4(a,b,c):
                        self.dataForPIC4 = self.selectedScaleValue4.get()
                        self.label4.config(text = str(self.selectedScaleValue4.get()))

                self.selectedScaleValue4.trace('w', sendScaleValue4)

        def setButton1On(self, event):  #detect if scale button1 is pressed
                self.button1 = 1
      
        def setButton1Off(self, event):  #detect if scale button1 is released
                self.button1 = 0

        def setButton2On(self, event):  #detect if scale button2 is pressed
                self.button2 = 1
      
        def setButton2Off(self, event):  #detect if scale button2 is released
                self.button2 = 0
	  
        def setButton3On(self, event):  #detect if scale button3 is pressed
                self.button3 = 1
      
        def setButton3Off(self, event):  #detect if scale button3 is released
                self.button3 = 0

        def setButton4On(self, event):  #detect if scale button4 is pressed
                self.button4 = 1
      
        def setButton4Off(self, event):  #detect if scale button4 is released
                self.button4 = 0
           

# Entry point in the program
if __name__ == "__main__":
        # Build the Scale object
        uiElements = UIElements()
        # Start background thread to run second loop
        thread = threading.Thread(target = test_loop, args=(uiElements,))
        thread.daemon = True
        thread.start()
        # Start loop in main thread
        uiElements.root.mainloop()



   
	
