main:
    addi a0, x0, 3      # calculate 5!
    jal ra, factorial
    # result is now in a0
    jal x0, end         # stop here

factorial:
    addi sp, sp, -8     # make space on stack
    sw ra, 4(sp)        # save return address
    sw a0, 0(sp)        # save n

    # if n <= 1, return 1
    addi t0, x0, 1
    ble a0, t0, base    # if a0 <= 1, go to base case

    # recursive case: n * factorial(n-1)
    addi a0, a0, -1     # a0 = n-1
    jal ra, factorial   # call factorial(n-1)
    
    lw t0, 0(sp)        # load n back from stack
    mul a0, a0, t0      # a0 = n * factorial(n-1)

    lw ra, 4(sp)        # restore return address
    addi sp, sp, 8      # free stack
    jalr x0, ra, 0      # return

base:
    addi a0, x0, 1      # return 1
    lw ra, 4(sp)        # restore ra
    addi sp, sp, 8      # free stack
    jalr x0, ra, 0      # return

end:
    nop                 # program ends here


# **Trace for 3!:**
# ```
# factorial(3)
#   → factorial(2)
#       → factorial(1)
#           → returns 1
#       → 2 * 1 = 2
#   → 3 * 2 = 6