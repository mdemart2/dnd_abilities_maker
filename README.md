# dnd_abilities_maker
Messing around with making "fair" but random ability scores using 4d6 drop worst method (most often used). My method: Generate random characters using the 4d6 drop worst method until you have 3 such that: none are overpowered, underpowered, or that one is strictly better than another. The player may pick 1 of any of those 3 characters.

## What is a "strictly better" character than another?
Say you have two characters a and b. Put their ability scores in order from lowest to highest. If it's always the case that a's n-th highest ability score is at least as high as b's n-th highest, then a is a strictly better character than b.

## What is overpowered or underpowered?
Obviously subjective! But in my case:

* Overpowered:
    * Total score is >= 76
    * Best score is 18
    * 3rd best score is >=15
    * Worst score is > 11
* Underpowered:
    * Total score is <= 71
    * Best score is < 16 (*super* subjective - the default matrix has a 15 max)
    * 3rd worst score is <=9
    * Worst score is < 6
