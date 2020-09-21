import csv

with open("details.csv", mode="w", newline='') as file:
    fieldNames = ["name", "status", "income", "FD_lists", "value_dict"]
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerow({"name": "AAA", "status": 'Professional', "income": 800000, "FD_lists": [12000, 45000, 300000, 200000],
                     "value_dict": {"House": 4500000, "Car": 600000, "Land": 4000000, "Jewels": 1000000}})
    writer.writerow({"name": "BBB", "status": 'Politician', "income": 10000000, "FD_lists": [2000000, 1000000, 25000000],
                     "value_dict": {"House": 30000000, "Car": 2000000, "Land": 100000000, "Jewels": 25000000}})
    writer.writerow({"name": "CCC", "status": 'Employee', "income": 700000, "FD_lists": [500000, 200000, 150000],
                     "value_dict": {"House": 1000000, "Jewels": 250000}})
    writer.writerow({"name": "DDD", "status": 'Professional', "income": 10, "FD_lists": [20, 20, 20, 50],
                     "value_dict": {"House": 4500000, "Car": 600000, "Land": 4000000, "Jewels": 1000000}})
    writer.writerow({"name": "EEE", "status": 'Politician', "income": 10, "FD_lists": [20, 20, 20, 50],
                     "value_dict": {"House": 10, "Car": 20, "Land": 30, "Jewels": 50}})
    writer.writerow({"name": "FFF", "status": 'Employee', "income": 5, "FD_lists": [500000, 200000, 150000],
                     "value_dict": {"House": 20, "Jewels": 10}})

with open("details.csv", newline='') as file:
    reader = csv.DictReader(file)
    for person in reader:
        totalDeposits = sum(eval(person["FD_lists"]))
        assets = sum(eval(person["value_dict"]).values())
        income = eval(person["income"])
        try:
            if person["status"] == "Professional":
                if 10*income < totalDeposits or assets > 25*income:
                    raise ValueError("IT RAID ALERT")
            elif person["status"] == "Politician":
                if 10*income < totalDeposits and assets > 10*income:
                    raise ValueError("Disproportionate Assets Alert")
            else:
                if 20*income < totalDeposits or assets > 20*income:
                    raise ValueError("Scam Alert!")
        except ValueError as e:
            print("Exception: ", e)
        else:
            print("\n", "-"*100, "\n")
            print("Good...your details:")
            print(f"name : {person['name']}", f"status : {person['status']}", f"income : {income}", f"sum of deposits : {totalDeposits}", f"sum of assets : {assets}",
                  f"deposits : {person['FD_lists']}", f"assets : {person['value_dict']}", sep="\n")
            print("\n", "-"*100, "\n")
