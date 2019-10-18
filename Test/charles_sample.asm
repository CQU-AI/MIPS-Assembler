Let A=-1.278*10^3, B=-3.90625*10^-1, the two numbers store in 16-digit NVIDIA mode. Assume that the Storage mode contains guard,round and sticky bit, and
round to nearest even. Load A,B to registers in 16-digit NVIDIA mode and calculate the sum of A and B.



Main:
addi $s1, $zero, 1          #load a plus or minus

sll $s1, $s1, 5                  #load a index
addi $s1, $s1, 10       
addi $s1, $s1, 15           

sll $s1, $s1, 10                #load a mantissa
addi $s1, $s1, 253

sll $s1, $s1, 1                  #load a guard
addi $s1, $s1, 0

sll $s1, $s1, 1                   #load a round
addi $s1, $s1, 0

sll $s1, $s1, 1                   #load a sticky
addi $s1, $s1, 0


addi $s2, $zero, 1          #load b plus or minus

sll $s2, $s2, 5                  #load b index
addi $s2, $s2, 10       
addi $s2, $s2, 15           

sll $s2, $s2, 10                #load b mantissa
addi $s2, $s2, 0

sll $s2, $s2, 1                  #load b guard
addi $s2, $s2, 0

sll $s2, $s2, 1                   #load b round
addi $s2, $s2, 1

 sll $s2, $s2, 1                   #load b sticky
addi $s2, $s2, 1


Jugdx:                               #judge which mantissa is larger
addi $t8,$zero,4095
and $s3,$s1,$t8
 
and $s4,$s2,$t8

slt $t0, $s3,$s4
beq $t0, $zero, S2s
j S1s


S1s:                                 #get plus 
srl $s5,$s1,18
srl $s6,$s2,18

beq $s5,$s6, Adds
j Exchange


S2s:                            #exchange and jump to s1s
add $t0, $s3,$zero
add $s3,$s4,$zero
add $s4,$t0,$zero
j S1s


Exchange:
add $t0, $s3,$zero
add $s3,$s4,$zero
add $s4,$t0,$zero
addi $s5,$zero,1
j  Subtract


Subtract:
sub $s7,$s3,$s4
j Resultf


Adds:
add $s7,$s3,$s4
j Resultf


Resultf:                       #combine the number and judge how to output
addi $t0,$zero,6
addi $t3,$zero,5
and $t1,$s7,$t0

slt $t2, $t1,$t3
beq $t2, $zero, Result2
j Result1


Result1:
addi $t0,$zero,31
addi $t2,$zero,2

add $s0, $zero, $s5
#add $t3, $s0, $zero
sll $s0, $s0, 5 
#add $t4, $s0, $zero

srl $t1, $s1, 13
and $t1,$t1,$t0
add $s0, $s0, $t1

sll $s0, $s0, 13
add $s0, $s0, $s7
#add $t5, $s0, $zero
srl $s0, $s0, 3  
sll $s0, $s0, 3  
#add $t6, $s0, $zero
j Done


Result2:
addi $t0,$zero,31
addi $t2,$zero,2

add $s0, $zero, $s5
sll $s0, $s0, 5 

srl $t1, $s1, 13
and $t1,$t1,$t0
add $s0, $s0, $t1

sll $s0, $s0, 13
add $s0, $s0, $s7
srl $s0, $s0, 3  
sll $s0, $s0, 3
addi $s0, $s0, 8
j Done

Done:
#the final result is in $s0, it’s 1 11001 0011111110 000
#which means -  25   0011111110
#in Decimal system is -1.278*10^3
