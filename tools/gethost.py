#!/usr/bin/env python
# -*- coding:GBK -*-
__author__ = ''

import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os
def pro():
    config = configparser.ConfigParser()
    pro_config_file = './config/runmodeconfig_test.conf'
    config.read(pro_config_file, encoding='utf-8')

    projectname = config.get('PROJECT', 'runame')
    return projectname
def host(project):
    config = configparser.ConfigParser()
    host_config_file = './config/dbconfig.conf'
    config.read(host_config_file, encoding='utf-8')

    url = config.get(project, 'url')
    return url
