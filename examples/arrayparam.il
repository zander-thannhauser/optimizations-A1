.data
    .float .float_const_0, 0.01000000
.text
.frame init, 8, %vr1
    loadI 0 => %vr2
    i2i %vr2 => %vr3
    loadI 10 => %vr4
    i2i %vr4 => %vr5
    loadI 10 => %vr4
    comp %vr3, %vr4 => %vr6
    testge %vr6 => %vr7
    cbr %vr7 -> .L1
.L0: nop
    loadI .float_const_0 => %vr8
    fload %vr8 => %vr9
    f2i %vr9 => %vr10
    mult %vr3, %vr10 => %vr11
    add %vr11, %vr5 => %vr12
    i2i %vr1 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr3, %vr14 => %vr16
    sub %vr17, %vr16 => %vr18
    store %vr12 => %vr18
    loadI 1 => %vr19
    add %vr3, %vr19 => %vr20
    i2i %vr20 => %vr3
    loadI 1 => %vr19
    add %vr5, %vr19 => %vr21
    i2i %vr21 => %vr5
    loadI 10 => %vr4
    comp %vr3, %vr4 => %vr6
    testge %vr6 => %vr7
    cbrne %vr7 -> .L0
.L1: nop
    ret
.frame writearray, 0, %vr22
    loadI 0 => %vr2
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr2, %vr14 => %vr23
    sub %vr17, %vr23 => %vr24
    load %vr24 => %vr25
    iwrite %vr25
    loadI 1 => %vr19
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr19, %vr14 => %vr26
    sub %vr17, %vr26 => %vr27
    load %vr27 => %vr28
    iwrite %vr28
    loadI 2 => %vr29
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr29, %vr14 => %vr30
    sub %vr17, %vr30 => %vr31
    load %vr31 => %vr32
    iwrite %vr32
    loadI 3 => %vr33
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr33, %vr14 => %vr34
    sub %vr17, %vr34 => %vr35
    load %vr35 => %vr36
    iwrite %vr36
    loadI 4 => %vr14
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr14, %vr14 => %vr37
    sub %vr17, %vr37 => %vr38
    load %vr38 => %vr39
    iwrite %vr39
    loadI 5 => %vr40
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr40, %vr14 => %vr41
    sub %vr17, %vr41 => %vr42
    load %vr42 => %vr43
    iwrite %vr43
    loadI 6 => %vr44
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr44, %vr14 => %vr45
    sub %vr17, %vr45 => %vr46
    load %vr46 => %vr47
    iwrite %vr47
    loadI 7 => %vr48
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr48, %vr14 => %vr49
    sub %vr17, %vr49 => %vr50
    load %vr50 => %vr51
    iwrite %vr51
    loadI 8 => %vr52
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr52, %vr14 => %vr53
    sub %vr17, %vr53 => %vr54
    load %vr54 => %vr55
    iwrite %vr55
    loadI 9 => %vr56
    i2i %vr22 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr56, %vr14 => %vr57
    sub %vr17, %vr57 => %vr58
    load %vr58 => %vr59
    iwrite %vr59
    ret
.frame inc, 0, %vr1
    load %vr1 => %vr60
    loadI 1 => %vr19
    add %vr60, %vr19 => %vr61
    load %vr1 => %vr60
    store %vr61 => %vr1
    ret
