def ponto_fixo_iteracao(f, p0, TOL=0.00000001, NMAX=10):
    for i in range(NMAX):
        p = f(p0)
        if abs(p - p0) < TOL:
            return p
        p0 = p
        print(p)
    return p