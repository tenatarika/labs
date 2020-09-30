# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 00:01:07 2020

@author: Furcas
"""
import json

from playsound import playsound

class Vocabular:
    @classmethod
    def trans(cls, word):
        morse = []
        WtoM = {'a': '.-', 'b': '-...', 'c': '-.-.',
                       'd': '-..', 'e': '.', 'f': '..-.',
                       'g': '--.', 'h': '....', 'i': '..',
                       'j': '.---', 'k': '-.-', 'l': '.-..',
                       'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                       'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                       'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                       'y': '-.--', 'z': '--..'}
        
        for ch in word:
            morse.append(WtoM[ch])
        return ''.join(morse)
    
    
    
    
    @classmethod
    def addWord(cls, word):
        data = cls.readJson()
        data.update({word: cls.trans(word)})
        cls.writeJson(data)
        
    @classmethod    
    def readJson(cls):
        try:
            data = json.load(open('dataWords.json'))
            
        except:
            data = {}
            
        return data
    
    
    
    @classmethod    
    def writeJson(cls, data):
        
        with open('dataWords.json', 'w') as f:
            
            json.dump(data, f, indent = 4, ensure_ascii=False)
       
    @classmethod
    def sortJson(cls):
        data = cls.readJson()
        
        list_keys = list(data.keys())
        list_keys.sort()
        sorted_data = {}
        
        for i in list_keys: #i == word
            sorted_data.update({i: data[i]})
        
        cls.writeJson(sorted_data)
        
    
    @classmethod
    def delWord(cls, word):
        data = cls.readJson()
        data.pop(word)
        cls.writeJson(data)
                
    @classmethod    
    def searcher(cls, word):
        data = cls.readJson()
        
        for i in data.keys():
            
            if i ==  word:
                return f'YES! Word {word} => {data[i]} '
            
        return f'No such word in the dictionary'
    
    @classmethod
    def wordPlayer(cls, word):
        pword = cls.trans(word)
        for i in pword:
            if i == '.':
               playsound('boom.mp3', True) 
            else:
               playsound('foo.mp3', True)
               return 'Done!'
         

voc = Vocabular()

print(voc.wordPlayer('korn'))