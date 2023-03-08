# profile Hidden Markov Model
# 1. get transition and emission probabilities

import numpy as np
import pandas as pd
import math
import argparse
from collections import Counter
import sys

#parser = argparse.ArgumentParser()
#filename = parser.add_argument('filename') 
#args = parser.parse_args()
class phmm:
    def __init__(self, filename):
        self.filename = filename
        self.seq = self.read_file(filename)
        self.marked, self.states = self.get_states()
        self.state_prob, self.transition_prob = self.transition()
        self.emission_prob = self.emission()
        
    def read_file(self, filename):
        with open(filename, 'r') as f:
            # read file into numpy array (rows: array of the sequence)
            lines = f.readlines()
            seq = [] 
            for line in lines:
                if not line.startswith('>') and line != "": 
                    seq.append(np.array(list(line.strip())))
            seq = np.array(seq)
        return seq

    def get_states(self):
        # marked: mark columns with match or mismatch
        marked = ["M"]
        for i, col in enumerate(self.seq.T):
            x = Counter(col) 
            if '-' in x:
                gaps = x['-']
            else:
                gaps = 0
            nuc = sum(x.values()) - gaps
            if nuc > gaps:       
                marked.append('M')
            else:
                marked.append('I')

        states = []
        for row, mark in zip(self.seq.T, marked[1:]):
            col_states = []
            for col in row:
                if col != "-" and mark == "M": # nuc in M state = M
                    col_states.append("M")
                elif col == "-" and mark == "M": # gap in M state = D
                    col_states.append("D")
                elif col != "-" and mark == "I": # nuc in I state = I
                    col_states.append("I")
                else:                            # ignore gaps in I state
                    col_states.append("-") 
            states.append(np.array(col_states)) # problem is that states is appending by col.  need to flip .T
        states = np.array(states).T 
        return marked, states,

    def transition(self):
        transition_counts = [] # length = # of match states
        #freq_t = {ind: {} for ind, key in enumerate(marked)}
        freq_t = {}
        match_states = [ind for ind, ele in enumerate(self.marked) if ele == "M"] # gets indices of match states
        match_states[-1] = match_states[-1]-1 # b/c length is +1 of seq, so last index will be out of index
        state_prob = {}
        for ind, m in enumerate(match_states[:-1]):
            match_before = match_states[m] # index col of match state before insert states
            match_after = match_states[m+1] 
            # state probability: M->state in first column
            if m == match_states[0]:
                for row in self.states.T[0]:
                    entry = ("M{}".format(row))
                    state_prob[entry] = state_prob.get(entry, 0) + 1
            # insert state(s)
            elif match_states[m]+1 != match_states[m+1]: 
                insert_nuc = self.seq.T[m:match_states[m+1]] # gets all the seq col. that are in the insert state
                insert_nuc = insert_nuc != "-" # bool array of all the nuc
                for ind_c, col in enumerate(insert_nuc.T): 
                    if np.any(col != False): # contains nuc. in insert col
                        if  self.states[ind_c][match_before-1] == "M":
                            freq_t["MI"] = freq_t.get("MI", 0) + 1
                        if self.states[ind_c][match_after] == "M": # I->M
                            freq_t["IM"] = freq_t.get("IM", 0) + 1
                        elif self.states[ind_c][match_after] == "D": # I->D
                            freq_t["ID"] = freq_t.get("ID", 0) + 1 
                        # I->I
                        for ind_r, row in enumerate(col[1:]):
                            if col[ind_r-1] == True and row == True:
                                freq_t["II"] = freq_t.get("II", 0) + 1 
                    else:
                        if self.states[ind_c][match_before-1] == "M" and self.states[ind_c][match_after] == "M":
                            freq_t["MM"] = freq_t.get("MM", 0) + 1                     

            # match state
            for j, row in enumerate(self.states.T[m]): # Iterate down col at corresponding index to match state in marked
                if m == 0: # if the first col, assume the previous state was a match (the begin state)
                    entry = ("M{}".format(row))
                    freq_t[entry] = freq_t.get(entry, 0) + 1
                else:
                    if self.states.T[m-1][j] == "-" or row == "-": # ignore gaps in insert state
                        continue
                    entry = ("{}{}".format(self.states.T[m-1][j],row))
                    freq_t[entry] = freq_t.get(entry, 0) + 1
            transition_counts.append(freq_t)
            freq_t = {}
        # if last column, assume transition is to match state?
        for j, row in enumerate(self.states.T[-1]):
            entry = ("{}{}".format(row,"M"))
            freq_t[entry] = freq_t.get(entry, 0) + 1
        transition_counts.append(freq_t)
        freq_t = {}
        # get probability of each starting state
        for key, value in state_prob.items():
            state_prob[key] = value/sum(state_prob.values())
        # get probability of state transitions for each position in sequence
        prob_t = []
        temp = {}
        for trans_p in transition_counts:
            tot = sum(trans_p.values())
            for key, value in trans_p.items():
                temp[key] = value/tot
            prob_t.append(temp)
            temp = {}
        return state_prob, prob_t

    def emission(self):
        # get emission probabilities
        # emission prob.
        freq = []
        temp = {'M':{}, 'I':{}}
        nuc = {'A':0, 'C':0, 'G':0, 'T':0}
        match_states = [ind for ind, ele in enumerate(self.marked) if ele == "M"] # gets indices of match states

        for m in match_states[:-1]:
            match_before = match_states[m] # index col of match state before insert states
            match_after = match_states[m+1]        
            # insert state(s)
            if match_states[m]+1 != match_states[m+1]: 
                insert_nuc = self.seq.T[m:match_states[m+1]-1] # gets all the seq col. that are in the insert state
                for col_i in insert_nuc:
                    for row_i in col_i:
                        if row_i != '-':
                            nuc[row_i] += 1
                temp['I'] = dict(Counter(temp['I']) + Counter(nuc))
                freq.append(temp)
                temp = {'M':{}, 'I':{}}
                nuc = {'A':0, 'C':0, 'G':0, 'T':0}
            # match state
            else:
                for col_m in self.seq.T[m]:
                    for row_m in col_m:
                        if row_m != '-':
                            nuc[row_m] += 1
                temp['M'] = dict(Counter(temp['M']) + Counter(nuc))
                freq.append(temp)
                temp = {'M':{}, 'I':{}}
                nuc = {'A':0, 'C':0, 'G':0, 'T':0}
        for col in self.seq.T[-1]:
            for row in col:
                if row != '-':
                    nuc[row] += 1
        if self.marked[-1] == 'M':
            temp['M'] = dict(Counter(nuc))
        else:
            temp['I'] = dict(Counter(nuc))
        freq.append(temp)
        
        # get emission probabilities
        emission_prob = []
        temp_t = {}
        temp_e = {}
        for emis_p in freq:
            tot = 0
            temp_t = {}
            temp_e = {}
            for val in emis_p.values():
                tot += sum(val.values())
            for t_key, value in emis_p.items():
                for e_key, e_val in value.items():
                    temp_e[e_key] = e_val/tot
                temp_t[t_key] = temp_e        
            emission_prob.append(temp_t)    
        return emission_prob

    def format_input(self):
        # format input into list of transition and emission states and probabilities as lists and list of lists
        # ex: output: 
        # emission_states = ["normal", "cold", "dizzy"]
        # transition_states = ["Healthy", "Fever"]
        # state = [[0.6, 0.4]]
        # transition = [[0.7,0.3], [0.4,0.6]] 
        # emission = [[0.5,0.3,0.1], [0.1,0.3,0.6]]
        # seq = ["normal", "cold", "dizzy"]
        
        transition_states = ["M", "D", "I"]
        transition = pd.DataFrame(columns=transition_states, index=transition_states)
        # row is the state it came from, col is the state it's going to
        for key, value in self.prob_t.items():
            transition[key[0]][key[1]] = value   
        emission_states = ["A", "C", "G", "T"]
        emission = pd.DataFrame(columns=emission_states, index=["M", "I"])
        for key, value in self.prob_e.items():
            for key1 in value.keys():
                emission.loc[key] = self.prob_e[key][key1]
        state = [list(self.state_prob.values())]
        df_state = pd.DataFrame(state, columns = ['M', 'D'])
        
        return df_state, transition, emission

    def get_consensus(self):
        # get consensus sequence
        # most frequent bases in a nucleotide alignment or in a multiple protein alignmen
        # Transition: [{'MM': 0.8, 'MD': 0.2}, {'MM': 0.6, 'MD': 0.2, 'DD': 0.2}, {'MM': 0.18181818181818182, 'IM': 0.18181818181818182, 'MI': 0.09090909090909091, 'ID': 0.09090909090909091, 'II': 0.2727272727272727, 'DI': 0.18181818181818182}, {'MM': 0.8, 'DM': 0.2}]
        # Emission: [{'M': {'A': 1.0}, 'I': {'A': 1.0}}, {'M': {'G': 1.0}, 'I': {'G': 1.0}}, {'M': {'A': 0.8333333333333334, 'G': 0.16666666666666666}, 'I': {'A': 0.8333333333333334, 'G': 0.16666666666666666}}, {'M': {'A': 0.0, 'C': 1.0, 'G': 0.0, 'T': 0.0}, 'I': {'A': 0.0, 'C': 1.0, 'G': 0.0, 'T': 0.0}}]
        consensus = ""
        # get the most frequent base in each column if it's not a gap
        for col in self.seq.T:
            most_freq = Counter(col).most_common(1)[0][0]
            if most_freq != "-":
                consensus += most_freq
        return consensus         
    
    def mutations(self):
        mutations = np.zeros(self.states.shape)
        consensus = self.get_consensus(self.seq)
        i = -1
        for ind_m, m in enumerate(marked[1:]):
            if m == "M": 
                i += 1 # index of match state in consensus)
                for ind_n, n in enumerate(self.seq.T[ind_m]): # iterate down column of seq at index match state
                    if n != consensus[i] and n != '-':
                        mutations[ind_n][ind_m] = self.prob_e[i]['M'][n]
        return mutations
    
    def viterbi(self, state, transition, transition_states, emission, emission_states, seq, log=0):
        # input: list of state, transition, and emission prob as lists
        # state should be in format: [[p1, p2, ...]]
        # transition indices: list of states
        for trans, emis in zip(transitions, emissions):
            state, transition, emission = format_prob(state, trans, transition_states, emis, emission_states)
        
        if transition.shape[1]!= emission.shape[0]: 
            # num rows of trans. states must equal num col. of emission states
            print("Number of rows in transition state must equal number of columns in emission states", file=sys.stderr)
        probability = 1
        path = []
        if type(seq) == str:
            seq = [*seq]
        for s,i in zip(seq, range(len(seq))):
            if i == 0: # if first in seq, use state prob.
                prob1 = {}
                for st in state:
                    prob1[st] = float(state[st] * emission[s][st]) 
                t_state = max(prob1, key=prob1.get)
                path.append(t_state) # add max probability to path
                if log == 1:
                    prev_prob = math.log2(prob1[path[0]])
                else:
                    prev_prob = prob1[path[0]]
                prev_state = t_state
            else:
                prob = {}           
                for t in transition:      
                    if log == 1:
                        prob[t] = prev_prob +  math.log2(transition[prev_state][t] * emission[s][t])
                    else:
                        prob[t] = prev_prob * (transition[prev_state][t] * emission[s][t])
                x = max(prob, key=prob.get)
                path.append(x)
                prev_prob = prob[x]
                prev_state = x
        return path, prev_prob
    
