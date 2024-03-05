print("welcome to the jungle baby")

"""lista = ["Debanhi", "Marianna","Mario","Elida"]

print(lista)

new_element = input("Deseas agregar otro elemento a la lista?")

lista.append(new_element)

print("agregaste "+ new_element)

print(" a continuacion tu lista:")

print(lista)"""

#try to read elements from file
filename = 'elements.txt'


"""with open(filename) as file_object:
	#contents = file_object.read()
	lines = file_object.readlines()

print(lines)"""

"""print("ESPACIO")	
for line in lines:
	print(line.rstrip())

#agregar nuevo elemento a la lista y archivo de texto
new_element = input("Agrega un nuevo elemento: ")

with open(filename, 'a') as file_object:
	file_object.write(new_element+'\n')"""

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

