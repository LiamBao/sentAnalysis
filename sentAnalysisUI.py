# -*- coding: utf-8 -*-
#auther='liam_bao@163.com'

###########################################################################
## Python code generated with wxFormBuilder (version Sep 2017)
## https://wiki.wxpython.org//
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import sys, os
import re
# import subprocess

# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET

import wx
import wx.lib.dialogs
import wx.wizard

###########################################################################
## Class SentimentConfigWizard
###########################################################################

class dialogConfig(wx.Frame)
    
    def __init__(self):
    # 情感词典
    self.posdict = self.deal_wrap('dict/emotion_dict/pos_all_dict.txt')
    self.negdict = self.deal_wrap('dict/emotion_dict/neg_all_dict.txt')
    # 程度副词词典
    self.mostdict = self.deal_wrap('dict/degree_dict/most.txt')   # 权值为2
    self.verydict = self.deal_wrap('dict/degree_dict/very.txt')   # 权值为1.5
    self.moredict = self.deal_wrap('dict/degree_dict/more.txt')  # 权值为1.25
    self.ishdict = self.deal_wrap('dict/degree_dict/ish.txt')   # 权值为0.5
    self.insufficientdict = self.deal_wrap('dict/degree_dict/insufficiently.txt')  # 权值为0.25
    self.inversedict = self.deal_wrap('dict/degree_dict/inverse.txt')  # 权值为-1

    def clacSentiment(self, parameter_list):
        pass


if __name__=="__main__":
    app=wx.App(False)
    wizard=dialogConfig(None)
    
    wizard.FitToPage(wizard.ESXiBasicInfo)
    wizard.RunWizard(wizard.ESXiBasicInfo)
    wizard.Destroy()

    app.MainLoop()
    
