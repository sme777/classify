from unittest import TestCase
from framework import AssemblyTest, print_coverage


class TestAbs(TestCase):
    def test_zero(self):
        t = AssemblyTest(self, "abs.s")
        # load 0 into register a0
        t.input_scalar("a0", 0)
        # call the abs function
        t.call("abs")
        # check that after calling abs, a0 is equal to 0 (abs(0) = 0)
        t.check_scalar("a0", 0)
        # generate the `assembly/TestAbs_test_zero.s` file and run it through venus
        t.execute()

    def test_one(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", 1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()


    def test_negative_one(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", -1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()

    def test_negative_zero(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", -0)
        t.call("abs")
        t.check_scalar("a0", 0)
        t.execute()

    def test_postive_large_value(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", 43168)
        t.call("abs")
        t.check_scalar("a0", 43168)
        t.execute()

    def test_negative_large_value(self):
        # same as test_zero, but with input 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", -78214)
        t.call("abs")
        t.check_scalar("a0", 78214)
        t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("abs.s", verbose=False)


class TestRelu(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 0, 3, 0, 5, 0, 7, 0, 9])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()

    def test_simple2(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=78)

    def test_long_list(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, -5, -6, 7, 8, -2, 4, 7, 3, -2, 2, -5, 4, -4])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 0, 0, 7, 8, 0, 4, 7, 3, 0, 2, 0, 4, 0])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
    def test_all_negative(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([-1, -5, -6, -7, -8, -2, -4, -7, -3])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        
    def test_all_positive(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, 5, 6, 7, 8, 2, 4, 7, 3, 2, 34, 12, 567, 209])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 5, 6, 7, 8, 2, 4, 7, 3, 2, 34, 12, 567, 209])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute()
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus

    @classmethod
    def tearDownClass(cls):
        print_coverage("relu.s", verbose=False)


class TestArgmax(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        #raise NotImplementedError("TODO")
        # TODO
        # load address of the array into register a0
        # TODO
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])

        #raise NotImplementedError("TODO")
        # TODO
        # load address of the array into register a0
        t.input_array("a0", array0)
        # set a1 to the length of the array
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        t.call("argmax")
        # check that the register a0 contains the correct output
        t.check_scalar("a0", 8)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    def test_simple2(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("argmax")
        # check that the array0 was changed appropriately
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=77)
    
    def test_simple3(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([100, -2, 3, -4, 5, -6, 7, -8, 9])
        #raise NotImplementedError("TODO")
        # TODO
        # load address of the array into register a0
        t.input_array("a0", array0)
        # set a1 to the length of the array
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        t.call("argmax")
        # check that the register a0 contains the correct output
        t.check_scalar("a0", 0)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    def test_simple4(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([100, -2, 3, -4, 500, -6, 7, -8, 9])
        #raise NotImplementedError("TODO")
        # TODO
        # load address of the array into register a0
        t.input_array("a0", array0)
        # set a1 to the length of the array
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        t.call("argmax")
        # check that the register a0 contains the correct output
        t.check_scalar("a0", 4)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()
    
    def test_simple5(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([-100, -2, -3, -4, -500, -6, -7, -8, -9])
        #raise NotImplementedError("TODO")
        # TODO
        # load address of the array into register a0
        t.input_array("a0", array0)
        # set a1 to the length of the array
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        t.call("argmax")
        # check that the register a0 contains the correct output
        t.check_scalar("a0", 1)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()

    def test_hard(self):
        t = AssemblyTest(self, "argmax.s")
        # create an array in the data section
        array0 = t.array([100, 2, 3, 4, 500, 6, 7, 8, 9])
        #raise NotImplementedError("TODO")
        # TODO
        # load address of the array into register a0
        t.input_array("a0", array0)
        # set a1 to the length of the array
        t.input_scalar("a1", len(array0))
        # call the `argmax` function
        t.call("argmax")
        # check that the register a0 contains the correct output
        t.check_scalar("a0", 4)
        # generate the `assembly/TestArgmax_test_simple.s` file and run it through venus
        t.execute()
    @classmethod
    def tearDownClass(cls):
        print_coverage("argmax.s", verbose=False)



class TestDot(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        v0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 9)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 285)
        t.execute()

    def test_simple2(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        v0 = [45, 2, -2, 4, 12, 43, 7, 8, -3]
        v1 = [0, 3, 3, 4, 90, 6, 32, 1, 401]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 9)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 383)
        t.execute()

    def test_stride(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        v0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 2)
        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 22)
        t.execute()

    def test_stride2(self):
        t = AssemblyTest(self, "dot.s")
        # create arrays in the data section
        #raise NotImplementedError("TODO")
        v0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 3)
        t.input_scalar("a4", 2)
        # call the `dot` function
        t.call("dot")
        # check the return value
        # TODO
        t.check_scalar("a0", 48)
        t.execute()

    def test_edgecase1(self):
        t = AssemblyTest(self, "dot.s")
        # create an array in the data section
        
        # load address of `array0` into register a0
        v0 = [45, 2, -2, 4, 12, 43, 7, 8, -3]
        v1 = [0, 3, 3, 4, 90, 6, 32, 1, 401]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 0)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        # set a1 to the length of our array
        
        # call the relu function
        t.call("dot")
        # check that the array0 was changed appropriately
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=75)

    def test_edgecase2(self):
        t = AssemblyTest(self, "dot.s")
        # create an array in the data section
        
        # load address of `array0` into register a0
        v0 = [45, 2, -2, 4, 12, 43, 7, 8, -3]
        v1 = [0, 3, 3, 4, 90, 6, 32, 1, 401]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 9)
        t.input_scalar("a3", 0)
        t.input_scalar("a4", 1)
        # set a1 to the length of our array
        
        # call the relu function
        t.call("dot")
        # check that the array0 was changed appropriately
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=76)

    def test_edgecase3(self):
        t = AssemblyTest(self, "dot.s")
        # create an array in the data section
        
        # load address of `array0` into register a0
        v0 = [45, 2, -2, 4, 12, 43, 7, 8, -3]
        v1 = [0, 3, 3, 4, 90, 6, 32, 1, 401]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 9)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 0)
        # set a1 to the length of our array
        
        # call the relu function
        t.call("dot")
        # check that the array0 was changed appropriately
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=76)


    def test_edgecase4(self):
        t = AssemblyTest(self, "dot.s")
        # create an array in the data section
        
        # load address of `array0` into register a0
        v0 = [45, 2, -2, 4]
        v1 = [0, 3, 3, 4, 90, 6, 32, 1, 401]
        array0 = t.array(v0)
        array1 = t.array(v1)


        # TODO
        # load array addresses into argument registers
        # TODO
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        # load array attributes into argument registers
        # TODO
        t.input_scalar("a2", 9)
        t.input_scalar("a3", 0)
        t.input_scalar("a4", 0)
        # set a1 to the length of our array
        
        # call the relu function
        t.call("dot")
        # check that the array0 was changed appropriately
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=76)

    @classmethod
    def tearDownClass(cls):
        print_coverage("dot.s", verbose=False)


