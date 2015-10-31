League of Rate

A Python 2.7 Program that uses the Riot API to calculate the most efficent champion spell
The program imports the Riot API using json, pip, and request to pull the static data of champions.
It calculates the score of each champion based their base Attack damage, attack range, and MP and each spell stats of AP effect, cooldown, and cost.

To Run:
Since Riot does not allow developers to share API keys, you will need to add your own key to the program in order for the program to run
In main.py, add your API key to the api variable

The formula:
This is built on the concept of progression of each champion and improving their spells.
The score is based on the rate in which the spells are cast and how much damage they can do. 
((((AD at 18 - AD at 1)/18) *(AttackRange/100))/((Attack Speed at 18 - Attack Speed at 1)/18)) + ((((AP at 18 - AP at 1)/18)/((energy cost at 18 - energy cost at 1)/18))*((mgregen at 18 - mgregen at 1)/18))

Version 1.0
-Published code to Github! Hello!
-Optimized for League of Legends Patch 5.21
-Removed my API so I don't get in trouble with Riot. (Get your own API key!)
-Current output says Katarina's Ultimate is the most efficent spell in the game

Legal Stuff
This program DOES NOT calculate the best champion and their spells in the game. 
The program does not completely take in all game variables such as items, your runes, and your skills



"League of Rate"  isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. 
League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. 
League of Legends © Riot Games, Inc.
