# Criei uma lista que possui 5 nomes
namesList = [ 'Mário' , 'Rafael', 'Rodrigo', 'Fábio', 'Luciano']


# Criei uma função onde adiciona o sobrenome destes 5 nomes "da Silva"
def addLastName(name):
    return name + ' da Silva'


# crio a variavél "updatedNames" que recebe o retorno da função map()
# a função map() recebe por parâmetro minha função "addLastName", e minha lista "namesList"
# excutando assim uma função especifica para cada item na minha lista iterando ela
updatedNames = map(addLastName, namesList)


# aqui eu printo o resultado
print(list(updatedNames))