import dearpygui.dearpygui as dpg
from theme import *
from fonts import *
import os, ctypes, random, string
from threading import Thread
from overlay import *
from config import *

class Menu:
    def __init__(self):
        self.window_width = 520
        self.window_height = 350

    def setup_window(self):
        dpg.create_context()

        with dpg.font_registry():
            # load font
            if not os.path.exists(FONT_ARIAL):
                ctypes.windll.user32.MessageBoxW(0, "Fonts could not be loaded. Please restart and try again", "Error", 0x10)
                os._exit(0)

            self.font = dpg.add_font(FONT_ARIAL, 16)

        with dpg.handler_registry():
            dpg.bind_theme(Theme.window())
            dpg.bind_font(self.font)
            dpg.add_mouse_drag_handler(callback=self.draw_window)

    def create_window(self):
        with dpg.window(label="", width=self.window_width, height=self.window_height, no_collapse=True, no_move=True, no_resize=True, on_close=lambda: os._exit(0)):
            with dpg.tab_bar():

                with dpg.tab(label="Self"):

                    dpg.add_button(
                        pos=(10, 62),
                        label="Health",
                        user_data="health",
                        callback=self.set_health
                    )

                    dpg.add_button(
                        pos=(67, 62),
                        label="Armor",
                        callback=self.set_armor
                    )

                    dpg.add_button(
                        pos=(122, 62),
                        label="Suicide",
                        user_data="suicide",
                        callback=self.set_health
                    )

                    dpg.add_checkbox(
                        pos=(10, 95),
                        label="Godmode",
                        default_value=Config.godmode,
                        user_data="godmode",
                        callback=self.change_state
                    )

                    dpg.add_checkbox(
                        pos=(10, 127),
                        label="Invisible",
                        default_value=Config.invisible,
                        user_data="invisible",
                        callback=self.change_state
                    )

                    dpg.add_checkbox(
                        pos=(10, 159),
                        label="Fast Run",
                        default_value=Config.fast_run,
                        user_data="fast_run",
                        callback=self.change_state
                    )

                    dpg.add_slider_int(
                        pos=(140, 159),
                        width=100,
                        min_value=1,
                        max_value=10,
                        label="Speed",
                        default_value=Config.fast_run_speed,
                        callback=self.change_fast_run
                    )

                    dpg.add_checkbox(
                        pos=(10, 191),
                        label="Vehicle Boost",
                        default_value=Config.vehicle_boost,
                        user_data="vehicle_boost",
                        callback=self.change_state
                    )

                    dpg.add_slider_int(
                        pos=(140, 191),
                        width=100,
                        min_value=1,
                        max_value=10,
                        label="Speed",
                        default_value=Config.vehicle_boost_speed,
                        callback=self.change_vehicle_boost
                    )
                
                with dpg.tab(label="Visual"):

                    dpg.add_slider_int(
                        pos=(10, 62),
                        width=140,
                        min_value=0,
                        max_value=500,
                        default_value=Config.max_distance,
                        label="Distance",
                        callback=self.change_max_distance
                    )

                    dpg.add_checkbox(
                        pos=(10, 95),
                        label="Box",
                        user_data="box",
                        callback=self.change_state
                    )

                    dpg.add_color_edit(
                        pos=(120, 95),
                        label="Color",
                        no_alpha=True,
                        no_inputs=True,
                        no_tooltip=True,
                        no_options=True,
                        default_value=[255, 0, 71, 255],
                        user_data="box",
                        callback=self.change_color
                    )

                    dpg.add_combo(
                        pos=(230, 95),
                        width=80,
                        label="Style",
                        items=["normal", "corner"],
                        default_value=Config.box_style,
                        callback=self.change_box_style
                    )

                    dpg.add_checkbox(
                        pos=(10, 127),
                        label="Fill",
                        user_data="fill",
                        callback=self.change_state
                    )

                    dpg.add_color_edit(
                        pos=(120, 127),
                        label="Color",
                        no_alpha=True,
                        no_inputs=True,
                        no_tooltip=True,
                        no_options=True,
                        default_value=[17, 11, 13, 255],
                        user_data="fill",
                        callback=self.change_color
                    )

                    dpg.add_checkbox(
                        pos=(10, 159),
                        label="Line",
                        user_data="line",
                        callback=self.change_state
                    )

                    dpg.add_color_edit(
                        pos=(120, 159),
                        label="Color",
                        no_alpha=True,
                        no_inputs=True,
                        no_tooltip=True,
                        no_options=True,
                        default_value=[248, 222, 2, 255],
                        user_data="line",
                        callback=self.change_color
                    )

                    dpg.add_checkbox(
                        pos=(10, 191),
                        label="Distance",
                        user_data="distance",
                        callback=self.change_state
                    )

                    dpg.add_color_edit(
                        pos=(120, 191),
                        label="Color",
                        no_alpha=True,
                        no_inputs=True,
                        no_tooltip=True,
                        no_options=True,
                        default_value=[212, 212, 212, 255],
                        user_data="distance",
                        callback=self.change_color
                    )

                    dpg.add_checkbox(
                        pos=(10, 223),
                        label="Health",
                        user_data="health",
                        callback=self.change_state
                    )

                    dpg.add_checkbox(
                        pos=(10, 255),
                        label="Crosshair",
                        user_data="crosshair",
                        callback=self.change_state
                    )

                    dpg.add_color_edit(
                        pos=(120, 255),
                        label="Color",
                        no_alpha=True,
                        no_inputs=True,
                        no_tooltip=True,
                        no_options=True,
                        default_value=[255, 0, 71, 255],
                        user_data="crosshair",
                        callback=self.change_color
                    )

        dpg.create_viewport(x_pos=600, y_pos=300, title="".join(random.choices(string.ascii_letters, k=10)), width=self.window_width, height=self.window_height, decorated=False, resizable=False)

    def set_health(self, sender, app_data, user_data):
        try:
            process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
            process = pm.open_process(process_name)
            module = pm.get_module(process, process_name)["base"]
            world = pm.r_int64(process, module + offsets[process_name]["world"])
            local_player = pm.r_int64(process, world + 0x8)

            if user_data == "health":
                pm.w_float(process, local_player + 0x280, 300)
            else:
                pm.w_float(process, local_player + 0x280, 0)
        except:
            pass

    def set_armor(self):
        try:
            process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
            process = pm.open_process(process_name)
            module = pm.get_module(process, process_name)["base"]
            world = pm.r_int64(process, module + offsets[process_name]["world"])
            local_player = pm.r_int64(process, world + 0x8)
            pm.w_float(process, local_player + 0x1530, 100)
        except:
            pass

    def change_state(self, sender, app_data, user_data):
        if user_data == "godmode":
            Config.godmode = dpg.get_value(sender)

        elif user_data == "invisible":
            try:
                process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
                process = pm.open_process(process_name)
                module = pm.get_module(process, process_name)["base"]
                world = pm.r_int64(process, module + offsets[process_name]["world"])
                local_player = pm.r_int64(process, world + 0x8)
                pm.w_byte(process, local_player + 0x2C, 0x1 if dpg.get_value(sender) else 0x37)
            except:
                pass

        elif user_data == "fast_run":
            Config.fast_run = dpg.get_value(sender)

        elif user_data == "vehicle_boost":
            Config.vehicle_boost = dpg.get_value(sender)

        elif user_data == "box":
            Config.box = dpg.get_value(sender)
        
        elif user_data == "fill":
            Config.fill = dpg.get_value(sender)

        elif user_data == "line":
            Config.line = dpg.get_value(sender)

        elif user_data == "distance":
            Config.distance = dpg.get_value(sender)

        elif user_data == "health":
            Config.health = dpg.get_value(sender)

        elif user_data == "crosshair":
            Config.crosshair = dpg.get_value(sender)

    def change_color(self, sender, app_data, user_data):
        value = dpg.get_value(sender)
        color = {"r": int(value[0]), "g": int(value[1]), "b": int(value[2]), "a": int(value[3])}

        if user_data == "box":
            Config.box_color = color
        
        elif user_data == "fill":
            Config.fill_color = color

        elif user_data == "line":
            Config.line_color = color

        elif user_data == "distance":
            Config.distance_color = color

        elif user_data == "crosshair":
            Config.crosshair_color = color

    def change_fast_run(self, sender):
        if not Config.fast_run:
            return
        
        try:
            process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
            process = pm.open_process(process_name)
            module = pm.get_module(process, process_name)["base"]
            world = pm.r_int64(process, module + offsets[process_name]["world"])
            local_player = pm.r_int64(process, world + 0x8)
            player_info = pm.r_int64(process, local_player + 0x10C8)
            pm.w_float(process, player_info + 0x0CF0, dpg.get_value(sender))
        except:
            pass

    def change_vehicle_boost(self, sender):
        if not Config.vehicle_boost:
            return
        
        try:
            process_name = next((process.info["name"] for process in psutil.process_iter(["name"]) if re.search(r"^FiveM_b\d+_GTAProcess\.exe$", process.info.get("name", ""))), None)
            process = pm.open_process(process_name)
            module = pm.get_module(process, process_name)["base"]
            world = pm.r_int64(process, module + offsets[process_name]["world"])
            local_player = pm.r_int64(process, world + 0x8)
            vehicle = pm.r_uint64(process, local_player + 0x0D30)
            handling = pm.r_uint64(process, vehicle + 0x938)
            pm.w_float(process, handling + 0x4C, dpg.get_value(sender))
        except:
            pass

    def change_max_distance(self, sender):
        Config.max_distance = dpg.get_value(sender)

    def change_box_style(self, sender):
        Config.box_style = dpg.get_value(sender)

    def set_items_theme(self):
        for item in dpg.get_all_items():
            item_type = dpg.get_item_info(item)["type"]

            if item_type == "mvAppItemType::mvCheckbox":
                dpg.bind_item_theme(item, Theme.checkbox())

            elif item_type == "mvAppItemType::mvCombo":
                dpg.bind_item_theme(item, Theme.combo())
            
            elif item_type == "mvAppItemType::mvSliderFloat" or item_type == "mvAppItemType::mvSliderInt":
                dpg.bind_item_theme(item, Theme.slider())

            elif item_type == "mvAppItemType::mvButton":
                dpg.bind_item_theme(item, Theme.button())

            elif item_type == "mvAppItemType::mvInputText":
                dpg.bind_item_theme(item, Theme.input())

            elif item_type == "mvAppItemType::mvColorEdit":
                dpg.bind_item_theme(item, Theme.color_picker())

    def run(self):
        self.set_items_theme()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def draw_window(self, sender, app, user):
        if dpg.get_mouse_pos(local=False)[1] <= 50:
            pos = dpg.get_viewport_pos()
            dpg.set_viewport_pos([pos[0] + app[1], max(pos[1] + app[2], 0)])


menu = Menu()
overlay = Overlay()

menu.setup_window()
menu.create_window()

thread = Thread(target=overlay.update, daemon=True)
thread.start()

menu.run()

