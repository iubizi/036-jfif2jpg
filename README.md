# 036-jfif2jpg

036 jfif2jpg

jfif is actually jpg, but basically all software can't open it, so it can only be converted into jpg to open.

jfif should be the dumbest suffix in history.

## bugs

1. If test.jpg already exists, you cannot change test.jfif to test.jpg because it will overwrite the previous file. In order to avoid this problem, error handling (try) is used in the code, and the new file is modified to test.new.jpg
