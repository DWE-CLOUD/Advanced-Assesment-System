import ftplib
from nltk.tokenize import*
import os
l1={"pwd":"awsd","lgn":"aodeveloper@outlook.com"}
l2=[1233]
opt=[]
#$$$$$$$2662892922627628728783674654641136637636746746579703999055
def helper()
    #import PyAudio

    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")


        try:
            s_in = r.recognize_google(audio_text)

            print("Text: " + r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")
print("Advanced Test Systems :: By Akshit Ohri")
print("")
input_1=input("Identify Yourself : ")
print("Hey !",input_1,", What's Your Designation (Teacher : 1 & Student : 2) : ",end='')
input_2=int(input(""))
if input_2==1:
    login_in=input("Login Username : ")
    login_pwd=input("Login Password : ")
    l=l1.get("pwd")
    z=l1.get("lgn")
    if login_in==z and login_pwd==l:
        print("Logged In !")
        in_sec=int(input("Please enter Security PIN to access all tests : "))
        in_str=str(in_sec)
        if in_sec in l2:
            print("Security Test Passed ! .. Loading All tests :) ")
            print("")
            FTP_HOST_1 = "ftpupload.net"
            FTP_USER_1 = "epiz_29685346"
            FTP_PASS_1 = "zgQK2LN7A7"
            ftp_1 = ftplib.FTP(FTP_HOST_1, FTP_USER_1, FTP_PASS_1)
            ftp_1.encoding = "utf-8"
            ftp_1.cwd("./htdocs/"+in_str)
            ftp_1.dir()
            print()
            in_ask=int(input("Want to Create a [1] new quiz or [2] edit previous test :  "))
            if in_ask==1:
                in_ap=int(input("Approx Questions : "))
                os.chdir(r"questions")
                o=0
                q=0
                n=in_ap
                while range(0,n+1):
                   q += 1
                   if n==q:
                       in_ex=int(input("Do you want to exit [1] for yes and [2] for no : "))
                       if in_ex==2:
                           n_t=int(input("How many more questions : "))
                           n=n+n_t
                           print("Ok , we have added new lenght of questions ..")
                       else:
                           break
                   f=open("quest"+str(q)+".txt","a")
                   print("This is Q.",q)
                   in_quest=input("Question : ")
                   f.write(in_quest)
                   f.write("\n")
                   ask_quest=int(input(" Objective [1] , Subjective [2] or Oral [3] : "))
                   if ask_quest==1:
                       f.write("Tx#264857$$$$$$$2662892998627628728783674654645636637636746746579708999055")
                       f.write("\n")
                       in_opt=int(input("No. Of Options : "))
                       if in_opt!=0:
                           print()
                           o=0
                       else:
                           print("As No perfect value is assigned , The default value of (4 Options) is applied!")
                           in_opt=4
                           o=0
                       while range(0,in_opt):
                           o += 1
                           input_3 = input("Option " + str(o) + ": ")
                           opt.append(input_3)
                           f.write(input_3)
                           f.write("\n")
                           if o==in_opt:
                               in_r_o=str(input("Correct option : "))
                               f.write(in_r_o)
                               f.write("\n")
                               f.close()
                               break
                   elif ask_quest==2:
                       f.write("Tx#264857$$$$$$$2662892922627628728783674654641136637636746746579703999055")
                       f.write("\n")
                       ans_acc_t=input("Answer According to You : ")
                       f.write(ans_acc_t)
                   elif ask_quest==3:
                       f.write("Tx#264857$$$$$$$2662892922627628728783674654641136637636746746579703999055")
                       f.write("\n")
                       ans_acc_t = input("Answer According to You [oral] : ")
                       f.write(ans_acc_t)
                   f.close()
                print()
                deploy_ask=int(input("Your Questions are now ready ! , Do you want to deploy it ? ( [1] yes and [2] no : "))
                ## Questions dir is your directory path
                list = os.listdir()
                file_count = len(list)
                l1 = []
                name_f = []
                check = [" Tx#264857$$$$$$$2662892998627628728783674654645636637636746746579708999055",
                         ' Tx#264857$$$$$$$2662892922627628728783674654641136637636746746579703999055',
                         ' Tx#264857$$$$$$$2662892922627628728783674654641136637636746746579703999055']
                for i in range(1, file_count + 1):
                    file_name = "quest" + str(i) + ".txt"
                    name_f.append(file_name)
                    i += 1
                # print(name_f)
                for y in range(file_count):
                    with open(name_f[y], 'r') as file:
                        quest = file.read()
                    z = sent_tokenize(quest)  # Tokenizing Question from file
                    l1.append(z)  # Converting them to a list
                    listToStr = ' '.join(map(str, l1))  # List to String
                    patn = re.sub(r"[\([{})\]]", "", listToStr)  # Removing all list signs
                    n_patn = patn.replace("'", "")
                    n_patn_1 = n_patn.replace("\\n", ",")  # removing (') caused by a list
                    q_quest = n_patn_1.strip().split(',')  # Spliting up all
                    print(q_quest)
                    # print(q_quest[0],q_quest[1],q_quest[-1]) # 1st one is identifying question , 2nd one is identifying type , 3rd one is getting correct option
                    # print(check_1)
                    # print(check)
                    if q_quest[1] == check[0]:
                        q1, t1, ans1 = q_quest[0], q_quest[1], q_quest[-1]
                        """
                        q_quest.pop(0)
                        q_quest.pop(1)
                        q_quest.pop(-1)
                        options1=q_quest
                        """
                    elif q_quest[1] == check[1]:
                        q1, t1, ans1 = q_quest[0], q_quest[1], q_quest[-1]
                    elif q_quest[1] == check[2]:
                        q1, t1, ans1 = q_quest[0], q_quest[1], q_quest[-1]
                if deploy_ask==1:

                    print("Converted")
                elif deploy_ask==2:
                    print("undeployed")
                else:
                    print("Bye")

        else:
            print("Security Test failed! ... Logging Out !")
    else:
        print("Invalid")
elif input_2==2:
    print("It isn't intended for students")
else:
    print("Bye")




