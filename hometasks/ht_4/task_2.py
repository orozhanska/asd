# recommendation_tests.py
# i took into account only friends of directs friends, not friends of friends of direct friends etc
# the task did not mentioned how deep into the graph we should go, as far as I remember 
def recommend_friends(graph, user):
    recommendations = {}
    for direct_friend in graph.get(user, set()):
        for friend in graph.get(direct_friend, set()):
            if (friend not in graph.get(user, set())) and (friend != user):
                if friend not in recommendations.keys():
                    recommendations[friend] = 0
                
                recommendations[friend] +=1
    
    recommendations = list(sorted(recommendations.items(), key= lambda x: -x[1]))
    return recommendations

def recommend_friends_weighted(graph, user):
    recommendations = {}
  
    # graph = {A: {(B, 0.2), (D, 1)},
    #            ...}  

    direct_friends = {direct_friend for direct_friend, _ in graph.get(user, set())}
    
    for direct_friend, direct_weight in graph.get(user, set()):
        for friend, weight in graph.get(direct_friend, set()):
            if friend not in direct_friends and friend != user:
                if friend not in recommendations:
                    recommendations[friend] = 0
                
                recommendations[friend] += direct_weight + weight  # or use other relationships 

    recommendations = sorted(recommendations.items(), key=lambda x: -x[1])
    return recommendations


def format_recommendations(user, recommendations):
    """
    Format the recommendations to match the expected output format.
    """
    output = f"Recommendations for {user}:\n"
    for potential_friend, mutual_count in recommendations:
        output += f"'{potential_friend}': {mutual_count} mutual friend{'s' if mutual_count > 1 else ''}\n"
    return output.strip()

def lists_are_equal_unordered(list1, list2):
    """
    Check if two lists of tuples are equal, ignoring the order of elements with the same count.
    """
    return sorted(list1, key=lambda x: (-x[1], x[0])) == sorted(list2, key=lambda x: (-x[1], x[0]))

def test_recommendation_system():
    """
    Run tests for the recommendation system with formatted output verification.
    """
    # Test 1: Simple graph
    graph1 = {
        'A': {'B', 'C', 'D'},
        'B': {'A', 'C', 'E'},
        'C': {'A', 'B', 'F'},
        'D': {'A'},
        'E': {'B'},
        'F': {'C'}
    }
    user = 'A'
    recommendations = recommend_friends(graph1, user)
    formatted_result = format_recommendations(user, recommendations)

    expected_output = [
        ('E', 1),
        ('F', 1)
    ]

    assert lists_are_equal_unordered(recommendations, expected_output), (
        f"Test 1 failed. Expected:\n{expected_output}\nGot:\n{recommendations}"
    )

    # Test 2: Larger graph
    graph2 = {
        '1': {'2', '3'},
        '2': {'1', '4', '5'},
        '3': {'1', '5', '6'},
        '4': {'2'},
        '5': {'2', '3'},
        '6': {'3'}
    }
    user = '1'
    recommendations = recommend_friends(graph2, user)
    formatted_result = format_recommendations(user, recommendations)

    expected_output = [
        ('5', 2),
        ('4', 1),
        ('6', 1)
    ]

    assert lists_are_equal_unordered(recommendations, expected_output), (
        f"Test 2 failed. Expected:\n{expected_output}\nGot:\n{recommendations}"
    )

    # Test 3: Edge case - No potential friends
    graph3 = {
        'X': {'Y'},
        'Y': {'X'}
    }
    user = 'X'
    recommendations = recommend_friends(graph3, user)
    formatted_result = format_recommendations(user, recommendations)

    expected_output = []
    assert recommendations == expected_output, (
        f"Test 3 failed. Expected:\n{expected_output}\nGot:\n{recommendations}"
    )

    # Test 4: Self-loop (ignored)
    graph4 = {
        'U': {'U', 'V'},
        'V': {'U', 'W'},
        'W': {'V'}
    }
    user = 'U'
    recommendations = recommend_friends(graph4, user)
    formatted_result = format_recommendations(user, recommendations)

    expected_output = [
        ('W', 1)
    ]
    assert recommendations == expected_output, (
        f"Test 4 failed. Expected:\n{expected_output}\nGot:\n{recommendations}"
    )

    # Test 5: Weighted graph (weights ignored for simplicity)
    graph5 = {
        'A': {'B', 'C', 'D'},
        'B': {'A', 'C', 'E'},
        'C': {'A', 'B', 'F'},
        'D': {'A'},
        'E': {'B'},
        'F': {'C'}
    }
    user = 'A'
    recommendations = recommend_friends(graph5, user)
    formatted_result = format_recommendations(user, recommendations)

    expected_output = [
        ('E', 1),
        ('F', 1)
    ]

    assert lists_are_equal_unordered(recommendations, expected_output), (
        f"Test 5 failed. Expected:\n{expected_output}\nGot:\n{recommendations}"
    )

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_recommendation_system()
