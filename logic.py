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

    