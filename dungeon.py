dungeon = {
    "entrance": {"treasure": 10, "trap": False, "description": "A dark cave entrance"},
    "hall": {"treasure": 50, "trap": True, "description": "A long hall with spikes"},
    "vault": {"treasure": 100, "trap": False, "description": "The golden vault"},
    "secret": {"treasure": 75, "trap": False, "description": "Hidden secret room"},
    "exit": {"treasure": 25, "trap": True, "description": "Tricky exit corridor"}
}
money=0
for room in dungeon:
    data = dungeon[room]
    if data["trap"] == True:
        print("#",data["description"]+"...", "TRAP! Skipped!")
    else:
        money += data["treasure"]
        print("#",data["description"]+"...", "+",str(data["treasure"]),"gold")
print("# You collected", money, "gold coins!")