class TestMatmul(TestCase):

    def do_matmul(self, m0, m0_rows, m0_cols, m1, m1_rows, m1_cols, result, code=0):
        t = AssemblyTest(self, "matmul.s")
        # we need to include (aka import) the dot.s file since it is used by matmul.s
        t.include("dot.s")

        # create arrays for the arguments and to store the result
        array0 = t.array(m0)
        array1 = t.array(m1)
        array_out = t.array([0] * len(result))

        # load address of input matrices and set their dimensions
        #raise NotImplementedError("TODO")
        # TODO
        t.input_array("a0", array0)
        t.input_scalar("a1", m0_rows)
        t.input_scalar("a2", m0_cols)
        t.input_array("a3", array1)
        t.input_scalar("a4", m1_rows)
        t.input_scalar("a5", m1_cols)
        t.input_array("a6", array_out)
        # load array attributes into argument registers
        # TODO
        # load address of output array
        # TODO

        # call the matmul function
        t.call("matmul")

        # check the content of the output array
        # TODO
        #t.check_stdout("a6")

        t.check_array(array_out, result)
        # generate the assembly file and run it through venus, we expect the simulation to exit with code `code`
        t.execute(code=code)

    def test_simple(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150]
        )

    def test_simple2(self):
        self.do_matmul(
            [1], 1, 1,
            [1], 1, 1,
            [1]
        )
    def test_simple3(self):
            self.do_matmul(
                [1, 0, 1, 0], 2, 2,
                [1, 0, 1, 0], 2, 2,
                [1, 0, 1, 0]
            )

    def test_hard(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6], 3, 2,
            [1, 2, 3, 4, 7, 8], 2, 3,
            [9, 16, 19, 19, 34, 41, 29, 52, 63]
        )
    def test_hard2(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6], 2, 3,
            [1, 2, 3, 4, 7, 8], 3, 2,
            [28, 34, 61, 76]
        )

    def test_hard3(self):
        self.do_matmul(
            [8, -189, 230, 7, -7], 5, 1,
            [230, 9, 120, -8, 2], 1, 5,
            [1840, 72, 960, -64, 16, -43470,
             -1701, -22680, 1512, -378, 52900,
              2070, 27600, -1840, 460, 1610,
               63, 840, -56, 14, -1610,
                -63, -840, 56, -14]
        )

    def test_edgecase_matmul1(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150], 74
        )
    def test_edgecase_matmul2(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 2,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150], 72
        )
    def test_edgecase_matmul3(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150], 72
        )

    def test_edgecase_matmul4(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150], 73
        )

    def test_edgecase_matmul5(self):
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 0,
            [30, 36, 42, 66, 81, 96, 102, 126, 150], 73
        )




    @classmethod
    def tearDownClass(cls):
        print_coverage("matmul.s", verbose=False)