.frame main, 44 
    loadI 0 => %vr2
    loadI 0 => %vr2
    i2i %vr0 => %vr15
    loadI 40 => %vr64
    sub %vr15, %vr64 => %vr65
    loadI -4 => %vr13
    add %vr65, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr2, %vr14 => %vr23
    sub %vr17, %vr23 => %vr24
    store %vr2 => %vr24
    loadI 0 => %vr2
    loadI 1 => %vr19
    i2i %vr0 => %vr65
    loadI 40 => %vr64
    sub %vr65, %vr64 => %vr68
    loadI -4 => %vr13
    add %vr68, %vr13 => %vr66
    loadI 4 => %vr14
    mult %vr19, %vr14 => %vr26
    sub %vr66, %vr26 => %vr67
    store %vr2 => %vr67
    loadI 0 => %vr2
    loadI 2 => %vr29
    i2i %vr0 => %vr68
    loadI 40 => %vr64
    sub %vr68, %vr64 => %vr71
    loadI -4 => %vr13
    add %vr71, %vr13 => %vr69
    loadI 4 => %vr14
    mult %vr29, %vr14 => %vr30
    sub %vr69, %vr30 => %vr70
    store %vr2 => %vr70
    loadI 0 => %vr2
    loadI 3 => %vr33
    i2i %vr0 => %vr71
    loadI 40 => %vr64
    sub %vr71, %vr64 => %vr74
    loadI -4 => %vr13
    add %vr74, %vr13 => %vr72
    loadI 4 => %vr14
    mult %vr33, %vr14 => %vr34
    sub %vr72, %vr34 => %vr73
    store %vr2 => %vr73
    loadI 0 => %vr2
    loadI 4 => %vr14
    i2i %vr0 => %vr74
    loadI 40 => %vr64
    sub %vr74, %vr64 => %vr77
    loadI -4 => %vr13
    add %vr77, %vr13 => %vr75
    loadI 4 => %vr14
    mult %vr14, %vr14 => %vr37
    sub %vr75, %vr37 => %vr76
    store %vr2 => %vr76
    loadI 0 => %vr2
    loadI 5 => %vr40
    i2i %vr0 => %vr77
    loadI 40 => %vr64
    sub %vr77, %vr64 => %vr80
    loadI -4 => %vr13
    add %vr80, %vr13 => %vr78
    loadI 4 => %vr14
    mult %vr40, %vr14 => %vr41
    sub %vr78, %vr41 => %vr79
    store %vr2 => %vr79
    loadI 0 => %vr2
    loadI 6 => %vr44
    i2i %vr0 => %vr80
    loadI 40 => %vr64
    sub %vr80, %vr64 => %vr83
    loadI -4 => %vr13
    add %vr83, %vr13 => %vr81
    loadI 4 => %vr14
    mult %vr44, %vr14 => %vr45
    sub %vr81, %vr45 => %vr82
    store %vr2 => %vr82
    loadI 0 => %vr2
    loadI 7 => %vr48
    i2i %vr0 => %vr83
    loadI 40 => %vr64
    sub %vr83, %vr64 => %vr86
    loadI -4 => %vr13
    add %vr86, %vr13 => %vr84
    loadI 4 => %vr14
    mult %vr48, %vr14 => %vr49
    sub %vr84, %vr49 => %vr85
    store %vr2 => %vr85
    loadI 0 => %vr2
    loadI 8 => %vr52
    i2i %vr0 => %vr86
    loadI 40 => %vr64
    sub %vr86, %vr64 => %vr89
    loadI -4 => %vr13
    add %vr89, %vr13 => %vr87
    loadI 4 => %vr14
    mult %vr52, %vr14 => %vr53
    sub %vr87, %vr53 => %vr88
    store %vr2 => %vr88
    loadI 0 => %vr2
    loadI 9 => %vr56
    i2i %vr0 => %vr89
    loadI 40 => %vr64
    sub %vr89, %vr64 => %vr92
    loadI -4 => %vr13
    add %vr92, %vr13 => %vr90
    loadI 4 => %vr14
    mult %vr56, %vr14 => %vr57
    sub %vr90, %vr57 => %vr91
    store %vr2 => %vr91
    i2i %vr92 => %vr63
    i2i %vr63 => %vr1
    call init, %vr1
    call writearray, %vr1
    loadI 0 => %vr2
    i2i %vr2 => %vr3
    loadI 9 => %vr56
    comp %vr3, %vr56 => %vr93
    testgt %vr93 => %vr94
    cbr %vr94 -> .L3
.L2: nop
    i2i %vr1 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr3, %vr14 => %vr16
    sub %vr17, %vr16 => %vr18
    load %vr18 => %vr95
    loadI 1 => %vr19
    add %vr3, %vr19 => %vr20
    mult %vr95, %vr20 => %vr96
    i2i %vr1 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr3, %vr14 => %vr16
    sub %vr17, %vr16 => %vr18
    store %vr96 => %vr18
    i2i %vr1 => %vr15
    loadI -4 => %vr13
    add %vr15, %vr13 => %vr17
    loadI 4 => %vr14
    mult %vr3, %vr14 => %vr16
    sub %vr17, %vr16 => %vr18
    call inc, %vr18
    loadI 1 => %vr19
    add %vr3, %vr19 => %vr20
    i2i %vr20 => %vr3
    loadI 9 => %vr56
    comp %vr3, %vr56 => %vr93
    testgt %vr93 => %vr94
    cbrne %vr94 -> .L2
.L3: nop
    call writearray, %vr1
    ret
