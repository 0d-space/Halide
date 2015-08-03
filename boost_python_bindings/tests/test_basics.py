#!/usr/bin/python3

# to be called via nose, for example
# nosetests-3.4 -v path_to/tests/test_basics.py

from halide import *

def test_types():

    t0 = Int(32)
    t1 = Int(16)

    assert t0 != t1
    assert t0.is_float() == False
    assert t1.is_float() == False

    print("Int(32) type:", Int(32))
    print("Int(16) type:", Int(16))

    return

def test_basics():

    input = ImageParam(UInt(16), 2, 'input')
    x, y = Var('x'), Var('y')

    blur_x = Func('blur_x')
    blur_xx = Func('blur_xx')
    blur_y = Func('blur_y')

    yy = cast(Int(32), 1)
    assert yy.type() == Int(32)
    print("yy type:", yy.type())

    z = x + 1
    input[x,y]
    input[0,0]
    input[z,y]
    input[x+1,y]
    print("ping 0.2")
    input[x,y]+input[x+1,y]

    if False:
        aa = blur_x[x,y]
        bb = blur_x[x,y+1]
        aa + bb
        blur_x[x,y]+blur_x[x,y+1]

    print("ping 0.3")
    (input[x,y]+input[x+1,y]) / 2
    print("ping 0.4")
    blur_x[x,y]
    print("ping 0.4.1")
    blur_xx[x,y] = input[x,y]



    print("ping 0.5")
    blur_x[x,y] = (input[x,y]+input[x+1,y]+input[x+2,y])/3
    print("ping 1")
    blur_y[x,y] = (blur_x[x,y]+blur_x[x,y+1]+blur_x[x,y+2])/3

    xi, yi = Var('xi'), Var('yi')
    print("ping 2")
    #blur_y.tile(x, y, xi, yi, 8, 4).parallel(y).vectorize(xi, 8)
    blur_x.compute_at(blur_y, x).vectorize(x, 8)


    blur_y.compile_jit()
    print("Compiled to jit")

    return


if __name__ == "__main__":
    test_types()
    test_basics()