class TestReadMatrix(TestCase):

    def do_read_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #v0 = t.array(v0)
        t.check_array(rows, [3])
        t.check_array(cols, [3])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
    
    def do_read_matrix2(self, fail='', code=0):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input2.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        #v0 = t.array(v0)
        t.check_array(rows, [4])
        t.check_array(cols, [4])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
    
    def do_read_matrix3(self, fail='', code=0):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input3.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        #v0 = t.array(v0)
        t.check_array(rows, [3])
        t.check_array(cols, [4])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def do_read_matrix4(self, fail='', code=0):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input4.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6]
        #v0 = t.array(v0)
        t.check_array(rows, [2])
        t.check_array(cols, [3])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def do_read_matrix5(self, fail='malloc', code=88):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input4.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6]
        #v0 = t.array(v0)
        t.check_array(rows, [2])
        t.check_array(cols, [3])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def do_read_matrix6(self, fail='fopen', code=90):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input4.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6]
        #v0 = t.array(v0)
        t.check_array(rows, [2])
        t.check_array(cols, [3])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def do_read_matrix7(self, fail='fread', code=91):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input4.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6]
        #v0 = t.array(v0)
        t.check_array(rows, [2])
        t.check_array(cols, [3])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def do_read_matrix8(self, fail='fclose', code=92):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input4.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])

        # load the addresses to the output parameters into the argument registers
        # TODO
        t.input_array("a1", rows)
        t.input_array("a2", cols)


        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        # TODO
        v0 = [1, 2, 3, 4, 5, 6]
        #v0 = t.array(v0)
        t.check_array(rows, [2])
        t.check_array(cols, [3])
        t.check_array_pointer("a0", v0)

        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def test_simple(self):
        self.do_read_matrix()

    def test_simple2(self):
        self.do_read_matrix2()
    
    def test_simple3(self):
        self.do_read_matrix3()

    def test_simple4(self):
        self.do_read_matrix4()

    def test_simple5(self):
        self.do_read_matrix5()

    def test_simple6(self):
        self.do_read_matrix6()

    def test_simple7(self):
        self.do_read_matrix7()

    def test_simple8(self):
        self.do_read_matrix8()

    

    @classmethod
    def tearDownClass(cls):
        print_coverage("read_matrix.s", verbose=False)


