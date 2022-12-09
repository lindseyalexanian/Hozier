#!/usr/bin/env python3
# song_tricks.py

import pandas as pd
import os
import random

# check working directory
os.getcwd()

class SongTricks:
    
    def __init__(self, songs_file):
        self.songs = songs_file
        
    def song_df(self):
        # read in text file
        songs_df = pd.read_table(self.songs, sep="\t", header=None)

        # change column header
        songs_df.columns = ["Song"]
        
        return songs_df
    
    def song_list(self):
        songs_df = self.song_df()
        song_list = songs_df.Song.tolist()
        
        return song_list
        
    
    def song_randomizer(self):
        # get song df in og order
        songs_df = self.song_df()
        
        # shuffle it (randomly)
        songs_shuffled = songs_df.sample(frac=1).reset_index()
        songs_shuffled = songs_shuffled.drop(columns=["index"])

        return songs_shuffled
    
    def give_me_a_song(self):
        # pick song randomly
        what_song_is_it = random.choice(self.songs)
        
        print(f"The song is: {what_song_is_it}")
        return what_song_is_it
        

    def song_assign(self):
        # input people's names (Comma separated)
        input_string = input("Enter guest names separated by comma ")
        guest_list  = input_string.split(",")
        
        # put in a pandas df
        guest_df = pd.DataFrame(guest_list)
        # name column
        guest_df.columns = ["guest_name"]
        
        # get song list
        song_list = self.song_list()
        
        # get random songs
        random_songs = random.sample(song_list, len(guest_list))
        
        # make song assignment column w/ random selections
        guest_df["song_assignment"] = random_songs
        
        # write to csv
        guest_df.to_csv("hozier_song_assignments.csv", index=None)
        
        return guest_df
        

# testing!
x = SongTricks("hozier_song_list.txt").song_assign()
