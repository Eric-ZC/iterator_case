import pytest
from soium import Driver
from soium import Keys
from soium.utils.logger import console
from soium.utils.asserts import assert_that
from soium.utils.random import random_number
from soium.utils.retry import retry_attempts

from src.conf import settings


class TestWallpaper:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver: Driver, settings_page):
        console.print("\n执行前置操作")
        driver.launch_app(*settings.packages.settings)
        settings_page.click_display()
        yield
        console.print("\n执行后置操作")
        driver.close_app()

    @pytest.mark.swift_2_pro
    @pytest.mark.swift_1_pro
    def test_system_wallpaper(self, driver: Driver, settings_page, display_page):
        """系统壁纸"""
        display_page.click_wallpaper()
        display_page.select_wallpaper()
        display_page.wallpaper_options()
        display_page.setting_wallpaper()
        display_page.setting_main_wallpaper()

    @pytest.mark.D4_504_Pro
    def test_system_wallpaper_oir(self, driver: Driver, settings_page, display_page):
        """系统壁纸"""
        display_page.click_wallpaper()
        display_page.select_wallpaper()
        display_page.wallpaper_options_d5()
        # display_page.setting_wallpaper_oir()
        display_page.setting_wallpaper_d5()
        display_page.setting_main_wallpaper()

    @pytest.mark.swan_1_pro
    def test_swan_1_pro(self,driver: Driver, settings_page, display_page):
        """系统壁纸"""
        display_page.click_wallpaper()
        display_page.select_wallpaper()
        display_page.wallpaper_options_swan()
        display_page.setting_wallpaper_oir()
        display_page.setting_main_wallpaper()

    @pytest.mark.android11
    @pytest.mark.D4_504
    def test_system_wallpaper_oir(self, driver: Driver, settings_page, display_page):
        """系统壁纸"""
        display_page.click_wallpaper_android11()
        display_page.select_wallpaper()
        display_page.wallpaper_options_d5()
        # display_page.setting_wallpaper_oir()
        display_page.setting_wallpaper_d5()
        display_page.setting_main_wallpaper()
        driver.press_keycode(Keys.HOME)
