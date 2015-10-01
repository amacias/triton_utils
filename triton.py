from __future__ import division
from math import floor


def ceildiv(a, b):
    return -(-a // b)


def combat(def_ships, def_weapons, att_ships, att_weapons):
    def_weapons += 1
    def_rounds = ceildiv(def_ships, att_weapons)
    surviving_att = att_ships - (def_rounds * def_weapons)
    if surviving_att > 0:
        return "Attacker wins with %i ships remaining" % surviving_att
    else:
        att_rounds = ceildiv(att_ships, def_weapons)
        surviving_def = def_ships - ((att_rounds - 1) * att_weapons)
        return "Defender wins with %i ships remaining" % surviving_def


def buy_ind(star_resources, level):
    return floor(1000. * level / star_resources)


def buy_eco(star_resources, level):
    return floor(500. * level / star_resources)


def buy_sci(star_resources, level):
    return floor(4000. * level / star_resources)


def buy_warp(star_resources):
    return floor(10000. / star_resources)


def improve_eco(star_resources, start_lvl, end_lvl):
    return sum(buy_eco(star_resources, _) for _ in range(start_lvl + 1, end_lvl + 1))


def improve_ind(star_resources, start_lvl, end_lvl):
    return sum(buy_ind(star_resources, _) for _ in range(start_lvl + 1, end_lvl + 1))


def improve_sci(star_resources, start_lvl, end_lvl):
    return sum(buy_sci(star_resources, _) for _ in range(start_lvl + 1, end_lvl + 1))


def tech_cost(level):
    return (level - 1) * 144


def research_time(researched, science, target_lvl):
    hours = (tech_cost(target_lvl) - researched) / science
    print "Current Research ETA: %dd %dh" % (hours // 24, hours % 24)


def ships_per_hour(infrastructure, manufacturing=1):
    return infrastructure * (manufacturing + 5)
