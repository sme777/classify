.globl matmul

.text
# =======================================================
# FUNCTION: Matrix Multiplication of 2 integer matrices
# 	d = matmul(m0, m1)
# Arguments:
# 	a0 (int*)  is the pointer to the start of m0 
#	a1 (int)   is the # of rows (height) of m0
#	a2 (int)   is the # of columns (width) of m0
#	a3 (int*)  is the pointer to the start of m1
# 	a4 (int)   is the # of rows (height) of m1
#	a5 (int)   is the # of columns (width) of m1
#	a6 (int*)  is the pointer to the the start of d
# Returns:
#	None (void), sets d = matmul(m0, m1)
# Exceptions:
#   Make sure to check in top to bottom order!
#   - If the dimensions of m0 do not make sense,
#     this function terminates the program with exit code 72.
#   - If the dimensions of m1 do not make sense,
#     this function terminates the program with exit code 73.
#   - If the dimensions of m0 and m1 don't match,
#     this function terminates the program with exit code 74.
# =======================================================
matmul:

	#checks m0 is a valid matrix
	addi t0, x0, 1
    blt a1, t0, done1
    blt a2, t0, done1
    #checks m1 is a valid matrix
    blt a4, t0, done2
    blt a5, t0, done2
    #checks m0 dim matches m1 dim
    bne a2, a4, done3
	
    #initalize outer loop counter
	addi t0, x0, 0
    #initialize inner loop counter
    addi t1, x0, 0
    # Prologue
    
	j outer_loop_start

outer_loop_start:
	#checks that the outer loop counter has not reached the end of matrix
	mul t5, a1, a2
    bge t0, t5, outer_loop_end
    #resets the placeholder for matrix 2
    add t2, x0, a3
    j inner_loop_start
	

inner_loop_start:

	bge t1, a6, inner_loop_end

	addi sp, sp, -20
    sw a0, 0(sp)
    sw a1, 4(sp)
    sw a2, 8(sp)
    sw a3, 12(sp)
    sw a4, 16(sp)
    
    #add a0, x0, a0
    add a1, x0, t2
	addi a3, x0, 1
    add a4, x0, a5
    
	j dot
    lw a0, 0(a6)
    addi a6, a6, 4
	#save the returned value
    
    
    lw a4, 16(sp)
    lw a3, 12(sp)
    lw a2, 8(sp)
    lw a1, 4(sp)
    lw a0, 0(sp)
	addi sp, sp, 20


	addi t1, t1, 1
    j inner_loop_end

inner_loop_end:

	bge t1, a6, outer_loop_continue
	addi t2, t2, 4
	j inner_loop_start


outer_loop_continue:
	#make a big jump to the next chunk of the row numbers
    addi t4, x0, 4
    mul t4, a2, t4
    #increment the matrix 1 by 4*col_matrix1
    add a0, a0, t4
    #sets the inner loop counter to 0
    addi t1, x0, 0
    #increments the outer loop counter by 1
    addi t0, t0, 1
	j outer_loop_start
    
outer_loop_end:
    # Epilogue
    #a6 = ...
    
    ret
    
    
done1:
	addi a1, x0, 72
    j exit2
    
done2:
	addi a1, x0, 73
    j exit2
    
done3:
	addi a1, x0, 74
    j exit2
