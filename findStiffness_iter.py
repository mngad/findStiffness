import pyperclip as pc
import findStiffness as fs


def iter(i, incrSize):

    stiffnesslist = []
    while i > 0:
        stiffnesslist.append(fs.findStiffness(
            i, incrSize, False, 'M:\HT_Compression_All\HT_Compression_3+post+frozen__BETTER_NAMING'))
        i = i - 1
        pc.copy(''.join(stiffnesslist))


if __name__ == "__name__":
    iter(100, 1)
