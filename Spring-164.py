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
                    Times_of_compression1=0
                    blockw=5
                    blockw1=4
                    assxw1=0
                    assxw2=0
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

                    Times_of_compression=0
                    
                    countraz=0
                    assxw=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    count4=1
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=2
                    block2=0

                    count_time_of_copression=0

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

                                    if count_time_of_copression==0:
                                        sda9=sda
                                        count4=int(sda[:8],2)
                                        sda=sda[8:]
                                        #print(count4)
                                        Times_of_compression=int(sda[:16],2)
                                        sda=sda[16:]
                                        
                                        #print(Times_of_compression)
                                        count_time_of_copression=1
                                    
                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                block3=0
                                sda3=""

                                
                                Save=sda2[:8]
                                sda2=sda2[8:]
                               
                                Tranformation=0
                                combinations=int(Save,2)
                                #print(combinations)
                                
                                if combinations==255:
                                    Tranformation=1
                                    
                                if Tranformation==0:
                                    combinations1=combinations+1
                                    combinations1_bytes=combinations1*8
                                    Save_V=sda2[:combinations1_bytes]
                                    sda2=sda2[combinations1_bytes:]


                                    size_data3=sda2
                                    if size_data3[0:9]=="000000001":
                                        sda2=sda2[9:]
                                    elif size_data3[0:8]=="00000001":
                                        sda2=sda2[8:]
                                    elif size_data3[0:7]=="0000001":
                                        sda2=sda2[7:]
                                    elif size_data3[0:6]=="000001":
                                        sda2=sda2[6:]
                                    elif size_data3[0:5]=="00001":
                                        sda2=sda2[5:]
                                    elif size_data3[0:4]=="0001":
                                        sda2=sda2[4:]
                                    elif size_data3[0:3]=="001":
                                        sda2=sda2[3:]
                                    elif size_data3[0:2]=="01":
                                        sda2=sda2[2:]
                                    elif size_data3[0:1]=="1":
                                        sda2=sda2[1:]


                                
                                sda3=sda2
                                

                                if Tranformation==1:

                                            sda4=sda3
                                            #print(sda4)
                                if Tranformation==0:
                                            G=bin(combinations)[2:]
                                            F=len(G)
                                            C="0"+str(F)+"b"
                                            #print(C)
                                            Bits=0
                                            block3=0
                                            sda4=""
                                            lenf3=len(sda3)
                                            while block3<lenf3:
                                                e4=sda3[block3:block3+F]
                                                e5=""
                                                
                                                Bits1=0
                                                Bits=0
                                                while e4!=e5:
                                                    
                                                    e5=Save_V[Bits1:Bits1+8]
                                                    Bits1+=8
                                                    Bits+=1
                                                    
                                                if e4==e5:
                                                    sda4=sda4+e5
                                                    block3+=F
                                    
                                
                                   
                                    
                                Times_of_compression1+=1
                                assxw=assxw+1
                                assxw1=0
                                sda2=sda4
                                #print(sda2)
                                if assxw==1:
                                            assxw1=0
                                            #print(count4)
                                            
                                            while assxw1!=50:
                                                    assxw=0
                                                    sda3=""
                                                    sda5=""
                                                    sda8=""
                                                    sda4=""
                                                    block3=0
                                                    lenf2=len(sda2)
                                                 
                                                   
                                                    count4=1
                                                    while block3<lenf2:
                                                        count4+=1
                                                        e5=sda2[block3:block3+8]


                                                        Reverse=0
                                                        e11=""
                                                        
                                                        #print(e5)

                                                        while e5!=e11:

                                                            if Reverse==256:
                                                                Reverse=0

                                                            e4=format(Reverse,'08b')
                                                            
                                                            e6=e4
                                                            e10=e4[:3]+e4[3:5][::-1]+e4[5:]
                                                            e4=e10[::-1]
                                                            e14=e4
                                                            #print(count4)

                                                            
                                                            
                                                            if e4[0:2]=="01":
                                                                if count4==4:
                                                                    e4=e4[2:]
                                                                elif count4!=4:
                                                                    e4=e4[3:]
                                                                if count4==4:
                                                                    e7="11"+e4
                                                                
                                                                elif count4!=4:
                                                                    e7="11"+e4+e14[2:3]
                                                                    #print(len(e4))
                                                                
                                                            elif e4[0:2]=="10":
                                                                if count4==4:
                                                                    e4=e4[2:]
                                                                elif count4!=4:
                                                                    e4=e4[2:]
                                                                if count4==4:
                                                                    e7="00"+e4
                                                                
                                                                elif count4!=4:
                                                                    e7="10"+e4
                                                            
                                                            elif e4[0:2]=="00":
                                                                if count4==4:
                                                                    e4=e4[2:]
                                                                elif count4!=4:
                                                                    e4=e4[2:]
                                                                if count4==4:
                                                                    e7="10"+e4
                                                                    
                                                                elif count4!=4:
                                                                    e7="01"+e4
                                                            
                                                            elif e4[0:2]=="11":
                                                                if count4==4:
                                                                    e4=e4[2:]
                                                                elif count4!=4:
                                                                    e4=e4[2:]
                                                                if count4==4:
                                                                    e7="01"+e4
                                                                
                                                                elif count4!=4:
                                                                    e7="00"+e4
                                                                
                                                            e11=e7
                                                            #print(e11)
                                                            #if len(e11)!=8:
                                                                #print(e11)

                                                        
                                                            #print(e12)
                                                            Reverse+=1
                                                            #print(e11)
                                                            
                                                            #print(e11)
                                                        sda3+=e6
                                                       
                                                        #print(count4)
                                                        block3+=8
	                                           
	                                            #print(e5)
	                                            
	                        
	                                            #print(len(sda3))
                                                    if count4==1:
                                                           count4=4	                                            
	                                              
	                                            #print(sda2)
	                                            
                                                    sda2=sda3
                                                    #print(sda2)
                                                    assxw1=assxw1+1
                                                    n = int(sda3, 2)
                                                    qqwslenf=len(sda3)
                                                    qqwslenf=(qqwslenf/8)*2
                                                    qqwslenf=str(qqwslenf)
                                                    qqwslenf="%0"+qqwslenf+"x"
                                                    jl=binascii.unhexlify(qqwslenf % n)
                                            #print(jl)

                                            #print(count4)
                                            if assxw1==50:
                                                    if Times_of_compression==Times_of_compression1:
                                                        assxw2=1
                                                    if assxw2==1:
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
                                    #print(count4)
                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                    #print(sda2)
                                  
                                   
                                    count4=1
                                    while block3<lenf2:
                                        count4+=1
                                        count2+=1
                                        if count1<(2**32)-1:
                                            count1+=1
                                        e4=sda2[block3:block3+8]
                                        e6=e4
                                        e10=e4[:3]+e4[3:5][::-1]+e4[5:]
                                        e4=e10[::-1]
                                        e14=e4
                                        if count4==5:
                                            count4=0
                                        if e4[0:2]=="01":
                                            if count4==4:
                                                e4=e4[2:]
                                            elif count4!=4:
                                                e4=e4[3:]
                                            if count4==4:
                                                sda3+="11"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="11"+e4+e14[2:3]
                                            block3+=8
                                        elif e4[0:2]=="10":
                                            if count4==4:
                                                e4=e4[2:]
                                            elif count4!=4:
                                                e4=e4[2:]
                                            if count4==4:
                                                sda3+="00"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="10"+e4
                                            block3+=8
                                        elif e4[0:2]=="00":
                                            if count4==4:
                                                e4=e4[2:]
                                            elif count4!=4:
                                                e4=e4[2:]
                                            if count4==4:
                                                sda3+="10"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="01"+e4
                                            block3+=8
                                        elif e4[0:2]=="11":
                                            if count4==4:
                                                e4=e4[2:]
                                            elif count4!=4:
                                                e4=e4[2:]
                                            if count4==4:
                                                sda3+="01"+e4
                                                count4=1
                                            elif count4!=4:
                                                sda3+="00"+e4
                                            block3+=8
                                        #print(len(sda3))
                                    	
             
                                    
                                   
                                    #print(count4)
                                    
          	
                                    #print(sda3)
                                    #os.system("pause")
                                    
                                    sda2=sda3
                                    assxw=assxw+1
                                    if assxw==50:
                                        #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(sda2)
                                        #os.system("pause")
                                        
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
                                        
                                        
                                        #print(len(sda3))
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

                                        #print(len(sda4))
                                        if len(sda4)>len(sda2) or Times_of_compression==65535:
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
