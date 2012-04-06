def calc_product(mu, nu, ss, rr):
    mu2 = mu + nu
    ss2 = ss + rr

    print "Gauss 1: mu=%f, s2=%f" % (mu, ss)
    print "Gauss 2: nu=%f, r2=%f" % (nu, rr)
    print "Result : mu'=%f, s2'=%f" % (mu2, ss2)

    return mu2, ss2

calc_product(8, 10, 4, 6)
