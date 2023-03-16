from time import time
cvf=0
import os
import binascii
namez = input("ul or for compress cl for extract for compress ")
#@Author Jurijus pacalovas
class compression:
    def cryptograpy_compression(self):
                

        
            
    
                self.name = "Written: Jurijus pacalovas"
                if namez=="ul":
                    name = input("What is name of file? ")
                    namea="file.WhiteHall"
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
                    if namez=="cl":
                        name = input("What is name of file? ")
                        namea="file.WhiteHall"
                        namem=""
                        namema="?"
                        block2=0
                        
                        count1=12
                        count2=0
                        count3=0
                        count4=0
              

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
                                   

                                    
                                    while block3<lenf2:
                                    	    count4+=1
                                    	    count2+=1
                                    	    if count1<(2**8)-1:
                                    	    	count1+=1
                                    	    e4=sda2[block3:block3+8]
                                    	    e6=e4
                                    	    
                                    	  
                                    	    	
                                    	    
                                    	   
                                    	    e4=e4[0:2][::-1]+e4[:2]+e4[2:]
                                    	    e4=e4[0:8]
                                    	    #print(e4)
                                    	    #print(s1)
                                    	    #print(s2)
                                    	    e3=format(count4,"016b") 
                                    	    e3=e3[0:4] 
                                    	    #print(e3)
                                    	    
                                    	    if count4==((2**16)-1):
                                    	    	count4=0
      
                                    	    if e4[0:4]==e3 and len(e4)==8 and count1<2**8 and count2<2**8:
                                    	    	e3="0"+e4[4:]
                                    	    	sda3+=e3
                                    	    	block3+=8
                                    	    	#print(e3)
                                    	    elif len(e4)!=1024:
                                    	    	sda3+=e6
                                    	    	block3+=8
                                    	

                                              
                                    e5=format(count1,"08b")
                                    #print(e5)
                                    count1=0
                                    count2=0
                                    count4=0
                                    sda3="1"+sda3
                                    lenf=len(sda3)
                                    add_bits=""
                                    count_bits=8-lenf%8
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=8:
                                            while z<count_bits:
                                            	       add_bits="0"+add_bits
                                            	       z=z+1
                                    sda3=add_bits+sda3                 	
                                    sda3=e5+sda3 
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
                                    if assxw==100:
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
