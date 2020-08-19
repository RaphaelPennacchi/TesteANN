def bissecao(f, a, b, TOL, MAXIT):
    fa = f(a)
    for i in range(MAXIT):
        c = (a + b) / 2 
        if (fc:= f(c)) == 0 or (b - a) / 2 <= TOL:
            return c
        if fa * fc > 0:
            a = c
        else:
            b = c
    return c

def newton(f, df, p0, TOL, MAXIT):
    for i in range(MAXIT):
        p = p0 - f(p0) / df(p0)
        if abs(p - p0) < TOL:
            return p
        p0 = p
    return p

def secantes(f, p0, p1, TOL, MAXIT):
    q0, q1 = f(p0), f(p1)
    for i in range(1, MAXIT):
        p = p1 - (q1 * (p1 - p0)) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p
        p0, q0, p1, q1 = p1, q1, p, f(p)
    return p

def posicao_falsa(f, p0, p1, TOL, MAXIT):
    q0, q1 = f(p0), f(p1)
    for i in range(1, MAXIT):
        p = p1 - (q1 * (p1 - p0) / (q1 - q0))
        if abs(p - p1) < TOL:
            return p
        q = f(p)
        if q * q1 < 0:
            p0, q0 = p1, q1
        p1, q1 = p, q
    return p