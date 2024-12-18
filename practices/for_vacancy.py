
interested = [] # <- not my business, so I leave it blank, srry tech-savvies
def look_for_talents(you: int, graph_social_network):
    for person in graph_social_network[you]:
        if interested[person]:
            print("Contact tg @orozhanska")
        else:
            print("Share with friends!")
            look_for_talents(person, graph_social_network)
    return 


