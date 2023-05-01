#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actua l name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#From letter file, read the letter and store it in a variable
PLACE_HOLDER = "[name]"
#Open the names file and store it in a variable and check the data
with open("./Input/Names/invited_names.txt",'r') as names_file:
    data = names_file.readlines()
    print(data)

#Open the letter files and use it for PLACEHOLDER with each name in the files
with open("./Input/Letters/starting_letter.txt",'r') as letter_file:
     letter = letter_file.read()
     for name in data:
          new_letter = letter.replace(PLACE_HOLDER,name.strip())
          # print(new_letter)
          stripped = name.strip()
          with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt",mode='w') as completed_letter:
              completed_letter.write(new_letter)
