import time
import random
import threading
import numpy as np
import dearpygui.dearpygui as dpg

class SpeechUI:
    def __init__(self):
        self.x = np.linspace(0,2 * np.pi, 50) # np.sin deals in radians which is# why I used an array from 0 to                     # 2*np.pi
        self.y = np.sin(self.x)

        self.speak = True

        dpg.create_context()
        dpg.create_viewport(title="Science Fair")

    def update_graph(self): # To update the sinewave
        while True:
            self.x = np.linspace(np.pi/6, random.randint(0, 50) * np.pi, 40)
            self.y = np.sin(self.x)
            dpg.configure_item("graph", default_value=list(self.y))
            time.sleep(0.15)

    def update_text(self, what_to_say=None): # To update the text
        if what_to_say is None:
            self.speak = False

        elif type(what_to_say) is str:
            dpg.configure_item("speech", text=what_to_say)
            print("updated!")
            self.speak = True

    def draw(self): 
        # Set the background color
        with dpg.theme(tag="base"):
            with dpg.theme_component():
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (51, 51, 55))
        
        # Only display the aesthtical waves once the person is speaking
        with dpg.window(label="simple plot", tag="main", width=1366, height=768):
            
            if self.speak is True:
                dpg.add_simple_plot(
                    tag="graph",
                    default_value=list(self.y),
                    height=400, 
                    width=1366)

                # Add a line seperator when speaking to seperate wave from speech text
                dpg.add_separator()
                dpg.add_spacer(height=20)
                
                with dpg.drawlist(width=1366, height=400):
                    dpg.draw_text(
                        tag="speech",
                        pos=(580, 150), 
                        text="ooga ooga", 
                        color=(250, 250, 250, 255), 
                        size=30)

            else:
                with dpg.drawlist(width=1366, height=400):
                    dpg.draw_line((0, 200), (1500, 200), color=(29, 151, 236, 103), thickness=3)
                    dpg.draw_text((580, 0), "Listening...", color=(250, 250, 250, 255), size=30)

                # Add a line seperator when speaking to seperate wave from speech text
                dpg.add_separator()
                dpg.add_spacer(height=10)

        dpg.bind_theme("base")

    def main(self):
        self.draw()
        print("after_draw")
        threading.Thread(target=self.update_graph).start()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.maximize_viewport()
        dpg.set_primary_window("main", True)
        dpg.start_dearpygui()
        dpg.destroy_context()