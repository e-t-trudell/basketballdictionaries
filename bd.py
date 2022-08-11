# # 1) Update the constructor to accept a dictionary with a single player's information instead of arguements for the attributes

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, 
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, 
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]
class Player:
    def __init__(self, players):
        self.name = 'name'
        self.age = 'age'
        self.position = 'position'
        self.team = 'team'
        self.players = players

test = Player(players[2])
[print("*Challenge One*")]
print(test.players['name'])

# 2) Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        self.kevin = kevin
        self.jason = jason
        self.kyrie = kyrie
    

crazy_kevin = Player(kevin['name'], kevin['age'], kevin['position'], kevin['team'])
jonesin_jason = Player(jason['name'], jason['age'], jason['position'], jason['team'])
katatonic_kyrie = Player(kyrie['name'], kyrie['age'], kyrie['position'], kyrie['team'])
print("*Chalenge Two*")
print(crazy_kevin.name)
print(jonesin_jason.name)
print(katatonic_kyrie.name)

# 3)Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

# this is incorrect use this to compare. this requires the player dictionaries from step two
# class Player:
#     def __init__(self, players):
#         self.name = 'name'
#         self.age = 'age'
#         self.position = 'position'
#         self.team = 'team'
#         self.players = players

players = [{"name": "Kevin Durant", 
			"age":34, 
    		"position": "small forward", 
			"team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age":24, 
    	"position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age":32, 
        "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age":33, 
        "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age":32, 
        "position": "Power Foward", "team": "Philidelphia 76ers"},
    {"name": "Michael Jorden", "age":23, 
    	"position": "Point Guard", "team": "Chicago Bulls"}]
# this is how you pass in a dictionary
class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']

	# method to print new team list at the end instead of printing objects
    @classmethod
    def get_team(cls, team_list):
        cls.list = team_list
        print("*Ninja Bonus*")
        print(team_list)
Player.get_team(players[0:6])


# this is an example template
# eric = Player(dictionary)
eric = Player(players[0])
# print(f"{eric.name}, {eric.age}, {eric.position}, {eric.team}")
# eric.get_name(new_team[0:6])
# print(f"{eric.name}, {eric.age}, {eric.position}, {eric.team}")

new_team = []
for player in (players):
	# print(player)
	kevin = Player(player)
	new_team.append(kevin)
# this prints the objects in the new team list. 
# print(new_team)
# this prints name at 0 index, etc etc at 0 index in the list of new_team
print("*Challenge Three*")
print(f"{new_team[0].name}, {new_team[0].age}, {new_team[0].position}, {new_team[0].team}")
print(f"{new_team[1].name}, {new_team[1].age}, {new_team[1].position}, {new_team[1].team}")
print(f"{new_team[2].name}, {new_team[2].age}, {new_team[2].position}, {new_team[2].team}")
print(f"{new_team[3].name}, {new_team[3].age}, {new_team[3].position}, {new_team[3].team}")
print(f"{new_team[4].name}, {new_team[4].age}, {new_team[4].position}, {new_team[4].team}")
print(f"{new_team[5].name}, {new_team[5].age}, {new_team[5].position}, {new_team[5].team}")
    

