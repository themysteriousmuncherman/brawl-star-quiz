import requests

url = "https://brawlstarsapi.p.rapidapi.com/brawlers"

headers = {
	"x-rapidapi-key": "753e27db50msh9fe97b423205deap191643jsn9766ce6def38",
	"x-rapidapi-host": "brawlstarsapi.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)



print(response.json())


data = response.json()


choice = input("What brawler would you like to learn about? ")


for i in data:
    if i["name"].lower() == choice.lower():
        print(f"Brawler: {i['name']}")
        print(f"1st Star Power: {i['1st star power']}")
        print(f"2nd Star Power: {i['2nd star power']}")
        print(f"1st Gadget: {i['1st gadget']}")
        print(f"2nd Gadget: {i['2nd gadget']}")

