
# Truth Table Enumeration for Propositional Entailment

from itertools import product

def implies(a, b):
    return (not a) or b

# Knowledge Base
def KB(P, Q, R):
    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R
    return s1, s2, s3, s1 and s2 and s3

# Queries
def query_R(P, Q, R):
    return R

def query_RP(P, Q, R):
    return implies(R, P)

def query_QR(P, Q, R):
    return implies(Q, R)

# Display truth table
print("\nTRUTH TABLE")
print("-" * 95)

print(f"{'P':^5}{'Q':^5}{'R':^5}"
      f"{'Q->P':^8}{'P->~Q':^8}{'Q|R':^8}"
      f"{'KB':^8}{'R':^8}{'R->P':^8}{'Q->R':^8}")

print("-" * 95)

models = []

for P, Q, R in product([False, True], repeat=3):

    s1, s2, s3, kb = KB(P, Q, R)

    qr = query_R(P, Q, R)
    rp = query_RP(P, Q, R)
    qqr = query_QR(P, Q, R)

    models.append((P, Q, R, kb, qr, rp, qqr))

    values = [P, Q, R, s1, s2, s3, kb, qr, rp, qqr]

    print("".join(f"{str(v):^8}" for v in values))

print("-" * 95)

# Check entailment
def entails(query_index):
    for model in models:
        if model[3] and not model[query_index]:
            return False
    return True

print("\nENTAILMENT RESULTS")
print("-" * 40)

print("KB entails R      :", entails(4))
print("KB entails R -> P :", entails(5))
print("KB entails Q -> R :", entails(6))

print("-" * 40)
