from Integration.SendRequest import SendRequest
from Services.DataFrameService import CreateTableForExcel
from Services.UserService import CountUsers

# Construção da URL
BaseUrl = "https://jsonplaceholder.typicode.com/comments?postId="
id = str(input("Digite o Id: "))
url = BaseUrl + id

# Envio da requisição
data = SendRequest(url, "GET")

# Criação de tabela no excel com dados da requisição
CreateTableForExcel(data, "Usuários")

# Numeros de registros de usuários
NumbersUsers = CountUsers(data)

print("SUCCESS")
