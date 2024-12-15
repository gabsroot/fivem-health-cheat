import dearpygui.dearpygui as dpg

class Theme:
    @staticmethod
    def window():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # background color
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (17, 19, 22, 255))
                # border color
                dpg.add_theme_color(dpg.mvThemeCol_Border, (17, 19, 22, 255))
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # topbar color
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (17, 19, 22, 255))
                # close button hover color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (17, 19, 22, 255))
                # close button active color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (17, 19, 22, 255))
                # tab default color
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (28, 30, 36, 255))
                # tab hover color
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (150, 32, 68, 255))
                # tab active color
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (150, 32, 68, 255))

        return theme
    
    @staticmethod
    def button():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # default color
                dpg.add_theme_color(dpg.mvThemeCol_Button, (28, 30, 36, 255))
                # hover color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (36, 39, 46, 255))
                # active color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (150, 32, 68, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

        return theme
    
    @staticmethod
    def checkbox():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # bg default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (26, 28, 31, 255))
                # hover color
                dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (26, 28, 31, 255))
                # active color
                dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (26, 28, 31, 255))
                # mark color
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (150, 32, 68, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)

        return theme
    
    @staticmethod
    def combo():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # text indent
                dpg.add_theme_style(dpg.mvPlotStyleVar_AnnotationPadding, 0.05)
                # bg default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (26, 28, 31, 255))
                # bg hover color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (26, 28, 31, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # popup default color
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (26, 28, 31, 255))
                # popup border radius
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 4)
                # item hover color
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (50, 50, 50, 255))
                # item active color
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (72, 81, 102, 255))
                # item selected color
                dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (26, 28, 31, 255))
                # padding
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 30, 10)
                # button default color
                dpg.add_theme_color(dpg.mvThemeCol_Button, (50, 50, 50, 255))
                # button hover color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (150, 32, 68, 255))
                # button active color
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (72, 81, 102, 255))
                # tab scroll default color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (0, 18, 33, 255))
                # scroll bar default color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (18, 31, 46, 255))
                # scroll bar hover color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (18, 31, 46, 255))
                # scroll bar active color
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (18, 31, 46, 255))

        return theme
    
    @staticmethod
    def slider():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # text color
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                # default color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (26, 28, 31, 255))
                # hover color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (26, 28, 31, 255))
                # active color
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (26, 28, 31, 255))
                # border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # circle default color
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (50, 50, 50, 255))
                # circle active color
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (150, 32, 68, 255))
                # round cicle
                dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 3)
                # width circle
                dpg.add_theme_style(dpg.mvStyleVar_GrabMinSize, 10)
                # padding circle
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 3)

        return theme
    
    @staticmethod
    def color_picker():
        with dpg.theme() as theme:
            with dpg.theme_component():
                # btn border radius
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4)
                # popup border radius
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 8)
                # popup bg color
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (26, 28, 31, 255))
                # popup border color
                dpg.add_theme_color(dpg.mvPlotCol_FrameBg, (150, 32, 68, 255))
                # btn 
                dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, (26, 28, 31, 255))
                # btn hover
                dpg.add_theme_color(dpg.mvPlotCol_LegendBg, (26, 28, 31, 255))
                # btn click
                dpg.add_theme_color(dpg.mvPlotCol_LegendBorder, (26, 28, 31, 255))
                # color selector
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (26, 28, 31, 255))
                # padding
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 2)
                
        return theme
    
