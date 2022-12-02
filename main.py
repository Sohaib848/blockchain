from ecdsa import SigningKey
import json

skCS = SigningKey.generate() # uses NIST192p
vkCS = skCS.verifying_key #Ariane (boite qui verifie peut recuperer ca sur internet)


def mettre_sur_la_Blockchain(path):

    with open(path, "rb") as f:
        text = f.read()
    signature = skCS.sign(text)

    return str(signature)



def verifier_diplome(path):
    with open("BC.json") as f:
        BC = json.load(f)

    with open(path, "rb") as f:
        Diplome = f.read()
    
    Chain = BC["chain"]
    for i in range(len(Chain)):
        Trans = BC["chain"][i]["transactions"]
        for j in range(len(Trans)-1):
            text = Trans[j]["Hsigned"]
            sign = text[2:-1].encode().decode('unicode_escape').encode("raw_unicode_escape")
            try:
                vkCS.verify(sign, Diplome)
            except:
                None
            else:
                return True
    return False