def GetGATE():
    gate=input("Enter the Gate you want to train on: ")
    return gate.upper()

def GetLR():
    lr=float(input("Enter the Learning Rate: "))
    return lr

def GetEp():
    Ep=int(input("Enter the number of Epocs: "))
    return Ep
