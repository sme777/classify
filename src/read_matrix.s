.globl read_matrix

.text
# ==============================================================================
# FUNCTION: Allocates memory and reads in a binary file as a matrix of integers
#
# FILE FORMAT:
#   The first 8 bytes are two 4 byte ints representing the # of rows and columns
#   in the matrix. Every 4 bytes afterwards is an element of the matrix in
#   row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is a pointer to an integer, we will set it to the number of rows
#   a2 (int*)  is a pointer to an integer, we will set it to the number of columns
# Returns:
#   a0 (int*)  is the pointer to the matrix in memory
# Exceptions:
# - If malloc returns an error,
#   this function terminates the program with error code 88.
# - If you receive an fopen error or eof, 
#   this function terminates the program with error code 90.
# - If you receive an fread error or eof,
#   this function terminates the program with error code 91.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 92.
# ==============================================================================
read_matrix:

    # Prologue
    addi sp, sp, -44
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
	
    #stores filename
    add s0, x0, a0
    
    #saving pointer for row integer
    add s9, x0, a1
    
    #saving pointer for col integer
    add s8, x0, a2
    
    add a1, x0, s0
    addi a2, x0, 0
    
    #opening the file
    jal ra fopen
    blt a0, x0, edge2
    
    #saving the file descriptor
    add s1, x0, a0
    
    
    #allocating memory for row value
    #addi a0, x0, 4
    #jal ra malloc
    #checking if malloc failed
    #bge x0, a0, edge1 
    #saving pointer to allocated memory for row
    #add s9, x0, a0
    
    #allocating memory for column value
    #addi a0, x0, 4
    #jal ra malloc
    #checking if malloc failed
    #bge x0, a0, edge1 
    #saving pointer to allocated memory for column
    #add s8, x0, a0
    
    
	#making argument for reading 4 bytes
    addi a3, x0, 4
    
    #pointing a1 to file descriptor
    add a1, s1, x0
  
    #pointing a2 to the buffer for row
    add a2, x0, s9
    #reading the row number 
    jal ra fread
    lw s6, 0(s9)
    addi a3, x0, 4
    #checking for error in fread
    blt a0, x0, edge3
    blt a0, a3, edge3
    blt a3, a0, edge3
    
    #pointing a2 to the buffer for column
    add a2, x0, s8
    #reading the column number
    jal ra fread
    lw s5, 0(s8)
    addi a3, x0, 4
    #checking for error in fread
    blt a0, x0, edge3
    blt a0, a3, edge3
    blt a3, a0, edge3
    
    #allocating memory for the matrix
    #number of matrix elements
    mul s2, s5, s6 #check if s2 is actual matrix size
    #number of bytes to allocate for storing matrix
    slli a0, s2, 2
    jal ra malloc
    #checking if malloc failed
    bge x0, a0, edge1 
    #saving pointer to allocated memory for the matrix
    add s7, x0, a0
    
    #reading values into the matrix thingy
    #number of bytes to read
    slli a3, s2, 2
    #pointing file descriptor
    add a1, s1, x0
    #pointing buffer
    add a2, s7, x0
    #reading
    jal ra fread
    slli a3, s2, 2
    #checking for error in fread
    blt a0, x0, edge3
    blt a0, a3, edge3
    blt a3, a0, edge3
    
    #pointing a0 to our matrix
    add a1, s1, x0
    ebreak
    jal ra fclose
    blt a0, x0, edge4
    
    
    add a1, x0, s8
    add a2, x0, s9
    add a0, x0, s7
    
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
    lw ra, 40(sp)
    addi sp, sp, 44
    
    ret
    
	
	
    
edge1:
	addi a1, x0, 88
    j exit2

edge2:
	addi a1, x0, 90
    j exit2

edge3:
	addi a1, x0, 91
    j exit2

edge4:
	addi a1, x0, 92
    j exit2

