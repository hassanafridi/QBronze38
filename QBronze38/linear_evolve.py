def linear_evolve(B,v):
    state=[]
    for i in range(len(B)): 
        state.append(0) 
        for j in range(len(v)): 
            state[i] = state[i] + B[i][j] * v[j] 
    return state
