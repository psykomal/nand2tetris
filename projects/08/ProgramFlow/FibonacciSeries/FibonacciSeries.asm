// // push ARG 1

	@ARG
	D=M
	@1
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop pointer 1

	@3
	D=A
	@1
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// // push constant 0

	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop THAT 0

	@THAT
	D=M
	@0
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// // push constant 1

	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop THAT 1

	@THAT
	D=M
	@1
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// // push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // push constant 2

	@2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop ARG 0

	@ARG
	D=M
	@0
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// label None$MAIN_LOOP_START
(None$MAIN_LOOP_START)
// // push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// if-goto None$COMPUTE_ELEMENT
	@SP
	AM = M-1
	D = M
	@None$COMPUTE_ELEMENT
	D; JNE
// goto None$END_PROGRAM
	@None$END_PROGRAM
	0; JMP
// label None$COMPUTE_ELEMENT
(None$COMPUTE_ELEMENT)
// // push THAT 0

	@THAT
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // push THAT 1

	@THAT
	D=M
	@1
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// add
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M+D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop THAT 2

	@THAT
	D=M
	@2
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// // push pointer 1

	@3
	D=A
	@1
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // push constant 1

	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// add
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M+D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop pointer 1

	@3
	D=A
	@1
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// // push ARG 0

	@ARG
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // push constant 1

	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop ARG 0

	@ARG
	D=M
	@0
	D=A+D
	@R13
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@R13
	A=M
	M=D
// goto None$MAIN_LOOP_START
	@None$MAIN_LOOP_START
	0; JMP
// label None$END_PROGRAM
(None$END_PROGRAM)
