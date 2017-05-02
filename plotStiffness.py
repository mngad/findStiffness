import matplotlib.pyplot as plt
import findStiffness as fs


def plot(specs, fileType):
    data = fs.findStiffness(10, 1, True, 'M:\HT_Compression_All\G41-11')
    perSpec = int((len(data) - 1) / specs)
    for i in range(0, specs):
        fig = plt.figure()
        title = str(data[i * perSpec][2][:9]).replace('_', ' ')
        fig.suptitle(title, fontsize=22)
        ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])
        for a in range(perSpec):
            ax.plot(data[(i * perSpec) + a][0], data[(i * perSpec) + a][1],
                    label=str(data[i * perSpec + a][2][10:-16]), linewidth=2)
            print(data[i * perSpec + a][2])
            print('i = ' + str(i) + ', a = ' + str(a))
        ax.legend(
            bbox_to_anchor=(1.05, 1.), loc=2, borderaxespad=0.,
            fontsize=9)
        plt.xlabel('Displacement (mm)')
        plt.ylabel('Load (N)')
        plt.grid(True)
        # plt.show()
        plt.savefig(
            'M:\HT_Compression_All/' + str(title) + '.' + str(fileType),
            bbox_inches='tight')
        print('\n')


if __name__ == "__main__":
    plot(5, 'pdf')
    plot(5, 'png')
