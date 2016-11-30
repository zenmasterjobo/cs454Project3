#!/usr/bin/env python
# Jordan Bergero
# Kevin Ting
# Due December 6th

import sys
import rand

def derive (grammar, alpha, string, integer):
# generates a derivation of the form
# alpha =>alpha1 => alpha2 => … => alphaj-1 => w
 if(k == 1):
     if(a rule alpha -> w exists in G):
         return "alpha=>w", true
      else:
          return " ", false # the first output is irrelevant
      sym = leftmost non-terminal in current;
      for each rule R in G with sym on the left-side:
          let R be sym -> beta;
          next = replace(sym, beta, alpha)
          der, found = derive(next, w, k-1)
          if(found):
            return “alpha=>next” + der, true
          else:
              return “”, false
