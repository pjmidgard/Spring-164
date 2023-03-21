from time import time
cvf=0
import os
import binascii
namez = input("c  for compress or e for extract: ")
#@Author Jurijus Pacalovas
class compression:
    def cryptograpy_compression(self):
                

        
            
    
                self.name = "@Author: Jurijus Pacalovas"
                print(self.name)
                if namez=="e":
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                           print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit                    
                    namea=""
                    namem=""
                    namema="?"
                   
                    blockw=5
                    blockw1=4
                    assxw=0
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=2
                    block2=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()
                        import paq
                        data= paq.decompress(data)
                        s=str(data)
                        
            
                  
                        lenf1=len(data)
                        lenf5=len(data)
                        
            
                  
                        
                        if lenf1>(2**32)-1:
                            print("This file is too big");
                            raise SystemExit
                        if lenf1==0:
                            
                            raise SystemExit

                        assx=0
                        qqqwz=0
                        
            
                   
                        while assx<10:
                       
                            aas1=0
                            a1=0

                
           
                    
                            cvf=cvf+1
                            
                
                    
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

      
                                    
                                    
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                    
                                
                                    
                                    if countraz==1:

                                        
                                        
                                        

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                block3=0
                                sda3=""
                                
                                
                                
                                   
                                    
                                while block3<lenf2:
                                    	e4=sda2[block3:block3+102400]
                                    	shake_reverse=0
                                    	e6=e4
                                    	
                                    	d2=int(e6,2)
                                    	d3=d2
                                    	
                                    	if len(e4)==102400:
	                                    	
		                                  
		                                    
		                                    	
		                                            
		                                            if d2>=((2**(102400*8))-(2**89700)):
		                                            	d2=d2-(2**(102400*8))
		                                            d2=d2+(2**89700)
		                                            
		                                            
		                                     
                                                                      	
                                        		
                                        	
                                    	long_size=len(e4)
                                    	C="0"+str(long_size)+"b"
                                    	e3=format(d2,C)
                                    	#print(e3)
    
                                    	
                                    	sda3+=e3
                                    	block3+=102400
                                    	
                                    	
                                    	
                                    	
                                    	
                               
                                       
                               
                                
                                                     		 
                                sda2=sda3
                                n = int(sda3, 2)
                                qqwslenf=len(sda3)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                                jl=binascii.unhexlify(qqwslenf % n)
                                sssssw=len(jl)
                                data=jl
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                                assxw=assxw+1
                                if assxw==1:
                                         assx=10
                                         if assx==10:
                                             f2.write(jl)
                                             x2 = time()
                                             x3=x2-x
                                             return print(x3)
                

                           
    
            
    def cryptograpy_unpack(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        if os.path.exists(name):
                           print('Path is exists!')
                        else:
                            print('Path is not exists!')
                            raise SystemExit
                        namea=""
                        namem=""
                        namema="?"
                        block2=0
                        
                        count1=12
                        count2=0
                        count3=0
                        count4=1
                        count6=0
                        assxw1=0
                        Times_of_compression=0
              

                        assxw=0
                        blockw=5
                        blockw1=4
                        nameas=name
                        
                        nac=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
                        cvf=2
                        cvf1=0
                        s=""
                        e2=0
                        e3=2
                        e4=""
                        c=2
                        sw=2
                        elw=0
                       
                        sda3=""

                        sscvf=0
                        
                        qqqqwzl=0

                        block=0

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()
                        
                            s=str(data)
                            lenf1=len(data)
                            lenf5=len(data)
                            
                            if lenf1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            if lenf1==0:
                            	raise SystemExit
                            
                            assx=0
                            
                            qqqwz=0
                            while assx<10:
                          
                                aas1=0
                                a1=0
                                
                                cvf=cvf+1
                                
                                countraz=countraz+1

                                with open(nameas, "ab") as f2:
                                    if countraz==1:
                                        sda=bin(int(binascii.hexlify(data),16))[2:]
                                        lenf=len(sda)
                                        
                                        lenf1=len(data) 
                                        xc=(lenf1*8)-lenf
                                        z=0
                                        if xc!=0:
                                            while z<xc:
                                                sda="0"+sda
                                                z=z+1
                                        sda2=sda
                                        lenf3=len(sda2)
                                    lenf2=len(sda2)  
                                    block3=0
                                    sda3=""
                                    sda5=""
                                    sda8=""
                                    sda4=""
                                    
                                    count3+=1
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################


                                    
                                    while block3<lenf2:
                                        count4+=1
                                        count2+=1
                                        if count1<(2**32)-1:
                                            count1+=1
                                        e4=sda2[block3:block3+8]
                                        e6=e4
                                        e10=e4[:3]+e4[3:5][::-1]+e4[5:]
                                        e4=e10[::-1]
                                        if count4==5:
                                            count4=0
                                        if e4[0:2]=="01":
                                            if count4==4:
                                                e4=e4[1:]
                                            elif count4!=4:
                                                e4=e4[3:]
                                            if count4==4:
                                                sda3+="1"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="11"+e4+e4[2:3]
                                            block3+=8
                                        elif e4[0:2]=="10":
                                            if count4==4:
                                                e4=e4[1:]
                                            elif count4!=4:
                                                e4=e4[2:]
                                            if count4==4:
                                                sda3+="0"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="10"+e4
                                            block3+=8
                                        elif e4[0:2]=="00":
                                            if count4==4:
                                                e4=e4[1:]
                                            elif count4!=4:
                                                e4=e4[2:]
                                            if count4==4:
                                                sda3+="1"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="01"+e4
                                            block3+=8
                                        elif e4[0:2]=="11":
                                            if count4==4:
                                                e4=e4[1:]
                                            elif count4!=4:
                                                e4=e4[2:]
                                            if count4==4:
                                                sda3+="0"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="00"+e4
                                            block3+=8
                                    	
             
                                    
                                   
                                    #print(e5)
                                    
          	
                                    #print(len(sda3))
                                    
                                    sda2=sda3
                                    assxw=assxw+1
                                    if assxw==50:
                                        #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32# 
                                        block3=0
                                        assxw=0
                                       
                                        varations=-1
                                        combinations=-1
                                        Save_V=""
                                        Save=""
                                        V=""
                                        while varations!=256:
                                            block3=0
                                            varations+=1
                                            Times=0
                                            while block3<lenf2:
                                                e4=sda3[block3:block3+8]
                                                V=format(varations,'08b')
                                                if e4==V and Times==0:
                                                    Save_V=Save_V+e4
                                                    combinations+=1
                                                    Times=1
                                                block3+=8
	                                        
                                        		                                         
	                                        		
	                                        
                                       	
                                        	



                                        Save=format(combinations,'08b')
                                        
                                        Save=Save+Save_V
                                        
                                        
                                        #print(len(Save))
                                        sda4=""

                                        Save_Long=len(Save)
                                        combinations1=combinations+1
                                        #print(combinations)
                                       
                                        if combinations>127:
                                            sda4="11111111"+sda3
                                        else:
                                            G=bin(combinations)[2:]
                                            F=len(G)
                                            C="0"+str(F)+"b"
                                            #print(C)
                                            Bits=0
                                            block3=0
                                            sda4=""
                                            lenf3=len(sda3)
                                            while block3<lenf3:
                                                e4=sda3[block3:block3+8]
                                                e5=""
                                                
                                                Bits1=0
                                                Bits=0
                                                while e4!=e5:
                                                    V3=format(Bits,C)
                                                    e5=Save_V[Bits1:Bits1+8]
                                                    Bits1+=8
                                                    Bits+=1
                                                    
                                                if e4==e5:
                                                    sda4=sda4+V3
                                                    block3+=8
                                                    #print(block3)

                                        sda4="1"+sda4
                                        lenf=len(sda4)
                                        add_bits=""
                                        count_bits=8-lenf%8
                                        z=0
                                        if count_bits!=0:
                                                if count_bits!=8:
                                                    while z<count_bits:
                                                        add_bits="0"+add_bits
                                                        z=z+1
                                        sda4=add_bits+sda4
                                                
                                            
                                        sda4=Save+sda4
                                        Save=""
                                        Save_V=""
                                        Times_of_compression+=1
                                        if  len(sda4)>len(sda2):
                                        	sda4="11111111"+sda3                                        
                                        if len(sda4)<=496 or Times_of_compression==65535:
                                            Times_count=format(Times_of_compression,'016b')
                                            count_save=format(count4,'08b')
                                            sda4=count_save+Times_count+sda4                        
                                            assxw1=1
 
                                        sda2=sda4
                                        #print(len(sda4))

                                        
                                        
                                            
                                            	        
                                        n = int(sda4, 2)
                                                                                                    
                                            
                                        qqwslenf=len(sda4)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                         
                                        jl=binascii.unhexlify(qqwslenf % n)
          
                                                          
                                 
                                             
                                        #print(len(jl))
                                        
                                        
           

                      
                                        
                                  
                              
                                 
                                        
                                        
                                        #print(assxw1)
                                        
                                        if assxw1==1:
                                    
                                            assx=10
                                            if assx==10:
                                                   

                                                   
                                               
                                                   
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)        
                                                                                  														    
                                         



   
            
                     

d=compression()


  
xw=d.cryptograpy_compression()
print(xw)


xw1=d.cryptograpy_unpack()
print(xw1)
