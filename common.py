# -*- coding:utf-8 -*-
#作者：琴弦上的宇宙
#时间：2021年10月22日

import cv2
import pyautogui
import time
import win32gui
import win32con
import win32api

def FindHearthStoneWindow():
    handle=win32gui.FindWindow("UnityWndClass","炉石传说")
    if handle>0:
        left,top,right,bottom=win32gui.GetWindowRect(handle)
        if left>0 and top>0 and right>0 and bottom>0:
            return True,left,top,right,bottom,handle
    return False,0,0,0,0,handle

w,h=pyautogui.size()
def moveAndClick(x,y,t=1.5):
    if x>=10 and x<=(w-10) and y>=10 and y<=(h-10):
        pyautogui.moveTo(x,y)
        time.sleep(0.1)
        pyautogui.mouseDown(x,y)
        time.sleep(0.1)
        pyautogui.mouseUp(x,y)
        time.sleep(0.3)
        bFind,left,top,right,bottom,_nouse=FindHearthStoneWindow()
        if bFind:
            pyautogui.moveTo(left+20,top+10)
        else:
            pyautogui.moveTo(10,10)
        time.sleep(t)

def Move(x,y):
    pyautogui.moveTo(x,y)

def Scroll(x,y,bUp,s):
    pyautogui.moveTo(x,y)
    pyautogui.click()
    time.sleep(1)
    for i in range(s):
        if bUp:
            pyautogui.scroll(1)
        else:
            pyautogui.scroll(-1)
    time.sleep(0.1)
    bFind,left,top,right,bottom=FindHearthStoneWindow()
    if bFind:
        pyautogui.moveTo(left+20,top+10)
    else:
        pyautogui.moveTo(10,10)

def Click(x,y,b='left',t=0):
    if x>=10 and x<=(w-10) and y>=10 and y<=(h-10):
        pyautogui.mouseDown(x,y,button=b)
        time.sleep(0.1)
        pyautogui.mouseUp(x,y,button=b)
        time.sleep(0.1)
        bFind,left,top,right,bottom=FindHearthStoneWindow()
        if bFind:
            pyautogui.moveTo(left+20,top+10)
        else:
            pyautogui.moveTo(10,10)
        time.sleep(t)

def Drag(x0,y0,x1,y1,t=1.5):
    if x0>=10 and x0<=(w-10) and y0>=10 and y0<=(h-10) and \
       x1>=10 and x1<=(w-10) and y1>=10 and y1<=(h-10):
        pyautogui.moveTo(x0,y0)
        pyautogui.mouseDown(x0,y0)
        time.sleep(0.1)
        pyautogui.moveTo(x1,y1)
        time.sleep(0.1)
        pyautogui.mouseUp(x1,y1)
        time.sleep(0.1)
        bFind,left,top,right,bottom=FindHearthStoneWindow()
        if bFind:
            pyautogui.moveTo(left+20,top+10)
        else:
            pyautogui.moveTo(10,10)
        time.sleep(t)

def SaveScreen():
    bFind,left,top,right,bottom=FindHearthStoneWindow()
    if bFind:
        pyautogui.screenshot("resource/background.png",
            region=(left,top,right-left,bottom-top))
    else:
        pyautogui.screenshot("resource/background.png")
    return cv2.imread("resource/background.png",cv2.IMREAD_GRAYSCALE)

def SetModelPos(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,700,400, win32con.SWP_SHOWWINDOW)

def HeartStop():
    time.sleep(3*60)