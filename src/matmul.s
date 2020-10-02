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

	#Prologue
    
    addi sp, sp -44
    sw s0, 0(sp)
    sw s1, 4(sp)
    sw s2, 8(sp)
    sw s3, 12(sp)
    sw s4, 16(sp)
    sw s5, 20(sp)
    sw s6, 24(sp)
    sw s7, 28(sp)
    sw s8, 32(sp)
    sw s9, 36(sp)
    sw ra, 40(sp)
    
	addi s0, x0, 1
    blt a1, s0, done1
    blt a2, s0, done1
    #checks m1 is a valid matrix
    blt a4, s0, done2
    blt a5, s0, done2
    #checks m0 dim matches m1 dim
    bne a2, a4, done3
    #initalize outer loop counter
	addi s0, x0, 0
    #initialize inner loop counter
    addi s1, x0, 0
    
    add s2, x0, a0
    add s3, x0, a1
    add s4, x0, a2
    add s5, x0, a3
    add s6, x0, a4
    add s7, x0, a5
    add s8, x0, a6
    add s9, x0, a3
	j outer_loop_start

outer_loop_start:
	#checks that the outer loop counter has not reached the end of matrix
    bge s0, s3, outer_loop_end
    #resets the placeholder for matrix 2
    add s5, x0, s9
    j inner_loop_start
	

inner_loop_start:

	bge s1, s7, inner_loop_end

    add a0, x0, s2
    add a1, x0, s5
    add a2, x0, s4
	addi a3, x0, 1
    add a4, x0, s7
    #perform dot product
	jal ra dot
    #save the returned value
    sw a0, 0(s8)
    addi s5, s5, 4
	addi s8, s8, 4
	#increment inner loop counter
	addi s1, s1, 1
    j inner_loop_end

inner_loop_end:

	bge s1, s7, outer_loop_continue
	j inner_loop_start


outer_loop_continue:
	#make a big jump to the next chunk of the row numbers
    addi t1, x0, 4
    mul t1, s4, t1
    #increment the matrix 1 by 4*col_matrix1
    add s2, s2, t1
    #sets the inner loop counter to 0
    addi s1, x0, 0
    #increments the outer loop counter by 1
    addi s0, s0, 1
	j outer_loop_start
    
outer_loop_end:
    # Epilogue
    lw ra, 40(sp)
    lw s9, 36(sp)
    lw s8, 32(sp)
    lw s7, 28(sp)
    lw s6, 24(sp)
    lw s5, 20(sp)
    lw s4, 16(sp)
    lw s3, 12(sp)
    lw s2, 8(sp)
    lw s1, 4(sp)
    lw s0, 0(sp)
    addi sp, sp 44
    
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
