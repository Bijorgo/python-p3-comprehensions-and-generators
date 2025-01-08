#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [ num for num in num_list if num % 2 == 0 ]
    return even_list

def make_exclamation(sentence_list):
    exclam_list = [ sent + "!" for sent in sentence_list ]
    return exclam_list