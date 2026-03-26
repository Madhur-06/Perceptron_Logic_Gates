from perceptron import Perceptron
from gates import GATES
from helper import GetGATE, GetEp, GetLR

print("=" * 40)
print("   Perceptron Logic Gate Trainer")
print("=" * 40)

gate = GetGATE()

if(gate not in GATES or gate == "INPUTS"):
    print(f"  '{gate}' is not a valid gate.")
    print(f"  Valid options are: AND, OR, NAND, NOR, XOR")
    exit()

if(GATES[gate]["linearly_separable"]==False):
    print(f"\n  Note: {gate} is NOT linearly separable.")
    print("  A single perceptron cannot learn it perfectly.\n")

lr = GetLR()
epochs = GetEp()

X = GATES["INPUTS"]       
y = GATES[gate]["y"]      

print(f"\nTraining a Perceptron on the {gate} gate")
print("-" * 40)

p = Perceptron(lr, epochs)
p.fit(X, y)

print("Training Complete!")
print(f"  Weights : {p.weights}")
print(f"  Bias    : {p.bias}")
print(f"  Accuracy: {p.accuracy(X, y)}%")


