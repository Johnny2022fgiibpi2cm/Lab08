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




