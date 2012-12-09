import matplotlib.pyplot as plt, sys
import cPickle

if __name__ == "__main__":
    fnames = sys.argv[1:]
    results = {}
    for fname in fnames:
        with open(fname) as f:
            obj = cPickle.load(f)
            for (k, v) in obj.iteritems():
                if not k in results:
                    results[k] = []
                results[k].extend(v)
    for run in results['avg']:
        plt.plot(run)
    plt.show()
