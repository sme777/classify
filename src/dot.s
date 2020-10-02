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
# - If the length of the vector is less than 1, 				#done
#   this function terminates the program with error code 75.	#done
# - If the stride of either vector is less than 1,				#done
#   this function terminates the program with error code 76.	#done
# =======================================================
dot:

	addi sp, sp -28
	sw t0, 0(sp)
    sw t1, 4(sp)
    sw t2, 8(sp)
    sw t3, 12(sp)
    sw t4, 16(sp)
    sw t5, 20(sp)
    sw t6, 24(sp)
    


	addi t5, x0, 1
    blt a2, t5, done1
    # Prologue
	blt a3, t5, done2
    blt a4, t5, done2
    #counter index
    addi t0, x0, 0
    #counter total value
    addi t1, x0, 0
    
    j loop_start

loop_start:

	beq t0, a2, loop_end
	lw t2, 0(a0)			#loads the current element of a0
    lw t3, 0(a1)			#loads the current element of a1
	mul t4, t3, t2			#stores the current product
	add t1, t1, t4			#updates total dot product
	addi t0, t0, 1
	
    #incrmeneting the array
    addi t5, x0, 4
    mul t6, t5, a4
    mul t5, t5, a3
    
    
    add a0, a0, t5
    add a1, a1, t6
    j loop_start
loop_end:
    # Epilogue
    add a0, x0, t1
    
   
	lw t6, 24(sp)
    lw t5, 20(sp)
    lw t4, 16(sp)
    lw t3, 12(sp)
    lw t2, 8(sp)
    lw t1, 4(sp)
    lw t0, 0(sp)
    addi sp, sp 28
    
    ret
    
    
done1:
	addi a1, x0, 75
	j exit2
    
done2:
	addi a1, x0, 76
    j exit2
