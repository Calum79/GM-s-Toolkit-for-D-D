Hi, thanks for opening this.

Welcome to the Soul Striker DM Toolkit!

Included in this toolkit is a character data storage system, and a team/player data analysis script.

The following was made so that Dungeon/Game Masters can better understand player behaviours and damage outputs, and so they
can balance their encounters within their D&D games more fairly.

STEP 1 - TECHNICAL DETAILS:

The first thing you want to do is make sure you have Python installed, since the code for the
character initialiser and the spell save calculator run off python scripts.

Next, for convenience, you can alter the batch files in the data folder to give yourself a 
slightly smoother experience with the character initialiser and the spell check calculator.

When you open the batch file by pressing right click and then 'edit', each batch file should be 
formatted in the following way:

@echo off
"C:\Folder where python is installed\python.exe" "C:\Where the Soul Striker DM Toolkit is placed\DM's Toolkit\code and data\Lib\Python Script name.py"
pause

The batch files can be found in: Soul Striker DM Toolkit is placed\DM's Toolkit\code and data\Lib

Make sure to alter the paths appropriately!

Now, you can just open the character initialiser and the spell check calculator from the shortcuts 
right next to the character sheet and this text file!

STEP 2 - CHARACTER STORAGE

The character storage system is something of which should be used periodically throughout your journey DMing Soul Strikers.

When you open the storage system, first, input the current date.

Next, input the character you'd like to add an entry to. If this character is new, that's okay! Just type out their name, and
the script will prompt you to create a new character profile. Say yes and the relevant CSV files will be created.

The script will ask you to insert which spell was used. You can input anything, even if it's a weapon or an alternate move.
The data storage works as long as you are specific and consistent with the spelling.

You will then be prompted to input the damage, which is straightforward enough.

Something  to note, is the the 

STEP 3 - DATA ANALYSIS.

This is the component of the DM's toolkit where you can perform analysis on the combatitive efforts of the team, or  alternatively,
individual characters. To do so, start the data analysis program.

You will first be prompted if you want to do "quick analysis". This will use all stored data, giving you the total and average damage
for the the entire party and individual players on every single day. It will export the data to:
"C:\Where the Soul Striker DM Toolkit is placed\DM's Toolkit\code and data\Lib\quick_analysis.csv"

Obviously, you will be given a lot of data straight away, and this may make things a bit more confusing when analysing player data,
especially later in the campaign when you have potentially hundreds or thousands of entries to sift through.

For this reason, the data analysis script will allow you to find specific data entries.	

First, the script will ask if you want to do entire party or individual palyer analysis. 

Second, the script will ask if you want the output to be a total damage output or average damage output.

Third, the script will ask if you want rewuested type of damage output for a specific date, or for the entire campaign.

Afterwards, you should recieve the requested data.

The script is on an infinite loop, so you should be able to ask for as many queries as desired.






