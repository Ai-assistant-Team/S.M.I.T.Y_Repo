#https://pythonprogramming.altervista.org/animate-gif-in-tkinter/
##https://gist.github.com/skywodd/8b68bd9c7af048afcedcea3fb1807966

from tkinter import *
import tkinter as tk
from PIL import Image, ImageSequence, ImageTk
from itertools import count, cycle
import datetime
import pathlib
from tkinter import filedialog

from spotipy.client import Spotify
from Calendar import *
from playMusicSpotify import *
from translator import translateText
from open_program import *
from alarmClock import *

 
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
            #a = int((257/1920)*w)+5
            #b = int((261/1080)*h)+5
            #temp_image2 = im.resize((a, b),Image.ANTIALIAS)
            #im = ImageTk.PhotoImage(temp_image2)

        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def resize_gif(wi,hi):
    location = pathlib.Path(__file__).parent.absolute()
    # Output (max) size
    size = wi , hi

    # Open source
    im = Image.open('%s\\Home page\\home page gif3.gif'%(location))

    # Get sequence iterator
    frames = ImageSequence.Iterator(im)

    # Wrap on-the-fly thumbnail generator
    def thumbnails(frames):
        for frame in frames:
            thumbnail = frame.copy()
            thumbnail.thumbnail(size, Image.ANTIALIAS)
            yield thumbnail

    frames = thumbnails(frames)

    # Save output
    om = next(frames) # Handle first frame separately
    om.info = im.info # Copy sequence info
    om.save("aaa.gif", save_all=True, append_images=list(frames))

def process_comand(comand):
    if comand.__contains__('calendar'):
        calendar.pack(fill='both', expand =1)
        home_page.forget()
    elif comand.__contains__("settings"):
        home_page_go_to_setings("Button-1>")
    elif comand.__contains__('show me my tasks for ' ):
        date = comand.replace('show me my tasks for ','')
        date =turn_text_to_date(date)
        return show_me(date)
    elif comand.__contains__('spotify'):
        open_program('spotify')
        time.sleep(8)
        if comand.__contains__('from spotify') and comand.__contains__('play'):
            if comand.__contains__('by'):
                comand = comand.replace('play ','')
                comand = comand.replace(' from spotify','')
                comand2=comand.split(" by ")
                song_name = comand2[0]
                artist_name = comand2[1]
                songbyTitle(song_name,artist_name)
                return "Playing "+ song_name
            else:
                comand = comand.replace('play ','')
                comand = comand.replace(' from spotify','')
                songbyTitle(comand,None)
                return "Playing "+ comand
        elif comand.__contains__('pause'):
            pausePlayback()
            return 'Playback Paused'
        elif comand.__contains__('resume'):
            resumePlayback()
            return 'Playback Resumed'
        elif (comand.__contains__('add') and comand.__contains__('queue')):
            song = comand.replace('add ','')
            song  = song.replace(' to queue','')
            addToQueue(song)
            return song+' Added To The Queue'
        elif comand.__contains__('next song'):
            playNext()
            return 'Skiped To Next Track'
        elif comand.__contains__('Previous song'):
            playPrev()
            return 'Skipped To Previous Track'
    elif comand.__contains__('translate'):
        comand = comand.replace('translate ','')
        comand2=comand.split(" to ")
        text = comand2[0]
        language = comand2[1]
        return str(translateText(text,language))
    elif (comand.__contains__('open')):
        if comand.__contains__('notepad'):
            open_program('notepad')
            return 'Notepad is open'
        elif comand.__contains__('calculator'):
            open_program('calculator')
            return 'Calculator is open'
        elif comand.__contains__('messenger'):
            open_program('messenger')
            return 'Messenger is open'
        elif comand.__contains__('exlel'):
            open_program('exlel')
            return 'Exlel is open'
        elif comand.__contains__('word'):
            open_program('word')
            return 'Word is open'
        elif comand.__contains__('powerpoint'):
            open_program('powerpoint')
            return 'Powerpoint is open'
        elif comand.__contains__('access'):
            open_program('access')
            return 'Sccess is open'
        elif comand.__contains__('spotify'):
            open_program('spotify')
            return 'Spotify is open'
        

def get_comand(event):
    global message_history
    global line_count
    line_count = line_count +1
    if line_count == 8:
        line_count =0
        message_history =''
    message_history = message_history + '\nYou : ' + str(home_page_comand_text_field.get())
    message_history_label_text_field.config(text = message_history)
    message_history = message_history + '\nS.M.I.T.Y : ' + process_comand(str(home_page_comand_text_field.get()))
    line_count = line_count +1
    message_history_label_text_field.config(text = message_history)
    if line_count == 8:
        line_count =0
        message_history =''

def home_page_go_to_setings(event):
    settings.pack(fill='both', expand =1)
    home_page.forget()

def home_page_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    home_page_cloce_button.place_forget()
    home_page_exit_fullscreen_button.place_forget()
    home_page_fullscreen_button.place(relx = 0.96, rely = 0.0, width=((62*1920)/w), height=(28*1080)/h)

def home_page_fullscreen(event):
    screen.attributes('-fullscreen', True)
    home_page_fullscreen_button.place_forget()
    home_page_cloce_button.place(relx = 0.985, rely = 0.0, width=31, height=28)
    home_page_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=31, height=28)
    
def home_page_to_calendar(event):
    calendar.pack(fill='both', expand =1)
    home_page.forget()

def settings_save():
    global gender
    global settings_voice_control_on
    global settings_speak_key_on
    global settings_wake_up_on
    location = pathlib.Path(__file__).parent.absolute()
    f = open("%s\\settings.txt"%(location), "w")
    #Gender
    f.write('S.M.I.T.Y. Gender : ')
    f.write(gender)
    f.write('\n')
    #Username
    f.write('Username : ')
    f.write(str(settings_user_name_text_field.get()))
    f.write('\n')
    #Voice control
    if(settings_voice_control_on == 0):
        f.write('Voice control : 0\n')
    elif (settings_voice_control_on == 2):
        f.write('Voice control : 2\n')
    else:
        f.write('Voice control : 1\n')
    #Speak key
    if(settings_speak_key_on == 0):
        f.write('Speak key : 0\n')
    elif (settings_speak_key_on == 2):
        f.write('Speak key : 2\n')
    else:
        f.write('Speak key : 1\n')
    #Voice wake up
    if(settings_wake_up_on == 0 ):
        f.write('Voice wake up : 0\n')
    elif( settings_wake_up_on == 2):
        f.write('Voice wake up : 2\n')
    else:
        f.write('Voice wake up : 1\n')
    f.close()

def settings_load():
    global gender
    global settings_voice_control_on
    global settings_speak_key_on
    global settings_wake_up_on
    location = pathlib.Path(__file__).parent.absolute()
    f = open("%s\\settings.txt"%(location), "r")
    load_gender = f.readline()
    load_username = f.readline()
    load_settings_voice_control_on = f.readline()
    load_settings_speak_key_on = f.readline()
    load_settings_wake_up_on = f.readline()
    f.close()
    #Gender
    if(load_gender == 'S.M.I.T.Y. Gender : male\n'):
        settings_female_button.config(image = settings_female_off)
        settings_male_button.config(image = settings_male_on)
        gender = 'mele'
    else:
        settings_female_button.config(image = settings_female_on)
        settings_male_button.config(image = settings_male_off)
        gender = 'femele'
    #User name
    load_username = load_username.replace('Username : ','')
    load_username = load_username.replace('\n','')
    settings_user_name_text_field.delete(0, tk.END)
    settings_user_name_text_field.insert(0, load_username)
    #Voice control
    if(load_settings_voice_control_on == 'Voice control : 1\n'):
        settings_voice_control_on = 1
        settings_voice_control_button.config(image = settings_switch_on)
    elif (load_settings_voice_control_on == 'Voice control : 0\n') :
        settings_voice_control_on = 0
        settings_voice_control_button.config(image = settings_switch_off)
    elif (load_settings_voice_control_on == 'Voice control : 2\n') :
        settings_voice_control_on = 2
        settings_voice_control_button.config(image = settings_switch_off)
    
    #Speak key
    if(load_settings_speak_key_on == 'Speak key : 1\n'):
        settings_speak_key_on = 1
        settings_speak_key_button.config(image = settings_switch_on)
    elif (load_settings_speak_key_on == 'Speak key : 0\n') :
        settings_speak_key_on = 0
        settings_speak_key_button.config(image = settings_switch_off)
    elif (load_settings_speak_key_on == 'Speak key : 2\n') :
        settings_speak_key_on = 2
        settings_speak_key_button.config(image = settings_switch_off)
    
    #Voice wake up
    if(load_settings_wake_up_on == 'Voice wake up : 1\n'):
        settings_wake_up_on = 1
        settings_wake_up_button.config(image = settings_switch_on)
    elif (load_settings_wake_up_on == 'Voice wake up : 0\n') :
        settings_wake_up_on = 0
        settings_wake_up_button.config(image = settings_switch_off)
    elif (load_settings_wake_up_on == 'Voice wake up : 2\n') :
        settings_wake_up_on = 2
        settings_wake_up_button.config(image = settings_switch_off)
    
    


def settings_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    settings_cloce_button.place_forget()
    settings_exit_fullscreen_button.place_forget()
    settings_fullscreen_button.place(relx = 0.96, rely = 0.0, width=((62/1920)*w), height =(28/1080)*h)
    
def activate_female(event):
    global gender
    settings_female_button.config(image = settings_female_on)
    settings_male_button.config(image = settings_male_off)
    gender = 'female'

def activate_male(event):
    global gender 
    settings_female_button.config(image = settings_female_off)
    settings_male_button.config(image = settings_male_on)
    gender = 'male'

def activate_deactivate_voice_control(event):
    global settings_voice_control_on
    global settings_speak_key_on
    global settings_wake_up_on
    if settings_voice_control_on == 1:
        settings_voice_control_on = 0
        settings_voice_control_button.config(image = settings_switch_off)
        if settings_speak_key_on == 1:
            settings_speak_key_on = 2
        settings_speak_key_button.config(image = settings_switch_off)
        if settings_wake_up_on == 1:
            settings_wake_up_on = 2
        settings_wake_up_button.config(image = settings_switch_off)

    elif settings_voice_control_on == 0:
        settings_voice_control_on = 1
        settings_voice_control_button.config(image = settings_switch_on)
        if settings_speak_key_on == 2:
            settings_speak_key_on = 1
            settings_speak_key_button.config(image = settings_switch_on)
        if settings_wake_up_on == 2:
            settings_wake_up_on = 1
            settings_wake_up_button.config(image = settings_switch_on)

def activate_deactivate_speak_key(event):
    global settings_voice_control_on
    global settings_speak_key_on
    if settings_speak_key_on == 1:
        settings_speak_key_on = 0
        settings_speak_key_button.config(image = settings_switch_off)

    elif settings_speak_key_on == 0 or settings_speak_key_on == 2:
        settings_speak_key_on = 1
        settings_speak_key_button.config(image = settings_switch_on)
        settings_voice_control_on = 1
        settings_voice_control_button.config(image = settings_switch_on)


def activate_deactivate_wake_up(event):
    global settings_wake_up_on
    if settings_wake_up_on == 1:
        settings_wake_up_on = 0
        settings_wake_up_button.config(image = settings_switch_off)
        
    elif settings_wake_up_on == 0 or settings_wake_up_on == 2:
        settings_wake_up_on = 1
        settings_wake_up_button.config(image = settings_switch_on)
        settings_voice_control_on = 1
        settings_voice_control_button.config(image = settings_switch_on)

def settings_fullscreen(event):
    screen.attributes('-fullscreen', True)
    settings_fullscreen_button.place_forget()
    settings_cloce_button.place(relx = 0.985, rely = 0.0, width=31, height=28)
    settings_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)

def settings_go_to_home(event):
    home_page.pack(fill='both', expand =1)
    settings_save()
    settings.forget()

def settings_go_to_about(event):
    about_page.pack(fill='both', expand =1)
    settings.forget()

def settings_go_to_aplications(event):
    aplications.pack(fill='both', expand =1)
    settings.forget()

def about_page_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    about_page_cloce_button.place_forget()
    about_page_exit_fullscreen_button.place_forget()
    about_page_fullscreen_button.place(relx = 0.96, rely = 0.0, width=((62/1920)*w), height =(28/1080)*h)

def about_page_fullscreen(event):
    screen.attributes('-fullscreen', True)
    about_page_fullscreen_button.place_forget()
    about_page_cloce_button.place(relx = 0.985, rely = 0.0, width=31, height=28)
    about_page_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)


def about_page_go_to_settings(event):
    settings.pack(fill='both', expand =1)
    about_page.forget()

def about_page_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    about_page.forget()

def aplications_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    aplications_cloce_button.place_forget()
    aplications_exit_fullscreen_button.place_forget()
    aplications_fullscreen_button.place(relx = 0.96, rely = 0.0,width=((62/1920)*w), height =(28/1080)*h)

def aplications_fullscreen(event):
    screen.attributes('-fullscreen', True)
    aplications_fullscreen_button.place_forget()
    aplications_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
    aplications_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)

def aplications_go_to_settings(event):
    settings.pack(fill='both', expand =1)
    aplications.forget()

def aplications_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    aplications.forget()

def aplications_go_to_users_aplications(event):
    users_aplications.pack(fill='both', expand =1)
    aplications.forget()

def aplications_go_to_change_location(event):
    change_location.pack(fill='both', expand =1)
    aplications.forget()

