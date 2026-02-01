n = int(input ("enter the number of runner :"))
min =0 
min_player =0 
for i in range (1, n+1):
    seconds = int(input(f"enter finish time of player {i}:"  ))
    if i ==1 :
        min = seconds
        min_player = i 
    elif min > seconds:
        min = seconds
        min_player = i
print("the player", min_player, "has completed first with time of ", min,"seconds") 


