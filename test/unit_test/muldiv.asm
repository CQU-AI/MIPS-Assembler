addi $s1, $0, 0xacdb
addi $s2, $0, 0x7f7f7f7f
mult  $s1, $s2
mfhi $t1
mflo $t2
div $s2, $s1
mfhi $t3
mflo $t4