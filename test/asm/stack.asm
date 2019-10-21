addi $t1, $zero, 1
addi $t2, $zero, 2
addi $t3, $zero, 3
addi $sp, $sp, -12
sw $t1, 8($sp)
sw $t2, 4($sp)
sw $t3, 0($sp)
lw $t4, 0($sp)
lw $t5, 4($sp)
lw $t6, 8($sp)
addi $sp, $sp, 12
