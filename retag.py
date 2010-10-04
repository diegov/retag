#!/usr/bin/env python
import sys

def main():
    if len(sys.argv) < 3:
        print "Usage: %s file [action]" % (sys.argv[0])
        exit(1)

    file_name = sys.argv[1]
    action = sys.argv[2]

    c = TagContext(file_name)
    engine = DSLEngine(c)
    engine.execute(action)

if __name__ == "__main__":
    main()
