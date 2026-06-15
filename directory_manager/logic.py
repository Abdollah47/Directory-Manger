from settings import *
def write_file():
        print("*"*20)
        file_name=input("file name : ")
        if not file_name.endswith((".txt",".py")) :
            print("The file type must be pyhton or text file!")
            return True
        else:   
            content=input("file content: ")
            with open (file_name,"w") as file:
                
                    file.write(content)
                    print(f"{RED}'{file_name}'{YELLOW} was created succussfuly!")
                    return False
            

def change_dir(new_dir):
      print("*"*20)
      if os.path.isdir(new_dir):
            os.chdir(new_dir)
            print("working directory was changed succussfuly!")
            return True
      else:
            print(f"{RED}'{new_dir}'{YELLOW} directory doesn't exist!! ")
            return False
      


def copy_file(path,new_dir):
      print("*"*20)
      try:
            if os.path.isfile(path) :
                  shutil.copy2(path,new_dir)
                  print(f"'File {RED}'{path}'{YELLOW} was copied to {RED}'{new_dir}'{YELLOW} succussfuly!")
                  return True
            elif os.path.isdir(path):
                  shutil.copytree(path,new_dir)
                  print(f"Directory {RED}'{path}'{YELLOW} was copied to {RED}'{new_dir}'{YELLOW} succussfuly!")
                  return True
            else:
                  print("wrong path or new directory")
                  return False
      
      except Exception as e:
            print("Error! occured while copying!",e)
            return False

def move_file(path,new_dir)      :
            print("*"*20)
            if os.path.isfile(path) and os.path.isdir(new_dir):
                  try:
                        shutil.move(path,new_dir)
                        print(f"'File {RED}'{path}'{YELLOW} moved to {RED}'{new_dir}'{YELLOW} succussfuly!")
                        return True
                  except Exception as e:
                        print("Error! occured while copying!",e)
                        return False
            else:
                        print("wrong path or new directory")
                        return False


def delete_directory(path):
      print("*"*20)
      if os.path.isdir(path):
            try:
                  shutil.rmtree(path)
                  print(f"directory'{RED}{path}'{YELLOW} was deleted succussfuly!")

                  return True
            except Exception as e:
                  print("Error occured while deleting: ",e)
                  return False
      elif os.path.isfile(path):
            try: 
                  os.remove(path)    
                  print(f"file{RED}'{path}'{YELLOW} was deleted succussfuly!")  
                  return True
            except Exception as e:
                  print("Error occured while deleting: ",e)
                  return False
      else:
            print("path doesn't exist!")
            return False      

def renames(path,new_name):
      print("*"*20)
      if os.path.exists(path):
            try:
                  os.rename(path,new_name)
                  print(f"file name{RED}'{os.path.basename}'{YELLOW} was changed to {RED}'{new_name}'{YELLOW}")
                  return True
            except Exception as e:
                  print("Error occured! ",e)
                  return False
      else:
            print(f"this path {RED}'{path}'{YELLOW} doesn't exist!!!")
            return False
      


def create_dir(path):
            print("*"*20)
            try:
                  os.mkdir(path)
                  print(f"new directory {RED}'{path}'{YELLOW} was created!")
                  return True
            except Exception as e:
                  print("Error occured! ",e)
                  return False
      
def ecs_clicked():
            print("*"*20)
            holds=0
            duration=2
            while True:
                   if holds>=duration:
                        holds=0
                        print(f"{"*"*20}Thank You!!!{"*"*20}")
                        time.sleep(0.5)
                        os._exit(1)
                        
                   if keyboard.is_pressed("esc"):
                          time.sleep(0.1)
                          holds+=0.1
                   else:
                          holds=0       

                   

                  
            
             
                    
                                
             
             

             



            
            

      

