// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// kind of makes sense. 

// Put your code here.

	@R0             
	D=M             //D=RAM[R0]
	@i
	M=D             //RAM[i]=R0
	@R2
	M=0             //RAM[R2]=0
(LOOP)
	@i
	D=M             //D=RAM[i]
	@END
	D;JEQ           //if i==0 goto END
	@R1
	D=M             //D=RAM[R1]
	@R2             
	M=D+M           //RAM[R2]=R1+RAM[R2]
	@i
	M=M-1           //i--
	@LOOP
	0;JMP
(END)
	@END
	0;JMP
