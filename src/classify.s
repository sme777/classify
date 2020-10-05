.globl classify

.text
classify:
    # =====================================
    # COMMAND LINE ARGUMENTS
    # =====================================
    # Args:
    #   a0 (int)    argc
    #   a1 (char**) argv
    #   a2 (int)    print_classification, if this is zero, 
    #               you should print the classification. Otherwise,
    #               this function should not print ANYTHING.
    # Returns:
    #   a0 (int)    Classification
    # Exceptions:
    # - If there are an incorrect number of command line args,
    #   this function terminates the program with exit code 89.
    # - If malloc fails, this function terminats the program with exit code 88.
    #
    # Usage:
    #   main.s <M0_PATH> <M1_PATH> <INPUT_PATH> <OUTPUT_PATH>
    
    #PROLOGUE
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
    sw s10, 40(sp)
    sw s11, 44(sp)
    sw ra, 48(sp)
    
    
    #Checking if correct number of args
    addi s0, x0, 5
    bne a0, s0, edge1
    
    #Saving passed in arguments
    add s0, x0, a0
    add s1, x0, a1
    add s2, x0, a2
    
	# =====================================
    # LOAD MATRICES
    # =====================================
    
    # Arguments for read_matrix:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is a pointer to an integer, we will set it to the number of rows
#   a2 (int*)  is a pointer to an integer, we will set it to the number of columns
# Returns:
#   a0 (int*)  is the pointer to the matrix in memory

    # Load pretrained m0
    # Setting arguments for read_matrix
    # Setting filename (a0)
    lw a0, 4(s1)
    
    #Pointing to int for number of rows
    addi sp, sp, -4
    sw s3, 0(sp)
    add a1, x0, sp
    
    #Pointing to int for number of columns
    addi sp, sp, -4
    sw s4, 0(sp)
    add a2, x0, sp
    
    jal ra read_matrix
    
    #saving pointer to returned matrix m0
    add s5, x0, a0
    #saving numrows m0 
    lw t0, 0(a1)
    #saving numcols m0
    lw t1, 0(a2)
    
    lw s4, 0(sp)
    addi sp, sp, 4
    lw s3, 0(sp)
    addi sp, sp, 4
    
    
    
    
    # Load pretrained m1
    # Setting arguments for read_matrix
    # Setting filename (a0)
    lw a0, 8(s1)
    
    #Pointing to int for number of rows
    addi sp, sp, -4
    sw s3, 0(sp)
    add a1, x0, sp
    
    #Pointing to int for number of columns
    addi sp, sp, -4
    sw s4, 0(sp)
    add a2, x0, sp
    
    jal ra read_matrix
    
    #saving pointer to returned matrix m1
    add s6, x0, a0
    #saving numrows m1
    lw t2, 0(a1)
    #saving numcols m1
    lw t3, 0(a2)
    
    
    lw s4, 0(sp)
    addi sp, sp, 4
    lw s3, 0(sp)
    addi sp, sp, 4


    # Load input matrix
    # Setting arguments for read_matrix
    # Setting filename (a0)
    lw a0, 12(s1)
    
    #Pointing to int for number of rows
    addi sp, sp, -4
    sw s3, 0(sp)
    add a1, x0, sp
    
    #Pointing to int for number of columns
    addi sp, sp, -4
    sw s4, 0(sp)
    add a2, x0, sp
    
    jal ra read_matrix
    
    #saving pointer to returned matrix input
    add s7, x0, a0
    #saving numrows input
    lw t4, 0(a1)
    #saving numcols input
    lw t5, 0(a2)
    
    lw s4, 0(sp)
    addi sp, sp, 4
    lw s3, 0(sp)
    addi sp, sp, 4

    # =====================================
    # RUN LAYERS
    # =====================================
    # 1. LINEAR LAYER:    m0 * input
    # 2. NONLINEAR LAYER: ReLU(m0 * input)
    # 3. LINEAR LAYER:    m1 * ReLU(m0 * input)
    
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
    
    # GENERATING FIRST LAYER (HIDDEN)
    #setting first rows
    add a1, t0, x0
    #setting first cols
    add a2, t1, x0
    #setting third matrix pointer
    add a3, s7, x0
    #setting second rows
    add a4, t4, x0
    #setting second cols
    add a5, t5, x0
    
    #allocating memory for the product
    #allocating memory for the matrix
    #number of matrix elements
    mul s3, a1, a5 #check if s2 is actual matrix size
    #number of bytes to allocate for storing matrix
    slli a0, s3, 2
    jal ra malloc
    #checking if malloc failed
    bge x0, a0, edge2 
    #saving pointer to allocated memory for the matrix for matmul
    add a6, x0, a0
    
    #setting first matrix pointer
    add a0, s5, x0
    
    jal ra matmul
    
    
    ebreak
    #storing the hidden layer 
    add s8, a6, x0
    
    
    # GENERATING SECOND LAYER
    # Arguments for relu:
# 	a0 (int*) is the pointer to the array
#	a1 (int)  is the # of elements in the array
# Returns:
#	None
	#point to hidden layer
    add a0, s8, x0
    #number of elements
    mul a1, t0, t5
    
    
    # GENERATING THIRD LAYER (SCORES)
    #setting second (m1) rows
    add a1, t2, x0
    #setting second (m1) cols
    add a2, t3, x0
    #setting third matrix pointer (to hidden layer matrix)
    add a3, s8, x0
    #setting hidden rows
    add a4, t0, x0
    #setting hidden cols
    add a5, t5, x0
    
    #allocating memory for the product
    #allocating memory for the matrix
    #number of matrix elements
    mul s3, a1, a5 #check if s2 is actual matrix size
    #number of bytes to allocate for storing matrix
    slli a0, s3, 2
    jal ra malloc
    #checking if malloc failed
    bge x0, a0, edge2 
    #saving pointer to allocated memory for the matrix for matmul
    add a6, x0, a0
    
    #setting second (m1) matrix pointer
    add a0, s6, x0
    
    jal ra matmul
    
    #storing the scores
    add s9, a6, x0
    
    # =====================================
    # WRITE OUTPUT
    # =====================================
    # Write output matrix
    
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
	
    lw a0, 16(s1)
    add a1, s9, x0
    add a2, t2, x0
    add a3, t5, x0
    
    jal ra write_matrix
    
    
    # =====================================
    # CALCULATE CLASSIFICATION/LABEL
    # =====================================
    # Call argmax
    
    # Arguments:
# 	a0 (int*) is the pointer to the start of the vector
#	a1 (int)  is the # of elements in the vector
# Returns:
#	a0 (int)  is the first index of the largest element

	add a0, s9, x0
    mul a1, t2, t5
    jal ra argmax
    add s10, a0, x0
    
    

	#Freeing memory
    add a1, s8, x0
    jal ra free
    add a1, s9, x0
    jal ra free

	# FIXME ADD CONDITION CHECKING A2 THAT WAS PASSED IN
    # Print classification
    bne s2, x0, no_print
    add a1, s10, x0
    jal ra print_int
    # Print newline afterwards for clarity
    li a1, '\n'
    jal print_char
    
    #PROLOGUE
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
    lw s10, 40(sp)
    lw s11, 44(sp)
    lw ra, 48(sp)
    addi sp, sp, 52

	#FIX ME: DON'T FORGET TO FREE MEMORY
    ret
    
    
edge1:
	addi a1, x0, 89
    j exit2
	
edge2:
	addi a1, x0, 88
    j exit2
    
no_print:
	ret
    

