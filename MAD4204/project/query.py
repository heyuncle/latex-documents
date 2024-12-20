def powerset(S):
    for i in range(2 ** len(S)):
        partial = []
        for j in range(len(S)):
            if (i >> j) % 2 == 1:
                partial.append(S[j])
        yield partial

def entail(A,B):
    pass

def inference(P, Q):
    for A, p in P:



if __name__ == '__main__':
    Q = []
    elt = input("Input name of skill (or 'end' when done): ")
    while elt != "end":
        Q.append(elt)
        elt = input("Input name of skill (or 'end' when done): ")

    P_y = set()
    P_n = set()
    P = set()
    P_m = set()

    A = list(powerset(Q))[1:]

    while True:
        P = P | P_y
        P_m = P_m | P_n

    blocks = [[] for i in range(Q)]
    

    for A in possible:
        if A == []: # do not include empty set
            continue
        for q in Q:
            if q in A: # queries APq with q in A
                continue
            blocks[len(A)].append((set(A), q))

    success = []
    for A, q in queries:
        print(
            "\nSuppose that a student under examination has just provided wrong responses to all the following questions:\n" +
            "- " + "\n- ".join(A) + "\n" +
            "\nIs it practically certain that this student will also fail the following?\n" +
            "- " + q + "\n"
        )
        if input("Input 'y' for yes, otherwise for no: ") == "y":
            success.append((A, q))

    # print(
    #     "Successful queries: " + 
    #     ", ".join(["{" + ",".join(A) + "}P" + q for A, q in success])
    # )

    # for A, q in success:
    #     for K in possible:
    #         if q in K and set(K).isdisjoint(set(A)):
    #             possible.remove(K)
    #             print("\tRemoved {" + ",".join(K) + "}")

    # print(
    #     "\nKnowledge states: " +
    #     ", ".join(["{" + ",".join(K) + "}" for K in possible])
    # )