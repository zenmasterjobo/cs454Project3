#!/usr/bin/env python
# Jordan Bergero
# Kevin Ting

from sys import argv

k = 0
terminals = []
nonterminals = []
rules = {}

def processInput(filename):
    global k, terminals, nonterminals, rules
    with open(filename) as f:
        content = f.readlines()
        k = int(content.pop(0))
        nonterminals = content.pop(0).split()
        terminals = content.pop(0).split()
        for line in content:
            line_lst = line.split()
            rules[line_lst.pop(0)] = line_lst

def debug_print():
    print "-----------------------------"
    print "K:\t%d" % k
    print "-----------------------------"
    print "Terminals:\t"
    for terminal in terminals:
        print terminal
    print "-----------------------------"
    print "Nonterminals:\t"
    for nonterminal in nonterminals:
        print nonterminal
    print "-----------------------------"
    print "Rules:\t"
    for key, value in rules.iteritems():
        print key, value
    print "-----------------------------"

def main():
    script, filename = argv
    processInput(filename)
    debug_print()

if __name__ == "__main__":
    main()
