# 036-jfif2jpg

036 jfif2jpg

jfif is actually jpg, but basically all software can't open it, so it can only be converted into jpg to open.

jfif should be the dumbest suffix in history.

## bugs and features

1. If test.jpg already exists, you cannot change test.jfif to test.jpg because it will overwrite the previous file. In order to avoid this problem, error handling (try) is used in the code, and the new file is modified to test.new.jpg

2. If you run this code on the command line, there will be a final exit without warning, so input() is added to avoid the Unexpected exit.

3. In order to avoid some problems, file system recursion is not used, so this code can only deal with formatting problems in the path (folder) where the code is located.
