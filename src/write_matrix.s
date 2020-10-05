.globl write_matrix

.text
# ==============================================================================
# FUNCTION: Writes a matrix of integers into a binary file
# FILE FORMAT:
#   The first 8 bytes of the file will be two 4 byte ints representing the
#   numbers of rows and columns respectively. Every 4 bytes thereafter is an
#   element of the matrix in row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is the pointer to the start of the matrix in memory
#   a2 (int)   is the number of rows in the matrix
#   a3 (int)   is the number of columns in the matrix
# Returns:
#   None
# Exceptions:
# - If you receive an fopen error or eof,
#   this function terminates the program with error code 93.
# - If you receive an fwrite error or eof,
#   this function terminates the program with error code 94.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 95.
# ==============================================================================
write_matrix:

    # Prologue
	addi sp, sp, -52
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
    sw a2, 40(sp)
    sw a3, 44(sp)
    sw ra, 48(sp)

	
	#saving function arguments
    add s0, x0, a0
	add s1, x0, a1
    add s2, x0, a2
    add s3, x0, a3
	
	#open file and save desrciptor
	add a1, x0, s0
    addi a2, x0, 1
    jal ra fopen
	blt a0, x0, edge1
    #saves descriptor
    add s4, x0, a0
    
    #settign arguments for fwrite
    
    #setting file descriptor
    add a1, x0, s4
    #setting buffer to read from
    
    #sw s2, 0(s9)
    #add a2, x0, s9      #FIXME maybe not buffer
    lw s2, 40(sp)
    lw a2, 0(s2)
    #setting number of items
    addi a3, x0, 1
    #setting the size of item
    addi a4, x0, 4
    
    #writing rows
    jal ra fwrite
    addi a3, x0, 1
    blt a0, a3, edge2
    
    #settign arguments for fwrite
    
    #setting file descriptor
    add a1, x0, s4
    #setting buffer to read from
  	#FIXME maybe not buffer
    lw s3, 44(sp)
    lw a2, 0(s3)
    #add a2, x0, s3 
    #setting number of items
    addi a3, x0, 1
    #setting the size of item
    addi a4, x0, 4
    
    
    #writing cols
    jal ra fwrite
    addi a3, x0, 1
    blt a0, a3, edge2
    
    #setting file descriptor
    add a1, x0, s4
    #setting buffer to read from
    add a2, x0, s1	#FIXME maybe not buffer
    #setting number of items
    mul a3, s2, s3
    #setting the size of item
    addi a4, x0, 4
    
    
    #writing cols
    jal ra fwrite
    addi a3, x0, 1
    blt a0, a3, edge2
    
    #calling flclose
    add a1, x0, s4
    jal ra fclose
    blt a0, x0, edge3
    
    # Epilogue
	lw s0, 0(sp)
    lw s1, 4(sp)
    lw s2, 8(sp)
    lw s3, 12(sp)
    lw s4, 16(sp)
    lw s5, 20(sp)
    lw s6, 24(sp)
    lw s7, 28(sp)
    lw s8, 32(sp)
    lw s9, 36(sp)
    lw a2, 40(sp)
    lw a3, 44(sp)
    lw ra, 48(sp)
    addi sp, sp, 52

    ret
    
    
edge1:
	addi a1, x0, 93
    j exit2
    
edge2:
	#implement flush
	addi a1, x0, 94
    j exit2
    
edge3:
	addi a1, x0, 95
    j exit2
