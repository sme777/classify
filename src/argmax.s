.globl argmax

.text
# =================================================================
# FUNCTION: Given a int vector, return the index of the largest
#	element. If there are multiple, return the one
#	with the smallest index.
# Arguments:
# 	a0 (int*) is the pointer to the start of the vector
#	a1 (int)  is the # of elements in the vector
# Returns:
#	a0 (int)  is the first index of the largest element
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 77.
# =================================================================
argmax:

    # Prologue
    addi t5, x0, 1
    #t5 is just for testing no element arrays (edge case)
    blt a1, t5, edge
    #initializing counter variable
    addi t0, x0, 0
    #t2 keeps track of our max index
    addi t2, x0, 0
    #t3 keeps track of our actual max value
    lw t3, 0(a0)

loop_start:
	beq t0, a1, loop_end
    #t1 keeps track of the current value in the array
	lw t1, 0(a0)
    #this checks if current value is less than or equal to max value so far
    bge t3, t1, loop_continue
    #change our max value
    addi t3, t1, 0
    #change our max index
    add t2, x0, t0
    
loop_continue:
	#moving pointers forward
    addi a0, a0, 4
    addi t0, t0, 1
    j loop_start


loop_end:
    addi a0, t2, 0
    # Epilogue
    ret 

edge:
	addi a1, x0, 77
    j exit2