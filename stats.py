import sys
import numpy
#updating the synced repo with a comment

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        stats_inflammation(sys.stdin, action)
    else:
        for filename in filenames:
            stats_inflammation(filename, action)


def stats_inflammation(filename,action):
        data = numpy.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)

        for val in values:
            print(val)

if __name__ == '__main__':
   main()
