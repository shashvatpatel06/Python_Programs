f = open('b.txt','w+')
ch = input("Enter the content :")
while(ch!='~'):
    f.write(ch+'\n')
    ch = input("Enter content :")
f.seek(0)
l=list(map(lambda s:s.strip().lower(),f.readlines()))
keyw = ['int','float','list','tuple','dictionary','set','complex','boolean']
for n in l:
    if(n in keyw):
        print(n,'->',"Keyword")
    else:
        try:
            if(float(n)):
                print(n,'->',"Number")
        except ValueError:
            print(n,'->',"Identifier")
f.close()
