import random
key1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
key2={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
plaintext=input("Enter text to be encrypted below.\n")
ciphertext=""
pad=[]
for i in range(10):
    pad.append(str(random.randint(1,27)))
indexer=0
for letters in plaintext:
    if indexer>9:
        indexer=0
    try:
        if letters.lower()==letters:
            nums=key1[letters]
            try:
                index_int=nums+int(pad[indexer])
                assert index_int<27
            except AssertionError:
                index_int-=26
            result=key2[index_int]
            ciphertext+=result
            indexer+=1
        elif letters.upper()==letters:
            nums=key1[letters.lower()]
            try:
                index_int=nums+int(pad[indexer])
                assert index_int<27
            except AssertionError:
                index_int-=26
            result=key2[index_int].upper()
            ciphertext+=result
            indexer+=1
    except KeyError:
        ciphertext+=letters
        continue
print(f"\nPlaintext\n---------\n{plaintext}\n\nCiphertext\n----------\n{ciphertext}\n\nKey-pad\n---------\n{'-'.join(pad)}")
