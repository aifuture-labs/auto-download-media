from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

from seleniumwire import webdriver

import dearpygui.dearpygui as dpg


# def change_text(sender, app_data):
#     dpg.set_value("text item", f"Mouse Button ID: {app_data}")


# def visible_call(sender, app_data):
#     # print("I'am visible")
#     pass


# def change_text(sender, app_data):
#     dpg.set_value(
#         "text_item", f"Mouse Button: {app_data[0]}, Down Time: {app_data[1]} seconds")


if __name__ == "__main__":
    # options = webdriver.ChromeOptions()
    # options = ChromeOptions()
    # options.page_load_strategy
    # options.add_argument("--headless=new")

    # # start tbe session
    # driver = webdriver.Chrome(options=options,)

    # # take action on browser
    # driver.get("https://www.baidu.com")

    # # establish waiting strategy
    # driver.implicitly_wait(0.5)

    # # request browser information
    # curr_url = driver.current_url
    # title = driver.current_url

    # print('current url {} and title {}'.format(curr_url, title))

    # # find link elements
    # uris = driver.find_elements(
    #     by=By.XPATH, value="//ul[@id='hotsearch-content-wrapper']//li")

    # for ele in uris:
    #     _ele = ele.find_element(by=By.XPATH, value="./a")
    #     print("{0}-[{1}]".format("hot link->",_ele.get_attribute("href")))

    # for request in driver.requests:
    #     if request.response:
    #         print(
    #             request.url,
    #             request.response.status_code,
    #             request.response.headers['Content-Type']
    #         )

    dpg.create_context()

    # print("uuid", dpg.generate_uuid())

    # with dpg.item_handler_registry(tag="widget handler") as handler:
    #     dpg.add_item_clicked_handler(callback=change_text)
    #     dpg.add_item_visible_handler(callback=visible_call)

    # with dpg.window(tag="one", show=True, menubar=False, width=500, height=300) as window:
    #     dpg.add_text("Click me with any mouse button", tag="text item")
    #     dpg.add_text(
    #         "Close window with arrow to change visible state printing to console", tag="text item 2")
    #     button1 = dpg.add_button(label="Press Me!")

    #     slider_int = dpg.add_slider_int(label="Slide to the left!", width=100)
    #     slider_float = dpg.add_slider_float(
    #         label="Slide to the right!", width=100)

    #     # An item's unique identifier (tag) is returned when
    #     # creating items.
    #     print(
    #         f"Printing item tag's: {window}, {button1}, {slider_int}, {slider_float}")

    # with dpg.window(tag="vv", label="Example", modal=True):
    #     with dpg.group():
    #         dpg.add_button(label="View the Terminal for item tags")
    #         print(dpg.last_item())
    #         print(dpg.last_container())
    #         print(dpg.last_root())
    # # bind item handler registry to item
    # dpg.bind_item_handler_registry("text item", "widget handler")
    # dpg.bind_item_handler_registry("text item 2", "widget handler")

    # dpg.create_viewport(title='Custom Title', width=800, height=600)
    # dpg.configure_item('a', )

    # with dpg.value_registry():
    #     dpg.add_bool_value(default_value=True, tag="bool_value")
    #     dpg.add_string_value(default_value="Default string", tag="string_value")

    # with dpg.window(label="Tutorial"):
    #     dpg.add_checkbox(label="Radio Button1", source="bool_value")
    #     dpg.add_checkbox(label="Radio Button2", source="bool_value")

    #     dpg.add_input_text(label="Text Input 1", source="string_value")
    #     dpg.add_input_text(label="Text Input 2", source="string_value", password=True)
    
    # with dpg.table():
    #     pass

    # dpg.create_viewport(title='Custom Title', width=800, height=600)
    # with dpg.window(label="Main"):

    #     with dpg.menu_bar():
    #         with dpg.menu(label="Themes"):
    #             dpg.add_menu_item(label="Dark")
    #             dpg.add_menu_item(label="Light")
    #             dpg.add_menu_item(label="Classic")

    #             with dpg.menu(label="Other Themes"):
    #                 dpg.add_menu_item(label="Purple")
    #                 dpg.add_menu_item(label="Gold")
    #                 dpg.add_menu_item(label="Red")

    #         with dpg.menu(label="Tools"):
    #             dpg.add_menu_item(label="Show Logger")
    #             dpg.add_menu_item(label="Show About")

    #         with dpg.menu(label="Oddities"):
    #             dpg.add_button(label="A Button")
    #             dpg.add_simple_plot(label="Menu plot", default_value=(0.3, 0.9, 2.5, 8.9), height=80)

    # dpg.create_viewport(title='Custom Title', width=800, height=600)

    # def callback(sender, app_data, user_data):
    #     print("Sender: ", sender)
    #     print("App Data: ", app_data)

    # with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id", width=700 ,height=400):
    #     dpg.add_file_extension(".*")
    #     dpg.add_file_extension("", color=(150, 255, 150, 255))
    #     dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
    #     dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
    #     dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")

    # with dpg.window(label="Tutorial", width=800, height=300):
    #     dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))

    # dpg.create_viewport(title='Custom Title', width=800, height=600)

    # def print_me(sender):
    #     print(f"Menu Item: {sender}")
    
    # dpg.create_viewport(title='Custom Title', width=600, height=200)

    # with dpg.viewport_menu_bar():
    #     with dpg.menu(label="File"):
    #         dpg.add_menu_item(label="Save", callback=print_me)
    #         dpg.add_menu_item(label="Save As", callback=print_me)

    #         with dpg.menu(label="Settings"):
    #             dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
    #             dpg.add_menu_item(label="Setting 2", callback=print_me)

    #     dpg.add_menu_item(label="Help", callback=print_me)

    #     with dpg.menu(label="Widget Items"):
    #         dpg.add_checkbox(label="Pick Me", callback=print_me)
    #         dpg.add_button(label="Press Me", callback=print_me)
    #         dpg.add_color_picker(label="Color Me", callback=print_me)
    
    # with dpg.window(label="Delete Files", modal=True, show=False, tag="modal_id", no_title_bar=True):
    #     dpg.add_text("All those beautiful files will be deleted.\nThis operation cannot be undone!")
    #     dpg.add_separator()
    #     dpg.add_checkbox(label="Don't ask me next time")
    #     with dpg.group(horizontal=True):
    #         dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))
    #         dpg.add_button(label="Cancel", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))

    # with dpg.window(label="Tutorial"):
    #     dpg.add_button(label="Open Dialog", callback=lambda: dpg.configure_item("modal_id", show=True))

    # dpg.create_viewport(title='Custom Title', width=800, height=600)

    with dpg.window(label="Tutorial"):
        with dpg.table(header_row=False):

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()

            # add_table_next_column will jump to the next row
            # once it reaches the end of the columns
            # table next column use slot 1
            for i in range(0, 4):
                with dpg.table_row():
                    for j in range(0, 3):
                        dpg.add_text(f"Row{i} Column{j}")

    dpg.create_viewport(title='Custom Title', width=800, height=600)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

    # driver.quit()
