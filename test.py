print("welcome to the jungle baby")

filename = 'elements.txt'

#crear funcion para consultar elementos del archivo
def get_elements_from_file(filename):
	with open(filename) as file_object:
			#contents = file_object.read()
			lines = file_object.readlines()
	return lines 

lines = get_elements_from_file(filename)
print(lines)

#esta funcion solo sirve para listar que hay en mi lista de forma ordenada	
def list_elements_from_file(filename):
	order_list = []
	lines = get_elements_from_file(filename)

	for line in lines:
		order_list.append(line.rstrip())

	return order_list

orderlist = list_elements_from_file(filename)
print(orderlist)
		
	
#funcion para agregar un elemento al archivo de texto
def add_new_entry_to_file(new_name,filename):
	with open(filename, 'a') as file_object:
		file_object.write(new_name+'\n')

	print("agregaste : "+ new_name)


add_new_entry_to_file("anitalabalatina",filename)
orderlist = list_elements_from_file(filename)
print(orderlist)

