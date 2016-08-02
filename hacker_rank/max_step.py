def  maxStep(n, k):

    curr_sum = 0
    for x in range(1,k+1):
        curr_sum += x
        # if we go above k, then we will skip k in our jumping so we can take all steps.
        if curr_sum > k:
            return countSteps(n)
        # if we'll hit k, then we need to skip taking a step on the first action
        if curr_sum == k:
            return countSteps(n)-1
    return 0

def countSteps(num):
    curr = 0
    for x in range(1, num+1):
        curr += x
    return curr


"""
The idea is that just get the optimal case. (step every time.) If it does not step on K, good. That should be the optimal solution.

If it happens to step on Kth stair, the optimal case must be all the steps without the first step(1st step).

###dealing with this problem
Everytime we take a step, we need to ensure that we won't be resting on the 'k'th step which is broken. All other steps we can take. Please check the solution below.


int fnMaxSteps(int n,int k){
int steps = 0;
for (int i=1;i<=n;i++){
	if(steps+i==k)
		continue;
	else
		steps+=i;
}
return steps;
}

Consider the case with n=4 and k=10.

Your solution will give: 1+2+3+0=6.

However the correct solution is: 0+2+3+4=9.
"""