def users_aplications_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    users_aplications_cloce_button.place_forget()
    users_aplications_exit_fullscreen_button.place_forget()
    users_aplications_fullscreen_button.place(relx = 0.96, rely = 0.0, width=62, height=28)

def users_aplications_fullscreen(event):
    screen.attributes('-fullscreen', True)
    users_aplications_fullscreen_button.place_forget()
    users_aplications_cloce_button.place(relx = 0.985, rely = 0.0, width=31, height=28)
    users_aplications_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=31, height=28)

def users_aplications_go_to_settings(event):
    settings.pack(fill='both', expand =1)
    users_aplications.forget()

def users_aplications_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    users_aplications.forget()

def users_aplications_go_to_add_aplications(event):
    add_aplication.pack(fill='both', expand =1)
    users_aplications.forget()

def add_aplication_go_to_users_aplications(event):
    users_aplications.pack(fill='both', expand =1)
    add_aplication.forget()

def add_aplications_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    add_aplication.forget()

def add_aplication_add_button(event):
    print(str(add_aplication_name_input.get()) + "\n"+str(add_aplication_location_input.get()))
    users_aplications.pack(fill='both', expand =1)
    add_aplication.forget()

def add_aplication_exit_fullscreen (event):
    screen.attributes('-fullscreen', False)
    add_aplication_cloce_button.place_forget()
    add_aplication_exit_fullscreen_button.place_forget()
    add_aplication_fullscreen_button.place(relx = 0.96, rely = 0.0, width=((62/1920)*w), height=(28/1080)*h)

def add_aplication_fullscreen (event):
    screen.attributes('-fullscreen', True)
    add_aplication_fullscreen_button.place_forget()
    add_aplication_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
    add_aplication_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)

def file_browse():
    location = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("all files", "*.*"),("jpg files", "*.jpg")))
    return str(location)

def add_aplication_location(event):
    add_aplication_location_input.insert(0, file_browse())

def minimize(event):
    screen.iconify()
def calendar_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    calendar_cloce_button.place_forget()
    calendar_exit_fullscreen_button.place_forget()
    calendar_fullscreen_button.place(relx = 0.96, rely = 0.0, width=62, height=28)

def calendar_fullscreen(event):
    screen.attributes('-fullscreen', True)
    calendar_fullscreen_button.place_forget()
    calendar_cloce_button.place(relx = 0.985, rely = 0.0, width=31, height=28)
    calendar_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=31, height=28)

def calendar_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    calendar.forget()

def get_todays_x_rel_position():
    calendar_x_rel_positions = [0.0435, 0.1735, 0.304, 0.434, 0.5645, 0.695, 0.8246]

    today = datetime.datetime.now()
    name_of_today = today.strftime("%a")

    if(name_of_today == "Sun"):
        return calendar_x_rel_positions[0]
    elif (name_of_today == "Mon"):
        return calendar_x_rel_positions[1]
    elif (name_of_today == "Tue"):
        return calendar_x_rel_positions[2]
    elif (name_of_today == "Wed"):
        return calendar_x_rel_positions[3]
    elif (name_of_today == "Thu"):
        return calendar_x_rel_positions[4]
    elif (name_of_today == "Fri"):
        return calendar_x_rel_positions[5]
    elif (name_of_today == "Sat"):
        return calendar_x_rel_positions[6]


    

def get_todays_y_rel_position():
    calendar_y_rel_positions = [0.104, 0.255, 0.4065, 0.557, 0.7094, 0.8599]

    today = datetime.datetime.now()
    months_first = datetime.datetime(today.year, today.month, 1)
    name_of_today = today.strftime("%a")
    name_of_months_first = months_first.strftime("%a")

    if(name_of_months_first == "Sun"):
        number = 0
    elif (name_of_months_first == "Mon"):
        number = 1
    elif (name_of_months_first == "Tue"):
        number = 2
    elif (name_of_months_first == "Wed"):
        number = 3
    elif (name_of_months_first == "Thu"):
        number = 4
    elif (name_of_months_first == "Fri"):
        number = 5
    elif (name_of_months_first == "Sat"):
        number = 6


    if name_of_months_first == "Sun" or name_of_months_first == "Mon" or name_of_months_first == "Tue" or name_of_months_first == "Wed" or name_of_months_first == "Thu":
        if(today.day<8-number):
            return calendar_y_rel_positions[0]
        elif(today.day <15-number):
            return calendar_y_rel_positions[1]
        elif(today.day <22-number):
            return calendar_y_rel_positions[2]
        elif(today.day <29-number):
            return calendar_y_rel_positions[3]
        else:
            return calendar_y_rel_positions[4]
    else:
        if(today.day<8-number):
           return calendar_y_rel_positions[0]
        elif(today.day <15-number):
            return calendar_y_rel_positions[1]
        elif(today.day <22-number):
           return calendar_y_rel_positions[2]
        elif(today.day <29-number):
            return calendar_y_rel_positions[3]
        elif(today.day <36-number):
            return calendar_y_rel_positions[4]
        else:
            return calendar_y_rel_positions[5]


def choose_months_image(month_number,year):
    date_of_months_first = datetime.datetime(year, month_number, 1)
    days_of_months_first = date_of_months_first.strftime("%a")
    #if february
    if(month_number == 2):
        #if february has 29 days
        if( year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            #if 1/2 = sunday
            if(days_of_months_first == "Sun"):
                calendar_month_days_label.config( image = calendar_sunday_29 )
            #if 1/2 = monday
            elif (days_of_months_first == "Mon"):
                 calendar_month_days_label.config( image = calendar_monday_29 )
                 #if 1/2 = tuesday
            elif (days_of_months_first == "Tue"):
                 calendar_month_days_label.config( image = calendar_tuesday_29 )
                 #if 1/2 = wednesday
            elif (days_of_months_first == "Wed"):
                 calendar_month_days_label.config( image = calendar_wednesday_29 )
                 #if 1/2 = thursday
            elif (days_of_months_first == "Thu"):
                 calendar_month_days_label.config( image = calendar_thursday_29 )
                 #if 1/2 = friday
            elif (days_of_months_first == "Fri"):
                 calendar_month_days_label.config( image = calendar_friday_29 )
                 #if 1/2 = saturday
            elif (days_of_months_first == "Sat"):
                 calendar_month_days_label.config( image = calendar_saturday_29 )
        else:
            #if 1/2 = sunday
            if(days_of_months_first == "Sun"):
                calendar_month_days_label.config( image = calendar_sunday_28 )
            #if 1/2 = monday
            elif (days_of_months_first == "Mon"):
                 calendar_month_days_label.config( image = calendar_monday_28 )
                 #if 1/2 = tuesday
            elif (days_of_months_first == "Tue"):
                 calendar_month_days_label.config( image = calendar_tuesday_28 )
                 #if 1/2 = wednesday
            elif (days_of_months_first == "Wed"):
                 calendar_month_days_label.config( image = calendar_wednesday_28 )
                 #if 1/2 = thursday
            elif (days_of_months_first == "Thu"):
                 calendar_month_days_label.config( image = calendar_thursday_28 )
                 #if 1/2 = friday
            elif (days_of_months_first == "Fri"):
                 calendar_month_days_label.config( image = calendar_friday_28 )
                 #if 1/2 = saturday
            elif (days_of_months_first == "Sat"):
                 calendar_month_days_label.config( image = calendar_saturday_28 )
    #month with 31 days
    elif month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12 :
        #if 1/2 = sunday
            if(days_of_months_first == "Sun"):
                calendar_month_days_label.config( image = calendar_sunday_31 )
            #if 1/2 = monday
            elif (days_of_months_first == "Mon"):
                 calendar_month_days_label.config( image = calendar_monday_31 )
                 #if 1/2 = tuesday
            elif (days_of_months_first == "Tue"):
                 calendar_month_days_label.config( image = calendar_tuesday_31 )
                 #if 1/2 = wednesday
            elif (days_of_months_first == "Wed"):
                 calendar_month_days_label.config( image = calendar_wednesday_31 )
                 #if 1/2 = thursday
            elif (days_of_months_first == "Thu"):
                 calendar_month_days_label.config( image = calendar_thursday_31 )
                 #if 1/2 = friday
            elif (days_of_months_first == "Fri"):
                 calendar_month_days_label.config( image = calendar_friday_31 )
                 #if 1/2 = saturday
            elif (days_of_months_first == "Sat"):
                 calendar_month_days_label.config( image = calendar_saturday_31 )
    elif month_number == 2 or month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11 :
        #if 1/2 = sunday
            if(days_of_months_first == "Sun"):
                calendar_month_days_label.config( image = calendar_sunday_30 )
            #if 1/2 = monday
            elif (days_of_months_first == "Mon"):
                 calendar_month_days_label.config( image = calendar_monday_30 )
                 #if 1/2 = tuesday
            elif (days_of_months_first == "Tue"):
                 calendar_month_days_label.config( image = calendar_tuesday_30 )
                 #if 1/2 = wednesday
            elif (days_of_months_first == "Wed"):
                 calendar_month_days_label.config( image = calendar_wednesday_30 )
                 #if 1/2 = thursday
            elif (days_of_months_first == "Thu"):
                 calendar_month_days_label.config( image = calendar_thursday_30 )
                 #if 1/2 = friday
            elif (days_of_months_first == "Fri"):
                 calendar_month_days_label.config( image = calendar_friday_30 )
                 #if 1/2 = saturday
            elif (days_of_months_first == "Sat"):
                 calendar_month_days_label.config( image = calendar_saturday_30 )


def get_year_first_digit(year):
    if(year>=0 and year <1000):
        calendar_year_fists_position.config(image = calendar_zero )
    elif(year <2000):
        calendar_year_fists_position.config(image = calendar_one )
    elif(year <3000):
        calendar_year_fists_position.config(image = calendar_two )
    elif(year <4000):
        calendar_year_fists_position.config(image = calendar_three )
    elif(year <5000):
        calendar_year_fists_position.config(image = calendar_four )
    elif(year <6000):
        calendar_year_fists_position.config(image = calendar_five )
    elif(year <7000):
        calendar_year_fists_position.config(image = calendar_six )
    elif(year <8000):
        calendar_year_fists_position.config(image = calendar_seven )
    elif(year <9000):
        calendar_year_fists_position.config(image = calendar_eight )
    elif(year <10000):
        calendar_year_fists_position.config(image = calendar_eight )

def get_year_second_digit(year):
    if(year>=0 and year <100):
        calendar_year_second_position.config(image = calendar_zero )
    elif(year <200):
        calendar_year_second_position.config(image = calendar_one )
    elif(year <300):
        calendar_year_second_position.config(image = calendar_two )
    elif(year <400):
        calendar_year_second_position.config(image = calendar_three )
    elif(year <500):
        calendar_year_second_position.config(image = calendar_four )
    elif(year <600):
        calendar_year_second_position.config(image = calendar_five )
    elif(year <700):
        calendar_year_second_position.config(image = calendar_six )
    elif(year <800):
        calendar_year_second_position.config(image = calendar_seven )
    elif(year <900):
        calendar_year_second_position.config(image = calendar_eight )
    elif(year <1000):
        calendar_year_second_position.config(image = calendar_eight )

def get_year_third_digit(year):
    if(year>=0 and year <10):
        calendar_year_third_position.config(image = calendar_zero )
    elif(year <20):
        calendar_year_third_position.config(image = calendar_one )
    elif(year <30):
        calendar_year_third_position.config(image = calendar_two )
    elif(year <40):
        calendar_year_third_position.config(image = calendar_three )
    elif(year <50):
        calendar_year_third_position.config(image = calendar_four )
    elif(year <60):
        calendar_year_third_position.config(image = calendar_five )
    elif(year <70):
        calendar_year_third_position.config(image = calendar_six )
    elif(year <80):
        calendar_year_third_position.config(image = calendar_seven )
    elif(year <90):
        calendar_year_third_position.config(image = calendar_eight )
    elif(year <100):
        calendar_year_third_position.config(image = calendar_eight )

def get_year_fourth_digit(year):
    if(year>=0 and year <1):
        calendar_year_fourth_position.config(image = calendar_zero )
    elif(year <2):
        calendar_year_fourth_position.config(image = calendar_one )
    elif(year <3):
        calendar_year_fourth_position.config(image = calendar_two )
    elif(year <4):
        calendar_year_fourth_position.config(image = calendar_three )
    elif(year <5):
        calendar_year_fourth_position.config(image = calendar_four )
    elif(year <6):
        calendar_year_fourth_position.config(image = calendar_five )
    elif(year <7):
        calendar_year_fourth_position.config(image = calendar_six )
    elif(year <8):
        calendar_year_fourth_position.config(image = calendar_seven )
    elif(year <9):
        calendar_year_fourth_position.config(image = calendar_eight )
    elif(year <10):
        calendar_year_fourth_position.config(image = calendar_eight )

def get_year(year):
    get_year_first_digit(year)
    get_year_second_digit(year%1000)
    get_year_third_digit(year%100)
    get_year_fourth_digit(year%10)

def get_next_month_name_image(event):
    global month
    global year

    month = month +1

    if(month == 13):
        month =1
        year = year +1
        get_year(year)
    choose_months_image(month,year)
    today = datetime.datetime.now()
    if(month == today.month and year == today.year):
        calendar_today_label.config(relx = get_todays_x_rel_position(), rely = get_todays_y_rel_position())
    if month == 1:
        calendar_month_label.config(image = calendar_january)
    elif month == 2:
        calendar_month_label.config(image = calendar_february)
    elif month == 3:
        calendar_month_label.config(image = calendar_march)
    elif month == 4:
        calendar_month_label.config(image = calendar_april)
    elif month == 5:
        calendar_month_label.config(image = calendar_may)
    elif month == 6:
        calendar_month_label.config(image = calendar_june)
    elif month == 7:
        calendar_month_label.config(image = calendar_july)
    elif month == 8:
        calendar_month_label.config(image = calendar_august)
    elif month == 9:
        calendar_month_label.config(image = calendar_september)
    elif month == 10:
        calendar_month_label.config(image = calendar_octomber)
    elif month == 11:
        calendar_month_label.config(image = calendar_november)
    elif month == 12:
        calendar_month_label.config(image = calendar_december)

def get_previous_month_name_image(event):
    global month
    global year
    month = month -1
    if(month == 0):
        month =12
        year = year -1
        get_year(year)
    choose_months_image(month,year)
    today = datetime.datetime.now()
    if(month == today.month and year == today.year):
        calendar_today_label.config(relx = get_todays_x_rel_position(), rely = get_todays_y_rel_position())
    if month == 1:
        calendar_month_label.config(image = calendar_january)
    elif month == 2:
        calendar_month_label.config(image = calendar_february)
    elif month == 3:
        calendar_month_label.config(image = calendar_march)
    elif month == 4:
        calendar_month_label.config(image = calendar_april)
    elif month == 5:
        calendar_month_label.config(image = calendar_may)
    elif month == 6:
        calendar_month_label.config(image = calendar_june)
    elif month == 7:
        calendar_month_label.config(image = calendar_july)
    elif month == 8:
        calendar_month_label.config(image = calendar_august)
    elif month == 9:
        calendar_month_label.config(image = calendar_september)
    elif month == 10:
        calendar_month_label.config(image = calendar_octomber)
    elif month == 11:
        calendar_month_label.config(image = calendar_november)
    elif month == 12:
        calendar_month_label.config(image = calendar_december)

def go_to_my_websites(event):
    my_websites.pack(fill='both', expand =1)
    aplications.forget()

def my_websites_go_to_aplications(event):
    aplications.pack(fill='both', expand =1)
    my_websites.forget()

def my_websites_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    my_websites.forget()

def users_urls_load(names,urls):
    location = pathlib.Path(__file__).parent.absolute()
    f = open("%s\\users_urls.txt"%(location), "r")
    for x in range(10):
        temp = f.readline()
        names[x] = temp.replace('\n','')
        temp = f.readline()
        urls[x] = temp.replace('\n','')
    f.close()

def my_websites_go_to_add_website(event,number):
    global website_number
    website_number = number
    add_website.pack(fill='both', expand =1)
    my_websites.forget()

def my_websites_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    my_websites_cloce_button.place_forget()
    my_websites_exit_fullscreen_button.place_forget()
    my_websites_fullscreen_button.place(relx = 0.96, rely = 0.0,width=((62/1920)*w), height =(28/1080)*h)

def my_websites_fullscreen(event):
    screen.attributes('-fullscreen', True)
    my_websites_fullscreen_button.place_forget()
    my_websites_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
    my_websites_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)


