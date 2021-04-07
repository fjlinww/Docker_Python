#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Viterbi Algorithm for HMM
# dp, time complexity O(mn^2), m is the length of sequence of observation, n is the number of hidden states

# five elements for HMM

states = ('Rainy', 'Sunny')
 
observations = ('walk', 'shop', 'clean', 'walk')
 
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
 
transition_probability = {
    'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
    }
 
emission_probability = {
    'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
    }


# definition of the Viterbi Algorithm
def Viterbi(states, obs, s_pro, t_pro, e_pro):
	path = { s:[] for s in states} # init path: path[s] represents the path ends with s
	curr_pro = {}
	for s in states:
		curr_pro[s] = s_pro[s]*e_pro[s][obs[0]] #start with the first observation state: 0.6x0.5, 0.4x0.1

	for i in range(1, len(obs)):  #start with 1,2,...,len(obs)-1
		last_pro = curr_pro
		curr_pro = {}
		for curr_state in states:
			max_pro, last_sta = max(((last_pro[last_state]*t_pro[last_state][curr_state]*e_pro[curr_state][obs[i]], last_state) 
				                       for last_state in states))
			
			curr_pro[curr_state] = max_pro
			path[curr_state].append(last_sta)
		#print ('%s'%(curr_pro))
		#print ('%s'%(path))

	# find the final largest probability
	max_pro = -1
	max_path = None
	for s in states:
		path[s].append(s)
		if curr_pro[s] > max_pro:
			max_path = path[s]
			max_pro = curr_pro[s]
	return max_path

# main function
if __name__ == '__main__':
	print (Viterbi(states, observations, start_probability, transition_probability, emission_probability))
