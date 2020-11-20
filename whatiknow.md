# What I can use and short notes on those chips 

> Nand : Not and And 
	- 2 inputs and 1 output. out 1 when both are 0 out is 0 otherwise
> Or : 2 inps and 1 out
	- either or both inputs are true then out is also true false otherwise
> Or8Way : 8 inputs 1 output
	- Doing the or operator on every output. Out = 1 or 2 or 3 ... or 8 
> Or16 : 
	- 16 bit Or. meaning 16 inputs 16 outputs
> XOR : Exclusive or meaning that it returns true(1) only when both inputs are not same for example ( 0 1 or 1 0 )
> Multiplexers(Mux): selecting one inp out of many depending on the sel variable
	- Mux - 2 1-bit inp 1 sel 1 1-bit out
	- Mux16 - 2 16-bit inputs 1 sel and 1 16-bit out
		```
			for i = 0..15 in out[i] = in[i] if sel == 1; 0 otherwise
		```
	- Mux4Way16 - 4 16-bit inputs, 2 sel, 1 16-bit out
		```
			out = a if sel == 0(sel[1]) 0(sel[0])
				= b if sel == 0 1
				= c if sel == 1 0 
				= d if sel == 1 1
			Note: the hdl language gives the sel in a wierd way. sel[0] is the last digit
		```
	- Mux8Way16 - 8 16-bit inputs, 3 sel, 1 16-bit output
		```
			same as before but with sel like -- 0 0 0 or 1 1 1 or 1 0 1 -- 
		```
> De Multiplexors(DMux): Takes some arbitrary input and positions it based on a sel variable
	- DMux - 1 in, 1 sel, 2 out
		```
			{a,b} : {in,0} if sel = 0
					{0,in} if sel = 1
		```
	- DMux4Way - 1 inp, 2 sel, 4 out
		```
			{a,b,c,d} : {in,0,0,0} if sel == 0 0
						{0,in,0,0} if sel == 0 1
						{0,0,in,0} if sel == 1 0
						{0,0,0,in} if sel == 1 1
		```
	- DMux8way - 1 inp, 3 sel 8 out
		```
			{a,b,c,d,e,f,g,h} : {in,0,0,0,0,0,0,0} if sel == 0 0 0 
								...
								...
								...
								{0,0,0,0,0,0,0,in} if sel == 1 1 1 
		```
