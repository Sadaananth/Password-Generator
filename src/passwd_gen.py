import random

CharaterList = "!@#$%?&*-+"
min_length = 8

def getListCount():
	
	line_count = 0
	file_obj = open('character.txt','r')
	
	for indiv_line in file_obj:
		line_count = line_count + 1
	
	file_obj.close()
	
	return line_count
	
'''
not used now 
'''	
def make_char_caps(character_name,loc):
	
	return_character = ""
	index = 0
	for character in character_name:
		
		if index == loc :
			return_character = return_character + character.upper()
		else:
			return_character = return_character + character
		
		index = index + 1
	
	return return_character

def remove_char(character_name,token):
	
	return_character = ""
	
	for character in character_name:
	
		if character == token:
			break
		else:
			return_character = return_character + character
	
	return return_character

def getRandomCharacter(no_of_character):
	
	selected_character = ""
	character_file = open('character.txt','r')
	character_to_select = random.randrange(no_of_character)
	index = 0
	
	for line in character_file:
	
		if index == character_to_select:
			break;
		else:
			index = index + 1;
	
	selected_character = remove_char(line,"\n")
	character_file.close()
	
	return selected_character
		
def check_entry(character_name):
	
	retval = 0
	entry_file = open('entry.txt', 'r+')
	
	for entry_line in entry_file:
		
		if character_name == remove_char(entry_line,"\n"):
			break
		else:
			retval = 1
	entry_file.close()
	
	return retval

def make_password(character_name):
	
	integer_out = random.randrange(10)
	output_string = character_name + `integer_out`
	output_string = output_string + CharaterList[random.randrange(len(CharaterList))]
	
	while len(output_string) < min_length:
		
		integer_out = random.randrange(10)
		output_string = output_string + `integer_out`
		
	return output_string
	
def add_entry_to_list(string_to_paste):

	character_to_store = string_to_paste + "\n"
	file_to_write = open('entry.txt', 'a')
	file_to_write.write(character_to_store)
	file_to_write.close()
		
def main():
	
	input_from_user = ""
	
	while 1:
		character_name = getRandomCharacter(getListCount())
		generated_passwd = make_password(character_name)	
		
		if check_entry( generated_passwd ) == 1:
			print("Generated Password : %r" %generated_passwd)
			input_from_user = raw_input("Have you used it ? type y/n : ") 
			
			if input_from_user == "y":
				continue
			else:
				add_entry_to_list(generated_passwd)
				print("Input is added to the list")
				break	
			
main()
