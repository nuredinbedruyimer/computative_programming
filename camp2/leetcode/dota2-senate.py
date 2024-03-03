def get_player_position(word):

    N = len(word)

    radiant_queue = deque()

    dire_queue = deque()

    for i in range(N):
        if word[i]=='R':
            radiant_queue.append(i)
        else:
            dire_queue.append(i)
    return radiant_queue ,  dire_queue




def get_winner(sanate):
    
    N = len(sanate)

    radiant_queue , dire_queue = get_player_position(sanate)

    while radiant_queue and dire_queue:

        radiant_index = radiant_queue.popleft()

        dire_index =  dire_queue.popleft()

        #  if radiant placed befre that of dire it removed the dire fighter

        if radiant_index < dire_index:

            radiant_queue.append(radiant_index + N)
        
        #  do the same if the dire found in the front

        else:

            dire_queue.append(dire_index + N)

    
    return radiant_queue , dire_queue




def get_result(sanate):

    radiant , dire = get_winner(sanate)

    if radiant:
        return "Radiant"
    if dire:
        return "Dire"



    




class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        return get_result(senate)