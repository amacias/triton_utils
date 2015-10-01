from __future__ import division
from math import floor


def ceildiv(a, b):
    return -(-a // b)


def combat(ds, dw, ats, atw):
    dw += 1
    df_rounds = ceildiv(ds, atw)
    surviving_at = ats - (df_rounds * dw)
    if surviving_at > 0:
        return "Attacker wins with %i ships remaining" % surviving_at
    else:
        at_rounds = ceildiv(ats, dw)
        surviving_df = ds - ((at_rounds - 1) * atw)
        return "Defender wins with %i ships remaining" % surviving_df


def buy_ind(res, level):
    return floor(1000. * level / res)


def buy_eco(res, level):
    return floor(500. * level / res)


def buy_sci(res, level):
    return floor(4000. * level / res)


def buy_warp(res):
    return floor(10000. / res)


def improve_eco(res, start_lvl, end_lvl):
    return sum(buy_eco(res, _) for _ in range(start_lvl + 1, end_lvl + 1))


def improve_ind(res, start_lvl, end_lvl):
    return sum(buy_ind(res, _) for _ in range(start_lvl + 1, end_lvl + 1))


def improve_sci(res, start_lvl, end_lvl):
    return sum(buy_sci(res, _) for _ in range(start_lvl + 1, end_lvl + 1))
