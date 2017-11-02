# dnd_abilities_maker
Messing around with making "fair" but random ability scores using 4d6 drop worst method (most often used). My method: The player may pick 1 of any 3 random sets of ability scores none of which are overpowered or underpowered and such that no set is strictly better than another (e.g. [10, 12, 13, 14, 15, 17] is strictly better than [8, 10, 13, 14, 15, 16])

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
