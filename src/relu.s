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
    addi sp, sp, -16
    sw s0, 0(sp)
    sw s1, 4(sp)
    sw s5, 8(sp)
    sw ra, 12(sp)
    
    addi s5, x0, 1
    blt a1, s5, edge
    addi s0, x0, 0

loop_start:
	beq s0, a1, loop_end
	lw s1, 0(a0)
    bge s1, x0, loop_continue
    addi s1, x0, 0
    sw s1, 0(a0)
    
loop_continue:
    addi a0, a0, 4
    addi s0, s0, 1
    j loop_start
    
loop_end:

    # Epilogue
    lw ra, 12(sp)
    lw s5, 8(sp)
    lw s1, 4(sp)
    lw s0, 0(sp)
    addi sp, sp, 16
    ret
    
edge:
	addi a1, x0, 78
    j exit2
