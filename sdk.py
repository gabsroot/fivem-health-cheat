import pyMeow as pm
import math

def world_to_screen(view_matrix, world_pos):
    screen_width = pm.get_screen_width()
    screen_height = pm.get_screen_height()

    view_matrix_4x4 = [view_matrix[i:i+4] for i in range(0, 16, 4)]
    view_matrix_4x4_T = [[view_matrix_4x4[j][i] for j in range(4)] for i in range(4)]

    vec_x = view_matrix_4x4_T[1]
    vec_y = view_matrix_4x4_T[2]
    vec_z = view_matrix_4x4_T[3]

    screen_pos = [
        vec_x[0] * world_pos["x"] + vec_x[1] * world_pos["y"] + vec_x[2] * world_pos["z"] + vec_x[3],
        vec_y[0] * world_pos["x"] + vec_y[1] * world_pos["y"] + vec_y[2] * world_pos["z"] + vec_y[3],
        vec_z[0] * world_pos["x"] + vec_z[1] * world_pos["y"] + vec_z[2] * world_pos["z"] + vec_z[3],
    ]

    if screen_pos[2] <= 0.1:
        return None

    screen_pos[2] = 1.0 / screen_pos[2]
    screen_pos[0] *= screen_pos[2]
    screen_pos[1] *= screen_pos[2]

    x_temp = screen_width / 2
    y_temp = screen_height / 2

    screen_pos[0] = x_temp + 0.5 * screen_pos[0] * screen_width + 0.5
    screen_pos[1] = y_temp - 0.5 * screen_pos[1] * screen_height - 0.5

    return {"x": screen_pos[0], "y": screen_pos[1]}

def get_distance(pos1, pos2):
    return math.sqrt((pos1["x"] - pos2["x"]) ** 2 + (pos1["y"] - pos2["y"]) ** 2 + (pos1["z"] - pos2["z"]) ** 2)

def get_box(entity_pos, base_width, base_height, distance):
    min_scale = 0.2
    max_scale = 1.0
    scale_factor = max(min_scale, min(max_scale, 20 / distance))
    width = base_width * scale_factor
    height = base_height * scale_factor
    box_x = entity_pos["x"] - width / 2
    box_y = entity_pos["y"] - height / 2
    return box_x, box_y, width, height
