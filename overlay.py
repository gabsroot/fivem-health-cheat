import pyMeow as pm
import psutil, re, ctypes, os, random, string
from fonts import *
from offsets import *
from sdk import *
from config import *

class Overlay:
    def __init__(self):
        try:
            process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
            self.process = pm.open_process(process_name)
            module = pm.get_module(self.process, process_name)["base"]

            self.replay = pm.r_int64(self.process, module + offsets[process_name]["replay"])
            self.world = pm.r_int64(self.process, module + offsets[process_name]["world"])
            self.viewport = pm.r_int64(self.process, module + offsets[process_name]["viewport"])
        except:
            ctypes.windll.user32.MessageBoxW(0, "Process FiveM_bXXXX_GTAProcess.exe not found. Run the loader only inside the server.", "Error", 0x10)
            os._exit(0)

    def update(self):
        title = "".join(random.choices(string.ascii_letters, k=10))
        pm.overlay_init(target=title, title=title, fps=144)
        pm.load_font(fileName=FONT_ARIAL, fontId=1)

        max_health = 200
        min_health = 100
        bar_width = 2

        while pm.overlay_loop():
            try:
                local_player = pm.r_int64(self.process, self.world + 0x8)
                local_player_pos = pm.r_vec3(self.process, local_player + 0x90)
                replay_interface = pm.r_int64(self.process, self.replay + 0x18)
                view_matrix = pm.r_floats(self.process, self.viewport + 0x24C, 16)

                if Config.godmode:
                    try:
                        pm.w_float(self.process, local_player + 0x280, 300)
                    except:
                        pass

                # crosshair
                if Config.crosshair:
                    pm.draw_circle_lines(centerX=pm.get_screen_width() / 2, centerY=pm.get_screen_height() / 2, radius=3, color=Config.crosshair_color)

                # watermark
                # pm.draw_rectangle_rounded(posX=14, posY=14, width=172, height=27, roundness=0.2, segments=1, color=pm.fade_color(pm.get_color("#ff0047"), 0.4))
                # pm.draw_rectangle_rounded(posX=15, posY=15, width=170, height=25, roundness=0.2, segments=1, color=pm.fade_color(pm.get_color("#111316"), 0.9))
                # pm.draw_font(fontId=1, text=f"github.com/gabsroot", posX=25, posY=19, fontSize=15, spacing=2, tint=pm.get_color("#d4d4d4"))

                if not replay_interface:
                    continue

                entities = pm.r_int64(self.process, replay_interface + 0x100)

                if not entities:
                    continue

                r_entities = pm.r_int64(self.process, replay_interface + 0x108)

                for i in range(r_entities):
                    try:
                        entity = pm.r_int64(self.process, entities + (i * 0x10))

                        # not ent, ignore me
                        if not entity or entity == local_player:
                            continue

                        entity_health = pm.r_float(self.process, entity + 0x280)
                        entity_pos = pm.r_vec3(self.process, entity + 0x90)
                        distance = get_distance(local_player_pos, entity_pos)

                        if distance > Config.max_distance:
                            continue

                        screen = world_to_screen(view_matrix, entity_pos)

                        # basepos
                        base_width = 50
                        base_height = 100
                        box_x, box_y, width, height = get_box(screen, base_width, base_height, distance)

                        # box fill
                        if Config.fill:
                            pm.draw_rectangle(posX=box_x, posY=box_y, width=width, height=height, color=pm.fade_color(Config.fill_color, 0.5))

                        # box normal
                        if Config.box:
                            if Config.box_style == "normal":
                                pm.draw_rectangle_lines(
                                    posX=box_x,
                                    posY=box_y,
                                    width=width,
                                    height=height,
                                    color=Config.box_color,
                                    lineThick=1
                                )

                            else:
                                # box corner
                                corner_length = min(width, height) * 0.2
                                line_thick = 1
                                
                                # top left
                                pm.draw_line(box_x, box_y, box_x + corner_length, box_y, Config.box_color, line_thick)
                                pm.draw_line(box_x, box_y, box_x, box_y + corner_length, Config.box_color, line_thick)
                                
                                # top right
                                pm.draw_line(box_x + width, box_y, box_x + width - corner_length, box_y, Config.box_color, line_thick)
                                pm.draw_line(box_x + width, box_y, box_x + width, box_y + corner_length, Config.box_color, line_thick)

                                # bottom left
                                pm.draw_line(box_x, box_y + height, box_x + corner_length, box_y + height, Config.box_color, line_thick)
                                pm.draw_line(box_x, box_y + height, box_x, box_y + height - corner_length, Config.box_color, line_thick)

                                # bottom right
                                pm.draw_line(box_x + width, box_y + height, box_x + width - corner_length, box_y + height, Config.box_color, line_thick)
                                pm.draw_line(box_x + width, box_y + height, box_x + width, box_y + height - corner_length, Config.box_color, line_thick)

                        # box line
                        if Config.line:
                            pm.draw_line(startPosX=pm.get_screen_width() / 2, startPosY=pm.get_screen_height() - 50, endPosX=screen["x"], endPosY=box_y + height, color=pm.fade_color(Config.line_color, 0.3), thick=1)
                        
                        # distance
                        if Config.distance:
                            pm.draw_font(fontId=1, text=f"{int(distance)}m", posX=screen["x"] - 10, posY=box_y + height + 5, fontSize=12, spacing=0.0, tint=Config.distance_color)

                        # health bar
                        if Config.health:
                            health = entity_health
                            bar_height = height

                            if health < min_health:
                                health = min_health

                            if health > max_health:
                                health = max_health

                            health_percentage = (health - min_health) / (max_health - min_health)
                            health_bar_height = bar_height * health_percentage

                            # red
                            pm.draw_rectangle(
                                posX=box_x - bar_width - 4,
                                posY=box_y,
                                width=bar_width,
                                height=bar_height,
                                color=pm.get_color("#bd2045")
                            )

                            # green
                            pm.draw_rectangle(
                                posX=box_x - bar_width - 4,
                                posY=box_y + (bar_height - health_bar_height),
                                width=bar_width,
                                height=health_bar_height,
                                color=pm.get_color("#41e295")
                            )

                    except:
                        pass

                pm.end_drawing()

            except:
                pass
