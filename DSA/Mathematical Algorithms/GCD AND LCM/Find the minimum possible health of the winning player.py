#Minimum possible health of the winning player

#Question
'''
Given an array health[] where health[i] is the health of the ith player in a game, any player can attack any other player in the game. The health of the player being attacked will be
reduced by the amount of health the attacking player has. The task is to find the minimum possible health of the winning player.'''

#Logic
'''

 In order to minimize the health of the last player, only the player with the smaller health will attack a player with the larger health and by doing so if only two players are
 involved then the minimum health of the  last player is nothing but the GCD of the
 initial healths of the two players. So, the result will be the GCD of all the elements of the given array.
'''
from math import gcd
def minHealth(arr,n):
    final_gcd=0
    for i in range(n):
        final_gcd=gcd(final_gcd,arr[i])
    return final_gcd

health=list(map(int, input("Enter the numbers separated by comma :").split(',')))
length=len(health)
print("The minimum possible health of the winning player is",minHealth(health,length))
