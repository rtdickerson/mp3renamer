# mp3renamer
Simple python script to rename mp3 files for better display on your MP3 player.

My MP3 player has a tiny screen and huge names were difficult to read, especially when I'm listening to a book on tape on a long drive.  I know I'm in book "Right Ho Jeeves!" I just need to know what part.  This would turn "Right Ho Jeeves - Disk 1 - Track 1.mp3" into "part01.mp3"  I guess there are a dozen ways to do this, this was just how I did it.  Enjoy.

Assume you ripped a book on tape CD to a directory and the
files aren't in a file name convention you need.. like the file
name looks like Bob_Smith_Where_The_Roses_Bloom_D1_T2.mp3
which is just too long for your display.
This quick script will iterate through the files and rename
them to part{nn}.mp3 which will show up on the screen.

--type   File extension, default is .mp3
--token  What the beginning of the file looks like so the track
         can be parsed.  ex. "Bob_Smith_Where_The_Roses_Bloom_D1_T"
--endmode if selected, says the number is at the end
--test   doesn't actually rename 

Example A:
   track name: "Bob_Smith_Where_The_Roses_Bloom_D1_T2.mp3"
   The track number is at the end, so we want
      --endmode --token "_D1_"

Example B:
    track name: "12 - Red Ferns Grow Wildly.mp3"
    The track number is at the beginning, so we want
       --token " - "
