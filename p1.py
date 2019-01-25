import numpy as np
myState2=[(np.sqrt(0.1)*1.j, '101'),(np.sqrt(0.5), '000') ,(-np.sqrt(0.4), '010' )]
def prettyPrintBinary(state):
    output="";
    for i in range(len(state)):
        if i == len(state)-1:
            output += str(state[i][0]) + "|"+state[i][1]+">";
        else:
            output += str(state[i][0]) + "|"+state[i][1]+">"+"+ ";
    print(output);


def prettyPrintInteger(state):
    output="";
    for i in range(len(state)):
        if i == len(state)-1:
            output += str(state[i][0]) + "|"+str(int(state[i][1],len(state[i][1])))+">";
        else:
            output += str(state[i][0]) + "|"+str(int(state[i][1],len(state[i][1])))+">"+"+ ";
    print(output);
def stateToVec(state):
    vec = np.zeros(len(state),dtype=complex);
    for i in range(len(state)):
        vec[i] = state[i][0]
    return vec;
prettyPrintBinary(myState2);
prettyPrintInteger(myState2);
print(len(stateToVec(myState2)));


identity = np.identity(2)
hadmard = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
def HadmardArray(i,k):
    size = 2**k
    j = 0
    if(i==0):
        if k==1:
            return hadmard
        return np.kron(HadmardArray(i,k-1),identity)

    else:
        return np.kron(identity,HadmardArray(i-1,k-1))

print(np.equal((HadmardArray(1,3)),mat))
