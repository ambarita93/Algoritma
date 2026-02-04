#algoritma bisection

a = 0
b = 2.5

TOL= 0.000001
N0 = 1200
def f(x):
    y=x**2-5*x+6
    return y
FA = f(a)
FB = f(b)
if FA*FB < 0:
    for i in range(N0):
        p = a + (b-a)/2
        FP = f(p)

        if FP == 0 or ((b-a)/2)<TOL:
            print('hasil',p,i)
            break
        elif FA*FP > 0:
            print('di elif',p,i,FA,FP)
            a = p
            FA = FP
        elif FA*FP <0:
            b=p
        if i == N0:
            print("Prosedur tidak berhasil meski sudah melalui{} iterasi".format(N0))
else:
    print('Nila f(a)={} dan nilai f(b)={}. Silakan ganti a dan b agar f(a) dan f(b) berbeda tanda'.format(FA,FB))