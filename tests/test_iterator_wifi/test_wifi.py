import time

import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestWiFi:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page,reset_wlan_network_page):
        console.print("\n执行前置操作")
        driver.switch_wifi(True)

        yield
        console.print("\n执行后置操作")
        # driver.launch_app(*settings.packages.settings)
        # settings_page.click_system()
        # reset_wlan_network_page.click_reset_options()
        # reset_wlan_network_page.reset_wlan_network_bluetooth()
        # reset_wlan_network_page.click_reset_setting()
        # reset_wlan_network_page.click_exec_reset()

    @pytest.mark.swan_1_pro
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    def test_connect_WiFi(self, driver: Driver,
                          notification_panel,
                          settings_page,
                          network_page,
                          wifi_page,
                          network_details_page,
                          reset_wlan_network_page):
        """连接WiFi"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

        wifi_list = {"yimin": {"Neostra-admin": "ad@666999"},
                     "imin": {"Neostra-VIP": "vip999999"}
                     }[driver.get_brand()]
        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi()
        wifi_page.get_wifi(*wifi_list)
        wifi_page.fill_password(*wifi_list.values())
        driver.press_keycode(Keys.ENTER)
        ssid = driver.get_current_ssid()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_connect_wifi_oir(self, driver: Driver,
                              notification_panel,
                              settings_page,
                              network_page,
                              wifi_page,
                              network_details_page,
                              reset_wlan_network_page):
        """连接WiFi"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

        wifi_list = {"yimin": {"Neostra-admin": "ad@666999"},
                         "imin": {"Neostra-VIP": "vip999999"}
                         }[driver.get_brand()]
        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi_android()
        wifi_page.get_wifi(*wifi_list)
        wifi_page.fill_password(*wifi_list.values())
        driver.press_keycode(Keys.ENTER)
        ssid = driver.get_current_ssid()

        # assert_that(ssid, f"Actual value '{ssid}' is not equal to expected value '{'Neostra-VIP'}'").is_equal_to("Neostra-VIP")
        # console.print("当前连接的WiFi是：" + str(driver.get_current_ssid()))

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_view_wifi_info_android(self,driver:Driver,wifi_page,settings_page,network_page):
        """查看wifi信息"""
        wifi_list = {"yimin": {"Neostra-admin": "ad@666999"},
                     "imin": {"Neostra-VIP": "vip999999"}
                     }[driver.get_brand()]
        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi_android()
        wifi_page.get_wifi(*wifi_list)
        # title = wifi_page.get_heard_title()
        # assert_that(title, f"Actual value '{title}' is not equal to expected value '{'Neostra-VIP'}'").is_equal_to("Neostra-VIP")

    @pytest.mark.swan_1_pro
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    def test_view_wifi_info(self, driver: Driver, wifi_page, settings_page, network_page):
        """查看wifi信息"""
        wifi_list = {"yimin": {"Neostra-admin": "ad@666999"},
                     "imin": {"Neostra-VIP": "vip999999"}
                     }[driver.get_brand()]
        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi()
        wifi_page.get_wifi(*wifi_list)

    @pytest.mark.swan_1_pro
    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    @pytest.mark.D4_504_Pro
    def test_wifi_without_(self,driver: Driver,wifi_page, settings_page, network_page,reset_wlan_network_page):
        """添加无密码wifi"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi()
        time.sleep(5)
        wifi_page.get_wifi("AA_2.4")
        time.sleep(5)
        ssid = driver.get_current_ssid()
        # console.print(ssid)
        # assert_that(ssid, f"Actual value '{ssid}' is not equal to expected value '{'中兴'}'").is_equal_to("中兴")

        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_wifi_without_pad(self, driver: Driver, wifi_page, settings_page, network_page, reset_wlan_network_page):
        """添加无密码wifi"""
        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()

        driver.launch_app(*settings.packages.settings)
        settings_page.click_network()
        network_page.click_wifi_android()
        time.sleep(5)
        wifi_page.get_wifi("中兴")
        time.sleep(5)
        ssid = driver.get_current_ssid()
        # console.print(ssid)
        # assert_that(ssid, f"Actual value '{ssid}' is not equal to expected value '{'中兴'}'").is_equal_to("中兴")

        driver.launch_app(*settings.packages.settings)
        settings_page.click_system()
        reset_wlan_network_page.click_reset_options()
        reset_wlan_network_page.reset_wlan_network_bluetooth()
        reset_wlan_network_page.click_reset_setting()
        reset_wlan_network_page.click_exec_reset()
