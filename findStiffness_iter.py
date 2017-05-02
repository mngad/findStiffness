import pyperclip as pc
import findStiffness as fs

stiffnesslist = []
i = 100
incrSize = 1
while i > 0:
    stiffnesslist.append(fs.findStiffness(
        i, incrSize, False, 'M:\HT_Compression_All\HT_Compression_3+post+frozen__BETTER_NAMING'))
    i = i - 1
    pc.copy(''.join(stiffnesslist))
