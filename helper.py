# -*- coding: utf-8 -*-
##__author__=='Liam'#
import time
# import datetime
import xlsxwriter as wx
# from lxml import etree
# import re

# def parseDate(datestr):
#     if re.search('(\d+).*天[之|以]?前',datestr):
#         tmp=re.search('(\d+).*天[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(days = int(tmp)))
#     elif re.search('(\d+).*日[之|以]?前',datestr):
#         tmp=re.search('(\d+).*日[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(days = int(tmp)))
#     elif re.search('(\d+).*周[之|以]?前',datestr):
#         tmp=re.search('(\d+).*周[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(weeks = int(tmp)))
#     elif re.search('(\d+).*秒[钟]?[之|以]?前',datestr):
#         tmp=re.search('(\d+).*秒[钟]?[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(seconds = int(tmp)))
#     elif re.search('(\d+).*分钟[之|以]?前',datestr):
#         tmp=re.search('(\d+).*分钟[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(minutes = int(tmp)))
#     elif re.search('(\d+)个?.*星期[之|以]?前',datestr):
#         tmp=re.search('(\d+)个?.*星期[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(weeks = int(tmp)))
#     elif re.search('(\d+)个?.*礼拜[之|以]?前',datestr):
#         tmp=re.search('(\d+)个?.*礼拜[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(weeks = int(tmp)))
#     elif re.search('(\d+)个?.*小时[之|以]?前',datestr):
#         tmp=re.search('(\d+)个?.*小时[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(hours = int(tmp)))
#     elif re.search('(\d+)个?.*钟头[之|以]?前',datestr):
#         tmp=re.search('(\d+)个?.*钟头[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(hours = int(tmp)))
#     elif re.search('(\d+)个?.*钟点[之|以]?前',datestr):
#         tmp=re.search('(\d+)个?.*钟点[之|以]?前',datestr).group(1)
#         date_pa = (datetime.datetime.now() - datetime.timedelta(hours = int(tmp)))
#     elif re.search('(\d+)个?.*月[之|以]?前',datestr):
#         tmp=re.search('(\d+)个?.*月[之|以]?前',datestr).group(1)
#         date_pa = datetime.datetime.now() - relativedelta.relativedelta(months = int(tmp))
#     elif re.search('(\d+).*年[之|以]?前',datestr):
#         tmp=re.search('(\d+).*年[之|以]?前',datestr).group(1)
#         date_pa = datetime.datetime.now() - relativedelta.relativedelta(years = int(tmp))
#     elif re.search('\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}',datestr):
#         tmp=re.search('\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}',datestr).group()
#         date_pa=time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
#     elif re.search('\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}',datestr):
#         tmp=re.search('\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}',datestr).group()
#         date_pa=time.strptime(tmp, "%Y-%m-%d %H:%M")
#     elif  re.search('\d{4}-\d{1,2}-\d{1,2}',datestr):
#         tmp=re.search('\d{4}-\d{1,2}-\d{1,2}',datestr).group()
#         date_pa=time.strptime(tmp, "%Y-%m-%d")
#     elif  re.match('.*今.*天.*',datestr):
#         today = datetime.date.today()
#         if re.search('\d{1,2}:\d{1,2}:\d{1,2}',datestr):
#             tmp=re.search('\d{1,2}:\d{1,2}:\d{1,2}',datestr).group()
#             date_pa=time.strptime(str(today)+' '+tmp, "%Y-%m-%d %H:%M:%S")
#         else:
#             date_pa=time.strptime(str(today), "%Y-%m-%d")
#     elif re.match('.*昨.*天.*',datestr):
#         day = datetime.date.today()- datetime.timedelta(days=1)
#         if re.search('\d{1,2}:\d{1,2}:\d{1,2}',datestr):
#             tmp=re.search('\d{1,2}:\d{1,2}:\d{1,2}',datestr).group()
#             date_pa=time.strptime(str(day)+' '+tmp, "%Y-%m-%d %H:%M:%S")
#         else:
#             date_pa=time.strptime(str(day), "%Y-%m-%d")
#     elif re.match('.*前.*天.*',datestr):
#         day = datetime.date.today()- datetime.timedelta(days=2)
#         if re.search('\d{1,2}:\d{1,2}:\d{1,2}',datestr):
#             tmp=re.search('\d{1,2}:\d{1,2}:\d{1,2}',datestr).group()
#             date_pa=time.strptime(str(day)+' '+tmp, "%Y-%m-%d %H:%M:%S")
#         else:
#             date_pa=time.strptime(str(day), "%Y-%m-%d")
#     return date_pa


# def parseDateStr(date_pa):
#     return time.strftime("%Y-%m-%d %H:%M:%S", date_pa)


# def parseDateStrToStamp(datestr):
#     return time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))


def getExcel(filename, title, data):
    try:
        file_name = '%s%s' % (filename, ("%d" % (time.time() * 1000)))

        workbook = wx.Workbook(file_name + '.xlsx')
        worksheet = workbook.add_worksheet('post')
        for i in range(len(data)):
            for j in range(len(title)):
                if i == 0:
                    worksheet.write(i, j, title[j])
                worksheet.write(i + 1, j, data[i][j])

        workbook.close()
        print('\n File ' + file_name + ' Done!')
    except Exception as err:
        print(err)


# def json2html(json):
#     json = json.json()
#     json = str(json.get('msg')[1])
#     xmldata = etree.HTML(json)
#     return xmldata


# import ctypes  

# STD_INPUT_HANDLE = -10  
# STD_OUTPUT_HANDLE= -11  
# STD_ERROR_HANDLE = -12  
  
# FOREGROUND_BLACK = 0x0  
# FOREGROUND_BLUE = 0x01 # text color contains blue.  
# FOREGROUND_GREEN= 0x02 # text color contains green.  
# FOREGROUND_RED = 0x04 # text color contains red.  
# FOREGROUND_INTENSITY = 0x08 # text color is intensified.  
  
# BACKGROUND_BLUE = 0x10 # background color contains blue.  
# BACKGROUND_GREEN= 0x20 # background color contains green.  
# BACKGROUND_RED = 0x40 # background color contains red.  
# BACKGROUND_INTENSITY = 0x80 # background color is intensified.  
  
# class Color:  
#     ''''' See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp 
#     for information on Windows APIs.'''  
#     std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)  
      
#     def set_cmd_color(self, color, handle=std_out_handle):  
#         """(color) -> bit 
#         Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY) 
#         """  
#         bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)  
#         return bool  
      
#     def reset_color(self):  
#         self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)  
      
#     def print_red_text(self, print_text):  
#         self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)  
#         print (print_text)  
#         self.reset_color()  
          
#     def print_green_text(self, print_text):  
#         self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)  
#         print (print_text)  
#         self.reset_color()  
      
#     def print_blue_text(self, print_text):   
#         self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)  
#         print (print_text)  
#         self.reset_color()  
            
#     def print_red_text_with_blue_bg(self, print_text):  
#         self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)  
#         print (print_text)    
#         self.reset_color()      
  
# if __name__ == "__main__":  
#     clr = Color()  
#     clr.print_red_text('red')  
#     clr.print_green_text('green')  
#     clr.print_blue_text('blue')  
#     clr.print_red_text_with_blue_bg('background') 
    