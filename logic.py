'''
Voting logic
'''

import csv
import os

class Voting:
    '''
    Handles voting logic
    '''

    def __init__(self) -> None:
        '''
        Initialize names
        '''
        self._vote_file = 'votes.csv'
        self._voter_file = 'voters.txt'

    def validate_id(self, voter_id: str) -> bool:
        '''
        Validate voter id
        '''

        return voter_id.isdigit()

    def has_voted(self, voter_id: str) -> bool:
        '''
        Checks if a voter has already voted
        '''
        if not os.path.exists(self._voter_file):
            return False

        with open(self._voter_file, "r") as file:
            voters = file.read().splitlines()

        return voter_id in voters

    def save_vote(self, voter_id: str, candidate: str) -> None:
        '''
        Saves voting information
        '''
        with open(self._voter_file, "a") as file:
            file.write(f"{voter_id}\n")

        new_file = not os.path.exists(self._vote_file)

        with open(self._vote_file, "a", newline="") as file:
            writer = csv.writer(file)

            if new_file:
                writer.writerow(["ID", "Candidate"])

            writer.writerow([voter_id, candidate])

    