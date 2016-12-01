#!/usr/bin/env python
# Jordan Bergero
# Kevin Ting
# Due December 6th

from sys import argv

k = 0
w = ""
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
            if line_lst != []:
                key = line_lst.pop(0)
                if key in rules:
                    if line_lst == []:
                        line_lst.append("")
                    rules[key] += line_lst
                else:
                    rules[key] = line_lst

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


def leftmost_nonterminal(alpha):
    for i, letter in enumerate(alpha):
        if letter in nonterminals:
            return letter, i
    return None,None
def replace_nonterminal(index, rule, alpha):
    word = alpha[:index] + rule + alpha[index+1:]
    return word

def has_nonterminal(alpha): 
    for letter in alpha:
        if letter in nonterminals:
            return True
    return False

def derive (alpha, k, der, found):
    # generates a derivation of the form
    # alpha =>alpha1 => alpha2 => ... => alphaj-1 => w
    if k == 1:
        next_alpha = ""
        if has_nonterminal(alpha):
            print alpha
            sym, index = leftmost_nonterminal(alpha)
            rules_for_sym = rules[sym]
            for rule in rules_for_sym:
                next_alpha = replace_nonterminal(index, rule, alpha)
                if next_alpha == w:
                    return der + "%s=>%s" % (ialpha, next_alpha), True
            return "", False

        else:
            print alpha
            if alpha != w:
                return "", False
            else:
                print "found alpha"
                return der + "%s=>%s" % (alpha, next_alpha), True
    index = 0
    if has_nonterminal(alpha):
        sym, index = leftmost_nonterminal(alpha)
        rules_for_sym = []
        rules_for_sym = rules[sym]
        for rule in rules_for_sym:
            next_alpha = replace_nonterminal(index, rule, alpha)
            derive(next_alpha, k-1, der + "%s => %s" % (alpha, next_alpha), found)

    
def main():
    global w
    global k
    script, filename = argv
    processInput(filename)
    debug_print()
    w = "abbaba"
    #w = raw_input("What is w?: ")
    der, found = derive("S", k, "", False) 
    if not found:
        print "Fucking better"
    print "ouput: %s" % der
if __name__ == "__main__":
    main()
