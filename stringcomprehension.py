##string='''
##practice program for the com pre hensive in py
##'''
##
##wordslst=string.split(' ')
##print(wordslst)
##wordslst=[i.strip("\n") for i in wordslst ]
##print(wordslst)
##
##ans={i:len(i) for i in wordslst }
##print(ans)


string='''
practice program for the com pre hensive in py
'''

wordslst=string.split(' ')
#print(wordslst)
wordslst=[i.strip("\n") for i in wordslst ]
#print(wordslst)

ans={i:i[::-1] for i in wordslst }
print(ans)


