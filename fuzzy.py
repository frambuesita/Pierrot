import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl

# Define fuzzy variables
pierrot_potential = ctrl.Antecedent(np.arange(0,101,1), 'pierrot_potential')
rival_danger = ctrl.Antecedent(np.arange(0,101,1), 'rival_danger')
bet = ctrl.Consequent(np.arange(0,101,1), 'bet')

# Membership functions for pierrot_potential
pierrot_potential['lowest'] = fuzz.trimf(pierrot_potential.universe, [0, 0, 20])
pierrot_potential['low'] = fuzz.trimf(pierrot_potential.universe, [10, 25, 40])
pierrot_potential['medium'] = fuzz.trimf(pierrot_potential.universe, [30, 50, 70])
pierrot_potential['high'] = fuzz.trimf(pierrot_potential.universe, [60, 75, 90])
pierrot_potential['highest'] = fuzz.trimf(pierrot_potential.universe, [90, 100, 100])

# Membership functions for rival_danger
rival_danger['lowest'] = fuzz.trimf(rival_danger.universe, [0, 0, 20])
rival_danger['low'] = fuzz.trimf(rival_danger.universe, [10, 25, 40])
rival_danger['medium'] = fuzz.trimf(rival_danger.universe, [30, 50, 70])
rival_danger['high'] = fuzz.trimf(rival_danger.universe, [60, 75, 90])
rival_danger['highest'] = fuzz.trimf(rival_danger.universe, [90, 100, 100])

# Membership functions for bet
bet['lowest'] = fuzz.trimf(bet.universe, [0, 0, 5])
bet['low'] = fuzz.trimf(bet.universe, [5, 10, 15])
bet['medium'] = fuzz.trimf(bet.universe, [15, 40, 55])
bet['high'] = fuzz.trimf(bet.universe, [50, 70, 85])
bet['highest'] = fuzz.trimf(bet.universe, [80, 100, 100])

# Define fuzzy rules

# Rules for 'lowest' pierrot_potential
rule_lowest_lowest = ctrl.Rule(pierrot_potential['lowest'] & rival_danger['lowest'], bet['low'])
rule_lowest_low = ctrl.Rule(pierrot_potential['lowest'] & rival_danger['low'], bet['lowest'])
rule_lowest_medium = ctrl.Rule(pierrot_potential['lowest'] & rival_danger['medium'], bet['lowest'])
rule_lowest_high = ctrl.Rule(pierrot_potential['lowest'] & rival_danger['high'], bet['lowest'])
rule_lowest_highest = ctrl.Rule(pierrot_potential['lowest'] & rival_danger['highest'], bet['lowest'])

# Rules for 'low' pierrot_potential
rule_low_lowest = ctrl.Rule(pierrot_potential['low'] & rival_danger['lowest'], bet['medium'])
rule_low_low = ctrl.Rule(pierrot_potential['low'] & rival_danger['low'], bet['low'])
rule_low_medium = ctrl.Rule(pierrot_potential['low'] & rival_danger['medium'], bet['low'])
rule_low_high = ctrl.Rule(pierrot_potential['low'] & rival_danger['high'], bet['lowest'])
rule_low_highest = ctrl.Rule(pierrot_potential['low'] & rival_danger['highest'], bet['lowest'])

# Rules for 'medium' pierrot_potential
rule_medium_lowest = ctrl.Rule(pierrot_potential['medium'] & rival_danger['lowest'], bet['high'])
rule_medium_low = ctrl.Rule(pierrot_potential['medium'] & rival_danger['low'], bet['medium'])
rule_medium_medium = ctrl.Rule(pierrot_potential['medium'] & rival_danger['medium'], bet['medium'])
rule_medium_high = ctrl.Rule(pierrot_potential['medium'] & rival_danger['high'], bet['low'])
rule_medium_highest = ctrl.Rule(pierrot_potential['medium'] & rival_danger['highest'], bet['low'])

# Rules for 'high' pierrot_potential
rule_high_lowest = ctrl.Rule(pierrot_potential['high'] & rival_danger['lowest'], bet['highest'])
rule_high_low = ctrl.Rule(pierrot_potential['high'] & rival_danger['low'], bet['high'])
rule_high_medium = ctrl.Rule(pierrot_potential['high'] & rival_danger['medium'], bet['medium'])
rule_high_high = ctrl.Rule(pierrot_potential['high'] & rival_danger['high'], bet['low'])
rule_high_highest = ctrl.Rule(pierrot_potential['high'] & rival_danger['highest'], bet['low'])

# Rules for 'highest' pierrot_potential
rule_highest_lowest = ctrl.Rule(pierrot_potential['highest'] & rival_danger['lowest'], bet['highest'])
rule_highest_low = ctrl.Rule(pierrot_potential['highest'] & rival_danger['low'], bet['highest'])
rule_highest_medium = ctrl.Rule(pierrot_potential['highest'] & rival_danger['medium'], bet['high'])
rule_highest_high = ctrl.Rule(pierrot_potential['highest'] & rival_danger['high'], bet['medium'])
rule_highest_highest = ctrl.Rule(pierrot_potential['highest'] & rival_danger['highest'], bet['low']) 

rules = [
    rule_lowest_lowest, rule_lowest_low, rule_lowest_medium, rule_lowest_high, rule_lowest_highest,
    rule_low_lowest, rule_low_low, rule_low_medium, rule_low_high, rule_low_highest,
    rule_medium_lowest, rule_medium_low, rule_medium_medium, rule_medium_high, rule_medium_highest,
    rule_high_lowest, rule_high_low, rule_high_medium, rule_high_high, rule_high_highest,
    rule_highest_lowest, rule_highest_low, rule_highest_medium, rule_highest_high, rule_highest_highest
]

# Create control system
betting_ctrl = ctrl.ControlSystem(rules)
betting_simulation = ctrl.ControlSystemSimulation(betting_ctrl)

def compute_bet(pierrot_value, rival_value):
    betting_simulation.input['pierrot_potential'] = pierrot_value
    betting_simulation.input['rival_danger'] = rival_value

    betting_simulation.compute()
    return betting_simulation.output['bet']