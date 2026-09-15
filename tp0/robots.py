# Exercice 4
# Question 1 

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

robots_double_mission = robots_exploration & robots_transport # exploration INTERSECTION transport
robots_toutes_missions = robots_exploration | robots_transport # exploration UNION transport
robots_exploration_seulement = robots_exploration - robots_transport # exploration SEULEMENT

assert robots_double_mission(robots_exploration, robots_transport) == {"R5", "R7"}
assert robots_toutes_missions(robots_exploration, robots_transport) == {"R2", "R3", "R5", "R7", "R9"}
assert robots_exploration_seulement(robots_exploration, robots_transport) == {"R2"}

# Question 2 

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")

def ajouter_robot_mission(mission, robot):
    return mission | {robot} 


def retirer_robot_mission(mission, robot):
    return mission - {robot}

assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}

assert robots_transport == {"R5", "R9", "R7", "R3"}  