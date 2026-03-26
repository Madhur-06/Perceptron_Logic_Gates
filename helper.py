def GetMethod():
    print("Select training method:")
    print("  1. Perceptron Trick")
    print("  2. Hinge Loss")
    method = input("Enter 1 or 2: ")
    if method == "1":
        return "perceptron"
    elif method == "2":
        return "hinge"
    else:
        print(f"  '{method}' is not valid. Please enter 1 or 2.")
        exit()

def GetGATE():
    gate=input("Enter the Gate you want to train on: ")
    return gate

def GetLR():
    lr=float(input("Enter the Learning Rate: "))
    return lr

def GetEp():
    Ep=int(input("Enter the number of Epocs: "))
    return Ep