def add_website_go_to_users_aplications(event):
    my_websites.pack(fill='both', expand =1)
    add_website.forget()

def add_a_website(event,websites_name,websites_url):
    names = ["ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE"]
    urls = ["ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL"]
    
    location = pathlib.Path(__file__).parent.absolute()
    f = open("%s\\users_urls.txt"%(location), "r")
    for x in range(10):
        names[x] = f.readline()
        urls[x] = f.readline()
    f.close()
    names[website_number]= websites_name + '\n'
    urls[website_number] = websites_url + '\n'
    f = open("%s\\users_urls.txt"%(location), "w")
    for b in range(10):
        f.write(names[b])
        f.write(urls[b])
    f.close()

    my_websites.pack(fill='both', expand =1)
    add_website.forget()

def add_websites_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    add_website_cloce_button.place_forget()
    add_website_exit_fullscreen_button.place_forget()
    add_website_fullscreen_button.place(relx = 0.96, rely = 0.0,width=((62/1920)*w), height =(28/1080)*h)

def add_websites_fullscreen(event):
    screen.attributes('-fullscreen', True)
    add_website_fullscreen_button.place_forget()
    add_website_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
    add_website_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)

def change_location_exit_fullscreen(event):
    screen.attributes('-fullscreen', False)
    change_location_cloce_button.place_forget()
    change_location_exit_fullscreen_button.place_forget()
    change_location_fullscreen_button.place(relx = 0.96, rely = 0.0,width=((62/1920)*w), height =(28/1080)*h)

def change_location_fullscreen(event):
    screen.attributes('-fullscreen', True)
    change_location_fullscreen_button.place_forget()
    change_location_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
    change_location_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)

def change_location_go_to_users_aplications(event):
    users_aplications.pack(fill='both', expand =1)
    change_location.forget()

def change_location_go_to_home_page(event):
    home_page.pack(fill='both', expand =1)
    change_location.forget()

def change_location(event,name,location):
    users_aplications.pack(fill='both', expand =1)
    change_location.forget()



screen = tk.Tk()
screen.title("Home")
w, h = screen.winfo_screenwidth(), screen.winfo_screenheight()
screen.geometry("%dx%d+0+0" % (w, h))

screen.attributes('-fullscreen', True)
location = pathlib.Path(__file__).parent.absolute()
#############################################################################################################################################################################
#      A       DDDDDD                A        PPPPPPPP    PPPPPPPP
#     A A      D     D              A A       PP      PP  PP      PP
#    A   A     D      D            A   A      PP      PP  PP      PP
#   AAAAAAA    D      D           AAAAAAA     PPPPPPPP    PPPPPPPP
#  A       A   D     D           A       A    PP          PP
# A         A  DDDDDD           A         A   PP          PP
#############################################################################################################################################################################
add_aplication = tk.Frame()
#BackGround
        #open image
add_aplication_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
add_aplication_resized_backGroundImage = add_aplication_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

add_aplication_new_backGroundImage = ImageTk.PhotoImage(add_aplication_resized_backGroundImage)
    #Label
add_aplication_backGroundImage_label = Label(add_aplication, image=add_aplication_new_backGroundImage, borderwidth=0)
#header
add_aplication_header = Label(add_aplication,borderwidth=0,background = "#0d0029")

