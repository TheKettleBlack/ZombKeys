# ZombKeys
A zombie killing typing game. Requires PyGame and Python.

How to play:

Hit [Enter] to start a round. Type the word above the zombie's head, and hit [Space] to shoot a zombie and kill it. Words get longer and more zombkeys spawn each round. If a zombie reaches your fortification before you've killed it, it will damage your fortification for a number of points equal to the number of letters in the word. If your fortification health reaches zero, it's game over!

![ZombKeys Gameplay Screenshot](/ZombKeys_Gameplay_Screenshot.png?raw=true "ZombKeys Gameplay Screenshot")

## v0.1 (3/25/23)
- Initial release

## v0.2 (3/26/23)
- The padding on the zombkey word has been increased for improved legibility
- A program icon has been added for the window
- When you kill a zombkey, there is blood spatter added to the ground which is cleared between rounds
- The speed of zombkeys increases more slowly as you advance in level
- To spread out higher level zombkeys, the potential spawn area increases as you advance in level
- Levels now sometimes have variable word length
- The "Remaining" information has been removed from the stats bar
- Added fortification health feature and information to the stats bar
- Game no longer ends immediately after 1 zombkey reaches your fortification
- Fire now appears when a zombkey reaches your fortification
- Fortification health decreases by 1 for every letter of the breaching zombkey

## v0.3 (4/7/23)
- Cleaned up the word lists, removing duplicate and offensive words
- Any typed characters are now cleared between rounds
- The player now moves in line with any zombkey they shoot

## v0.4 (4/14/23)
- Variable zombkey speed
- [Enter] now starts a round, and [Space] now shoots

## v0.5 (5/6/23)
- You now get credit for the kill of a breaching zombkey
- If you shoot a zombkey that brings your score to a multiple of 10, a bomb will appear on the killing field if there is not already one available
- Note: Breaching zombkeys that bring the score to a multiple of 10 do NOT spawn a bomb; you've got to earn it
- If a zombkey walks over a bomb, they will explode and you get credit for the kill
- Unnecessary calls removed (sprites created that were unused)