class TestWriteMatrix(TestCase):

    def do_write_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        v1 = 3
        v2 = 3
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        t.check_file_output(outfile, "outputs/test_write_matrix/reference.bin")

    def do_write_matrix2(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student2.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([10, -2, 303, 41, 3205, 666, -7, 82, 96, 52, -81, 0])
        v1 = 4
        v2 = 3
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        t.check_file_output(outfile, "outputs/test2.bin")

    def do_write_matrix_tall(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student3.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([1, 3, 5, 7, 11, 34, 45, -42, 0, 8, 601, 32, -98, 
            51, 62, -78, -1, -2, 7, -31, 49, 99, 305, 678, 1, 1, 0, 
            1, 45, 5, 5, 7, -4, 5, 82, -45, 12, 34, 55, 0])
        v1 = 20
        v2 = 2
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        t.check_file_output(outfile, "outputs/test_write_matrix/test3.bin")

    def do_write_matrix_wide(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student4.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([1, 3, 5, 7, 11, 34, 45, -42, 0, 8, 601, 32, -98, 
            51, 62, -78, -1, -2, 7, -31, 49, 99, 305, 678, 1, 1, 0, 
            1, 45, 5, 5, 7, -4, 5, 82, -45, 12, 34, 55, 0])
        v1 = 2
        v2 = 20
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        t.check_file_output(outfile, "outputs/test_write_matrix/test4.bin")

    def do_write_matrix_edge1(self, fail='fopen', code=93):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student2.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([10, -2, 303, 41, 3205, 666, -7, 82, 96, 52, -81, 0])
        v1 = 4
        v2 = 3
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        #t.check_file_output(outfile, "outputs/test2.bin")

    def do_write_matrix_edge2(self, fail='fwrite', code=94):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student2.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([10, -2, 303, 41, 3205, 666, -7, 82, 96, 52, -81, 0])
        v1 = 4
        v2 = 3
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        #t.check_file_output(outfile, "outputs/test2.bin")

    def do_write_matrix_edge3(self, fail='fclose', code=95):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student2.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        #raise NotImplementedError("TODO")

        v0 = t.array([10, -2, 303, 41, 3205, 666, -7, 82, 96, 52, -81, 0])
        v1 = 4
        v2 = 3
        t.input_array("a1", v0)
        t.input_scalar("a2", v1)
        t.input_scalar("a3", v2)
        # TODO
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        #t.check_file_output(outfile, "outputs/test2.bin")


    def test_simple(self):
        self.do_write_matrix()

    def test_simple2(self):
        self.do_write_matrix2()

    def test_long_col(self):
        self.do_write_matrix_tall()

    def test_long_row(self):
        self.do_write_matrix_wide()

    def test_edge1(self):
        self.do_write_matrix_edge1()

    def test_edge2(self):
        self.do_write_matrix_edge2()

    def test_edge3(self):
        self.do_write_matrix_edge3()
    @classmethod
    def tearDownClass(cls):
        print_coverage("write_matrix.s", verbose=False)


class TestClassify(TestCase):

    def make_test(self):
        t = AssemblyTest(self, "classify.s")
        t.include("argmax.s")
        t.include("dot.s")
        t.include("matmul.s")
        t.include("read_matrix.s")
        t.include("relu.s")
        t.include("write_matrix.s")
        return t

    def test_simple0_input0(self):
        t = self.make_test()
        out_file = "outputs/test_basic_main/student0.bin"
        ref_file = "outputs/test_basic_main/reference0.bin"
        args = ["inputs/simple0/bin/m0.bin", "inputs/simple0/bin/m1.bin",
                "inputs/simple0/bin/inputs/input0.bin", out_file]

        t.input_scalar("a0", 5)
        #t.input_array("a1", t.array(args))
        t.input_scalar("a2", 0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args)

        # compare the output file and
        # raise NotImplementedError("TODO")
        # TODO
        t.check_file_output(out_file, ref_file)


        # compare the classification output with `check_stdout`
        t.check_stdout("2")

    def test_simple1_input0(self):
        t = self.make_test()
        out_file = "outputs/test_basic_main/student1.bin"
        ref_file = "outputs/test_basic_main/reference1.bin"
        args = ["inputs/simple1/bin/m0.bin", "inputs/simple1/bin/m1.bin",
                "inputs/simple1/bin/inputs/input0.bin", out_file]

        t.input_scalar("a0", 5)
        #t.input_array("a1", t.array(args))
        t.input_scalar("a2", 0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args)

        # compare the output file and
        # raise NotImplementedError("TODO")
        # TODO
        t.check_file_output(out_file, ref_file)


        # compare the classification output with `check_stdout`
        t.check_stdout("1")

    def test_edge1(self):
        t = self.make_test()
        out_file = "outputs/test_basic_main/student1.bin"
        ref_file = "outputs/test_basic_main/reference1.bin"
        args = ["inputs/simple1/bin/m0.bin", "inputs/simple1/bin/m1.bin",
                "inputs/simple1/bin/inputs/input0.bin", out_file]

        t.input_scalar("a0", 4)
        #t.input_array("a1", t.array(args))
        t.input_scalar("a2", 0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, code=89)

    def test_edge2(self):
        t = self.make_test()
        out_file = "outputs/test_basic_main/student1.bin"
        ref_file = "outputs/test_basic_main/reference1.bin"
        args = ["inputs/simple1/bin/m0.bin", "inputs/simple1/bin/m1.bin",
                "inputs/simple1/bin/inputs/input0.bin", out_file]

        t.input_scalar("a0", 5)
        #t.input_array("a1", t.array(args))
        t.input_scalar("a2", 0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, fail='malloc', code=88)

    def test_edge3(self):
        t = self.make_test()
        out_file = "outputs/test_basic_main/student1.bin"
        ref_file = "outputs/test_basic_main/reference1.bin"
        args = ["inputs/simple1/bin/m0.bin", "inputs/simple1/bin/m1.bin",
                "inputs/simple1/bin/inputs/input0.bin", out_file]

        t.input_scalar("a0", 5)
        #t.input_array("a1", t.array(args))
        t.input_scalar("a2", 7)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args)
        t.check_stdout('')
    

    @classmethod
    def tearDownClass(cls):
        print_coverage("classify.s", verbose=False)


class TestMain(TestCase):

    def run_main(self, inputs, output_id, label):
        args = [f"{inputs}/m0.bin", f"{inputs}/m1.bin", f"{inputs}/inputs/input0.bin",
                f"outputs/test_basic_main/student{output_id}.bin"]
        reference = f"outputs/test_basic_main/reference{output_id}.bin"
        t = AssemblyTest(self, "main.s", no_utils=True)
        t.call("main")
        t.execute(args=args, verbose=False)
        t.check_stdout(label)
        t.check_file_output(args[-1], reference)

    def test0(self):
        self.run_main("inputs/simple0/bin", "0", "2")

    def test1(self):
        self.run_main("inputs/simple1/bin", "1", "1")
