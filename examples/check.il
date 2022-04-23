.data
    .string .str_const_0, "SUCCESS"
.text
.frame main, 12 
    loadI 1 => %vr1
    i2i %vr1 => %vr2
    loadI 0 => %vr3
    i2i %vr3 => %vr4
    loadI 10 => %vr5
    i2i %vr5 => %vr6
    loadI 10 => %vr5
    comp %vr2, %vr5 => %vr7
    testgt %vr7 => %vr8
    cbr %vr8 -> .L1
.L0: nop
    loadI 0 => %vr3
    comp %vr2, %vr3 => %vr9
    testge %vr9 => %vr10
    cbr %vr10 -> .L3
    loadI 1 => %vr1
    mod %vr6, %vr1 => %vr11
    i2i %vr11 => %vr4
.L3: nop
    loadI 1 => %vr1
    add %vr2, %vr1 => %vr12
    i2i %vr12 => %vr2
    loadI 10 => %vr5
    comp %vr2, %vr5 => %vr7
    testgt %vr7 => %vr8
    cbrne %vr8 -> .L0
.L1: nop
    loadI .str_const_0 => %vr13
    swrite %vr13
    ret
