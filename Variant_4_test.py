def get_fare(data):
 choice = 32
 res = []
 for line in data:
      if line.split(",")[10] != 'Cabin':
            fare = float(line.split(",")[10])
            name = line.split(",")[3] + line.split(",")[4]
            if fare >= choice:
                res.append(name[1:-1])
 return res

with open("data.csv") as file:
 data = file.readlines()
print(get_fare(data))

def test_fare():
 data = ['0,1,2,.Грейнджер, Гермиона.,5,6,7,8,9,56', '0,1,2,/Поттер, Гарри.,5,6,7,8,9,5', '0,1,2,-Уизли, Рон.,5,6,7,8,9,31']
 assert get_fare(data) == ['Грейнджер Гермиона']




