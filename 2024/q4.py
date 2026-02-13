num_candidates = int(input("Enter number of candidates: "))

candidates ={}
for i in range(num_candidates):
    name= input(f"Enter name of candidate {i+1}:")
    candidates[name]=0

num_voters = int(input("Enter number of voters: "))
voted_users =set()

for i in range(num_voters):
    voter_name = input("Enter your name: ")

    if voter_name in voted_users:
        print("You have already voted!")
        continue
    print("Candidates:",list(candidates.keys()))
    vote=input("Enter candidate name to vote: ")

    if vote in candidates:
        candidates[vote] +=1
        voted_users.add(voter_name)
        print("Vote recorded.")
    else:
        print("Invalid candidate.")

#finding winner
max_votes= max(candidates.values())
winners= [name for name, votes in candidates.items() if votes == max_votes]

print("\nVoting Results:")
for name,votes in candidates.items():
    print(f"{name}: {votes} votes")

if len(winners) ==1:
    print(f"\nWinner is: {winners[0]}")
else:
    print("\nIt's a tie between:",", ".join(winners))