"""
seq = read_file('pHMM_test.txt')
marked, states = get_states(seq)
state_prob, transition_counts, prob_t = transition(states, seq, marked)
emission_prob = emission(states,seq, marked)
print("State probability: ", state_prob)
print("Transition probability: ", prob_t)
print("Emission probability: ", emission_prob)
#seq = read_file(args.filename)
#marked, states = get_states(seq)
#transition_counts, prob_t = transition(states)
#emission_counts = emission(states,seq)
# prob_t format: {'MM':prob}
# emission counts format

state: (array([['M', 'M', '-', '-', '-', 'M'],
        ['M', 'D', 'I', '-', '-', 'M'],
        ['M', 'M', '-', 'I', 'I', 'D'],
        ['D', 'D', 'I', 'I', 'I', 'M'],
        ['M', 'M', '-', '-', '-', 'M']], dtype='<U1'),
prob: {'MM': 0.8125,
'MD': 0.125,
'DD': 0.25,
'IM': 0.3333333333333333,
'MI': 0.0625,
'ID': 0.16666666666666666,
'II': 0.5,
'DI': 0.5,
'DM': 0.25},
emissions: {'M': {'A': 0.36363636363636365,
'G': 0.2727272727272727,
'C': 0.36363636363636365},
'I': {'A': 0.8333333333333334, 'G': 0.16666666666666666}},
"""

