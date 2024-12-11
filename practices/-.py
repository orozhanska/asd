def recommend_friends_weighted(graph, user):
    recommendations = {}
    
    # Get the direct friends of the user
    direct_friends = {direct_friend for direct_friend, _ in graph.get(user, set())}
    
    # Iterate over each direct friend of the user
    for direct_friend, direct_weight in graph.get(user, set()):
        # Iterate over each friend of the direct friend
        for friend, weight in graph.get(direct_friend, set()):
            # Check if the friend is not the user and not a direct friend
            if friend != user and friend not in direct_friends:
                if friend not in recommendations:
                    recommendations[friend] = 0
                
                # Calculate the mutual friend score as the sum of weights of the direct friendship
                # and the friendship between the direct friend and the mutual friend
                recommendations[friend] += direct_weight + weight
    
    # Sort recommendations based on the number of mutual friends (in descending order)
    recommendations = sorted(recommendations.items(), key=lambda x: -x[1])
    
    return recommendations

# Example usage
graph = {
    'A': {('B', 0.2), ('D', 1)},
    'B': {('A', 0.2), ('C', 0.5)},
    'C': {('B', 0.5), ('F', 1)},
    'D': {('A', 1)},
    'E': {('F', 0.8)},
    'F': {('C', 1), ('E', 0.8)}
}

user = 'A'

recommendations = recommend_friends_weighted(graph, user)
print("Recommendations for", user)
for friend, score in recommendations:
    print(f"{friend}: {score} mutual friends")
