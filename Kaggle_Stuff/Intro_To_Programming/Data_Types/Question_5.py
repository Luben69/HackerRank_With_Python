def cost_of_project(engraving, solid_gold):
    engraved_units = len(engraving)
    if solid_gold:
        base_cost = 100
        engraving_cost_per_unit = 10
    else:
        base_cost = 50
        engraving_cost_per_unit = 7

    cost = base_cost + (engraved_units * engraving_cost_per_unit)
    return cost


# Check your answer
q5.check()