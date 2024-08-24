#Given a dictionary of username
#and status:["online"|"offline"]
#return the number of players
#that are online

players={
    "Deepak":"offline",
    "Kavin":"online",
    "Divya Prakash":"offline",
    "Pradeesh":"online",
    "Shankar":"offline",
    "Jegan":"online",
    "Shafiullah":"online"

}

def online(players):
    result=0
    for key,value in players.items():
        if value =="online":
            print(key)
            result+=1
    return result

print(online(players))