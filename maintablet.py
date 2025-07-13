from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from PyQt5.QtWebEngineWidgets import *
import pygame
import tkinterweb
from time import strftime
from tkinterweb import HtmlFrame
from datetime import datetime
import os
import sys
import shutil
import vlc
import time
import psutil
from tkinter import ttk
from tkinter import messagebox


class mainTablet:
    def __init__(self, window):
        pygame.mixer.init()
        self.window = window
        self.window = window
        self.window.geometry('800x600')
        self.window.title('ACC Tablet')
        self.window.iconbitmap('Icons\\15.ico')
        self.window.resizable(width = False, height= False)
        self.mainTabletFrame = Frame(self.window)
        self.mainTabletFrame.pack(anchor=N, fill=BOTH, expand= True, side=LEFT)
        
        cursor_path = "@arrow.cur"
        loading_cursor_path = "@loading.cur"
        self.mainTabletFrame.config(cursor=cursor_path)
        oldRestartLogo = Image.open("Icons\RestartLogo.png")
        restartLogo = ImageTk.PhotoImage(oldRestartLogo)
        
        oldShutdownLogo = Image.open("Icons\shutdownLogo.png")
        shutdownLogo = ImageTk.PhotoImage(oldShutdownLogo)
        
        oldLogOffLogo = Image.open("Icons\logoutLogo.png")
        logOffLogo = ImageTk.PhotoImage(oldLogOffLogo)
        
        loadingLogo = Image.open("Icons\loadingLogo.png")
        loadingLogo = ImageTk.PhotoImage(loadingLogo)
        
        oldsettingsLogo = Image.open("Icons\settingsIcon.png")
        settingsLogo = ImageTk.PhotoImage(oldsettingsLogo)
        
        closeLogo = Image.open("Icons\closeLogo.png")
        closeLogo = ImageTk.PhotoImage(closeLogo)
        
        oldSearchLogo = Image.open("Icons\searchButton.png")
        defaultSearchLogo = ImageTk.PhotoImage(oldSearchLogo)
        
        oldHomeLogo = Image.open("Icons\homePage.png")
        
        oldBackLogo = Image.open("Icons\BackButton.png")
        
        oldRightLogo = Image.open("Icons\RightButton.png")
        
        oldUpLogo = Image.open("Icons\\upButton.png")
        
        oldPlayPauseLogo = Image.open("Icons\playPauseLogo.png")
        
        oldFastForwardLogo = Image.open("Icons\FastForwardLogo.png")
        
        oldRewindLogo = Image.open("Icons\RewindLogo.png")
        
        oldStopLogo = Image.open("Icons\stopLogo.png")
        
        oldSelectLogo = Image.open("Icons\selectIcon.png")
        
        oldTrashLogo = Image.open("Icons\\trashIcon.png")
        
        oldOpenFileLogo = Image.open("Icons\openFileLogo.png")
        
        oldWarningLogo = Image.open("Icons\warning.png")
        
        #user preferences
        self.startColor = "Grey"
        def shutdownSystem():
            try:
                self.sound.stop()
            except AttributeError:
                pass
            def playShutdownSound():
                pygame.mixer.music.load('SoundEffect\microsoft-windows-2000-shutdown-sound.mp3')
                pygame.mixer.music.play()
            playShutdownSound()
            self.mainTabletFrame.destroy()
            shutdownFrame = Frame(self.window)
            shutdownFrame.pack(anchor=N, fill=BOTH, expand= True, side=LEFT)
            shutdownFrame.pack_propagate(False)
            shutdownFrame.config(cursor=loading_cursor_path)
            loginLogo = Image.open("Icons\mainLogo.png")
            loginLogo = ImageTk.PhotoImage(loginLogo)
            loginLabel = Label(shutdownFrame, image = loginLogo)
            loginLabel.image = loginLogo
            loginLabel.pack()
            loadingLabel = Label(shutdownFrame, image = loadingLogo)
            loadingLabel.image = loadingLogo
            loadingLabel.pack()
            shutdownLabel = Label(shutdownFrame, text = "Shutting down... Good bye.", font = ("Arial", 16))
            shutdownLabel.pack()
            shutdownFrame.after(8000, exit)
        
        def restartSystem():
            try:
                self.sound.stop()
            except AttributeError:
                pass
            def restartProgram():
                python = sys.executable
                os.execl(python, python, *sys.argv)
            def playShutdownSound():
                pygame.mixer.music.load('SoundEffect\microsoft-windows-2000-shutdown-sound.mp3')
                pygame.mixer.music.play()
            playShutdownSound()
            self.mainTabletFrame.destroy()
            shutdownFrame = Frame(self.window)
            shutdownFrame.pack(anchor=N, fill=BOTH, expand= True, side=LEFT)
            shutdownFrame.pack_propagate(False)
            shutdownFrame.config(cursor=loading_cursor_path)
            loginLogo = Image.open("Icons\mainLogo.png")
            loginLogo = ImageTk.PhotoImage(loginLogo)
            loginLabel = Label(shutdownFrame, image = loginLogo)
            loginLabel.image = loginLogo
            loginLabel.pack()
            loadingLabel = Label(shutdownFrame, image = loadingLogo)
            loadingLabel.image = loadingLogo
            loadingLabel.pack()
            shutdownLabel = Label(shutdownFrame, text = "Restarting...", font = ("Arial", 16))
            shutdownLabel.pack()
            shutdownFrame.after(8000, lambda: restartProgram())

        def loadingSystemScreen():
            def start_progress(duration):
                progress_bar['value'] = 0
                progress = 0 # Reset progress bar
                step = 1 / (duration)  # Step size to complete in 'duration' seconds

                def update():
                    nonlocal progress
                    if progress < 100:
                        progress += step
                        progress_bar['value'] += progress
                        loadingFrame.after(1, update)  # Update every 100ms (10 times per second)

                update()  # Start updating
            loadingFrame = Frame(self.mainTabletFrame, width = 800, height = 600)
            loadingFrame.pack()
            loadingFrame.pack_propagate(False)
            loadingFrame.config(cursor=loading_cursor_path)
            oldLogoLogo = Image.open("Icons\homeLogo.png")
            logo = ImageTk.PhotoImage(oldLogoLogo.resize((100,100)))
            logoLabel = Label(loadingFrame, image = logo)
            logoLabel.pack()
            logoLabel.image = logo
            logoText = Label(loadingFrame, text = "ACC Corporation")
            logoText.pack()
            progress_bar = ttk.Progressbar(loadingFrame, orient="horizontal", length=250, mode="determinate")
            progress_bar.pack(pady = 10)
            start_progress(3000)
            
            def destroyLoadingFrame():
                loadingFrame.destroy()
            loadingFrame.after(3000, lambda: destroyLoadingFrame())
        def loginScreen():
            self.loginFrame = Frame(self.mainTabletFrame, background="white", width = 800, height = 600)
            self.loginFrame.pack()
            self.loginFrame.pack_propagate(False)
            loginLogo = Image.open("Icons\mainLogo.png")
            loginLogo = ImageTk.PhotoImage(loginLogo)
            self.loginFrame.config(cursor = cursor_path)
            loginLabel = Label(self.loginFrame, image = loginLogo)
            loginLabel.image = loginLogo
            loginLabel.pack()
            
            loginButtonFrame = Frame(self.loginFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            loginButtonFrame.pack()
            
            loginButton = Button(loginButtonFrame, text = "Login", bg = "White", font = ("Arial", 16), command=lambda: loginPressed())
            loginButton.pack()
            
            smallShutdownLogo = ImageTk.PhotoImage(oldShutdownLogo.resize((49,49)))
            shutdownButtonFrame = Frame(self.loginFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            shutdownButtonFrame.place(x = 0, y = 0)
            shutdownButton = Button(shutdownButtonFrame, image = smallShutdownLogo, command = lambda: shutdownSystem())
            shutdownButton.image = smallShutdownLogo
            shutdownButton.pack()

            def loginPressed():
                loginButtonFrame.destroy()
                shutdownButtonFrame.destroy()
                self.loginFrame.config(cursor=loading_cursor_path)
                loadingLabel = Label(self.loginFrame, image = loadingLogo)
                loadingLabel.image = loadingLogo
                loadingLabel.pack()
                welcomeLabel = Label(self.loginFrame, text = "Welcome", font = ("Arial", 16), background="white")
                welcomeLabel.pack()
                self.loginFrame.after(3000, lambda: mainAppScreen())
        
        def logoutAccount():
            try:
                self.sound.stop()
            except AttributeError:
                pass
            def playLogoutSound():
                pygame.mixer.music.load('SoundEffect\win98logoff.mp3')
                pygame.mixer.music.play()
            playLogoutSound()
            
            def destroyLogOutFrame():
                shutdownFrame.destroy()
                self.mainTabletFrame = Frame(self.window)
                self.mainTabletFrame.pack(anchor=N, fill=BOTH, expand= True, side=LEFT)
                loginScreen()
            self.mainTabletFrame.destroy()
            shutdownFrame = Frame(self.window)
            shutdownFrame.pack(anchor=N, fill=BOTH, expand= True, side=LEFT)
            shutdownFrame.pack_propagate(False)
            shutdownFrame.config(cursor=loading_cursor_path)
            loginLogo = Image.open("Icons\mainLogo.png")
            loginLogo = ImageTk.PhotoImage(loginLogo)
            loginLabel = Label(shutdownFrame, image = loginLogo)
            loginLabel.image = loginLogo
            loginLabel.pack()
            loadingLabel = Label(shutdownFrame, image = loadingLogo)
            loadingLabel.image = loadingLogo
            loadingLabel.pack()
            shutdownLabel = Label(shutdownFrame, text = "Logging Off...", font = ("Arial", 16))
            shutdownLabel.pack()
            shutdownFrame.after(4000, lambda: destroyLogOutFrame())
            
        
        def mainAppScreen():
            self.loginFrame.destroy()
            def showContext(event, context):
                context.post(event.x_root, event.y_root)
            mainAppFrame = Frame(self.mainTabletFrame, width = 800, height = 600)
            mainAppFrame.pack()
            mainAppFrame.configure(bg = "Grey")
            taskbarContext = Menu(mainAppFrame, tearoff = 0)
            taskbarContext.add_command(label = "Change How Start Looks in Settings", command=lambda: settingsPressed())
            taskbarContext.add_command(label = "Change Color in Settings", command=lambda: settingsPressed())
            taskbarContext.add_command(label = "Search", command=lambda: searchPressed())
            mainAppFrame.bind("<Button-3>", lambda event: showContext(event, taskbarContext))
            
            def playStartupSound():
                pygame.mixer.music.load('SoundEffect\microsoft-windows-2000-startup-sound.mp3')
                pygame.mixer.music.play()
            playStartupSound()
            background = Image.open("Icons\defaultBackground.png")
            background = ImageTk.PhotoImage(background)
            defaultBackgroundLabel = Label(mainAppFrame, image = background)
            defaultBackgroundLabel.image = background
            defaultBackgroundLabel.place(x = 0, y = 90)
            desktopMenu = Menu(mainAppFrame, tearoff = 0)
            desktopMenu.add_command(label = "Open Explorer", command=lambda: explorePressed(defaultLocation="ExploreFiles", fileType= ""))
            desktopMenu.add_command(label = "Change Theme in Settings", command=lambda: settingsPressed())
            desktopMenu.add_command(label = "Change Desktop Background in Settings", command=lambda: settingsPressed())
            defaultBackgroundLabel.bind("<Button-3>", lambda event: showContext(event, desktopMenu))
            
            oldStartLogo = Image.open("Icons\homeLogo.png")
            logo = ImageTk.PhotoImage(oldStartLogo)
            homeButtonFrame = Frame(mainAppFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            homeButtonFrame.place(x = 0, y = 0)
            self.homeButton = Button(homeButtonFrame, image = logo, command = lambda: homePressed(mainAppFrame))
            self.homeButton.image = logo
            self.homeButton.pack()
            
            internetButtonFrame = Frame(mainAppFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            internetButtonFrame.place(x = 95, y = 0)
            internetLogo = Image.open("Icons\internetLogo.png")
            internetLogo = ImageTk.PhotoImage(internetLogo)
            internetButton = Button(internetButtonFrame, image = internetLogo, command = lambda: internetPressed())
            internetButton.image = internetLogo
            internetButton.pack()
            
            fileButtonFrame = Frame(mainAppFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            fileButtonFrame.place(x = 190, y = 0)
            fileLogo = Image.open("Icons\exploreLogo.png")
            fileLogo = ImageTk.PhotoImage(fileLogo)
            fileButton = Button(fileButtonFrame, image = fileLogo, command = lambda: explorePressed(defaultLocation="ExploreFiles", fileType= ""))
            fileButton.image = fileLogo
            fileButton.pack()
            
            playerButtonFrame = Frame(mainAppFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            playerButtonFrame.place(x = 285, y = 0)
            playerLogo = Image.open("Icons\playerLogo.png")
            playerLogo = ImageTk.PhotoImage(playerLogo)
            playerButton = Button(playerButtonFrame, image = playerLogo, command = lambda: mediaPlayerPressed())
            playerButton.image = playerLogo
            playerButton.pack()
            
            textButtonFrame =  Frame(mainAppFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
            textButtonFrame.place(x = 380, y = 0)
            textLogo = Image.open("Icons\wordLogo.png")
            textLogo = ImageTk.PhotoImage(textLogo)
            textButton = Button(textButtonFrame, image = textLogo, command = lambda: wordProcessPressed())
            textButton.image = textLogo
            textButton.pack()
            
            timeLabel = Label(mainAppFrame, text = "00:00:00", font = ("Arial, 25"), background= "grey")
            timeLabel.place(x = 600, y = 30)
            buildLabel = Label(mainAppFrame, text = "Build 0001.\nIssues will occur while using this system.\nDo not share to the public.\n", background= "white")
            buildLabel.place(x = 0, y = 400)
            
            warningSystem = Frame(mainAppFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 550)
            warningSystem.place(x = 100, y = 250)
            warningSystem.pack_propagate(False)
            warningLogo = ImageTk.PhotoImage(oldWarningLogo)
            warningImageLabel = Label(warningSystem, image = warningLogo)
            warningImageLabel.place(x = 5, y = 0)
            warningImageLabel.image = warningLogo
            appliedLabel = Label(warningSystem, text = "NOTE: Issues will occur while using the system.\nDO NOT SHARE TO THE PUBLIC" , background = "white", font = ("Arial", 15))
            appliedLabel.place(x = 100, y = 10)
            okButton = ttk.Button(warningSystem, text = "Proceed", command = lambda: closeApp(warningSystem))
            okButton.pack(pady = 80)
            
            def settingsPressed():
                def changeBackground():
                    def applyBackground():
                        if selected_option.get() == "Default":
                            background = Image.open("Icons\defaultBackground.png")
                        elif selected_option.get() == "Night Sky":
                            background = Image.open("Backgrounds\\accBetaBackground1.png")
                        elif selected_option.get() == "Fish":
                            background = Image.open("Backgrounds\\accBetaBackground2.png")
                        background = ImageTk.PhotoImage(background)
                        defaultBackgroundLabel.config(image = background)
                        defaultBackgroundLabel.image = background
                        appliedLabel.config(text = "Applied Background Change")
                    
                    askFrame = Frame(mainFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 550)
                    askFrame.place(x = 100, y = 250)
                    askFrame.pack_propagate(False)
                    appliedLabel = Label(askFrame, text = "No Changes Made", background = "white", font = ("Arial", 15))
                    appliedLabel.pack()
                    
                    # Options for dropdown menu
                    options = ["Default", "Night Sky", "Fish"]
                    selected_option = StringVar()
                    selected_option.set(options[0])  # Set default value

                    # Dropdown menu
                    dropdown = OptionMenu(askFrame, selected_option, *options)
                    dropdown.config(font=("Arial", 12))
                    dropdown.config(cursor = cursor_path)
                    dropdown.pack(pady = 15)
                    applyButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    applyButtonFrame.pack(pady = 5)
                    applyButton = Button(applyButtonFrame, text = "Apply", font = ("Arial", 16), command = lambda: applyBackground())
                    applyButton.pack()
                    okButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    okButtonFrame.pack()
                    okButton = Button(okButtonFrame, text = "Ok", font = ("Arial", 16), command = lambda: askFrame.destroy())
                    okButton.pack()
                def changeColor():
                    def applyColor():
                        if selected_option.get() == "Default":
                            mainAppFrame.configure(bg = "Grey")
                            timeLabel.config(background= "Grey")
                            self.startColor = "Grey"
                        elif selected_option.get() == "Sleek Blue":
                            mainAppFrame.configure(bg = "#4f42b5")
                            timeLabel.config(background= "#4f42b5")
                            self.startColor = "#4f42b5"
                        elif selected_option.get() == "Ocean Blue":
                            mainAppFrame.configure(bg = "#189ad3")
                            timeLabel.config(background= "#189ad3")
                            self.startColor = "#189ad3"
                        elif selected_option.get() == "Leafy Green":
                            mainAppFrame.configure(bg = "#c1d11f")
                            timeLabel.config(background= "#c1d11f")
                            self.startColor = "#c1d11f"
                            self.startMenuFrame.configure(background = "#c1d11f")
                        elif selected_option.get() == "Hot Pink":
                            mainAppFrame.configure(bg = "#FF69B4")
                            timeLabel.config(background= "#FF69B4")
                            self.startColor = "#FF69B4"
                        self.startMenuFrame.configure(background = self.startColor)
                        settingsFrame.configure(background = self.startColor)
                        titleLabel.config(bg = self.startColor)
                        appliedLabel.config(text = "Applied Color Change")
                    
                    askFrame = Frame(mainFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 550)
                    askFrame.place(x = 100, y = 250)
                    askFrame.pack_propagate(False)
                    appliedLabel = Label(askFrame, text = ("Current Color Hex: ", self.startColor) , background = "white", font = ("Arial", 15))
                    appliedLabel.pack()
                    
                    # Options for dropdown menu
                    options = ["Default", "Ocean Blue", "Sleek Blue", "Leafy Green", "Hot Pink"]
                    selected_option = StringVar()
                    selected_option.set(options[0])  # Set default value

                    # Dropdown menu
                    dropdown = OptionMenu(askFrame, selected_option, *options)
                    dropdown.config(font=("Arial", 12))
                    dropdown.pack(pady = 15)
                    applyButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    applyButtonFrame.pack(pady = 5)
                    applyButton = Button(applyButtonFrame, text = "Apply", font = ("Arial", 16), command = lambda: applyColor())
                    applyButton.pack()
                    okButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    okButtonFrame.pack()
                    okButton = Button(okButtonFrame, text = "Ok", font = ("Arial", 16), command = lambda: askFrame.destroy())
                    okButton.pack()
                def changeStart():
                    def changeStartClassic():
                        try:
                            self.startMenuFrame.destroy()
                        except AttributeError:
                            pass
                            
                        self.homeButton.config(command = lambda: homeContextPressed(mainAppFrame))
                        appliedLabel.config(text = "Applied Classic Start")
                    def changeStartDefault():
                        try:
                            self.startMenuFrame.destroy()
                        except AttributeError:
                            pass
                            
                        self.homeButton.config(command = lambda: homePressed(mainAppFrame))
                        appliedLabel.config(text = "Applied Default Start")
                    def add_tooltip(widget, text):
                        tooltip = ttk.Label(askFrame, text=text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10))
                        tooltip.place_forget()

                        def show_tooltip(event):
                            tooltip.place(x=0, y=0)

                        def hide_tooltip(event):
                            tooltip.place_forget()

                        widget.bind("<Enter>", show_tooltip)
                        widget.bind("<Leave>", hide_tooltip)
                    askFrame = Frame(mainFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 550)
                    askFrame.place(x = 100, y = 250)
                    askFrame.pack_propagate(False)
                    appliedLabel = Label(askFrame, text = "No Changes Made", background = "white", font = ("Arial", 15))
                    appliedLabel.pack()
                    classicStartButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    classicStartButtonFrame.pack()
                    classicStartButtonButton = Button(classicStartButtonFrame, text = "Classic Start", font = ("Arial", 16), command = lambda: changeStartClassic())
                    classicStartButtonButton.pack()
                    defaultStartButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    defaultStartButtonFrame.pack()
                    defaultStartButtonButton = Button(defaultStartButtonFrame, text = "Default Start", font = ("Arial", 16), command = lambda: changeStartDefault())
                    defaultStartButtonButton.pack()
                    okButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    okButtonFrame.pack(pady = 15)
                    okButton = Button(okButtonFrame, text = "Ok", font = ("Arial", 16), command = lambda: askFrame.destroy())
                    okButton.pack()
                    add_tooltip(classicStartButtonButton, "Classic start brings back the retro feeling of classic context menus.")
                    add_tooltip(defaultStartButtonButton, "Experience the latest and greatest with the ACC Default Start")
                def changeTheme():
                    def applyTheme():
                        if selected_option.get() == "Default":
                            mainAppFrame.configure(bg = "Grey")
                            timeLabel.config(background= "Grey")
                            self.startColor = "Grey"
                            background = Image.open("Icons\defaultBackground.png")
                        elif selected_option.get() == "Night Sky":
                            mainAppFrame.configure(bg = "Grey")
                            timeLabel.config(background= "Grey")
                            self.startColor = "Grey"
                            background = Image.open("Backgrounds\\accBetaBackground1.png")
                        elif selected_option.get() == "Fish":
                            mainAppFrame.configure(bg = "#189ad3")
                            timeLabel.config(background= "#189ad3")
                            self.startColor = "#189ad3"
                            background = Image.open("Backgrounds\\accBetaBackground2.png")
                        self.startMenuFrame.configure(background = self.startColor)
                        settingsFrame.configure(background = self.startColor)
                        titleLabel.config(bg = self.startColor)
                        appliedLabel.config(text = "Applied Theme Change")
                        background = ImageTk.PhotoImage(background)
                        defaultBackgroundLabel.config(image = background)
                        defaultBackgroundLabel.image = background
                    
                    askFrame = Frame(mainFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 550)
                    askFrame.place(x = 100, y = 250)
                    askFrame.pack_propagate(False)
                    appliedLabel = Label(askFrame, text = "No Changes Made", background = "white", font = ("Arial", 15))
                    appliedLabel.pack()
                    
                    # Options for dropdown menu
                    options = ["Default", "Night Sky", "Fish"]
                    selected_option = StringVar()
                    selected_option.set(options[0])  # Set default value

                    # Dropdown menu
                    dropdown = OptionMenu(askFrame, selected_option, *options)
                    dropdown.config(font=("Arial", 12))
                    dropdown.config(cursor = cursor_path)
                    dropdown.pack(pady = 15)
                    applyButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    applyButtonFrame.pack(pady = 5)
                    applyButton = Button(applyButtonFrame, text = "Apply", font = ("Arial", 16), command = lambda: applyTheme())
                    applyButton.pack()
                    okButtonFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                    okButtonFrame.pack()
                    okButton = Button(okButtonFrame, text = "Ok", font = ("Arial", 16), command = lambda: askFrame.destroy())
                    okButton.pack()
                    
                settingsFrame = Frame(mainAppFrame, width = 800, height = 600)
                settingsFrame.configure(background = self.startColor)
                settingsFrame.pack()
                titleLabel = Label(settingsFrame, text = "Settings", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(settingsFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(settingsFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(settingsFrame, width = 800, height = 515, background = "white")
                mainFrame.place(x = 0, y = 90)
                mainFrame.pack_propagate(False)
                changeStartButtonFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                changeStartButtonFrame.pack()
                changeStartButtonButton = Button(changeStartButtonFrame, text = "Change Start Appearance", font = ("Arial", 16), command = lambda: changeStart())
                changeStartButtonButton.pack()
                changeThemeFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                changeThemeFrame.pack()
                changeThemeButton = Button(changeThemeFrame, text = "Change Theme", font = ("Arial", 16), command = lambda: changeTheme())
                changeThemeButton.pack()
                changeBackgroundFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                changeBackgroundFrame.pack()
                changeBackgroundButton = Button(changeBackgroundFrame, text = "Change Background", font = ("Arial", 16), command = lambda: changeBackground())
                changeBackgroundButton.pack()
                changeColorFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                changeColorFrame.pack()
                changeColorButton = Button(changeColorFrame, text = "Change Dock Color", font = ("Arial", 16), command = lambda: changeColor())
                changeColorButton.pack()
            def clock():
                def updateTime():
                    currentTime = strftime('%I:%M:%S %p')
                    timeLabel.config(text= currentTime)
                    timeLabel.after(1000, updateTime)
                
                updateTime()
            
            def homePressed(app):
                self.homeButton.config(command = lambda: destroyStart())
                self.startMenuFrame = Frame(app, width = 90, height = 120)
                self.startMenuFrame.configure(background= self.startColor)
                self.startMenuFrame.place(x = 0, y = 100)
                def destroyStart():
                    self.startMenuFrame.destroy()
                    self.homeButton.config(command = lambda: homePressed(app))
                def allPrograms():
                    context_start = Menu(self.startMenuFrame, tearoff = 0)
                    context_start.add_command(label = "Internet", command = lambda: internetPressed())
                    context_start.add_command(label = "Explorer", command = lambda: explorePressed(defaultLocation="ExploreFiles", fileType= ""))
                    context_start.add_command(label = "Media Player", command = lambda: mediaPlayerPressed())
                    context_start.add_command(label = "Wordpad", command = lambda: wordProcessPressed())
                    context_start.add_command(label = "Clock", command = lambda: clockApp())
                    context_start.add_command(label = "ACC Game Hub", command = lambda: gameHubPressed())
                    context_start.add_command(label = "Calculator", command = lambda: calcPressed())
                    context_start.post(allProgramsButton.winfo_rootx(), allProgramsButton.winfo_rooty() + allProgramsButton.winfo_height())
                allProgramsButtonFrame = Frame(self.startMenuFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                allProgramsButtonFrame.pack()
                allProgramsButton = Button(allProgramsButtonFrame, text = "All Programs", command = lambda: allPrograms())
                allProgramsButton.pack()
                searchStart = oldSearchLogo
                searchStart = searchStart.resize((55, 55))
                searchStart = ImageTk.PhotoImage(searchStart)
                searchButtonFrame = Frame(self.startMenuFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                searchButtonFrame.pack()
                searchButton = Button(searchButtonFrame, image = searchStart, command = lambda: searchPressed())
                searchButton.image = searchStart
                searchButton.pack()
                
                settingsStart = oldsettingsLogo
                settingsStart = settingsStart.resize((55, 55))
                settingsStart = ImageTk.PhotoImage(settingsStart)
                settingsButtonFrame = Frame(self.startMenuFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                settingsButtonFrame.pack()
                settingsButton = Button(settingsButtonFrame, image = settingsStart, command = lambda: settingsPressed())
                settingsButton.image = settingsStart
                settingsButton.pack()
                
                shutdownStart = oldShutdownLogo
                shutdownStart = shutdownStart.resize((55,55))
                shutdownStart = ImageTk.PhotoImage(shutdownStart)
                shutdownButtonFrame = Frame(self.startMenuFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                shutdownButtonFrame.pack()
                shutdownButton = Button(shutdownButtonFrame, image = shutdownStart, command = lambda: shutdownSystem())
                shutdownButton.image = shutdownStart
                shutdownButton.pack()

                restartStart = oldRestartLogo
                restartStart = restartStart.resize((55,55))
                restartStart = ImageTk.PhotoImage(restartStart)
                restartButtonFrame = Frame(self.startMenuFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                restartButtonFrame.pack()
                restartButton = Button(restartButtonFrame, image = restartStart, command = lambda: restartSystem())
                restartButton.image = restartStart
                restartButton.pack()
                
                logoffStart = oldLogOffLogo
                logoffStart = logoffStart.resize((55,55))
                logoffStart = ImageTk.PhotoImage(logoffStart)
                logOffButtonFrame = Frame(self.startMenuFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                logOffButtonFrame.pack()
                logOffButton = Button(logOffButtonFrame, image = logoffStart, command = lambda: logoutAccount())
                logOffButton.image = logoffStart
                logOffButton.pack()
            def homeContextPressed(app):
                context_start = Menu(app, tearoff = 0)
                submenu = Menu(context_start, tearoff=0)
                submenu.add_command(label = "Internet", command = lambda: internetPressed())
                submenu.add_command(label = "Explorer", command = lambda: explorePressed(defaultLocation="ExploreFiles", fileType= ""))
                submenu.add_command(label = "Media Player", command = lambda: mediaPlayerPressed())
                submenu.add_command(label = "Wordpad", command = lambda: wordProcessPressed())
                submenu.add_command(label = "Clock", command = lambda: clockApp())
                submenu.add_command(label = "ACC Game Hub", command = lambda: gameHubPressed())
                submenu.add_command(label = "Calculator", command = lambda: calcPressed())
                context_start.add_command(label = "Search", command = lambda: searchPressed())
                context_start.add_command(label = "Settings", command = lambda: settingsPressed())
                context_start.add_cascade(label = "All Programs", menu = submenu)
                context_start.add_command(label = "Shutdown", command = lambda: shutdownSystem())
                context_start.add_command(label = "Restart", command = lambda: restartSystem())
                context_start.add_command(label = "Log Off", command = lambda: logoutAccount())
                context_start.post(self.homeButton.winfo_rootx(), self.homeButton.winfo_rooty() + self.homeButton.winfo_height())
            def closeApp(app):
                try:
                    self.sound.stop()
                except AttributeError:
                    pass
                app.destroy()

            def searchPressed():
                def searchEnter(text):
                    if text == "calc":
                        pass
                    elif text == "clock":
                        clockApp()
                        searchFrame.destroy()
                    elif text == "explore":
                        explorePressed(defaultLocation="ExploreFiles", fileType= "")
                        searchFrame.destroy()
                    elif text == "player":
                        mediaPlayerPressed()
                        searchFrame.destroy()
                    elif text == "system1":
                        system1Pressed()
                        searchFrame.destroy()
                    elif text == "gameHub":
                        gameHubPressed()
                        searchFrame.destroy()
                    elif text == "settings":
                        settingsPressed()
                        searchFrame.destroy()
                    elif text == "about":
                        searchFrame.destroy()
                        messagebox.showinfo("About", "ACC 1.0\nBuild 0001\nIssues will occur while using the system.\nDO NOT SHARE TO THE PUBLIC")
                    elif text == "classicstart":
                        self.startMenuFrame.destroy()
                        self.homeButton.config(command = lambda: homeContextPressed(mainAppFrame))
                        searchFrame.destroy()
                    elif text == "calculator":
                        searchFrame.destroy()
                        calcPressed()
                    else:
                        warningLabel = Label(searchFrame, text = ("There is no item stored on the system called: " + text), fg = "red", font = 16)
                        warningLabel.place(x = 0, y = 70)
                searchFrame = Frame(mainAppFrame, width = 800, height = 600)
                searchFrame.pack()
                titleLabel = Label(searchFrame, text = "Search", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                searchBoxFrame = Frame(searchFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                searchBoxFrame.place(x = 0, y = 30)
                searchBox = Entry(searchBoxFrame, font = ("Arial, 15"), width = 35)
                searchBox.pack()
                goButtonFrame = Frame(searchFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                goButtonFrame.place(x = 405, y = 30)
                searchLogo = oldSearchLogo.resize((30, 30))
                searchLogo = ImageTk.PhotoImage(searchLogo)
                searchButton = Button(goButtonFrame, image = searchLogo, command = lambda: searchEnter(searchBox.get()))
                searchButton.image = searchLogo
                searchButton.pack()
                closeButtonFrame = Frame(searchFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(searchFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                    
            
            def internetPressed():
                visitedWebsites = ["www.google.com"]
                def searchEnter(text):
                    websiteLink = "www."
                    url = ""
                    if websiteLink in text:
                        url = text
                        htmlFrame.load_website(text)
                    elif text == "Homepage":
                        htmlFrame.load_website("www.google.com")
                    else:
                        url = ("https://www.google.com/search?q=" + text)
                        htmlFrame.load_website(url)
                        searchBox.delete(0, END)
                        searchBox.insert(0, url)
                    onNavigation(url)
                
                def onNavigation(url):
                    visitedWebsites.append(url)
                    if len(visitedWebsites)-1 > 0:
                        backButton.config(state = NORMAL)

                def backPressed():
                    indexCurWebsite = ""
                
                def rightPressed():
                    indexCurWebsite = ""
                
                internetFrame = Frame(mainAppFrame, width = 800, height = 600)
                internetFrame.configure(background = self.startColor)
                internetFrame.pack()
                self.titleLabel = Label(internetFrame, text = "Internet", font = ("Arial", 15), bg = self.startColor)
                self.titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(internetFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(internetFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                htmlFrame = HtmlFrame(internetFrame, width = 800, height = 515)
                htmlFrame.place(x = 0, y = 90)
                htmlFrame.onNavigation = onNavigation
                
                searchBoxFrame = Frame(internetFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                searchBoxFrame.place(x = 195, y = 30)
                searchBox = Entry(searchBoxFrame, font = ("Arial, 15"), width = 35)
                searchBox.pack()
                
                def updateSearchBox():
                    searchBox.delete(0, END)
                    searchBox.insert(0, htmlFrame.webview.url)
                def homepagePressed():
                    htmlFrame.load_website("www.google.com")
                    searchBox.delete(0, END)
                    searchBox.insert(0, "Homepage")
                homepagePressed()
                backButtonFrame = Frame(internetFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                backButtonFrame.place(x = 15, y = 30)
                backLogo = oldBackLogo.resize((45,45))
                backLogo = ImageTk.PhotoImage(backLogo)
                backButton = Button(backButtonFrame, image = backLogo)
                backButton.image = backLogo
                backButton.pack()
                
                rightButtonFrame = Frame(internetFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                rightButtonFrame.place(x = 75, y = 30)
                rightLogo = oldRightLogo.resize((45,45))
                rightLogo = ImageTk.PhotoImage(rightLogo)
                rightButton = Button(rightButtonFrame, image = rightLogo)
                rightButton.image = rightLogo
                rightButton.pack()
                
                if len(visitedWebsites)-1 == 0:
                    backButton.config(state=DISABLED)
                    rightButton.config(state=DISABLED)
                    
                searchButtonFrame = Frame(internetFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                searchButtonFrame.place(x = 600, y = 30)
                internetSearchLogo = oldSearchLogo.resize((30, 30))
                internetSearchLogo = ImageTk.PhotoImage(internetSearchLogo)
                searchButton = Button(searchButtonFrame, image = internetSearchLogo, command = lambda: searchEnter(searchBox.get()))
                searchButton.image = internetSearchLogo
                searchButton.pack()
                
                homeButtonFrame = Frame(internetFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                homeButtonFrame.place(x = 135, y = 30)
                internetHomeLogo = oldHomeLogo.resize((45, 45))
                internetHomeLogo = ImageTk.PhotoImage(internetHomeLogo)
                homeButton = Button(homeButtonFrame, image = internetHomeLogo, command = lambda: homepagePressed())
                homeButton.image = internetHomeLogo
                homeButton.pack()

                internetFrame.after(3000, lambda: updateSearchBox())
            def explorePressed(defaultLocation, fileType):
                defaultHomeLocation = defaultLocation
                defaultFolderName = "Explorer"
                currentFolder = defaultLocation
                fileLogo = Image.open("Icons\exploreLogo.png")
                fileLogo = fileLogo.resize((134, 149))
                fileLogo = ImageTk.PhotoImage(fileLogo)
                if fileType == "System Files":
                    defaultFolderName = "system1"
                    fileLogo = Image.open("Icons\system1Logo.png")
                    fileLogo = fileLogo.resize((134, 149))
                    fileLogo = ImageTk.PhotoImage(fileLogo)
                    
                
                documentsLogo = Image.open("Icons\documentFolderLogo.png")
                documentsLogo = documentsLogo.resize((134, 149))
                documentsLogo = ImageTk.PhotoImage(documentsLogo)
                
                musicFolderLogo = Image.open("Icons\musicFolderLogo.png")
                musicFolderLogo = musicFolderLogo.resize((134, 149))
                musicFolderLogo = ImageTk.PhotoImage(musicFolderLogo)
                
                picturesFolderLogo = Image.open("Icons\picturesFolderLogo.png")
                picturesFolderLogo = picturesFolderLogo.resize((134, 149))
                picturesFolderLogo = ImageTk.PhotoImage(picturesFolderLogo)
                
                defaultFolderLogo = Image.open("Icons\defaultFolderLogo.png")
                defaultFolderLogo = defaultFolderLogo.resize((134, 149))
                defaultFolderLogo = ImageTk.PhotoImage(defaultFolderLogo)
                
                
                textLogo = Image.open("Icons\\textLogo.png")
                textLogo = textLogo.resize((134, 149))
                textLogo = ImageTk.PhotoImage(textLogo)
                
                imageLogo = Image.open("Icons\imageLogo.png")
                imageLogo = imageLogo.resize((134,149))
                imageLogo = ImageTk.PhotoImage(imageLogo)
                
                pdfLogo = Image.open("Icons\pdfLogo.png")
                pdfLogo = pdfLogo.resize((134, 149))
                pdfLogo = ImageTk.PhotoImage(pdfLogo)
                
                pythonLogo = Image.open("Icons\pythonLogo.png")
                pythonLogo = pythonLogo.resize((134, 149))
                pythonLogo = ImageTk.PhotoImage(pythonLogo
                                                )
                musicLogo = Image.open("Icons\musicIcon.png")
                musicLogo = musicLogo.resize((134, 149))
                musicLogo = ImageTk.PhotoImage(musicLogo)
                
                unknownFileLogo = Image.open("Icons\\unknownProgramLogo.png")
                unknownFileLogo = unknownFileLogo.resize((134, 149))
                unknownFileLogo = ImageTk.PhotoImage(unknownFileLogo)
                
                selectFileLogo = oldSelectLogo.resize((30, 30))
                selectFileLogo = ImageTk.PhotoImage(selectFileLogo)
                
                trashLogo = oldTrashLogo.resize((30, 30))
                trashLogo = ImageTk.PhotoImage(trashLogo)
                
                openFileLogo = oldOpenFileLogo.resize((30, 30))
                openFileLogo = ImageTk.PhotoImage(openFileLogo)
                
                renameFileLogo = Image.open("Icons\\renameFileLogo.png")
                renameFileLogo = renameFileLogo.resize((30,30))
                renameFileLogo = ImageTk.PhotoImage(renameFileLogo)
                
                def loadFiles(filePath):
                    files = os.listdir(filePath)
                    for file in files:
                        self.explorerListbox.insert(END, file)
                
                def refreshFiles(filePath):
                    self.explorerListbox.delete(0, END)
                    loadFiles(filePath)
                def deleteFile():
                    selectedIndex = self.explorerListbox.curselection()
                    if selectedIndex:
                        fileName = self.explorerListbox.get(selectedIndex)
                        filePath = os.path.join(currentFolder, fileName)
                        askFrame = Frame(mainFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 350)
                        askFrame.pack()
                        askFrame.pack_propagate(False)
                        askLabel = Label(askFrame, text = "Do you want to delete the file?", font = ("Arial", 15), background = "white")
                        askLabel.pack()
                        yesFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                        yesFrame.place(x = 10, y = 50)
                        yesButton = Button(yesFrame, text = "Yes", font = ("Arial", 15), background = "white", command = lambda: yesDelete())
                        yesButton.pack()
                        noFrame = Frame(askFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                        noFrame.place(x = 100, y = 50)
                        noButton = Button(noFrame, text = "No", font = ("Arial", 15), background = "white", command = lambda: noDelete())
                        noButton.pack()
                    
                    def yesDelete():
                        askFrame.destroy()
                        try:
                            os.remove(filePath)
                            refreshFiles(defaultHomeLocation)
                        except FileNotFoundError:
                            warningFrame = Frame(mainFrame, background = "white", highlightbackground= "black", highlightthickness= 2, height = 200, width = 350)
                            warningFrame.pack()
                            warningFrame.pack_propagate(False)
                            warningLabel = Label(warningFrame, text = "Unable to delete file.", font = ("Arial", 15), background = "white")
                            warningLabel.pack()
                            okFrame = Frame(warningFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                            okFrame.place(x = 10, y = 50)
                            okButton = Button(okFrame, text = "Ok", font = ("Arial", 15), background = "white")
                            okButton.pack()
                    
                    def noDelete():
                        askFrame.destroy()
                
                def openFile():
                    selectedIndex = self.explorerListbox.curselection()
                    if selectedIndex:
                        selectedItem = self.explorerListbox.get(selectedIndex)
                        filePath = os.path.join(defaultHomeLocation, selectedItem)
                        if os.path.isdir(filePath):
                            currentFolder = filePath
                            refreshFiles(currentFolder)
                            if currentFolder == "ExploreFiles\Documents":
                                self.fileImage.config(image = documentsLogo)
                                self.fileImage.image = documentsLogo
                                self.fileNameLabel.config(text = "Documents")
                                self.fileTypeLabel.config(text = "Folder")
                            elif currentFolder == "ExploreFiles\Music":
                                self.fileImage.config(image = musicFolderLogo)
                                self.fileImage.image = musicLogo
                                self.fileNameLabel.config(text = "Music")
                                self.fileTypeLabel.config(text = "Folder")
                            elif currentFolder == "ExploreFiles\Pictures":
                                self.fileImage.config(image = picturesFolderLogo)
                                self.fileImage.image = picturesFolderLogo
                                self.fileNameLabel.config(text = "Pictures")
                                self.fileTypeLabel.config(text = "Folder")
                            elif currentFolder == "ExploreFiles":
                                fileLogo = Image.open("Icons\exploreLogo.png")
                                fileLogo = fileLogo.resize((134, 149))
                                fileLogo = ImageTk.PhotoImage(fileLogo)
                                self.fileImage.config(image = fileLogo)
                                self.fileImage.image = fileLogo
                                self.fileNameLabel.config(text = "Explorer")
                                self.fileTypeLabel.config(text = "Folder")
                            else:
                                self.fileImage.config(image = defaultFolderLogo)
                                self.fileImage.image = defaultFolderLogo
                                self.fileNameLabel.config(text = selectedItem)
                                self.fileTypeLabel.config(text = "Folder")
                        else:
                            _, fileExtension = os.path.splitext(selectedItem)
                        

                def selectFile():
                    selectedIndex = self.explorerListbox.curselection()
                    if selectedIndex:
                        selectedItem = self.explorerListbox.get(selectedIndex)
                        filePath = os.path.join(defaultHomeLocation, selectedItem)
                        if selectedItem == "Documents":
                            self.fileImage.config(image = documentsLogo)
                            self.fileImage.image = documentsLogo
                            self.fileNameLabel.config(text = "Documents")
                            self.fileTypeLabel.config(text = "Folder")
                        elif selectedItem == "Music":
                            self.fileImage.config(image = musicFolderLogo)
                            self.fileImage.image = musicLogo
                            self.fileNameLabel.config(text = "Music")
                            self.fileTypeLabel.config(text = "Folder")
                        elif selectedItem == "Pictures":
                            self.fileImage.config(image = picturesFolderLogo)
                            self.fileImage.image = picturesFolderLogo
                            self.fileNameLabel.config(text = "Pictures")
                            self.fileTypeLabel.config(text = "Folder")
                        elif selectedItem == "ExploreFiles":
                            fileLogo = Image.open("Icons\exploreLogo.png")
                            fileLogo = fileLogo.resize((134, 149))
                            fileLogo = ImageTk.PhotoImage(fileLogo)
                            self.fileImage.config(image = fileLogo)
                            self.fileImage.image = fileLogo
                            self.fileNameLabel.config(text = "Explorer")
                            self.fileTypeLabel.config(text = "Folder")
                        else:
                            self.renameFileButton.config(state = NORMAL)
                            if os.path.isdir(filePath):
                                self.fileImage.config(image = defaultFolderLogo)
                                self.fileImage.image = defaultFolderLogo
                                self.fileNameLabel.config(text = selectedItem)
                                self.fileTypeLabel.config(text = "Folder")
                            else:
                                _, fileExtension = os.path.splitext(selectedItem)
                                image = ""
                                fileType = ""
                                if fileExtension in ['.txt', '.md']:
                                    image = textLogo
                                    fileType = "Text File"
                                elif fileExtension in ['.jpg', '.jpeg', '.png', '.gif']:
                                    image = imageLogo
                                    fileType = "Image File"
                                elif fileExtension in ['.pdf']:
                                    image = pdfLogo
                                    fileType = "PDF File"
                                elif fileExtension in ['.py']:
                                    image = pythonLogo
                                    fileType = "Python File"
                                elif fileExtension in ['.mp3']:
                                    image = musicLogo
                                    fileType = "Music File"
                                else:
                                    image = unknownFileLogo
                                    fileType = "File"
                                self.fileImage.config(image = image)
                                self.fileImage.image = image
                                self.fileNameLabel.config(text = selectedItem)
                                self.fileTypeLabel.config(text = fileType)

                        modificationTime = os.path.getatime(filePath)
                        modificationDate = datetime.fromtimestamp(modificationTime)
                        self.dateTimeModifiedLabel.config(text = (f"Last Modified: {modificationDate}"))
                        self.deleteFileButton.config(state = ACTIVE)
                        if filePath == "ExploreFiles\Documents" or filePath == "ExploreFiles\Music" or filePath == "C:\\Users\\Adam\\Documents\\Codes\\Tablet\maintablet.py" or filePath == "C:\\Users\\Adam\\Documents\\Codes\\Tablet\ExploreFiles" or filePath == "C:\\Users\\Adam\\Documents\\Codes\\Tablet\SoundEffect" or filePath == "C:\\Users\\Adam\\Documents\\Codes\\Tablet\Icons" or filePath == "ExploreFiles\Pictures":
                            self.deleteFileButton.config(state = DISABLED)
                exploreFrame = Frame(mainAppFrame, width = 800, height = 600)
                exploreFrame.configure(background = self.startColor)
                exploreFrame.pack()
                titleLabel = Label(exploreFrame, text = "Explorer", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(exploreFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(exploreFrame, width = 800, height = 515, background = "white")
                mainFrame.place(x = 0, y = 90)
                mainFrame.pack_propagate(False)
                
                backButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                backButtonFrame.place(x = 15, y = 30)
                backLogo = oldBackLogo.resize((45,45))
                backLogo = ImageTk.PhotoImage(backLogo)
                backButton = Button(backButtonFrame, image = backLogo)
                backButton.image = backLogo
                backButton.pack()
                rightButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                rightButtonFrame.place(x = 75, y = 30)
                rightLogo = oldRightLogo.resize((45,45))
                rightLogo = ImageTk.PhotoImage(rightLogo)
                rightButton = Button(rightButtonFrame, image = rightLogo)
                rightButton.image = rightLogo
                rightButton.pack()
                homeButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                homeButtonFrame.place(x = 135, y = 30)
                exploreUpLogo = oldUpLogo.resize((45, 45))
                exploreUpLogo = ImageTk.PhotoImage(exploreUpLogo)
                homeButton = Button(homeButtonFrame, image = exploreUpLogo)
                homeButton.image = exploreUpLogo
                homeButton.pack()
                
                searchBoxFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                searchBoxFrame.place(x = 195, y = 30)
                searchBox = Entry(searchBoxFrame, font = ("Arial, 15"), width = 35)
                searchBox.pack()
                goButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                goButtonFrame.place(x = 600, y = 30)
                searchLogo = oldSearchLogo.resize((30, 30))
                searchLogo = ImageTk.PhotoImage(searchLogo)
                searchButton = Button(goButtonFrame, image = searchLogo)
                searchButton.image = searchLogo
                searchButton.pack()
                
                #information column
                fileInformationFrame = Frame(mainFrame, width = 300, height = 515, background = self.startColor, highlightbackground = "black", highlightthickness = 2, bd = 0)
                fileInformationFrame.place(x = 500, y = 0)
                fileInformationFrame.pack_propagate(False)
                self.fileImage = Label(fileInformationFrame, image = fileLogo, background = self.startColor)
                self.fileImage.image = fileLogo
                self.fileImage.pack(pady = 5)
                self.fileNameLabel = Label(fileInformationFrame, text = defaultFolderName, background = self.startColor, font = ("Arial", 13))
                self.fileNameLabel.pack(pady = 5)
                self.fileTypeLabel = Label(fileInformationFrame, text = fileType, background = self.startColor, font = ("Arial", 13))
                self.fileTypeLabel.pack()
                modificationTime = os.path.getmtime(defaultHomeLocation)
                modificationDate = datetime.fromtimestamp(modificationTime)
                self.dateTimeModifiedLabel = Label(fileInformationFrame, text = (f"Last Modified: {modificationDate}"), background = self.startColor, font = ("Arial", 8))
                self.dateTimeModifiedLabel.pack()
               
                #mainExplorer
                exploreListboxFrame = Frame(mainFrame)
                exploreListboxFrame.place(x = 4, y = 40)
                self.explorerListbox = Listbox(exploreListboxFrame, font = ("Arial", 30), width = 21, height = 10, background = "white", highlightthickness= 1)
                self.explorerListbox.pack(side = LEFT, fill = BOTH)
                loadFiles(defaultHomeLocation)
                exploreListboxScroll = Scrollbar(exploreListboxFrame)
                exploreListboxScroll.pack(side = RIGHT, fill = BOTH)
                self.explorerListbox.config(yscrollcommand= exploreListboxScroll.set)
                exploreListboxScroll.config(command = self.explorerListbox.yview)
                
                selectItemButtonFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                selectItemButtonFrame.place(x = 0, y = 0)
                selectItemButton = Button(selectItemButtonFrame, background = "white", image = selectFileLogo, command = lambda: selectFile())
                selectItemButton.image = selectFileLogo
                selectItemButton.pack()
                deleteFileButtonFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                deleteFileButtonFrame.place(x = 45, y = 0)
                self.deleteFileButton = Button(deleteFileButtonFrame, background = "white", image = trashLogo, command = lambda: deleteFile())
                self.deleteFileButton.image = trashLogo
                self.deleteFileButton.pack()
                self.deleteFileButton.config(state = DISABLED)
                openFileButtonFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                openFileButtonFrame.place(x = 90, y = 0)
                openFileButton = Button(openFileButtonFrame, background = "white", image = openFileLogo, command = lambda: openFile())
                openFileButton.image = openFileLogo
                openFileButton.pack()
                renameFileButtonFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                renameFileButtonFrame.place(x = 135, y = 0)
                self.renameFileButton = Button(renameFileButtonFrame, background = "white", image = renameFileLogo)
                self.renameFileButton.image = renameFileLogo
                self.renameFileButton.pack()
                self.renameFileButton.config(state= DISABLED)
                openWithButtonFrame = Frame(mainFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                openWithButtonFrame.place(x = 180, y = 0)
                openWithButton = Button(openWithButtonFrame, text = "Open With", font = ("AriaL", 12))
                openWithButton.pack()
            def mediaPlayerPressed():
                self.sound = None
                self.pause = False
                
                def checkPlaying():
                    try:
                        if self.sound.is_playing():
                            self.currentlyPlayingSong.config(text = "Currently Playing Song")
                    except AttributeError:
                        pass
                #explore related
                def loadFiles():
                    files = os.listdir("ExploreFiles\Music")
                    for file in files:
                        self.exploreListbox.insert(END, file)
                def refreshFiles():
                    self.exploreListbox.delete(0, END)
                    loadFiles()
                def deleteFiles():
                    files = "ExploreFiles\Music"
                    selection = self.exploreListbox.curselection()
                    if selection:
                        fileName = self.exploreListbox.get(selection[0])
                        filePath = os.path.join(files, fileName)
                        try:
                            os.remove(filePath)
                            refreshFiles()
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            pass

                def importMusic():
                    files = filedialog.askopenfilenames()
                    destinationFolder = 'ExploreFiles\Music'
                    for filePath in files:
                        fileName = os.path.basename(filePath)
                        destination = os.path.join(destinationFolder, fileName)
                        shutil.copy(filePath, destination)
                    refreshFiles()

                #mediaPlayer related
                def loadMusic():
                    files = "ExploreFiles\Music"
                    selection = self.exploreListbox.curselection()
                    if selection:
                        fileName = self.exploreListbox.get(selection[0])
                        filePath = os.path.join(files, fileName)
                        try:
                            self.sound = vlc.MediaPlayer(filePath)
                            self.currentlyPlayingSong.config(text = fileName)
                        except pygame.error:
                            self.currentlyPlayingSong.config(text = "Not Playing")
                def playMusic():
                    playPauseButton.config(command = lambda: pauseMusic())
                    self.sound.play()

                def pauseMusic():
                    playPauseButton.config(command = lambda: playMusic())
                    self.sound.pause()
                def stopMusic():
                    self.sound.stop()
                    self.pause = False
                    self.currentlyPlayingSong.config(text = "Not Playing")
                def rewindMusic():
                    currentTime = self.sound.get_time()
                    self.sound.set_time(max(currentTime - 30000, 0))
                def fastForwardMusic():
                    currentTime = self.sound.get_time()
                    self.sound.set_time(currentTime + 30000)
                

                mediaFrame = Frame(mainAppFrame, width = 800, height = 600)
                mediaFrame.configure(background = self.startColor)
                mediaFrame.pack()
                titleLabel = Label(mediaFrame, text = "Media Player", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(mediaFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(mediaFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(mediaFrame, width = 800, height = 515, background = "white")
                mainFrame.place(x = 0, y = 90)
                
                musicLogo = Image.open("Icons\musicIcon.png")
                musicLogo = ImageTk.PhotoImage(musicLogo)
                currentlyPlayingFrame = Frame(mainFrame, width = 400, height = 515, background = "grey")
                currentlyPlayingFrame.place(x = 400, y = 0)
                currentlyPlayingFrame.pack_propagate(False)
                currentlyPlayingLabel = Label(currentlyPlayingFrame, text = "Currently Playing: ", font = ("Arial", 16, "bold"), background = "grey")
                currentlyPlayingLabel.pack()
                currentlyPlayingImage = Label(currentlyPlayingFrame, image = musicLogo)
                currentlyPlayingImage.image = musicLogo
                currentlyPlayingImage.pack(pady = 5)
                self.currentlyPlayingSong = Label(currentlyPlayingFrame, text = "Not Playing", background = "grey", font = ("Arial", 15), wraplength = 300)
                self.currentlyPlayingSong.pack(pady = 5)
                
                playPauseLogo = oldPlayPauseLogo.resize((50,50))
                playPauseLogo = ImageTk.PhotoImage(playPauseLogo)
                rewindLogo = oldRewindLogo.resize((30,30))
                rewindLogo = ImageTk.PhotoImage(rewindLogo)
                fastForwardLogo = oldFastForwardLogo.resize((30,30))
                fastForwardLogo = ImageTk.PhotoImage(fastForwardLogo)
                stopLogo = oldStopLogo.resize((30,30))
                stopLogo = ImageTk.PhotoImage(stopLogo)
                
                exploreFrame = Frame(mainFrame, width = 400, height = 515, background = "white")
                exploreFrame.place(x = 0, y = 0)
                loadSongButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                loadSongButtonFrame.place(x = 0, y = 0)
                loadSongButton = Button(loadSongButtonFrame, background = "white", text = "Load Song", font = ("Arial, 10"), command = lambda: loadMusic())
                loadSongButton.pack()
                importSongButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                importSongButtonFrame.place(x = 80, y = 0)
                importSongButton = Button(importSongButtonFrame, background = "white", text = "Import Music", font = ("Arial, 10"), command = lambda: importMusic())
                importSongButton.pack()
                deleteSongButtonFrame = Frame(exploreFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                deleteSongButtonFrame.place(x = 173, y = 0)
                deleteSongButton = Button(deleteSongButtonFrame, background = "white", text = "Delete Music", font = ("Arial, 10"), command = lambda: deleteFiles())
                deleteSongButton.pack()
                exploreListboxFrame = Frame(exploreFrame)
                exploreListboxFrame.place(x = 10, y = 40)
                self.exploreListbox = Listbox(exploreListboxFrame, font = ("Arial", 30), width = 16, height = 8, background = "white", highlightthickness= 1)
                self.exploreListbox.pack(side = LEFT, fill = BOTH)
                loadFiles()
                checkPlaying()
                exploreListboxScroll = Scrollbar(exploreListboxFrame)
                exploreListboxScroll.pack(side = RIGHT, fill = BOTH)
                self.exploreListbox.config(yscrollcommand= exploreListboxScroll.set)
                exploreListboxScroll.config(command = self.exploreListbox.yview)
                
                mediaButtonsFrame = Frame(mainFrame, width = 800, height = 100, background = "#101")
                mediaButtonsFrame.place(x = 0, y = 420)
                rewindButtonFrame = Frame(mediaButtonsFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                rewindButtonFrame.place(x = 300, y = 0)
                rewindButton = Button(rewindButtonFrame, image = rewindLogo, command = lambda: rewindMusic())
                rewindButton.image = rewindLogo
                rewindButton.pack()
                fastForwardButtonFrame = Frame(mediaButtonsFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                fastForwardButtonFrame.place(x = 420, y = 0)
                fastForwardButton = Button(fastForwardButtonFrame, image = fastForwardLogo, command = lambda: fastForwardMusic())
                fastForwardButton.image = fastForwardLogo
                fastForwardButton.pack()
                playPauseButtonFrame = Frame(mediaButtonsFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                playPauseButtonFrame.place(x = 350, y = 0)
                playPauseButton = Button(playPauseButtonFrame, image = playPauseLogo, command = lambda: playMusic())
                playPauseButton.image = playPauseLogo
                playPauseButton.pack()
                stopMusicButtonFrame = Frame(mediaButtonsFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                stopMusicButtonFrame.place(x = 465, y = 0)
                stopMusicButton = Button(stopMusicButtonFrame, image = stopLogo, command = lambda: stopMusic())
                stopMusicButton.image = stopLogo
                stopMusicButton.pack()
                
            def wordProcessPressed():
                wordFrame = Frame(mainAppFrame, width = 800, height = 600)
                wordFrame.configure(background = self.startColor)
                wordFrame.pack()
                wordFrame.pack_propagate(False)
                titleLabel = Label(wordFrame, text = "Wordpad", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(wordFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(wordFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(wordFrame, width = 800, height = 515, background = "white")
                mainFrame.place(x = 0, y = 90)
                toolBarFrame = Frame(mainFrame, width = 800, height = 45, background = "#D3D3D3")
                toolBarFrame.place(x = 0, y = 0)
                
                saveButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                openButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                copyButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                pasteButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                cutButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                fontFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                sizeFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                boldButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                italicsButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                underlineButtonFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                fontColorFrame = Frame(toolBarFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                textboxFrame = Frame(wordFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                textboxFrame.pack(pady = 140)
                textbox = Text(textboxFrame, width = 80, height = 60, font = ("Arial"))
                textbox.pack(side = "left", fill = "both", expand=True)
                wordpadScroll = Scrollbar(textboxFrame, orient="vertical", command=textbox.yview)
                wordpadScroll.pack(side = "right", fill = "y")
                textbox.config(yscrollcommand = wordpadScroll.set)
            #programs that are hidden
            def calcPressed():
                calcFrame = Frame(mainAppFrame, width = 800, height = 600)
                calcFrame.configure(background = self.startColor)
                calcFrame.pack()
                titleLabel = Label(calcFrame, text = "Calculator", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(calcFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(calcFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(calcFrame, width = 800, height = 515, background = "white")
                mainFrame.place(x = 0, y = 90)
                mainFrame.pack_propagate(False)
                # Function to handle button click
                def on_click(event):
                    global expression
                    text = event.widget.cget("text")
                    if text == "=":
                        try:
                            result = eval(expression)
                            input_var.set(result)
                            expression = str(result)
                        except Exception as e:
                            input_var.set("Error")
                            expression = ""
                    elif text == "C":
                        expression = ""
                        input_var.set("")
                    else:
                        expression += text
                        input_var.set(expression)

                # Expression variable
                global expression
                expression = ""
                input_var = StringVar()

                # Input field
                input_field = Entry(mainFrame, textvar=input_var, font=("Arial", 20), justify='right')
                input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)
                input_field.config(state = "readonly")

                # Button layout
                buttons = [
                    ["7", "8", "9", "/"],
                    ["4", "5", "6", "*"],
                    ["1", "2", "3", "-"],
                    ["C", "0", "=", "+"]
                ]

                # Add buttons to the window
                for i, row in enumerate(buttons):
                    for j, btn_text in enumerate(row):
                        button = Button(mainFrame, text=btn_text, font=("Arial", 20), width=5, height=2)
                        button.grid(row=i + 1, column=j, padx=5, pady=5)
                        button.bind("<Button-1>", on_click)
                                
            def clockApp():
                def clock():
                    def updateTime():
                        currentTime = strftime('%I:%M:%S %p')
                        clockLabel.config(text= currentTime)
                        clockLabel.after(1000, updateTime)
                    
                    updateTime()
                clockFrame = Frame(mainAppFrame, width = 800, height = 600)
                clockFrame.configure(background = self.startColor)
                clockFrame.pack()
                titleLabel = Label(clockFrame, text = "Clock App", font = ("Arial", 15), bg = self.startColor)
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(clockFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(clockFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(clockFrame, width = 800, height = 515, background = "black")
                mainFrame.place(x = 0, y = 90)
                mainFrame.pack_propagate(False)
                clockLabel = Label(mainFrame, font = ('digital-7', 50, 'bold'), background = 'black', foreground= 'red')
                clockLabel.pack()
                clock()
            
            def internetBetaPressed():
                pass
            
            def gameHubPressed():
                gameHubFrame = Frame(mainAppFrame, width = 800, height = 600)
                gameHubFrame.pack()
                titleLabel = Label(gameHubFrame, text = "ACC Game Hub", font = ("Arial", 15))
                titleLabel.place(x = 0, y = 0)
                closeButtonFrame = Frame(gameHubFrame, highlightbackground= "black", highlightthickness= 2, bd = 0)
                closeButtonFrame.place(x = 700, y = 0)
                closeButton = Button(closeButtonFrame, image = closeLogo, command = lambda: closeApp(gameHubFrame))
                closeButton.image = closeLogo
                closeButton.pack()
                mainFrame = Frame(gameHubFrame, width = 800, height = 515, background = "black")
                mainFrame.place(x = 0, y = 90)
                mainFrame.pack_propagate(False)
            def system1Pressed():
                defaultHomeLocation = "C:\\Users\\Adam\\Documents\\Codes\\Tablet"
                explorePressed(defaultHomeLocation, fileType= "System Files")
                
            
            
            clock()       
        loadingSystemScreen()
        loginScreen()
        
def page():
    window = Tk()
    mainTablet(window)
    window.mainloop()
       
if __name__ == '__main__':
    page()