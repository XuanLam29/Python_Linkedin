#
# Read and write files using the built-in Python file methods
#

from os import close


def main():  
  # Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt", "r")
  
  # Open the file for appending text to the end


  # write some lines of data to the file
  '''for i in range (10):
        f.write("this is a line" + str(i)+ "\r\n")'''
  
  # close the file when done
  ''' f.close()'''
  help(open)
  print(help)
  # Open the file back up and read the contents 
  #f= open("textfile.txt","r")
  '''if f.mode =='r':
        contents = f.read()
        print(contents)'''
    
if __name__ == "__main__":
  main()
