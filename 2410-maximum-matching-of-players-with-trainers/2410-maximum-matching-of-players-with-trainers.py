class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        indt = len(trainers) - 1

        for i in range(len(players)-1, - 1, -1):
            if players[i] <= trainers[indt] and indt >= 0:
                indt-= 1
        return len(trainers) - (indt + 1) 
