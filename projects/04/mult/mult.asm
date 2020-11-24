// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// R0 = 4, R1 = 3
/*	int i=0;
	int product=R1;
	while(i < R0){
		product += R1;
		i++;
	}
	R2 = product;
*/

	@i
	M=0
	@product
	M=R1
(LOOP)
	@product
	D=M
	@R0
	D=D-A
	D;JGT
	@R1
	D=M
	@product	
	M=D+M	
	@i
	M=M+1	
	@LOOP
	0;JMP
(END)
	@END
	0;JMP
