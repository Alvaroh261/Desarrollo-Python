# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:23:07 2022

@author: Usuario
"""
# Import Module
import ConfigurationManager as conf
import logging
import sshtunnel
import pymysql
import pymongo


def connect_ssh(verbose=False, puerto=0):
    """Abrir el túnel SSH y conéctarse con un nombre de usuario y una contraseña.

    :param puerto: Puerto por el que conexta la base de datos
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    ssh_host = str(conf.appsettings("ssh.host"))
    ssh_username = str(conf.appsettings("ssh.username"))
    ssh_password = str(conf.appsettings("ssh.password"))

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    tunnel = sshtunnel.SSHTunnelForwarder(
        (ssh_host, 22), ssh_username=ssh_username, ssh_password=ssh_password,
        remote_bind_address=('127.0.0.1', int(puerto))
    )
    tunnel.start()

    return tunnel


def mysql_connect():
    """Abrir el túnel SSH y conéctarse con un nombre de usuario y una contraseña.
         Conéctese a un servidor MySQL usando la conexión de túnel SSH

    :return conn: Conexion a la base de datos de MySQL
    """
    tunnel = connect_ssh(False, conf.connectionstring("mysql.port"))

    conn = pymysql.connect(
        host=conf.connectionstring("mysql.host"),
        user=conf.connectionstring("mysql.username"),
        passwd=conf.connectionstring("mysql.password"),
        db=conf.connectionstring("mysql.database"),
        port=tunnel.local_bind_port
    )

    return conn, tunnel


def mongodb_connect():
    """Abrir el túnel SSH y conéctarse con un nombre de usuario y una contraseña.
         Conéctese a un servidor MySQL usando la conexión de túnel SSH

    :return tunnel: Conexion a la base de datos de MongoDB
    """
    tunnel = connect_ssh(False, 27017)

    uri = "mongodb://" + conf.connectionstring("mongodb.username") + ":" + conf.connectionstring(
        "mongodb.password") + "@" + conf.connectionstring("mongodb.host") + ":" + str(tunnel.local_bind_port)
    conn = pymongo.MongoClient(uri)

    return conn, tunnel


# SERVIDOR Y CUENTA DE CORREO POR DEFECTO
# El servidor que gestiona los correos enviados por la plataforma
def servidorCorreo():
    return conf.appsettings("email.Servidor")


# El remitente de los correos enviados por la plataforma
def remitenteCorreo():
    return conf.appsettings("email.Remitente")


# El usuario de la cuenta de correo
def usuarioCorreo():
    return conf.appsettings("email.User")


# El pass de la cuenta de correo
def passwordCorreo(): return conf.appsettings("email.Password")


# El puerto por el que trabaja el servidor
def puertoCorreo(): return conf.appsettings("email.Port")


# El puerto por el que trabaja el servidor
def sshPuerto(): return conf.appsettings("ssh.port")


# El puerto por el que trabaja el servidor
def sshHost(): return conf.appsettings("ssh.host")


# El puerto por el que trabaja el servidor
def sshUser(): return conf.appsettings("ssh.username")


# El puerto por el que trabaja el servidor
def sshPasswd(): return conf.appsettings("ssh.password")


# El puerto por el que trabaja el servidor
def sshRemoteBindAddress(): return conf.appsettings("sshremote_bind_address")


# El puerto por el que trabaja el servidor
def sshRemoteBindAddressPort(): return conf.appsettings("ssh.remote_bind_address_port")
