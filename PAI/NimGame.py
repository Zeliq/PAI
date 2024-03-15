import random

def print_board(heap):
    print(f"Current heap: {'|' * heap}")

def get_user_move(heap):
    while True:
        try:
            sticks_to_remove = int(input(f"Enter the number of sticks to remove (1-{min(heap, heap // 2)}): "))
            if 1 <= sticks_to_remove <= min(heap, heap // 2):
                return sticks_to_remove
            print(f"Invalid number of sticks. Please enter a number between 1 and {min(heap, heap // 2)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_computer_move(heap):
    xor_sum = heap
    for i in range(heap):
        xor_sum ^= i

    max_sticks = min(heap, heap // 2)
    return max(1, min(max_sticks, heap - xor_sum))

def nim_game():
    heap = 16
    player_turn = 1

    while heap > 1:
        print_board(heap)
        player_name = "Player 1" if player_turn == 1 else "Computer"
        sticks_to_remove = get_user_move(heap) if player_turn == 1 else get_computer_move(heap)
        heap -= sticks_to_remove
        print(f"{player_name} removes {sticks_to_remove} sticks.")
        player_turn = 3 - player_turn  # Switch player

    print_board(heap)
    winner = "Player 1" if player_turn == 2 else "Computer"
    print(f"{winner} picks the last stick ")
    print(f"\n{winner} is the winner!")

if __name__ == "__main__":
    nim_game()

 

def fuzzy_union(set1, set2):
    return {k: max(set1.get(k, 0), set2.get(k, 0)) for k in set1.keys() | set2.keys()}

def fuzzy_intersection(set1, set2):
    return {k: min(set1.get(k, 0), set2.get(k, 0)) for k in set1.keys() & set2.keys()}

def display_fuzzy_set(fuzzy_set):
    print("{" + ", ".join(f"{k}: {v}" for k, v in fuzzy_set.items()) + "}")

# Example fuzzy sets
set1 = {'a': 0.8, 'b': 0.6, 'c': 0.4, 'd': 0.2, 'e': 0.1}
set2 = {'a': 0.7, 'b': 0.5, 'c': 0.3, 'f': 0.9, 'g': 0.4}

print("Fuzzy set 1:")
display_fuzzy_set(set1)

print("\nFuzzy set 2:")
display_fuzzy_set(set2)

print("\nUnion of the fuzzy sets:")
display_fuzzy_set(fuzzy_union(set1, set2))

print("\nIntersection of the fuzzy sets:")
display_fuzzy_set(fuzzy_intersection(set1, set2))

#````````````````````````````````````````````````````````

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta): 
    if depth == 3: 
        return values[nodeIndex] 

    if maximizingPlayer: 
        best = float('-inf')

        for i in range(2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best) 

            if beta <= alpha: 
                break
        
        return best 
    
    else:
        best = float('inf')

        for i in range(2): 
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta) 
            best = min(best, val) 
            beta = min(beta, best) 

            if beta <= alpha: 
                break
        
        return best 
    
# Driver Code 
if __name__ == "__main__": 

    values = [10, 9, 14, 18, 5, 4, 50, 3] 
    print("The optimal value is :", minimax(0, 0, True, values, float('-inf'), float('inf')))

