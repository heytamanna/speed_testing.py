from time import * # * lgane sy hme koi extra tym nhi lgana pdega yeh khud he sb chiz ko import kr dega
import random as r #isse hm multiple strings yani lines ko print krwa skte h



def mistake(partest,usertest):# yeh hmne ek fxn bnaya
    error =0
    for i in range(len(partest)):#kitne tym tk chlana h yeh paratest decide krega
        try :
            if partest[i] !=usertest[i]:
                error = error + 1
        
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed  = len(userinput)/ time_R
    return round(speed)
    
while True:
     
    ck =input("ready to test : yes /no : ")
    if ck == "yes":
        test =["Himachal Pradesh is an ode to nature's masterpiece.",
        "The beauty of Himachal Pradesh is in its simplicity and untouched landscapes","my name is tamanna i am from himachal"]
        test1 = r.choice(test) #isse hm kese ko ek string ko print krwa skte h
        print("  ***** typing speed *****  ")
        print(test1)
        print() #yeh ek line ka break dy dega ()agr hm isko empty shodegy to
        print()
        time_1 = time()
        testinput=input(" Enter : ")#isme hm user sy input lygy
        time_2 =time()

        print("Speed : ", speed_time(time_1,time_2,testinput) , " w/sec")
        print("Error : ", mistake(test1,testinput))
    elif ck =="no":
        
        print("THANK YOU")
        break
    else:
        
        print("WRONG INPUT")