# use states as the index of an array that looks for transitions
# if index is M, then it's a marked col. will be 1 off b/c it indicates which state it came from 

# supposed to do this for every single seq. 
# states rn is the overall state (so a gap in a D col. is a deletion and a gap in a I col is a insertion)




# NOTES
"""
1. length depends on number of match states
2. match states depend on whether a column is mostly gaps or nuc.
if mostly gaps: column is an insertion
if mostly nuc: column is a match state

3. transition: match, insert, delete
emission: nucleotides or -

4. to avoid zero probabilities, use Laplace's rule: add one to each freq

5. no emission score for insertions b/c we assume emission distribution from insert states is the same as background, so probabilities cancel in log odds form
D-> I and I-> D transitions may not be present

6. want to allow aln to start and end in a delete / insert state:
    a. set begin state to be M0 and allow transitions to I0 and D1
    n. set end state to M l+1 

7. score of seq is just all the log score + log (prev)

8. assumed that an aln col of symbols corresponds either to emissions from the same match state / same insert state
    a. should mark which columns come from match states
    b. marked col, symbols -> match states and '-' -> delete states
    c. unmarked col. symbols assigned to insert states and gaps are ignored
    d. mark col. if >50% have symbols
    e. for MAP construction, max a posteriori choice determined



Possible additions:
1. use ambiguious characters (R,Y, etc.)
2. use previous knowledge about proteins: substitution matrices
3. MAP, determine whether / not to mark col

"""

# %%
