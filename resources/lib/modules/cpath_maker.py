# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcvfs
import json
import sqlite3 as database
from threading import Thread
from modules import xmls
# from modules.logger import logger
dialog = xbmcgui.Dialog()
window = xbmcgui.Window(10000)
Listitem = xbmcgui.ListItem
max_widgets = 10

settings_path = xbmcvfs.translatePath(
    "special://profile/addon_data/script.fentastic.helper.miki/"
)
database_path = xbmcvfs.translatePath(
    "special://profile/addon_data/script.fentastic.helper.miki/cpath_cache.db"
)
movies_widgets_xml, tvshows_widgets_xml = (
    "script-fentastic-widget_movies",
    "script-fentastic-widget_tvshows",
)
movies_main_menu_xml, tvshows_main_menu_xml = (
    "script-fentastic-main_menu_movies",
    "script-fentastic-main_menu_tvshows",
)
default_xmls = {
    "movie.widget": (movies_widgets_xml, xmls.default_widget, "MovieWidgets"),
    "tvshow.widget": (tvshows_widgets_xml, xmls.default_widget, "TVShowWidgets"),
    "movie.main_menu": (movies_main_menu_xml, xmls.default_main_menu, "MoviesMainMenu"),
    "tvshow.main_menu": (
        tvshows_main_menu_xml,
        xmls.default_main_menu,
        "TVShowsMainMenu",
    ),
}
main_include_dict = {
    "movie": {"main_menu": None, "widget": "MovieWidgets"},
    "tvshow": {"main_menu": None, "widget": "TVShowWidgets"},
}