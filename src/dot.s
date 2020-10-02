.globl dot

.text
# =======================================================
# FUNCTION: Dot product of 2 int vectors
# Arguments:
#   a0 (int*) is the pointer to the start of v0
#   a1 (int*) is the pointer to the start of v1
#   a2 (int)  is the length of the vectors
#   a3 (int)  is the stride of v0
#   a4 (int)  is the stride of v1
# Returns:
#   a0 (int)  is the dot product of v0 and v1
# Exceptions:
# - If the length of the vector is less than 1, 				
#   this function terminates the program with error code 75.	
# - If the stride of either vector is less than 1,				
#   this function terminates the program with error code 76.	
# =======================================================
dot:
	# Prologue
	addi sp, sp -32
    
	sw s0, 0(sp)
    sw s1, 4(sp)
    sw s2, 8(sp)
    sw s3, 12(sp)
    sw s4, 16(sp)
    sw s5, 20(sp)
    sw s6, 24(sp)
    sw ra, 28(sp)

	addi s5, x0, 1
    blt a2, s5, done1
   
	blt a3, s5, done2
    blt a4, s5, done2
    #counter index
    addi s0, x0, 0
    #counter total value
    addi s1, x0, 0
    
    j loop_start

loop_start:

	beq s0, a2, loop_end
	lw s2, 0(a0)			#loads the current element of a0
    lw s3, 0(a1)			#loads the current element of a1
	mul s4, s3, s2			#stores the current product
	add s1, s1, s4			#updates total dot product
	addi s0, s0, 1
	
    #incrmeneting the array
    addi s5, x0, 4
    mul s6, s5, a4
    mul s5, s5, a3
    
    
    add a0, a0, s5
    add a1, a1, s6
    j loop_start
loop_end:
    # Epilogue
    add a0, x0, s1
	
    lw ra, 28(sp)
	lw s6, 24(sp)
    lw s5, 20(sp)
    lw s4, 16(sp)
    lw s3, 12(sp)
    lw s2, 8(sp)
    lw s1, 4(sp)
    lw s0, 0(sp)
    
    addi sp, sp 32
    
    ret
    
    
done1:
	addi a1, x0, 75
	j exit2
    
done2:
	addi a1, x0, 76
    j exit2
