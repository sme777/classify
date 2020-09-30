.globl relu

.text
# ==============================================================================
# FUNCTION: Performs an inplace element-wise ReLU on an array of ints
# Arguments:
# 	a0 (int*) is the pointer to the array
#	a1 (int)  is the # of elements in the array
# Returns:
#	None
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 78.
# ==============================================================================
relu:
    # Prologue
    addi t5, x0, 1
    blt a1, t5, edge
    addi t0, x0, 0

loop_start:
	beq t0, a1, loop_end
	lw t1, 0(a0)
    bge t1, x0, loop_continue
    addi t1, x0, 0
    sw t1, 0(a0)
    
loop_continue:
    addi a0, a0, 4
    addi t0, t0, 1
    j loop_start
    
loop_end:

    # Epilogue
    ret
    
edge:
	addi a1, x0, 78
    j exit2
