#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2 == 0:
        return True
    else:
        return False



def remove_third_char(string: str) -> str:
    begin = string[0: 2]
    end= string[3: ]
    return begin + end
    
#aurait pu faire retun string[0:2] + string[3:]

def replace_char(string: str, old_char: str, new_char: str) -> str:
    newwrd = string.replace(old_char, new_char)
    return newwrd


def get_number_of_char(string: str, char: str) -> int:
    n=0
    for i in range(0, len(string)):
        if string[i]==char:
            n+=1
    return n


def get_number_of_words(sentence: str, word: str) -> int:
    m=0
    for i in sentence:
        word = sentence.split (' ')
        if word=='doo':
            m+=1    
     return m


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
