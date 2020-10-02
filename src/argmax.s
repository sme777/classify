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
    addi sp, sp -24
    sw s0, 0(sp)
    sw s1, 4(sp)
    sw s2, 8(sp)
    sw s3, 12(sp)
    sw s5, 16(sp)
    sw ra, 20(sp)
    
    
    addi s5, x0, 1
    #t5 is just for testing no element arrays (edge case)
    blt a1, s5, edge
    #initializing counter variable
    addi s0, x0, 0
    #t2 keeps track of our max index
    addi s2, x0, 0
    #t3 keeps track of our actual max value
    lw s3, 0(a0)

loop_start:
	beq s0, a1, loop_end
    #t1 keeps track of the current value in the array
	lw s1, 0(a0)
    #this checks if current value is less than or equal to max value so far
    bge s3, s1, loop_continue
    #change our max value
    addi s3, s1, 0
    #change our max index
    add s2, x0, s0
    
loop_continue:
	#moving pointers forward
    addi a0, a0, 4
    addi s0, s0, 1
    j loop_start


loop_end:
    addi a0, s2, 0
    # Epilogue
    lw ra, 20(sp)
    lw s5, 16(sp)
    lw s3, 12(sp)
    lw s2, 8(sp)
    lw s1, 4(sp)
    lw s0, 0(sp)
    
    addi sp, sp, 24
    ret 

edge:
	addi a1, x0, 77
    j exit2