temp_image = Image.open("%s\\Add Aplications\\title.png"%(location))
a = int((1336/1920)*w)+5
b = int((171/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_title_image = ImageTk.PhotoImage(temp_image2)
add_aplication_title = Label(add_aplication_header,image = add_aplication_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_title_aktri_image = ImageTk.PhotoImage(temp_image2)
add_aplication_title_aktri = Label(add_aplication_header,image = add_aplication_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_cloce_button_image = ImageTk.PhotoImage(temp_image2)
add_aplication_cloce_button = tk.Button(add_aplication_header,image = add_aplication_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
add_aplication_exit_fullscreen_button = tk.Button(add_aplication_header,image = add_aplication_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_minimize_button_image = ImageTk.PhotoImage(temp_image2)
add_aplication_minimize_button = tk.Button(add_aplication_header,image = add_aplication_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
add_aplication_fullscreen_button = tk.Button(add_aplication_header,image = add_aplication_fullscreen_button_image, borderwidth=0)

add_aplication_exit_fullscreen_button.bind("<Button-1>", add_aplication_exit_fullscreen)
add_aplication_fullscreen_button.bind("<Button-1>",add_aplication_fullscreen)
add_aplication_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
add_aplication_home_button = tk.Button(add_aplication_header, text = ' ', image = add_aplication_home_button_image, borderwidth=0)
add_aplication_home_button.bind("<Button-1>",add_aplications_go_to_home_page)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
add_aplication_user_button = tk.Button(add_aplication_header, image = add_aplication_user_button_image, borderwidth=0)

#user text label
add_aplication_user_text_label =Label(add_aplication_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#Name label
temp_image = Image.open("%s\\Add Aplications\\name.png"%(location))
a = int((191/1920)*w)+5
b = int((53/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_name_label_image = ImageTk.PhotoImage(temp_image2)
add_aplication_name_label =Label(add_aplication_backGroundImage_label, borderwidth=0, image = add_aplication_name_label_image)

#Location label
temp_image = Image.open("%s\\Add Aplications\\location.png"%(location))
a = int((268/1920)*w)+5
b = int((56/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_location_label_image = ImageTk.PhotoImage(temp_image2)
add_aplication_location_label =Label(add_aplication_backGroundImage_label, borderwidth=0, image = add_aplication_location_label_image)

#name text spot label
    #label
temp_image = Image.open("%s\\Add Aplications\\text_spot.png"%(location))
a = int(0.544*w)
b = int((84/1080)*h)
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_text_spot_label_image = ImageTk.PhotoImage(temp_image2)
add_aplication_name_text_spot_label =Label(add_aplication_backGroundImage_label, borderwidth=0, image = add_aplication_text_spot_label_image)
    #input
add_aplication_name_input = tk.Entry(add_aplication_name_text_spot_label, font = ("", 33), fg = "#00f9ff", width =1000 , borderwidth =0,background = "#167f95")

#location text spot label
    #label
add_aplication_location_text_spot_label =Label(add_aplication_backGroundImage_label, borderwidth=0, image = add_aplication_text_spot_label_image)
    #input
add_aplication_location_input = tk.Entry(add_aplication_location_text_spot_label, font = ("", 33), fg = "#00f9ff", width =1000 , borderwidth =0,background = "#167f95")


#browse to files button
    # Define image
temp_image = Image.open("%s\\Add Aplications\\browse_to_files.png"%(location))
a = int((164/1920)*w)+5
b = int((217/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_browse_to_files_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
add_aplication_browse_to_files_button = tk.Button(add_aplication_backGroundImage_label, image = add_aplication_browse_to_files_button_image, borderwidth=0)
add_aplication_browse_to_files_button.bind("<Button-1>",add_aplication_location)

#Cancel button
    # Define image
temp_image = Image.open("%s\\Add Aplications\\Cancel.png"%(location))
a = int((220/1920)*w)+5
b = int((97/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_cancel_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
add_aplication_cancel_button = Button(add_aplication_backGroundImage_label, text = ' ', image = add_aplication_cancel_button_image, borderwidth=0)
add_aplication_cancel_button.bind("<Button-1>",add_aplication_go_to_users_aplications)
#Add button
    # Add image
temp_image = Image.open("%s\\Add Aplications\\add.png"%(location))
a = int((162/1920)*w)+5
b = int((94/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_aplication_add_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
add_aplication_add_button_button = Button(add_aplication_backGroundImage_label, text = ' ', image = add_aplication_add_button_image, borderwidth=0, command=lambda:add_a_website ("<Button-1>,",9))



#add to window
add_aplication_backGroundImage_label.place( relx=0.0, rely= 0.15 )
add_aplication_header.place(relx=0.0, y= 0.0, width = w,height =(171/1080)*h)
add_aplication_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((1336/1920)*w), height=(171/1080)*h)
add_aplication_title_aktri.place(relx = 0.925, rely = 0.95,anchor ="sw", width=((142/1920)*w), height=(108/1080)*h)
add_aplication_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height=(43/1080)*h)
add_aplication_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height=(43/1080)*h)#-5x-5
add_aplication_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w), height=(43/1080)*h)
add_aplication_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
add_aplication_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
add_aplication_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)


add_aplication_name_label.place(relx = 0.05, rely = 0.2, width=((191/1920)*w), height=(53/1080)*h)
add_aplication_name_text_spot_label.place(relx = 0.25, rely = 0.18, relwidth=0.544, height=(84/1080)*h)
add_aplication_name_input.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(70/1080)*h)

add_aplication_location_label.place(relx = 0.05, rely = 0.4, width=((268/1920)*w), height=(56/1080)*h)
add_aplication_location_text_spot_label.place(relx = 0.25, rely = 0.375, relwidth=0.544, height=(84/1080)*h)
add_aplication_location_input.place(relx = 0.01, rely = 0.1, relwidth=0.97, height=(70/1080)*h)

add_aplication_browse_to_files_button.place(relx = 0.83, rely = 0.366, width=((164/1920)*w), height=(217/1080)*h)
add_aplication_cancel_button.place(relx=0.05, rely=0.858, width=((220/1920)*w), height=(97/1080)*h)
add_aplication_add_button_button.place(relx=0.884, rely=0.8599, width=((162/1920)*w), height=(94/1080)*h)
#############################################################################################################################################################################
#   ww            ww
#    ww    ww    ww
#     ww  wwww  ww
#      wwww  wwww
#       ww    ww
#############################################################################################################################################################################

my_websites= tk.Frame()
#BackGround
        #open image
my_websites_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
my_websites_resized_backGroundImage = my_websites_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

my_websites_new_backGroundImage = ImageTk.PhotoImage(my_websites_resized_backGroundImage)

    #Label
my_websites_backGroundImage_label = Label(my_websites, image=my_websites_new_backGroundImage, borderwidth=0)

#header
my_websites_header = Label(my_websites,borderwidth=0,background = "#0d0029")
#title
temp_image = Image.open("%s\\my websites\\title.png"%(location))
a = int((512/1920)*w)+5
b = int((56/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_title_image = ImageTk.PhotoImage(temp_image2)
my_websites_title = Label(my_websites_header,image = my_websites_title_image, borderwidth=0)
#akri titlou
temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_title_aktri_image = ImageTk.PhotoImage(temp_image2)
my_websites_title_aktri = Label(my_websites_header,image = my_websites_title_aktri_image, borderwidth=0)
#exit button
temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_cloce_button_image = ImageTk.PhotoImage(temp_image2)
my_websites_cloce_button = tk.Button(my_websites_header,image = my_websites_cloce_button_image, borderwidth=0, command = screen.destroy)
#exit fullscreen button
temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
my_websites_exit_fullscreen_button = tk.Button(my_websites_header,image = my_websites_exit_fullscreen_button_image, borderwidth=0)

#minimize window
temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_minimize_button_image = ImageTk.PhotoImage(temp_image2)
my_websites_minimize_button = tk.Button(my_websites_header,image = my_websites_minimize_button_image, borderwidth=0)
#fullscreen button
my_websites_fullscreen_button_image = PhotoImage(file="%s\\fullscreen_button.png"%(location))
temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
my_websites_fullscreen_button = tk.Button(my_websites_header,image = my_websites_fullscreen_button_image, borderwidth=0)

my_websites_exit_fullscreen_button.bind("<Button-1>", my_websites_exit_fullscreen)
my_websites_fullscreen_button.bind("<Button-1>",my_websites_fullscreen)
my_websites_minimize_button.bind("<Button-1>", minimize)

#back button
    # Define image
temp_image = Image.open("%s\\back_button.png"%(location))
a = int((48/1920)*w)+5
b = int((34/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_back_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
my_websites_back_button = tk.Button(my_websites_header, text = ' ', image = my_websites_back_button_image, borderwidth=0)
my_websites_back_button.bind("<Button-1>",my_websites_go_to_aplications)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
my_websites_home_button = tk.Button(my_websites_header, text = ' ', image = my_websites_home_button_image, borderwidth=0)
my_websites_home_button.bind("<Button-1>",my_websites_go_to_home_page)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
my_websites_user_button = tk.Button(my_websites_header, image = my_websites_user_button_image, borderwidth=0)

#user text label
my_websites_user_text_label =Label(my_websites_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#Change / Save websites buttons
    # Define image 1
temp_image = Image.open("%s\\my websites\\change-save_url.png"%(location))
a = int((376/1920)*w)+5
b = int((57/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_change_open_url_button_image = ImageTk.PhotoImage(temp_image2)
    # Define image 2
temp_image = Image.open("%s\\my websites\\change-save_url_2.png"%(location))
a = int((376/1920)*w)+5
b = int((57/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
my_websites_change_open_url_button_image_2 = ImageTk.PhotoImage(temp_image2)
    #define button
        #1
my_websites_change_save_url_label_1 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image_2, borderwidth=0)
        #2
my_websites_change_save_url_label_2 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image_2, borderwidth=0)
        #3
my_websites_change_save_url_label_3 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image_2, borderwidth=0)
        #4
my_websites_change_save_url_label_4 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image_2, borderwidth=0)
        #5
my_websites_change_save_url_label_5 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image_2, borderwidth=0)
        #6
my_websites_change_save_url_label_6 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image, borderwidth=0)
        #7
my_websites_change_save_url_label_7 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image, borderwidth=0)
        #8
my_websites_change_save_url_label_8 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image, borderwidth=0)
        #9
my_websites_change_save_url_label_9 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image, borderwidth=0)
        #10
my_websites_change_save_url_label_10 = Label(my_websites_backGroundImage_label, text = ' ', image = my_websites_change_open_url_button_image, borderwidth=0)

#load urls ans names
websites_names = ["ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE", "ADD WEBSITE"]
websites_url = ["ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL", "ADD URL"]

users_urls_load(websites_names,websites_url)

my_websites_url_1_name =Label(my_websites_change_save_url_label_1,text = websites_names[0] , borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_2_name =Label(my_websites_change_save_url_label_2,text = websites_names[1], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_3_name =Label(my_websites_change_save_url_label_3,text = websites_names[2], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_4_name =Label(my_websites_change_save_url_label_4,text = websites_names[3], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_5_name =Label(my_websites_change_save_url_label_5,text = websites_names[4], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_6_name =Label(my_websites_change_save_url_label_6,text = websites_names[5], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_7_name =Label(my_websites_change_save_url_label_7,text = websites_names[6], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_8_name =Label(my_websites_change_save_url_label_8,text = websites_names[7], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_9_name =Label(my_websites_change_save_url_label_9,text = websites_names[8], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))
my_websites_url_10_name =Label(my_websites_change_save_url_label_10,text = websites_names[9], borderwidth=0,background = "#167f95",fg = "#47d9fe", font = ("", 30))

#change seve url
    # setings button image
temp_image = Image.open("%s\\my websites\\go_to.png"%(location))
a = int((90/1920)*w)+5
b = int((62/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_save_url_button_image = ImageTk.PhotoImage(temp_image2)
#change seve ur2
    # setings button image
temp_image = Image.open("%s\\my websites\\go_to_2.png"%(location))
a = int((90/1920)*w)+5
b = int((62/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_save_url_button_image_2 = ImageTk.PhotoImage(temp_image2)
    #Add button


my_websites_user_button_1 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",0))
my_websites_user_button_2 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",1))
my_websites_user_button_3 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",2))
my_websites_user_button_4 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",3))
my_websites_user_button_5 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",4))
my_websites_user_button_6 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image_2, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",5))
my_websites_user_button_7 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image_2, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",6))
my_websites_user_button_8 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image_2, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",7))
my_websites_user_button_9 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image_2, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",8))
my_websites_user_button_10 = tk.Button(my_websites_backGroundImage_label, image = change_save_url_button_image_2, borderwidth=0, command=lambda:my_websites_go_to_add_website ("<Button-1>",9))

my_websites_backGroundImage_label.place( relx=0.0, rely= 0.155 )
my_websites_header.place(relx=0.0, rely= 0.0, width = w,height =171)
my_websites_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=(512/1920)*w, height=(56/1080)*h)
my_websites_title_aktri.place(relx = 0.92, rely = 0.41, width=((142/1920)*w), height =(108/1080)*h)
my_websites_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
my_websites_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
my_websites_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
my_websites_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height =(43/1080)*h)
my_websites_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height =(43/1080)*h)#-5x-5
my_websites_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w),height =(43/1080)*h)
my_websites_back_button.place(relx = 0.006, rely = 0.05, width=((48/1920)*w), height =(34/1080)*h)

my_websites_change_save_url_label_1.place(relx=0.255, rely= 0.075, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_2.place(relx=0.255, rely=0.25, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_3.place(relx=0.255, rely=0.425, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_4.place(relx=0.255,rely=0.6, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_5.place(relx=0.255, rely=0.775, width=((376/1920)*w), height=(57/1080)*h)

my_websites_change_save_url_label_6.place(relx=0.61, rely= 0.075, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_7.place(relx=0.61, rely= 0.25, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_8.place(relx=0.61, rely= 0.425, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_9.place(relx=0.61, rely= 0.6, width=((376/1920)*w), height=(57/1080)*h)
my_websites_change_save_url_label_10.place(relx=0.61, rely= 0.775, width=((376/1920)*w), height=(57/1080)*h)

my_websites_url_1_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_2_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_3_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_4_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_5_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_6_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_7_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_8_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_9_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)
my_websites_url_10_name.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(45/1080)*h)

my_websites_user_button_1.place(relx=0.47, rely= 0.075, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_2.place(relx=0.47, rely= 0.25, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_3.place(relx=0.47, rely= 0.425, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_4.place(relx=0.47, rely= 0.6, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_5.place(relx=0.47, rely= 0.775, width=((90/1920)*w), height=(62/1080)*h)

my_websites_user_button_6.place(relx=0.83, rely= 0.075, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_7.place(relx=0.83, rely= 0.25, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_8.place(relx=0.83, rely= 0.425, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_9.place(relx=0.83, rely= 0.6, width=((90/1920)*w), height=(62/1080)*h)
my_websites_user_button_10.place(relx=0.83, rely= 0.775, width=((90/1920)*w), height=(62/1080)*h)

#############################################################################################################################################################################
#      A       DDDDDD      WW                WW
#     A A      D     D      WW      WW      WW
#    A   A     D      D      WW    WWWW    WW
#   AAAAAAA    D      D       WW  WW  WW  WW
#  A       A   D     D         WWWW    WWWW  
# A         A  DDDDDD           WW      WW
#############################################################################################################################################################################
add_website = tk.Frame()

#BackGround
        #open image
add_website_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
add_website_resized_backGroundImage = add_website_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

add_website_new_backGroundImage = ImageTk.PhotoImage(add_website_resized_backGroundImage)
    #Label
add_website_backGroundImage_label = Label(add_website, image=add_website_new_backGroundImage, borderwidth=0)
#header
add_website_header = Label(add_website,borderwidth=0,background = "#0d0029")

temp_image = Image.open("%s\\Add website\\title.png"%(location))
a = int((846/1920)*w)+5
b = int((56/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_title_image = ImageTk.PhotoImage(temp_image2)
add_website_title = Label(add_website_header,image = add_website_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_title_aktri_image = ImageTk.PhotoImage(temp_image2)
add_website_title_aktri = Label(add_website_header,image = add_website_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_cloce_button_image = ImageTk.PhotoImage(temp_image2)
add_website_cloce_button = tk.Button(add_website_header,image = add_website_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
add_website_exit_fullscreen_button = tk.Button(add_website_header,image = add_website_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_minimize_button_image = ImageTk.PhotoImage(temp_image2)
add_website_minimize_button = tk.Button(add_website_header,image = add_website_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
add_website_fullscreen_button = tk.Button(add_website_header,image = add_website_fullscreen_button_image, borderwidth=0)

add_website_exit_fullscreen_button.bind("<Button-1>", add_websites_exit_fullscreen)
add_website_fullscreen_button.bind("<Button-1>",add_websites_fullscreen)
add_website_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
add_website_home_button = tk.Button(add_website_header, text = ' ', image = add_website_home_button_image, borderwidth=0)
add_website_home_button.bind("<Button-1>",add_aplications_go_to_home_page)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
add_website_user_button = tk.Button(add_website_header, image = add_website_user_button_image, borderwidth=0)

#user text label
add_website_user_text_label =Label(add_website_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#Name label
temp_image = Image.open("%s\\Add Aplications\\name.png"%(location))
a = int((191/1920)*w)+5
b = int((52/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_name_label_image = ImageTk.PhotoImage(temp_image2)
add_website_name_label =Label(add_website_backGroundImage_label, borderwidth=0, image = add_website_name_label_image)

#Location label
temp_image = Image.open("%s\\Add Aplications\\location.png"%(location))
a = int((268/1920)*w)+5
b = int((56/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_location_label_image = ImageTk.PhotoImage(temp_image2)
add_website_location_label =Label(add_website_backGroundImage_label, borderwidth=0, image = add_website_location_label_image)

#name text spot label
    #label
temp_image = Image.open("%s\\Add Aplications\\text_spot.png"%(location))
a = int(0.544*w)
b = int((84/1080)*h)
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_text_spot_label_image = ImageTk.PhotoImage(temp_image2)
add_website_name_text_spot_label =Label(add_website_backGroundImage_label, borderwidth=0, image = add_website_text_spot_label_image)
    #input
add_website_name_input = tk.Entry(add_website_name_text_spot_label, font = ("", 33), fg = "#00f9ff", width =1000 , borderwidth =0,background = "#167f95")
#location text spot label
    #label
add_website_location_text_spot_label =Label(add_website_backGroundImage_label, borderwidth=0, image = add_website_text_spot_label_image)
    #input
add_website_location_input = tk.Entry(add_website_location_text_spot_label, font = ("", 33), fg = "#00f9ff", width =1000 , borderwidth =0,background = "#167f95")

#Cancel button
    # Define image
temp_image = Image.open("%s\\Add Aplications\\Cancel.png"%(location))
a = int((220/1920)*w)+5
b = int((97/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_cancel_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
add_website_cancel_button = Button(add_website_backGroundImage_label, text = ' ', image = add_website_cancel_button_image, borderwidth=0)
add_website_cancel_button.bind("<Button-1>",add_website_go_to_users_aplications)
#Add button
    # Add image
temp_image = Image.open("%s\\Add Aplications\\add.png"%(location))
a = int((162/1920)*w)+5
b = int((94/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
add_website_add_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
add_website_add_button_button = Button(add_website_backGroundImage_label, text = ' ', image = add_website_add_button_image, borderwidth=0, command=lambda:add_a_website ("<Button-1>",str(add_website_name_input.get()),str(add_website_location_input.get())))



#add to window
add_website_backGroundImage_label.place( relx=0.0, rely= 0.15 )
add_website_header.place(relx=0.0, y= 0.0, width = w,height =(171/1080)*h)
add_website_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((846/1920)*w), height=(56/1080)*h)
add_website_title_aktri.place(relx = 0.925, rely = 0.95,anchor ="sw", width=((142/1920)*w), height=(108/1080)*h)
add_website_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height=(43/1080)*h)
add_website_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height=(43/1080)*h)#-5x-5
add_website_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w), height=(43/1080)*h)
add_website_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
add_website_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
add_website_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)


add_website_name_label.place(relx = 0.05, rely = 0.2, width=((191/1920)*w), height=(53/1080)*h)
add_website_name_text_spot_label.place(relx = 0.25, rely = 0.18, relwidth=0.544, height=(84/1080)*h)
add_website_name_input.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(70/1080)*h)

add_website_location_label.place(relx = 0.05, rely = 0.4, width=((268/1920)*w), height=(56/1080)*h)
add_website_location_text_spot_label.place(relx = 0.25, rely = 0.375, relwidth=0.544, height=(84/1080)*h)
add_website_location_input.place(relx = 0.01, rely = 0.1, relwidth=0.97, height=(70/1080)*h)

add_website_cancel_button.place(relx=0.05, rely=0.858, width=((220/1920)*w), height=(97/1080)*h)
add_website_add_button_button.place(relx=0.884, rely=0.8599, width=((162/1920)*w), height=(94/1080)*h)

#############################################################################################################################################################################
#    U     U         A       PPPPPPP  PPPPPPP SSSSSSS
#    U     U        A A      P     P  P     P S
#    U     U       A   A     PPPPPPP  PPPPPPP  SSSSS
#    U     U      AAAAAAA    P        P             S
#     UUUUU      A       A   P        P       SSSSSSS
#############################################################################################################################################################################

users_aplications= tk.Frame()

#BackGround
        #open image
users_aplications_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
users_aplications_resized_backGroundImage = users_aplications_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

users_aplications_new_backGroundImage = ImageTk.PhotoImage(users_aplications_resized_backGroundImage)

    #Label
users_aplications_backGroundImage_label = Label(users_aplications, image=users_aplications_new_backGroundImage, borderwidth=0)

#header
users_aplications_header = Label(users_aplications,borderwidth=0,background = "#0d0029")
users_aplications_title_image = PhotoImage(file="%s\\Users Aplications\\title.png"%(location))
users_aplications_title = Label(users_aplications_header,image = users_aplications_title_image, borderwidth=0)
users_aplications_title_aktri_image = PhotoImage(file="%s\\akrh titlou.png"%(location))
users_aplications_title_aktri = Label(users_aplications_header,image = users_aplications_title_aktri_image, borderwidth=0)
users_aplications_cloce_button_image = PhotoImage(file="%s\\exit_button.png"%(location))
users_aplications_cloce_button = tk.Button(users_aplications_header,image = users_aplications_cloce_button_image, borderwidth=0, command = screen.destroy)
users_aplications_exit_fullscreen_button_image = PhotoImage(file="%s\\exit_fullscreen_button.png"%(location))
users_aplications_exit_fullscreen_button = tk.Button(users_aplications_header,image = users_aplications_exit_fullscreen_button_image, borderwidth=0)
users_aplications_minimize_button_image =PhotoImage(file="%s\\minimize_button.png"%(location))
users_aplications_minimize_button = tk.Button(users_aplications_header,image = users_aplications_minimize_button_image, borderwidth=0)
users_aplications_fullscreen_button_image = PhotoImage(file="%s\\fullscreen_button.png"%(location))
users_aplications_fullscreen_button = tk.Button(users_aplications_header,image = users_aplications_fullscreen_button_image, borderwidth=0)

users_aplications_exit_fullscreen_button.bind("<Button-1>", users_aplications_exit_fullscreen)
users_aplications_fullscreen_button.bind("<Button-1>",users_aplications_fullscreen)
users_aplications_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
users_aplications_home_button_image = PhotoImage(file="%s\\home-button.png"%(location))
    #Add button
users_aplications_home_button = tk.Button(users_aplications_header, text = ' ', image = users_aplications_home_button_image, borderwidth=0)
users_aplications_home_button.bind("<Button-1>",users_aplications_go_to_home_page)

#User button
    # setings button image
users_aplications_user_button_image = PhotoImage(file="%s\\user-button.png"%(location))
    #Add button
users_aplications_user_button = tk.Button(users_aplications_header, image = users_aplications_user_button_image, borderwidth=0)

#user text label
users_aplications_user_text_label =Label(users_aplications_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#back button
    # Define image
users_aplications_back_button_image = PhotoImage(file="%s\\back_button.png"%(location))
    #define button
users_aplications_back_button = tk.Button(users_aplications_header, text = ' ', image = users_aplications_back_button_image, borderwidth=0)
users_aplications_back_button.bind("<Button-1>",users_aplications_go_to_settings)

#add aplication button
    #Define image
users_aplications_add_apication_button_image = PhotoImage(file="%s\\Users Aplications\\pluss_button.png"%(location))
    #define button
users_aplications_add_apication_button = tk.Button(users_aplications_backGroundImage_label, text = ' ', image = users_aplications_add_apication_button_image, borderwidth=0)
users_aplications_add_apication_button.bind("<Button-1>",users_aplications_go_to_add_aplications)

users_aplications_backGroundImage_label.place( relx=0.0, rely= 0.155 )
users_aplications_header.place(relx=0.0, rely= 0.0, width = w,height =171)
users_aplications_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=800, height=66)
users_aplications_title_aktri.place(relx = 0.92, rely = 0.41, width=142, height=108)
users_aplications_cloce_button.place(relx = 0.985, rely = 0.0, width=31, height=28)
users_aplications_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=31, height=28)
users_aplications_minimize_button.place(relx = 0.945, rely = 0.0, width=31, height=28)

users_aplications_home_button.place(relx = 0.006, rely = 0.35, width=43, height=43)
users_aplications_user_button.place(relx = 0.006, rely = 0.65, width=43, height=43)#-5x-5
users_aplications_user_text_label.place(relx = 0.0295, rely = 0.7, width=44, height=43)
users_aplications_back_button.place(relx = 0.006, rely = 0.05, width=48, height=34)

users_aplications_add_apication_button.place(relx = 0.9, rely = 0.8, width=131, height=130)
#############################################################################################################################################################################
#   CCCCC   LL
#  CC       LL
# CC        LL
#  CC       LL
#   CCCCC   LLLLLLLL
#############################################################################################################################################################################
change_location = tk.Frame()

#BackGround
        #open image
change_location_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
change_location_resized_backGroundImage = change_location_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

change_location_new_backGroundImage = ImageTk.PhotoImage(change_location_resized_backGroundImage)
    #Label
change_location_backGroundImage_label = Label(change_location, image=change_location_new_backGroundImage, borderwidth=0)
#header
change_location_header = Label(change_location,borderwidth=0,background = "#0d0029")

temp_image = Image.open("%s\\change location\\title.png"%(location))
a = int((705/1920)*w)+5
b = int((56/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_title_image = ImageTk.PhotoImage(temp_image2)
change_location_title = Label(change_location_header,image = change_location_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_title_aktri_image = ImageTk.PhotoImage(temp_image2)
change_location_title_aktri = Label(change_location_header,image = change_location_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_cloce_button_image = ImageTk.PhotoImage(temp_image2)
change_location_cloce_button = tk.Button(change_location_header,image = change_location_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
change_location_exit_fullscreen_button = tk.Button(change_location_header,image = change_location_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_minimize_button_image = ImageTk.PhotoImage(temp_image2)
change_location_minimize_button = tk.Button(change_location_header,image = change_location_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
change_location_fullscreen_button = tk.Button(change_location_header,image = change_location_fullscreen_button_image, borderwidth=0)

change_location_exit_fullscreen_button.bind("<Button-1>", change_location_exit_fullscreen)
change_location_fullscreen_button.bind("<Button-1>",change_location_fullscreen)
change_location_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
change_location_home_button = tk.Button(change_location_header, text = ' ', image = change_location_home_button_image, borderwidth=0)
change_location_home_button.bind("<Button-1>",change_location_go_to_home_page)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
change_location_user_button = tk.Button(change_location_header, image = change_location_user_button_image, borderwidth=0)

#user text label
change_location_user_text_label =Label(change_location_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#Name label
temp_image = Image.open("%s\\Add Aplications\\name.png"%(location))
a = int((191/1920)*w)+5
b = int((52/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_name_label_image = ImageTk.PhotoImage(temp_image2)
change_location_name_label =Label(change_location_backGroundImage_label, borderwidth=0, image = change_location_name_label_image)

#Location label
temp_image = Image.open("%s\\Add Aplications\\location.png"%(location))
a = int((268/1920)*w)+5
b = int((56/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_location_label_image = ImageTk.PhotoImage(temp_image2)
change_location_location_label =Label(change_location_backGroundImage_label, borderwidth=0, image = change_location_location_label_image)

#name text spot label
    #label
temp_image = Image.open("%s\\Add Aplications\\text_spot.png"%(location))
a = int(0.544*w)
b = int((84/1080)*h)
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_text_spot_label_image = ImageTk.PhotoImage(temp_image2)
change_location_name_text_spot_label =Label(change_location_backGroundImage_label, borderwidth=0, image = change_location_text_spot_label_image)
    #input
change_location_name_input = tk.Entry(change_location_name_text_spot_label, font = ("", 33), fg = "#00f9ff", width =1000 , borderwidth =0,background = "#167f95")
#location text spot label
    #label
change_location_location_text_spot_label =Label(change_location_backGroundImage_label, borderwidth=0, image = change_location_text_spot_label_image)
    #input
change_location_location_input = tk.Entry(change_location_location_text_spot_label, font = ("", 33), fg = "#00f9ff", width =1000 , borderwidth =0,background = "#167f95")

#Cancel button
    # Define image
temp_image = Image.open("%s\\Add Aplications\\Cancel.png"%(location))
a = int((220/1920)*w)+5
b = int((97/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_cancel_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
change_location_cancel_button = Button(change_location_backGroundImage_label, text = ' ', image = change_location_cancel_button_image, borderwidth=0)
change_location_cancel_button.bind("<Button-1>",change_location_go_to_users_aplications)
#Add button
    # Add image
temp_image = Image.open("%s\\Add Aplications\\add.png"%(location))
a = int((162/1920)*w)+5
b = int((94/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
change_location_add_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
change_location_add_button_button = Button(change_location_backGroundImage_label, text = ' ', image = change_location_add_button_image, borderwidth=0, command=lambda:change_location ("<Button-1>",str(add_website_name_input.get()),str(add_website_location_input.get())))



#add to window
change_location_backGroundImage_label.place( relx=0.0, rely= 0.15 )
change_location_header.place(relx=0.0, y= 0.0, width = w,height =(171/1080)*h)
change_location_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((705/1920)*w), height=(56/1080)*h)
change_location_title_aktri.place(relx = 0.925, rely = 0.95,anchor ="sw", width=((142/1920)*w), height=(108/1080)*h)
change_location_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height=(43/1080)*h)
change_location_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height=(43/1080)*h)#-5x-5
change_location_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w), height=(43/1080)*h)
change_location_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
change_location_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
change_location_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)


change_location_name_label.place(relx = 0.05, rely = 0.2, width=((191/1920)*w), height=(53/1080)*h)
change_location_name_text_spot_label.place(relx = 0.25, rely = 0.18, relwidth=0.544, height=(84/1080)*h)
change_location_name_input.place(relx = 0.01, rely = 0.1, relwidth=0.98, height=(70/1080)*h)

change_location_location_label.place(relx = 0.05, rely = 0.4, width=((268/1920)*w), height=(56/1080)*h)
change_location_location_text_spot_label.place(relx = 0.25, rely = 0.375, relwidth=0.544, height=(84/1080)*h)
change_location_location_input.place(relx = 0.01, rely = 0.1, relwidth=0.97, height=(70/1080)*h)

change_location_cancel_button.place(relx=0.05, rely=0.858, width=((220/1920)*w), height=(97/1080)*h)
change_location_add_button_button.place(relx=0.884, rely=0.8599, width=((162/1920)*w), height=(94/1080)*h)

#############################################################################################################################################################################
#           A       PPPPPPP  PPPPPPP SSSSSSS
#          A A      P     P  P     P S
#         A   A     PPPPPPP  PPPPPPP  SSSSS
#        AAAAAAA    P        P             S
#       A       A   P        P       SSSSSSS
#############################################################################################################################################################################
aplications= tk.Frame()
#BackGround
        #open image
aplications_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
aplications_resized_backGroundImage = aplications_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

aplications_new_backGroundImage = ImageTk.PhotoImage(aplications_resized_backGroundImage)

    #Label
aplications_backGroundImage_label = Label(aplications, image=aplications_new_backGroundImage, borderwidth=0)

#header
aplications_header = Label(aplications,borderwidth=0,background = "#0d0029")

temp_image = Image.open("%s\\Aplications\\title.png"%(location))
a = int((847/1920)*w)+5
b = int((52/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_title_image = ImageTk.PhotoImage(temp_image2)
aplications_title = Label(aplications_header,image = aplications_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_title_aktri_image = ImageTk.PhotoImage(temp_image2)
aplications_title_aktri = Label(aplications_header,image = aplications_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_cloce_button_image = ImageTk.PhotoImage(temp_image2)
aplications_cloce_button = tk.Button(aplications_header,image = aplications_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
aplications_exit_fullscreen_button = tk.Button(aplications_header,image = aplications_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_minimize_button_image = ImageTk.PhotoImage(temp_image2)
aplications_minimize_button = tk.Button(aplications_header,image = aplications_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
aplications_fullscreen_button = tk.Button(aplications_header,image = aplications_fullscreen_button_image, borderwidth=0)

aplications_exit_fullscreen_button.bind("<Button-1>", aplications_exit_fullscreen)
aplications_fullscreen_button.bind("<Button-1>",aplications_fullscreen)
aplications_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
aplications_home_button = tk.Button(aplications_header, text = ' ', image = aplications_home_button_image, borderwidth=0)
aplications_home_button.bind("<Button-1>",aplications_go_to_home_page)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
aplications_user_button = tk.Button(aplications_header, image = aplications_user_button_image, borderwidth=0)

#user text label
aplications_user_text_label =Label(aplications_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#back button
    # Define image
temp_image = Image.open("%s\\back_button.png"%(location))
a = int((48/1920)*w)+5
b = int((34/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_back_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
aplications_back_button = tk.Button(aplications_header, text = ' ', image = aplications_back_button_image, borderwidth=0)
aplications_back_button.bind("<Button-1>",aplications_go_to_settings)

#Icon labels
        #Excel
temp_image = Image.open("%s\\Aplications\\excel-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_excel_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_excel_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_excel_icon_image)
        #Word
temp_image = Image.open("%s\\Aplications\\word-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_word_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_word_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_word_icon_image)
        #Acces
temp_image = Image.open("%s\\Aplications\\acces-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_acces_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_acces_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_acces_icon_image)
        #Power Point
temp_image = Image.open("%s\\Aplications\\power-point-icon.png"%(location))
a = int((162/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_power_point_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_power_point_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_power_point_icon_image)
        #Spotify
temp_image = Image.open("%s\\Aplications\\spotify-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_spotify_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_spotify_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_spotify_icon_image)
        #Messenger
temp_image = Image.open("%s\\Aplications\\messenger-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_messenger_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_messenger_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_messenger_icon_image)
        #Websites
temp_image = Image.open("%s\\Aplications\\web-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_websites_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_websites_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_websites_icon_image)
        #Caclulator
temp_image = Image.open("%s\\Aplications\\calculator-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_cuclulator_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_cuclulator_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_cuclulator_icon_image)
        #NoteBook
temp_image = Image.open("%s\\Aplications\\notebook-icon.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_notebook_icon_image = ImageTk.PhotoImage(temp_image2)
aplications_notebook_icon =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_notebook_icon_image)
        #Users Applications
temp_image = Image.open("%s\\Aplications\\users-applications.png"%(location))
a = int((102/1920)*w)+5
b = int((137/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_users_applications_button_image = ImageTk.PhotoImage(temp_image2)
aplications_users_applications_button =tk.Button(aplications_backGroundImage_label, borderwidth=0, image = aplications_users_applications_button_image)
aplications_users_applications_button.bind("<Button-1>",aplications_go_to_users_aplications)
        #Your applications text label
temp_image = Image.open("%s\\Aplications\\your_applications-label-text.png"%(location))
a = int((285/1920)*w)+5
b = int((39/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_your_applications_text_label_image = ImageTk.PhotoImage(temp_image2)
aplications_your_applications_text_label =Label(aplications_backGroundImage_label, borderwidth=0, image = aplications_your_applications_text_label_image)

#Change / Save location Buttons
    # Define image
temp_image = Image.open("%s\\Aplications\\change-save location-button2.png"%(location))
a = int((376/1920)*w)+5
b = int((57/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
aplications_change_save_location_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
        #Excel button
aplications_change_save_location_button_excel = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_excel.bind("<Button-1>", aplications_go_to_change_location)
        #Word
aplications_change_save_location_button_word = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_word.bind("<Button-1>", aplications_go_to_change_location)
        #Acces
aplications_change_save_location_button_acces = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_acces.bind("<Button-1>", aplications_go_to_change_location)
        #Power Point
aplications_change_save_location_button_Power_Point = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_Power_Point.bind("<Button-1>", aplications_go_to_change_location)
        #Spotify
aplications_change_save_location_button_Spotify = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_Spotify.bind("<Button-1>", aplications_go_to_change_location)
        #Messenger
aplications_change_save_location_button_Messenger = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_Messenger.bind("<Button-1>", aplications_go_to_change_location)
        #Websites
aplications_change_save_location_button_Websites = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_Websites.bind("<Button-1>", go_to_my_websites)
        #Caclulator
aplications_change_save_location_button_Caclulator = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_Caclulator.bind("<Button-1>", aplications_go_to_change_location)
        #NoteBook
aplications_change_save_location_button_NoteBook = tk.Button(aplications_backGroundImage_label, text = ' ', image = aplications_change_save_location_button_image, borderwidth=0)
aplications_change_save_location_button_NoteBook.bind("<Button-1>", aplications_go_to_change_location)


#add to window
aplications_backGroundImage_label.place( relx=0.0, rely= 0.155 )
aplications_header.place(relx=0.0, rely= 0.0, width = w,height =(171/1080)*h)
aplications_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((847/1920)*w), height=(52/1080)*h)
aplications_title_aktri.place(relx = 0.92, rely = 0.41, width=((142/1920)*w), height=(108/1080)*h)
aplications_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
aplications_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
aplications_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)

aplications_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height=(43/1080)*h)
aplications_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height=(43/1080)*h)
aplications_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w), height=(43/1080)*h)
aplications_back_button.place(relx = 0.006, rely = 0.05, width=((48/1920)*w), height=(34/1080)*h)


aplications_excel_icon.place(relx=0.2, rely= 0.05, width = ((102/1920)*w),height =(137/1080)*h)#+0.175
aplications_word_icon.place(relx=0.2, rely= 0.225, width = ((102/1920)*w),height =(137/1080)*h)
aplications_acces_icon.place(relx=0.2, rely= 0.4, width = ((102/1920)*w),height =(137/1080)*h)
aplications_power_point_icon.place(relx=0.2, rely= 0.575, width = ((162/1920)*w),height =(137/1080)*h)
aplications_spotify_icon.place(relx=0.2, rely= 0.75, width = ((102/1920)*w),height =(137/1080)*h)

aplications_change_save_location_button_excel.place(relx=0.255, rely= 0.075, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_word.place(relx=0.255, rely=0.25, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_acces.place(relx=0.255, rely=0.425, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_Power_Point.place(relx=0.255,rely=0.6, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_Spotify.place(relx=0.255, rely=0.775, width=((376/1920)*w), height=(57/1080)*h)

aplications_messenger_icon.place(relx=0.55, rely= 0.05, width = ((102/1920)*w),height =(137/1080)*h)#+0.175
aplications_websites_icon.place(relx=0.55, rely= 0.225, width = ((102/1920)*w),height =(137/1080)*h)
aplications_cuclulator_icon.place(relx=0.55, rely= 0.4, width = ((102/1920)*w),height =(137/1080)*h)
aplications_notebook_icon.place(relx=0.55, rely= 0.575, width = ((102/1920)*w),height =(137/1080)*h)
aplications_users_applications_button.place(relx=0.55, rely= 0.75, width =((102/1920)*w),height =(137/1080)*h)

aplications_change_save_location_button_Messenger.place(relx=0.61, rely= 0.075, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_Websites.place(relx=0.61, rely= 0.25, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_Caclulator.place(relx=0.61, rely= 0.425, width=((376/1920)*w), height=(57/1080)*h)
aplications_change_save_location_button_NoteBook.place(relx=0.61, rely= 0.6, width=((376/1920)*w), height=(57/1080)*h)
aplications_your_applications_text_label.place(relx=0.61, rely= 0.8, width=((285/1920)*w), height=(39/1080)*h)
#############################################################################################################################################################################
#     A      BBBBBBB
#    A A     B      B
#   A   A    BBBBBBB
#  A AAA A   B      B
# A       A  BBBBBBBB
#############################################################################################################################################################################
about_page = tk.Frame(screen)
#BackGround
        #open image
about_page_backGroundImage = Image.open("%s\\About\\background.png"%(location))
        #resize image
about_page_resized_backGroundImage = about_page_backGroundImage.resize((w, h-160),Image.ANTIALIAS)
about_page_new_backGroundImage = ImageTk.PhotoImage(about_page_resized_backGroundImage)
    #Label
about_page_backGroundImage_label = Label(about_page, image=about_page_new_backGroundImage, borderwidth=0)

#Header
about_page_header = Label(about_page,borderwidth=0,background = "#0d0029")

temp_image = Image.open("%s\\About\\title.png"%(location))
a = int((422/1920)*w)+5
b = int((52/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
about_page_title_image = ImageTk.PhotoImage(temp_image2)
about_page_title = Label(about_page_header,image = about_page_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
about_page_title_aktri_image = ImageTk.PhotoImage(temp_image2)
about_page_title_aktri = Label(about_page_header,image = about_page_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
about_page_cloce_button_image = ImageTk.PhotoImage(temp_image2)
about_page_cloce_button = tk.Button(about_page_header,image = about_page_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
about_page_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
about_page_exit_fullscreen_button = tk.Button(about_page_header,image = about_page_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
about_page_minimize_button_image = ImageTk.PhotoImage(temp_image2)
about_page_minimize_button = tk.Button(about_page_header,image = about_page_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\Calendar\\title.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
about_page_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
about_page_fullscreen_button = tk.Button(about_page_header,image = about_page_fullscreen_button_image, borderwidth=0)

about_page_exit_fullscreen_button.bind("<Button-1>", about_page_exit_fullscreen)
about_page_fullscreen_button.bind("<Button-1>",about_page_fullscreen)
about_page_minimize_button.bind("<Button-1>", minimize)

#back button
    # Define image
about_page_back_button_image = PhotoImage(file="%s\\back_button.png"%(location))
    #define button
about_page_back_button = tk.Button(about_page_header, text = ' ', image = about_page_back_button_image, borderwidth=0)
about_page_back_button.bind("<Button-1>",about_page_go_to_settings)

#Home button
    # setings button image
about_page_home_button_image = PhotoImage(file="%s\\home-button.png"%(location))
    #Add button
about_page_home_button = tk.Button(about_page_header, text = ' ', image = about_page_home_button_image, borderwidth=0)
about_page_home_button.bind("<Button-1>",about_page_go_to_home_page)

#User button
    # setings button image
about_page_user_button_image = PhotoImage(file="%s\\user-button.png"%(location))
    #Add button
about_page_user_button = tk.Button(about_page_header, text = ' ', image = about_page_user_button_image, borderwidth=0)
#user text label
about_page_user_text_label =Label(about_page_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))


#add to window
about_page_backGroundImage_label.place( relx=0.0, rely= 0.155 )
about_page_header.place(relx=0.0, rely= 0.0, width = w,height =(171/1080)*h)
about_page_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((422/1920)*w), height =(52/1080)*h)
about_page_title_aktri.place(relx = 0.92, rely = 0.41, width=((142/1920)*w), height =(108/1080)*h)
about_page_back_button.place(relx = 0.006, rely = 0.05, width=((48/1920)*w), height =(34/1080)*h)
about_page_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height =(43/1080)*h)
about_page_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height =(43/1080)*h)#-5x-5
about_page_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w), height =(43/1080)*h)
about_page_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
about_page_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
about_page_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
#############################################################################################################################################################################
#    CCCCCC
#   CCC
#  CCC
#   CCC
#    CCCCCCC
#############################################################################################################################################################################
calendar = tk.Frame(screen)
#BackGround
    #open image
calendar_backgroundImage = Image.open("%s\\background.png"%(location))
#resize image
calendar_resized_backGroundImage = calendar_backgroundImage.resize((w, h-160),Image.ANTIALIAS)

calendar_new_backGroundImage = ImageTk.PhotoImage(calendar_resized_backGroundImage)

    #Label
calendar_backGroundImage_label = Label(calendar, image=calendar_new_backGroundImage, borderwidth=0)

#header
calendar_header = Label(calendar,borderwidth=0,background = "#0d0029")

temp_image = Image.open("%s\\Calendar\\title.png"%(location))
a = int((977/1920)*w)+5
b = int((44/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_title_image = ImageTk.PhotoImage(temp_image2)
calendar_title = Label(calendar_header,image = calendar_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_title_aktri_image = ImageTk.PhotoImage(temp_image2)
calendar_title_aktri = Label(calendar_header,image = calendar_title_aktri_image, borderwidth=0)

calendar_cloce_button_image = PhotoImage(file="%s\\exit_button.png"%(location))
temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_cloce_button_image = ImageTk.PhotoImage(temp_image2)
calendar_cloce_button = tk.Button(calendar_header,image = calendar_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
calendar_exit_fullscreen_button = tk.Button(calendar_header,image = calendar_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_minimize_button_image = ImageTk.PhotoImage(temp_image2)
calendar_minimize_button = tk.Button(calendar_header,image = calendar_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
calendar_fullscreen_button = tk.Button(calendar_header,image = calendar_fullscreen_button_image, borderwidth=0)


calendar_exit_fullscreen_button.bind("<Button-1>", calendar_exit_fullscreen)
calendar_fullscreen_button.bind("<Button-1>",calendar_fullscreen)
calendar_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
calendar_home_button = tk.Button(calendar_header, text = ' ', image = calendar_home_button_image, borderwidth=0)
calendar_home_button.bind("<Button-1>",calendar_go_to_home_page)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
calendar_user_button = tk.Button(calendar_header, image = calendar_user_button_image, borderwidth=0)

#user text label
calendar_user_text_label =Label(calendar_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#back button
    # Define image
temp_image = Image.open("%s\\back_button.png"%(location))
a = int((48/1920)*w)+5
b = int((34/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_back_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
calendar_back_button = tk.Button(calendar_header, text = ' ', image = calendar_back_button_image, borderwidth=0)
calendar_back_button.bind("<Button-1>",calendar_go_to_home_page)

#Year
    #Load Year numbers
temp_image = Image.open("%s\\Calendar\\year numbers\\0.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_zero = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\1.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_one = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\2.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_two = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\3.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_three = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\4.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_four = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\5.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_five = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\6.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_six = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\7.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_seven = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\8.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_eight = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\year numbers\\9.png"%(location))
a = int((46/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_nine = ImageTk.PhotoImage(temp_image2)

#deine image

calendar_year_label_background_label =Label(calendar_backGroundImage_label, borderwidth=0)
calendar_year_fists_position = Label(calendar_year_label_background_label,image =calendar_zero ,borderwidth = 0)
calendar_year_second_position = Label(calendar_year_label_background_label,image =calendar_zero ,borderwidth = 0)
calendar_year_third_position = Label(calendar_year_label_background_label,image =calendar_zero ,borderwidth = 0)
calendar_year_fourth_position = Label(calendar_year_label_background_label,image =calendar_zero ,borderwidth = 0)

#Get curent month and year
now = datetime.datetime.now()
global month
global year
month = now.month
year = now.year
get_year(year)

#Load Calendar pictures
    #sunday----------------------------------------------
temp_image = Image.open("%s\\Calendar\\S-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_sunday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\S-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_sunday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\S-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_sunday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\S-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_sunday_28 = ImageTk.PhotoImage(temp_image2)

    #monday--------------------------------------------------------------
temp_image = Image.open("%s\\Calendar\\M-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_monday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\M-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_monday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\M-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_monday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\M-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_monday_28 = ImageTk.PhotoImage(temp_image2)

    #tuesday--------------------------------------------------------------
temp_image = Image.open("%s\\Calendar\\TU-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_tuesday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\TU-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_tuesday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\TU-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_tuesday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\TU-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_tuesday_28 = ImageTk.PhotoImage(temp_image2)

    #wednesday--------------------------------------------------------------
temp_image = Image.open("%s\\Calendar\\W-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_wednesday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\W-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_wednesday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\W-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_wednesday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\W-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_wednesday_28 = ImageTk.PhotoImage(temp_image2)

    #thursday--------------------------------------------------------------
temp_image = Image.open("%s\\Calendar\\THU-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_thursday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\THU-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_thursday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\THU-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_thursday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\THU-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_thursday_28 = ImageTk.PhotoImage(temp_image2)

    #friday--------------------------------------------------------------
temp_image = Image.open("%s\\Calendar\\F-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_friday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\F-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_friday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\F-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_friday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\F-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_friday_28 = ImageTk.PhotoImage(temp_image2)

    #saturday--------------------------------------------------------------
temp_image = Image.open("%s\\Calendar\\SAT-31.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_saturday_31 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\SAT-30.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_saturday_30 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\SAT-29.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_saturday_29 = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\SAT-28.png"%(location))
a = int((1494/1920)*w)+5
b = int((725/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_saturday_28 = ImageTk.PhotoImage(temp_image2)

calendar_month_days_label = Label(calendar_backGroundImage_label, borderwidth=0)
choose_months_image(month,year)

#Month
    #Load month imagies
temp_image = Image.open("%s\\Calendar\\Months_Imagies\\1.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_january = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\2.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_february = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\3.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_march = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\4.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_april = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\5.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_may = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\6.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_june = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\7.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_july = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\8.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_august = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\9.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_september = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\10.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_octomber = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\11.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_november = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Calendar\\Months_Imagies\\12.png"%(location))
a = int((323/1920)*w)+5
b = int((65/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
calendar_december = ImageTk.PhotoImage(temp_image2)


calendar_month_image = PhotoImage(file="%s\\Calendar\\Months_Imagies\\%d.png"%(location, month))
    #define button
calendar_month_label = Label(calendar_backGroundImage_label, text = ' ', image = calendar_month_image, borderwidth=0) 

#Next Month
calendar_next_month_button_image = PhotoImage(file="%s\\Calendar\\next_month_button_image.png"%(location))
    #define button
calendar_next_month_button = tk.Button(calendar_backGroundImage_label, text = ' ', image = calendar_next_month_button_image, borderwidth=0)

#previous  Month
calendar_previous_month_button_image = PhotoImage(file="%s\\Calendar\\previous_month_button_image.png"%(location))
    #define button
calendar_previous_month_button = tk.Button(calendar_backGroundImage_label, text = ' ', image = calendar_previous_month_button_image, borderwidth=0)

calendar_next_month_button.bind("<Button-1>",get_next_month_name_image)
calendar_previous_month_button.bind("<Button-1>",get_previous_month_name_image)

#today fond

calendar_today_label_image = PhotoImage(file="%s\\Calendar\\today numbers\\%d.png"%(location,now.day))
calendar_today_label = Label(calendar_month_days_label,image =calendar_today_label_image, borderwidth=0)

#Add to screen
calendar_backGroundImage_label.place( relx=0.0, rely= 0.155 )

calendar_header.place(relx=0.0, rely= 0.0, width = w,height =(171/1080)*h)
calendar_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((977/1920)*w), height =(44/1080)*h)
calendar_title_aktri.place(relx = 0.92, rely = 0.41, width=((142/1920)*w), height =(108/1080)*h)

calendar_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
calendar_exit_fullscreen_button.place(relx = 0.965, rely = 0.0,width=((31/1920)*w), height =(28/1080)*h)
calendar_minimize_button.place(relx = 0.945, rely = 0.0, width=((43/1920)*w), height =(28/1080)*h)


calendar_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height =(43/1080)*h)
calendar_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height =(43/1080)*h)#-5x-5
calendar_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w), height =(43/1080)*h)
calendar_back_button.place(relx = 0.006, rely = 0.05, width=((48/1920)*w), height =(34/1080)*h)

calendar_month_label.place(relx = 0.38, rely = 0.03, width=((323/1920)*w), height =(65/1080)*h)
calendar_year_label_background_label.place(relx = 0.65, rely = 0.03, width=((184/1920)*w), height =(65/1080)*h)
calendar_year_fists_position.place(relx = 0.0, rely = 0.0, width=((46/1920)*w), height =(65/1080)*h)
calendar_year_second_position.place(relx = 0.2527, rely = 0.0, width=((46/1920)*w), height =(65/1080)*h)
calendar_year_third_position.place(relx = 0.5025, rely = 0.0, width=((46/1920)*w), height =(65/1080)*h)
calendar_year_fourth_position.place(relx = 0.75, rely = 0.0, width=((46/1920)*w), height =(65/1080)*h)
calendar_next_month_button.place(relx = 0.9, rely = 0.03, width=((51/1920)*w),height =(59/1080)*h)
calendar_previous_month_button.place(relx = 0.1, rely = 0.03, width=((51/1920)*w), height =(59/1080)*h)
calendar_month_days_label.place(relx = 0.5, rely = 0.55,anchor = "center", width=((1494/1920)*w), height =(725/1080)*h)

calendar_today_label.place(relx = get_todays_x_rel_position(), rely = get_todays_y_rel_position(), width=191, height=107)
#############################################################################################################################################################################
#  SSSSSSSS
#  S
#  SSSSSSSS
#         S
#  SSSSSSSS
#############################################################################################################################################################################
settings = tk.Frame(screen)
#BackGround
        #open image
settings_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
settings_resized_backGroundImage = settings_backGroundImage.resize((w, h-160),Image.ANTIALIAS)

settings_new_backGroundImage = ImageTk.PhotoImage(settings_resized_backGroundImage)

    #Label
settings_backGroundImage_label = Label(settings, image=settings_new_backGroundImage, borderwidth=0)

#header
settings_header = Label(settings,borderwidth=0,background = "#0d0029")
temp_image = Image.open("%s\\Settings\\title.png"%(location))
a = int(((670/1920)*w)+5)
b = int((57/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_title_image = ImageTk.PhotoImage(temp_image2)
settings_title = Label(settings_header,image = settings_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_title_aktri_image = ImageTk.PhotoImage(temp_image2)
settings_title_aktri = Label(settings_header,image = settings_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_cloce_button_image = ImageTk.PhotoImage(temp_image2)
settings_cloce_button = tk.Button(settings_header,image = settings_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
settings_exit_fullscreen_button = tk.Button(settings_header,image = settings_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_minimize_button_image = ImageTk.PhotoImage(temp_image2)
settings_minimize_button = tk.Button(settings_header,image = settings_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)
settings_fullscreen_button = tk.Button(settings_header,image = settings_fullscreen_button_image, borderwidth=0)

settings_exit_fullscreen_button.bind("<Button-1>", settings_exit_fullscreen)
settings_fullscreen_button.bind("<Button-1>",settings_fullscreen)
settings_minimize_button.bind("<Button-1>", minimize)

#Home button
    # setings button image
temp_image = Image.open("%s\\home-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_home_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
settings_home_button = tk.Button(settings_header, text = ' ', image = settings_home_button_image, borderwidth=0)
settings_home_button.bind("<Button-1>",settings_go_to_home)

#User button
    # setings button image
temp_image = Image.open("%s\\user-button.png"%(location))
a = int((43/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_user_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
settings_user_button = tk.Button(settings_header, image = settings_user_button_image, borderwidth=0)

#user text label
settings_user_text_label =Label(settings_header,text ="User", borderwidth=0,background = "#0d0029",fg = "white", font = ("", 16))

#back button
    # Define image
temp_image = Image.open("%s\\back_button.png"%(location))
a = int((48/1920)*w)+5
b = int((34/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_back_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
settings_back_button = tk.Button(settings_header, text = ' ', image = settings_back_button_image, borderwidth=0)

settings_back_button.bind("<Button-1>",settings_go_to_home)
    
#smity gender
    # Define image
temp_image = Image.open("%s\\Settings\\smiti gender.png"%(location))
a = int((400/1920)*w)+5
b = int((50/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_smity_gender_label_image = ImageTk.PhotoImage(temp_image2)
    #define label
settings_smity_gender_label = Label(settings_backGroundImage_label, text = ' ', image = settings_smity_gender_label_image, borderwidth=0)
    #female button
        # Define image
temp_image = Image.open("%s\\Settings\\female_on.png"%(location))
a = int((148/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_female_on = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Settings\\female_off.png"%(location))
a = int((148/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_female_off = ImageTk.PhotoImage(temp_image2)
        #define button
settings_female_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_female_on, borderwidth=0)
    #Male button
temp_image = Image.open("%s\\Settings\\male_off.png"%(location))
a = int((110/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_male_off = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Settings\\male_on.png"%(location))
a = int((110/1920)*w)+5
b = int((43/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_male_on = ImageTk.PhotoImage(temp_image2)

    #define button
settings_male_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_male_off, borderwidth=0)
global gender
gender = 'female'

    
settings_female_button.bind("<Button-1>", activate_female)
settings_male_button.bind("<Button-1>", activate_male)

#Username name
    # Define image
temp_image = Image.open("%s\\Settings\\user_name.png"%(location))
a = int((262/1920)*w)+5
b = int((52/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_user_name_label_image = ImageTk.PhotoImage(temp_image2)
    #define label
settings_username_label = Label(settings_backGroundImage_label, text = ' ', image = settings_user_name_label_image, borderwidth=0)
    #get name

settings_user_name_text_field =tk.Entry(settings_backGroundImage_label, font = ("", 35), fg = "#47d9fe", width =100 , borderwidth =0,background = "#1f0830")
settings_u_name ="<user name>"

def on_click(event):
    event.widget.delete(0, tk.END)

def get_name(event):
    print(str(settings_user_name_text_field.get()))
settings_user_name_text_field.insert(0, settings_u_name)
settings_user_name_text_field.bind("<Button-1>", on_click)
settings_user_name_text_field.bind("<Return>", get_name)

#switch
temp_image = Image.open("%s\\Settings\\on_switch.png"%(location))
a = int((173/1920)*w)+5
b = int((64/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_switch_on = ImageTk.PhotoImage(temp_image2)

temp_image = Image.open("%s\\Settings\\off_switch.png"%(location))
a = int((173/1920)*w)+5
b = int((64/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_switch_off = ImageTk.PhotoImage(temp_image2)
#All activated
#voice control
    # Define image
temp_image = Image.open("%s\\Settings\\Voice control.png"%(location))
a = int((354/1920)*w)+5
b = int((50/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_voice_control_label_image = ImageTk.PhotoImage(temp_image2)
    #define label
settings_voice_control_label = Label(settings_backGroundImage_label, text = ' ', image = settings_voice_control_label_image, borderwidth=0)
settings_voice_control_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_switch_on, borderwidth=0)
    #ON OFF veriable
global settings_voice_control_on
settings_voice_control_on = 1
    
#speak key
    # Define image
temp_image = Image.open("%s\\Settings\\Speak key.png"%(location))
a = int((264/1920)*w)+5
b = int((60/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_speak_key_label_image = ImageTk.PhotoImage(temp_image2)
    #define label
settings_speak_key_label = Label(settings_backGroundImage_label, text = ' ', image = settings_speak_key_label_image, borderwidth=0)
    #Define button
settings_speak_key_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_switch_on, borderwidth=0)
    #ON OFF veriable
global settings_speak_key_on
settings_speak_key_on = 1

#voice wake up
    # Define image
temp_image = Image.open("%s\\Settings\\voise wake up.png"%(location))
a = int((357/1920)*w)+5
b = int((60/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_wake_up_label_image = ImageTk.PhotoImage(temp_image2)
    #define label
settings_wake_up_label = Label(settings_backGroundImage_label, text = ' ', image = settings_wake_up_label_image, borderwidth=0)
#Define button
settings_wake_up_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_switch_on, borderwidth=0)
    #ON OFF veriable
global settings_wake_up_on
settings_wake_up_on = 1

settings_voice_control_button.bind("<Button-1>", activate_deactivate_voice_control)
settings_speak_key_button.bind("<Button-1>", activate_deactivate_speak_key)
settings_wake_up_button.bind("<Button-1>", activate_deactivate_wake_up)

#info button
temp_image = Image.open("%s\\Settings\\info_button.png"%(location))
a = int((206/1920)*w)+5
b = int((275/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_info_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
settings_info_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_info_button_image, borderwidth=0)
settings_info_button.bind("<Button-1>",settings_go_to_about)

#Applications button
temp_image = Image.open("%s\\Settings\\applications.png"%(location))
a = int((325/1920)*w)+5
b = int((275/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
settings_applicatons_button_image = ImageTk.PhotoImage(temp_image2)
    #define button
settings_applications_button = tk.Button(settings_backGroundImage_label, text = ' ', image = settings_applicatons_button_image, borderwidth=0)
settings_applications_button.bind("<Button-1>",settings_go_to_aplications)

#add to Settings
settings_backGroundImage_label.place( relx=0.0, rely= 0.155 )
settings_header.place(relx=0.0, rely= 0.0, width = w,height =(171/1080)*h)
settings_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((670/1920)*w), height =(57/1080)*h)
settings_title_aktri.place(relx = 0.92, rely = 0.41, width=((142/1920)*w), height =(108/1080)*h)
settings_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
settings_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)
settings_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height =(28/1080)*h)

settings_smity_gender_label.place(relx = 0.02, rely = 0.1, width=((400/1920)*w), height =(50/1080)*h)
settings_female_button.place(relx = 0.91, rely = 0.1, width=((148/1920)*w), height =(43/1080)*h)
settings_male_button.place(relx = 0.85, rely = 0.1, width=((110/1920)*w), height =(43/1080)*h)

settings_username_label.place(relx = 0.02, rely = 0.2, width=((262/1920)*w), height =(52/1080)*h)
settings_user_name_text_field.place(relx = 0.85, rely = 0.2, width=((273/1920)*w), height =(52/1080)*h)

settings_voice_control_label.place(relx = 0.02, rely = 0.3, width=((354/1920)*w), height =(50/1080)*h)
settings_voice_control_button.place(relx = 0.9, rely = 0.3, width=((173/1920)*w), height =(64/1080)*h)

settings_speak_key_label.place(relx = 0.12, rely = 0.4, width=((264/1920)*w), height =(60/1080)*h)
settings_speak_key_button.place(relx = 0.85, rely = 0.385, width=((173/1920)*w), height =(64/1080)*h)

settings_wake_up_label.place(relx = 0.12, rely = 0.5, width=((357/1920)*w), height =(60/1080)*h)
settings_wake_up_button.place(relx = 0.85, rely = 0.485, width=((173/1920)*w), height =(64/1080)*h)

settings_home_button.place(relx = 0.006, rely = 0.35, width=((43/1920)*w), height =(43/1080)*h)
settings_user_button.place(relx = 0.006, rely = 0.65, width=((43/1920)*w), height =(43/1080)*h)#-5x-5
settings_user_text_label.place(relx = 0.0295, rely = 0.7, width=((44/1920)*w),height =(43/1080)*h)
settings_back_button.place(relx = 0.006, rely = 0.05, width=((48/1920)*w), height =(34/1080)*h)

settings_info_button.place(relx = 0.1, rely = 0.625,width=((206/1920)*w), height =(275/1080)*h)
settings_applications_button.place(relx = 0.8, rely = 0.625, width=((325/1920)*w), height =(275/1080)*h)

settings_load()
#############################################################################################################################################################################
#    H    H
#    H    H
#    HHHHHH
#    H    H
#    H    H
#############################################################################################################################################################################
home_page = tk.Frame(screen)
#BackGround
        #open image
home_page_backGroundImage = Image.open("%s\\background.png"%(location))
        #resize image
home_page_resized_backGroundImage = home_page_backGroundImage.resize((w, h-171),Image.ANTIALIAS)

home_page_new_backGroundImage = ImageTk.PhotoImage(home_page_resized_backGroundImage)

    #Label
home_page_backGroundImage_label = Label(home_page, image=home_page_new_backGroundImage, borderwidth=0)
#GIF
a = int ((260/1920)*w)
b = int ((270/1080)*h)
resize_gif(a,b)
home_page_gif_label = ImageLabel(home_page,borderwidth=0)
home_page_gif_label.load('%s\\aaa.gif'%(location))

#header
home_page_header = Label(home_page,borderwidth=0,background = "#0d0029")
#home_page_title_image
temp_image = Image.open("%s\\Home page\\title.png"%(location))
a = int((405/1920)*w)+5
b = int((171/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_title_image = ImageTk.PhotoImage(temp_image2)

home_page_title = Label(home_page_header,image = home_page_title_image, borderwidth=0)

temp_image = Image.open("%s\\akrh titlou.png"%(location))
a = int((142/1920)*w)+5
b = int((108/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_title_aktri_image = ImageTk.PhotoImage(temp_image2)

home_page_title_aktri = Label(home_page_header,image = home_page_title_aktri_image, borderwidth=0)

temp_image = Image.open("%s\\exit_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_cloce_button_image = ImageTk.PhotoImage(temp_image2)

home_page_cloce_button = tk.Button(home_page_header,image = home_page_cloce_button_image, borderwidth=0, command = screen.destroy)

temp_image = Image.open("%s\\exit_fullscreen_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_exit_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)

home_page_exit_fullscreen_button = tk.Button(home_page_header,image = home_page_exit_fullscreen_button_image, borderwidth=0)

temp_image = Image.open("%s\\minimize_button.png"%(location))
a = int((31/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_minimize_button_image = ImageTk.PhotoImage(temp_image2)

home_page_minimize_button = tk.Button(home_page_header,image = home_page_minimize_button_image, borderwidth=0)

temp_image = Image.open("%s\\fullscreen_button.png"%(location))
a = int((62/1920)*w)+5
b = int((28/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_fullscreen_button_image = ImageTk.PhotoImage(temp_image2)

home_page_fullscreen_button = tk.Button(home_page_header,image = home_page_fullscreen_button_image, borderwidth=0)

home_page_exit_fullscreen_button.bind("<Button-1>", home_page_exit_fullscreen)
home_page_fullscreen_button.bind("<Button-1>",home_page_fullscreen)
home_page_minimize_button.bind("<Button-1>", minimize)

#Calendar button
    # setings button image
temp_image = Image.open("%s\\Home page\\calendar_button.png"%(location))
a = int((36/1920)*w)+5
b = int((40/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_calendar_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
home_page_calendar_button = tk.Button(home_page_header, text = ' ', image = home_page_calendar_button_image, borderwidth=0)
home_page_calendar_button.bind("<Button-1>",home_page_to_calendar)

#Settings button
    # setings button image
temp_image = Image.open("%s\\settings_button.png"%(location))
a = int((39/1920)*w)+5
b = int((40/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_settings_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
home_page_settings_button = tk.Button(home_page, text = ' ', image = home_page_settings_button_image, borderwidth=0)
    
home_page_settings_button.bind("<Button-1>", home_page_go_to_setings)

#weather
    # weather button image
temp_image = Image.open("%s\\Home page\\weather.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_weather_button_image = ImageTk.PhotoImage(temp_image2)
    #weather button
home_page_weather_button = tk.Button(home_page, image = home_page_weather_button_image, borderwidth=0)

#questions
    # questions button image
temp_image = Image.open("%s\\Home page\\questions.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_questions_button_image = ImageTk.PhotoImage(temp_image2)
    #questions button
home_page_questions_button = tk.Button(home_page, image = home_page_questions_button_image, borderwidth=0)

#time
    # time button image
temp_image = Image.open("%s\\Home page\\time.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_time_button_image = ImageTk.PhotoImage(temp_image2)
    #time button
home_page_time_button = tk.Button(home_page, image = home_page_time_button_image, borderwidth=0)

#news
    # news button image
temp_image = Image.open("%s\\Home page\\news.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_news_button_image = ImageTk.PhotoImage(temp_image2)
    #news button
home_page_news_button = tk.Button(home_page, image = home_page_news_button_image, borderwidth=0)

#calls
    # calls button image
temp_image = Image.open("%s\\Home page\\calls.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_calls_button_image = ImageTk.PhotoImage(temp_image2)
    #calls button
home_page_calls_button = tk.Button(home_page, image = home_page_calls_button_image, borderwidth=0)

#maps
    # maps button image
temp_image = Image.open("%s\\Home page\\maps.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_maps_button_image = ImageTk.PhotoImage(temp_image2)
    #maps button
home_page_maps_button = tk.Button(home_page, image = home_page_maps_button_image, borderwidth=0)

#mail
    # mail button image
temp_image = Image.open("%s\\Home page\\mail.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_mail_button_image = ImageTk.PhotoImage(temp_image2)
    #mail button
home_page_mail_button = tk.Button(home_page, image = home_page_mail_button_image, borderwidth=0)

#music
    # music button image
temp_image = Image.open("%s\\Home page\\music.png"%(location))
a = int((200/1920)*w)+5
b = int((185/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_music_button_image = ImageTk.PhotoImage(temp_image2)
    #music button
home_page_music_button = tk.Button(home_page, image = home_page_music_button_image, borderwidth=0)

#bottom line
home_page_bottom_line = Label(home_page,borderwidth=0,background = "#0d0029")


#Mic button
    # Mic button image
temp_image = Image.open("%s\\Home page\\microphone.png"%(location))
a = int((23/1920)*w)+5
b = int((45/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_mic_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
home_page_mic_button = tk.Button(home_page_bottom_line, text = ' ', image = home_page_mic_button_image, borderwidth=0)

#message history)
temp_image = Image.open("%s\\Home page\\message_history.png"%(location))
a = int((950/1920)*w)
b = int((325/1080)*h)+1
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
message_history_label_image = ImageTk.PhotoImage(temp_image2)

message_history_label = Label(home_page, image = message_history_label_image, borderwidth =0)
global message_history
global line_count
line_count =0
message_history = ""
message_history_label_text_field = Label(message_history_label,text = message_history, font = ("", 20), fg = "white", width =1000 , borderwidth =0,background = "#236877",anchor='w')

#get commands
def on_click(event):
    event.widget.delete(0, tk.END)
#comand_text_field =tk.Entry(bottom_line, font = ("", 33), fg = "white", width =1000 , borderwidth =0,background = "#0d0029")
home_page_comand_text_field =tk.Entry(home_page_bottom_line, font = ("", 25), fg = "white", width =1000 , borderwidth =0,background = "#0d0029")
home_page_comand_text_field.insert(0, "Ask S.M.I.T.Y. ")
home_page_comand_text_field.bind("<Button-1>", on_click)
home_page_comand_text_field.bind("<Return>",get_comand)

#Enter button
    # setings button image
temp_image = Image.open("%s\\Home page\\enter_button.png"%(location))
a = int((54/1920)*w)+5
b = int((38/1080)*h)+5
temp_image2 = temp_image.resize((a, b),Image.ANTIALIAS)
home_page_enter_button_image = ImageTk.PhotoImage(temp_image2)
    #Add button
home_page_enter_button = tk.Button(home_page_bottom_line, text = ' ', image = home_page_enter_button_image, borderwidth=0)
home_page_enter_button.bind("<Button-1>",get_comand)

#add to Home page
home_page.pack(fill='both', expand =1)
home_page_backGroundImage_label.place( relx=0.0, rely= 0.15 )
home_page_header.place(relx=0.0, y= 0.0, relwidth = 1.0,height =171)
home_page_title.place(relx = 0.5, rely = 0.5,anchor ="center", width=((405/1920)*w), height=(171/1080)*h)
home_page_title_aktri.place(relx = 0.92, rely = 0.41, width=((142/1920)*w), height=(108/1080)*h)
home_page_calendar_button.place(relx = 0.006, rely = 0.65, width=((36/1920)*w), height=(40/1080)*h)
home_page_settings_button.place(relx = 0.0065, rely = 0.01, width=((39/1920)*w), height=(40/1080)*h)
home_page_cloce_button.place(relx = 0.985, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
home_page_exit_fullscreen_button.place(relx = 0.965, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)
home_page_minimize_button.place(relx = 0.945, rely = 0.0, width=((31/1920)*w), height=(28/1080)*h)

home_page_gif_label.place(relx = 0.5, rely = 0.5,anchor ="center", width=((260/1920)*w))

home_page_weather_button.place(relx = 0.06, rely = 0.506,anchor ="center", width=((200/1920)*w), height=(185/1080)*h)
home_page_questions_button.place(relx = 0.17, rely = 0.519,anchor ="center", width=((200/1920)*w), height=(185/1080)*h)
home_page_time_button.place(relx = 0.28, rely = 0.505,anchor ="center", width=((200/1920)*w), height=(185/1080)*h)
home_page_news_button.place(relx = 0.375, rely = 0.504,anchor ="center", width=((190/1920)*w), height=(185/1080)*h)

home_page_calls_button.place(relx = 0.62, rely = 0.51,anchor ="center", width=((170/1920)*w), height=(185/1080)*h)
home_page_maps_button.place(relx = 0.72, rely = 0.51,anchor ="center", width=((170/1920)*w), height=(185/1080)*h)
home_page_mail_button.place(relx = 0.82, rely = 0.51,anchor ="center", width=((170/1920)*w), height=(185/1080)*h)
home_page_music_button.place(relx = 0.94, rely = 0.515,anchor ="center", width=((170/1920)*w), height=(185/1080)*h)

message_history_label.place(relx = 0.005, rely = 0.64, width=((950/1920)*w), height=(325/1080)*h)
message_history_label_text_field.place(relx = 0.008, rely = 0.03, relwidth=0.9, relheight=0.9)

home_page_bottom_line.place(relx=0.0, rely= 0.9515, relwidth = 1.0,height =52)
home_page_enter_button.place(relx = 0.965, rely = 0.13, width=((54/1920)*w), height=(38/1080)*h)
home_page_mic_button.place(relx = 0.005, rely = 0.06, width=((23/1920)*w), height=(45/1080)*h)
home_page_comand_text_field.place(relx=0.03, rely= 0.12, relwidth = 0.3,height =(36/1080)*h)

home_page.mainloop()
