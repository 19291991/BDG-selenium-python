import time

from Pages.PowerPage import PowerPage
import pytest


# ---------------TEST CASE VARIABLES-----------------
login_page_url = "https://www.saucedemo.com/"
positive_username = "standard_user"
positive_password = "secret_sauce"


@pytest.mark.usefixtures('init_driver')
class BurgerMenu:
    def menu_burger(self):

        obj = PowerPage(self.driver)
        obj.navigate_by_url(login_page_url)
        obj.do_login(positive_username, positive_password)
        obj.menu_navigate_to('all items')
        navigated_all_items = obj.get_item_value_by_name("https://www.saucedemo.com/inventory.html")
        obj.menu_navigate_to('close burger menu')
        navigated_close_menu_burger = obj.get_navigate_by_url("https://www.saucedemo.com/inventory.html")
        obj.menu_navigate_to('about')
        navigated_about = obj.get_navigate_by_url("https://saucelabs.com/")
        obj.menu_navigate_to('logout')
        navigated_logout = obj.get_navigate_by_url("https://www.saucedemo.com/")
        obj.menu_navigate_to('reset app state')
        navigated_reset_app_state = obj.get_navigate_by_url("https://www.saucedemo.com/inventory.html")
        obj.menu_navigate_to('close burger menu')
        navigated_close_menu_burger = obj.get_navigate_by_url("https://www.saucedemo.com/inventory.html")
        assert navigated_all_items
        assert navigated_close_menu_burger
        assert navigated_about
        assert navigated_logout
        assert navigated_reset_app_state
        assert navigated_close_menu_burger






















        # obj.menu_navigate_to("all items")
        # # navigate_to_all_items = obj.menu_navigate_to()
        # navigate_to_all_items = obj.do_click("all items")
        # obj.menu_navigate_to("about")
        # navigate_to_about = obj.do_click()
        # #navigate_to_about = obj.menu_navigate_to()
        # obj.menu_navigate_to("logout")
        # navigate_to_logout = obj.do_click()
        # #navigate_to_logout = obj.menu_navigate_to()
        # obj.menu_navigate_to("reset_app_state")
        # navigate_to_reset_app_state = obj.do_click()
        # #navigate_to_reset_app_state = obj.menu_navigate_to()
        # obj.menu_navigate_to("close burger menu")
        # navigate_to_close_burger_menu = obj.do_click()











