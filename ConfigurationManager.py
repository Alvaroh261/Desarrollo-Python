# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:23:07 2022

@author: Usuario
"""
# Import Module
import xml.etree.ElementTree as ET


def connectionstring(buscador):
    """Obtiene los datos ConnectionStringsSection para la configuración predeterminada de
    la aplicación actual.

    Excepciones:
        No se pudo recuperar un objeto ConnectionStringSettingsCollection.
    """

    tree = ET.parse('Config.xml')
    root = tree.getroot()
    value = ""

    for i in root.findall('connectionString'):
        for j in i.iter('add'):
            if j.attrib.get('key') == buscador:
                value = j.attrib.get('value')
                break

    return value


def appsettings(buscador):
    """Obtiene los datos AppSettingsSection para la configuración predeterminada de la 
    aplicación actual.

    Excepciones:
        No se pudo recuperar un objeto NameValueCollection con los datos de configuración de la aplicación.
    """

    tree = ET.parse('Config.xml')
    root = tree.getroot()
    value = ""

    for i in root.findall('appSetting'):
        for j in i.iter('add'):
            if j.attrib.get('key') == buscador:
                value = j.attrib.get('value')
                break

    return value
