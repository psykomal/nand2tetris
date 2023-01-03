// // push constant 0

	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
// // pop LCL 0

	@LCL
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
// label None$LOOP_START
(None$LOOP_START)
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
// // push LCL 0

	@LCL
	D=M
	@0
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
// // pop LCL 0

	@LCL
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
// if-goto None$LOOP_START
	@SP
	AM = M-1
	D = M
	@None$LOOP_START
	D; JNE
// // push LCL 0

	@LCL
	D=M
	@0
	A=A+D
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
