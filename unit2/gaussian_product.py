def calc_product(mu, nu, ss, rr):
    mu2 = float(rr*mu + ss*nu) / (ss + rr)
    ss2 = 1.0 / ((1.0/ss) + (1.0/rr))

    print "Gauss 1: mu=%f, s2=%f" % (mu, ss)
    print "Gauss 2: nu=%f, r2=%f" % (nu, rr)
    print "Result : mu'=%f, s2'=%f" % (mu2, ss2)

    return mu2, ss2

calc_product(1.0, 5.0, 1.0, 4.0)
