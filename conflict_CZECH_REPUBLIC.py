from dataclasses import dataclass

@dataclass
class collision_data:
    collisions: list[bool]
    collisionX: bool

    def any(self):
        return any(self.collisions) or self.collisionX

def conflict_czechk(pos_адин, pos_два):
    collisionY = pos_адин[3] >= pos_два[1] and pos_адин[1] <= pos_два[3]
    collisionX = pos_адин[2] >= pos_два[0] and pos_адин[0] <= pos_два[2]
    collisionX_left = collisionY and pos_два[2] >= pos_адин[2] >= pos_два[0] 
    collisionX_right = collisionY and pos_два[0] <= pos_адин[0] <= pos_два[2]
    collisionY_top = collisionX and pos_два[1] <= pos_адин[3] <= pos_два[3]
    collisionY_bottom = collisionX and pos_два[3] >= pos_адин[1] >= pos_два[1]
    
    return collision_data(collisions=[collisionX_left, collisionX_right, collisionY_top, collisionY_bottom], collisionX=collisionX)
