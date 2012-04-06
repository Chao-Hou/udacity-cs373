def calc_sum(mu, nu, ss, rr):
    mu2 = mu + nu
    ss2 = ss + rr

    print "=== Motion / Product"
    print "Gauss 1: mu=%f, s2=%f" % (mu, ss)
    print "Gauss 2: nu=%f, r2=%f" % (nu, rr)
    print "Result : mu'=%f, s2'=%f" % (mu2, ss2)

    return mu2, ss2

def calc_product(mu, nu, ss, rr):
    mu2 = float(rr*mu + ss*nu) / (ss + rr)
    ss2 = 1.0 / ((1.0/ss) + (1.0/rr))

    print "=== Measurement / Product"
    print "Gauss 1: mu=%f, s2=%f" % (mu, ss)
    print "Gauss 2: nu=%f, r2=%f" % (nu, rr)
    print "Result : mu'=%f, s2'=%f" % (mu2, ss2)

    return mu2, ss2

calc_product(1.0, 1.0, 1.0, 1.0)
calc_product(1.0, 5.0, 1.0, 1.0)
calc_product(1.0, 5.0, 1.0, 4.0)

calc_sum(1.0, 1.0, 1.0, 1.0)
calc_sum(1.0, 5.0, 1.0, 1.0)
calc_sum(1.0, 5.0, 1.0, 4.0)
