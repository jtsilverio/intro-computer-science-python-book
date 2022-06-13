import os

signatures = {'Creeper':'ye8009g2h1azzx33',
              'Code Red':'99dh1cz963bsscs3',
              'Blaster':'fdp1102k1ks6hgbc'}

def scan(pathname, signatures):
    for item in os.listdir(pathname):
        next = os.path.join(pathname, item)
        
        try:
            scan(next, signatures)
        except:
            for virus in signatures:
                if open(next).read().find(signatures[virus]) >= 0:
                    print("{}, found virus {}".format(next, virus))

scan("test_ch10/", signatures)