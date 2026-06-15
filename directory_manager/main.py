from settings import *
from logic import *






            

        






def main():
    while True:
        
        current_dir=os.getcwd()
        print(f"{GREEN}{20*"*"}{RED}DIRECTORY MANAGER{GREEN}{20*"*"}{RESET}")
        GREEN
        print(f"{GREEN}{"*"*40}\n{RED}Hold'ESC'for 2 second to quit the program(when u are not during an opperation!!!){GREEN}\n{"*"*40}{RESET}")
        print(f"{RED}CURRENT WORKING DIRECTORY: {YELLOW}'{current_dir}'{RED} ")
        print(f"{GREEN}{"*"*40}")
        
        print(f"{YELLOW}1.create file")
        print("2.copy")
        print("3.cut")
        print("4.delete")
        print("5.rename")
        print("6.create directory")
        print("7.change current working directory")
       
        
        command=input("...>")

        if command=="1":
            while True:
                 if not write_file():
                      break
        elif command=="2":
            while True:
                path=input("path: ")
                new_dir=input("new directory: ")
                if  copy_file(path,new_dir):
                    break
        elif command=="3":
            while True:
                path=input("file path: ")
                new_dir=input("new directory: ")
                if  move_file(path,new_dir):
                    break        
        elif command=="4":
            while True:
                path=input("file path or directory(Use it Wisely!!!):")
                if  delete_directory(path):
                    break        
        elif command=="5":
            while True:
                path=input("path: ")
                new_name=input("new name: ")
                if  renames(path,new_name):
                    break                      
        elif command=="6":
            while True:
                path=input("path: ")
                if  create_dir(path):
                    break                  
        elif command=="7":
            while True:
                 new_dir=input("new working directory: ")
                 if  change_dir(new_dir):
                    break
        else  :
            print("Invalid input")       
            continue
    
            
        

        
    
if __name__=="__main__":
    t1=threading.Thread(target=ecs_clicked,daemon=True)
    t1.start()
    main()
   
    
    

    print("*"*40)