#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on February 24, 2020, at 12:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'SGPV_Interaction'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Group': '001', 'Stimuli1': ['A', 'B'], 'Stimuli2': ['A', 'B']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\Experiment\\SGPV2_Interaction\\SGPV_Communicative\\SGPV_communicative_congruency.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.208,0.208,0.208], colorSpace='rgb',
    blendMode='avg', useFBO=True, gammaErrorPolicy ='warn',
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Start"
StartClock = core.Clock()
start_text_m1 = visual.TextStim(win=win, name='start_text_m1',
    text='Thank you for offering to take part in this experiment.',
    font='Comic Sans',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


win1 = visual.Window(
    size=[1920, 1080], fullscr=True, screen=2, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='Monitor2', color=[0.208,0.208,0.208], colorSpace='rgb',
    blendMode='avg', useFBO=True, gammaErrorPolicy = 'warn', 
    units='pix')

#strat instructiong
start_text_m2 = visual.TextStim(win=win1, name='start_text_m2',
    text='Thank you for offering to take part in this experiment.',
    font='Comic Sans',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


Instruction_m2 = visual.TextStim(win=win1, name='Instruction_m2',
    text="In the following experiment, you will complete a task in which you will have to communicate a series of pictorial stimuli using only your hands to your partner. \n\nDuring the experiment, you will either take the role of the gesturer or the interpreter. In each trial you will first see a picture on both of your screens. The picture is either the same or not. It will remain on both screens during the trial and provide a background to ease communication with your partner. \n\nThe target picture will only show on the gesturer’s screen, while there will be three different pictures on the interpreter’s screen. Pictures displayed on the interpreter’s screen will only differ in the action that the character performed, the character who performs the action and the object which the character interacts with. \n\nThe task for the interpreter is to confirm whether the shared picture on both screens is the same and to select the target picture based on the gesturer's gestural depiction and the shared picture. The interpreter is allowed to verbally describe the shared picture in confirmation period. but not allowed to produce any speech, gesture or body language during the selection period. \n\nThe task for the gesturer is to depict the target picture with only their hands.   The gesturer should make sure that the interpreter will select the correct picture, relying on the shared picture and using gestures alone. The gesturer is not allowed to produce speech during the experiment. \n\nEach trial will be completed when the interpreter correctly selects the target picture.\n\nPlease kindly inform the experimenter when you are ready.\n",
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
Pra_Instruction_m2 = visual.TextStim(win=win1, name='Pra_Instruction_m2',
    text='You will now have several practice trials to get familiar with the task.\n\nIn the practice trials, you will take turns to take the role of gesturer and interpreter. In each trial, you will first enter the confirmation period in which you will see a shared picture on both of your screens. The picture is either the same or not. The interpreter will need to verbally describe the picture to confirm with the gesturer whether you are seeing the same picture. The shared picture will remain on both screens during the trial and provide a background to ease communication with your partner. \n\nFor the interpreter. Your task is to verbally describe the shared picture and confirm whether you are having the same picture on both screens in the confirmation period and to guess what the target picture is based on the gesturer’s depiction in the selection period. You would have only one chance to provide the answer, so please be sure about the answer before you press the corresponding button. \n\nFor the gesturer, your task is to confirm with the interpreter that you are having the same shared picture on the screens in the confirmation period and to depict the target picture and make sure that the interpreter will select the correct picture, relying on the shared picture and using gesture alone in the selection period.\n\nPlease do not speak and do not point at any object in the room and the computer screen during other parts of the experiment.\n\nYou will be told what role you are going to take before each trial.\n\nPlease kindly inform the experimenter when you are ready.\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

end_text = visual.TextStim(win=win1, name='end_text',
    text='Thank you for participating. Please fill in the post-experiment questionnaire on your right-hand side.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


ins_conf_2 = visual.TextStim(win=win1, name='ins_conf_2',
    text='Please verbally describe this shared picture.\nPress Y if you are having the same picture on both screens.\nPress N if you are having different pictures.',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    

ins_conf_22 = visual.TextStim(win=win1, name='ins_conf_22',
    text='Please respond Yes if you believe you are having the same picture on both screens and No if you are having different pictures.',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

#TRIALS

img_pre_1_m2 = visual.ImageStim(
    win=win1,
    name='image_pre_1_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

     
img_pre_2_m2 = visual.ImageStim(
    win=win1,
    name='image_pre_2_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)    

img_ans_1_a_m2 = visual.ImageStim(
    win=win1,
    name='image_ans_1_a_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(480, 360), size=(463.32, 327.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
img_ans_1_b_m2 = visual.ImageStim(
    win=win1,
    name='image_ans_1_b_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(463.32, 327.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

img_ans_1_c_m2 = visual.ImageStim(
    win=win1,
    name='image_ans_1_c_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(480, -360), size=(463.32, 327.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    

img_pre_3_m2 = visual.ImageStim(
    win=win1,
    name='pra_img_pre_3_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
    
img_pre_4_m2 = visual.ImageStim(
    win=win1,
    name='pra_img_pre_4_m2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)   
    

img_tar_compre_1 = visual.ImageStim(
    win=win1,
    name='pra_img_tar_compre_1', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
    

square_win1 = visual.ImageStim(
    win=win1,
    name='square_win1', 
    image='Materials/square.png', mask=None,
    ori=0, pos=(480, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
    
#Real trial instruction
real_trial = visual.TextStim(win=win1, name='real_trail',
    text='You will now start the real trial.\n\nYou are going to take the role of the interpreter in the real trial. In each trial, you will first need to verbally describe the shared picture to make sure you are having the same pictures on both screens.\n\nAfter the confirmation period, you will need to select the target picture based on the gesturer\'s depiction and the shared picture. \n\nPlease do not produce any speech, gesture and body language, and do not point at any object in the room and the computer screen during the seletion period.\n\nPlease kindly inform the experimenter when you are ready.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
    
#Selection
text_N = visual.TextStim(win=win1, name='text_N',
    text='N',
    font='Arial',
    units='pix', pos=(100, -360), height=50, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_J = visual.TextStim(win=win1, name='text_J',
    text='J',
    font='Arial',
    units='pix', pos=(100, 0), height=50, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_U = visual.TextStim(win=win1, name='text_U',
    text='U',
    font='Arial',
    units='pix', pos=(100, 360), height=50, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
    
trial_num = 0


text_role_g_win1 = visual.TextStim(win=win1, name='text_r_g_1',
    text='You will be the gesturer in this trial',
    font='Arial',
    units='norm', pos=(0, -0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
    

text_role_i_win1 = visual.TextStim(win=win1, name='text_r_i_1',
    text='You will be the interpreter in this trial',
    font='Arial',
    units='norm', pos=(0, -0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);


# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
Instruction_m1 = visual.TextStim(win=win, name='Instruction_m1',
    text="In the following experiment, you will complete a task in which you will have to communicate a series of pictorial stimuli using only your hands to your partner. \n\nDuring the experiment, you will either take the role of the gesturer or the interpreter. In each trial you will first see a picture on both of your screens. The picture is either the same or not. It will remain on both screens during the trial and provide a background to ease communication with your partner. \n\nThe target picture will only show on the gesturer’s screen, while there will be three different pictures on the interpreter’s screen. Pictures displayed on the interpreter’s screen will only differ in the action that the character performed, the character who performs the action and the object which the character interacts with. \n\nThe task for the interpreter is to confirm whether the shared picture on both screens is the same and to select the target picture based on the gesturer's gestural depiction and the shared picture. The interpreter is allowed to verbally describe the shared picture in confirmation period. but not allowed to produce any speech, gesture or body language during the selection period. \n\nThe task for the gesturer is to depict the target picture with only their hands.   The gesturer should make sure that the interpreter will select the correct picture, relying on the shared picture and using gestures alone. The gesturer is not allowed to produce speech during the experiment. \n\nEach trial will be completed when the interpreter correctly selects the target picture.\n\nPlease kindly inform the experimenter when you are ready.\n",
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import numpy as np
import os
import cv2

trial_num = 1

path_file = 'F:\\Experiment\\SGPV2_Interaction\\SGPV_Communicative\\data\\' + str(expInfo['participant'])

isExists=os.path.exists(path_file)
 
if not isExists:
    os.makedirs(path_file) 
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "webcam_check1"
webcam_check1Clock = core.Clock()
Videomonitor1 = visual.ImageStim(
    win=win,
    name='Videomonitor1', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=True,
    texRes=128, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Check Camera 1 ',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Pra_ins"
Pra_insClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='You will now have several practice trials to get familiar with the task.\n\nIn the practice trials, you will take turns to take the role of gesturer and interpreter. In each trial, you will first enter the confirmation period in which you will see a shared picture on both of your screens. The picture is either the same or not. The interpreter will need to verbally describe the picture to confirm with the gesturer whether you are seeing the same picture. The shared picture will remain on both screens during the trial and provide a background to ease communication with your partner. \n\nFor the interpreter. Your task is to verbally describe the shared picture and confirm whether you are having the same picture on both screens in the confirmation period and to guess what the target picture is based on the gesturer’s depiction in the selection period. You would have only one chance to provide the answer, so please be sure about the answer before you press the corresponding button. \n\nFor the gesturer, your task is to confirm with the interpreter that you are having the same shared picture on the screens in the confirmation period and to depict the target picture and make sure that the interpreter will select the correct picture, relying on the shared picture and using gesture alone in the selection period.\n\nPlease do not speak and do not point at any object in the room and the computer screen during other parts of the experiment.\n\nYou will be told what role you are going to take before each trial.\n\nPlease kindly inform the experimenter when you are ready.\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "reminder"
reminderClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='You will be the gesturer in this trial.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pra_preview"
pra_previewClock = core.Clock()
pra_img_pre_1 = visual.ImageStim(
    win=win,
    name='pra_img_pre_1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_12 = keyboard.Keyboard()
text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "pra_descri_1"
pra_descri_1Clock = core.Clock()
pra_im_pre_a1 = visual.ImageStim(
    win=win,
    name='pra_im_pre_a1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pra_img_tar_descri_1 = visual.ImageStim(
    win=win,
    name='pra_img_tar_descri_1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_7 = keyboard.Keyboard()
square = visual.ImageStim(
    win=win,
    name='square', units='pix', 
    image='Materials/square.png', mask=None,
    ori=0, pos=(480, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "reminder_2"
reminder_2Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='You will be the interpreter in this trial.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pra_preview_2"
pra_preview_2Clock = core.Clock()
pra_img_pre_2 = visual.ImageStim(
    win=win,
    name='pra_img_pre_2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_17 = visual.TextStim(win=win, name='text_17',
    text='Please verbally describe this shared picture.\n\nPress Y if you are having the same picture on both screens.\n\nPress N if you are having different pictures ',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "pra_compre_2"
pra_compre_2Clock = core.Clock()
pra_img_pre_a2 = visual.ImageStim(
    win=win,
    name='pra_img_pre_a2', 
    image='sin', mask=None,
    ori=0, pos=(-480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
pra_img_ans4 = visual.ImageStim(
    win=win,
    name='pra_img_ans4', 
    image='sin', mask=None,
    ori=0, pos=(480, 360), size=(463.32, 327.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
pra_img_ans5 = visual.ImageStim(
    win=win,
    name='pra_img_ans5', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(463.32, 327.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
pra_img_ans6 = visual.ImageStim(
    win=win,
    name='pra_img_ans6', 
    image='sin', mask=None,
    ori=0, pos=(480, -360), size=(463.32, 327.24),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_8 = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='U',
    font='Arial',
    pos=(100, 360), height=50, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='J',
    font='Arial',
    pos=(100, 0), height=50, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='N',
    font='Arial',
    pos=(100, -360), height=50, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Real_trial_instruction"
Real_trial_instructionClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='You will now start the real trial.\n\nYou are going to take the role of the gesturer in the real trial. In each trial, you will first see a shared picture on both of your screens. The picture is either the same or not. You will first need to confirm with the interpreter whether you are seeing the same picture by answering yes or no in the confirmation period. \n\nAfter the confirmation period, your task is to depict the target picture and make sure that the interpreter will select the correct picture, relying on the shared picture and using gesture alone \n\nPlease be aware that pictures displayed on the interpreter’s screen will only differ in the action that the character performs, the character who performs the action and the object which the character interacts with. The information provided in the shared picture will remain the same across the different pictures on the interpreter’s screen.\n\nPlease do not produce any speech and do not point at any object in the room and the computer screen during the experiment.\n\nPlease kindly inform the experimenter when you are ready.\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "webcam_check1"
webcam_check1Clock = core.Clock()
Videomonitor1 = visual.ImageStim(
    win=win,
    name='Videomonitor1', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=True,
    texRes=128, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Check Camera 1 ',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "perivew"
perivewClock = core.Clock()
img_pv_1 = visual.ImageStim(
    win=win,
    name='img_pv_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()
text_18 = visual.TextStim(win=win, name='text_18',
    text='Please respond Yes if you believe you are having the same picture on both screens and No if you are having different pictures.',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "descri_1"
descri_1Clock = core.Clock()
im_pre_a1 = visual.ImageStim(
    win=win,
    name='im_pre_a1', 
    image='sin', mask=None,
    ori=0, pos=(-480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
img_tar_descri_1 = visual.ImageStim(
    win=win,
    name='img_tar_descri_1', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
square_trails = visual.ImageStim(
    win=win,
    name='square_trails', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Real_trial_instruction"
Real_trial_instructionClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='You will now start the real trial.\n\nYou are going to take the role of the gesturer in the real trial. In each trial, you will first see a shared picture on both of your screens. The picture is either the same or not. You will first need to confirm with the interpreter whether you are seeing the same picture by answering yes or no in the confirmation period. \n\nAfter the confirmation period, your task is to depict the target picture and make sure that the interpreter will select the correct picture, relying on the shared picture and using gesture alone \n\nPlease be aware that pictures displayed on the interpreter’s screen will only differ in the action that the character performs, the character who performs the action and the object which the character interacts with. The information provided in the shared picture will remain the same across the different pictures on the interpreter’s screen.\n\nPlease do not produce any speech and do not point at any object in the room and the computer screen during the experiment.\n\nPlease kindly inform the experimenter when you are ready.\n',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "webcam_check1"
webcam_check1Clock = core.Clock()
Videomonitor1 = visual.ImageStim(
    win=win,
    name='Videomonitor1', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(1280, 720),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=True,
    texRes=128, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Check Camera 1 ',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "perivew"
perivewClock = core.Clock()
img_pv_1 = visual.ImageStim(
    win=win,
    name='img_pv_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()
text_18 = visual.TextStim(win=win, name='text_18',
    text='Please respond Yes if you believe you are having the same picture on both screens and No if you are having different pictures.',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.06, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "descri_1"
descri_1Clock = core.Clock()
im_pre_a1 = visual.ImageStim(
    win=win,
    name='im_pre_a1', 
    image='sin', mask=None,
    ori=0, pos=(-480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
img_tar_descri_1 = visual.ImageStim(
    win=win,
    name='img_tar_descri_1', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(772.2, 545.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
square_trails = visual.ImageStim(
    win=win,
    name='square_trails', 
    image='sin', mask=None,
    ori=0, pos=(480, 0), size=(936.6, 636.6),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Thank you for participating. Please fill in the post-experiment questionnaire and video-consent form on your left-hand side. ',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
start_text_m2.setAutoDraw(True)
# keep track of which components have finished
StartComponents = [start_text_m1]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text_m1* updates
    if start_text_m1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text_m1.frameNStart = frameN  # exact frame index
        start_text_m1.tStart = t  # local t and not account for scr refresh
        start_text_m1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text_m1, 'tStartRefresh')  # time at next scr refresh
        start_text_m1.setAutoDraw(True)
    if start_text_m1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > start_text_m1.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            start_text_m1.tStop = t  # not accounting for scr refresh
            start_text_m1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(start_text_m1, 'tStopRefresh')  # time at next scr refresh
            start_text_m1.setAutoDraw(False)
    win1.flip()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_text_m1.started', start_text_m1.tStartRefresh)
thisExp.addData('start_text_m1.stopped', start_text_m1.tStopRefresh)
start_text_m2.setAutoDraw(False)
win1.flip()

# ------Prepare to start Routine "Instruction"-------
# update component parameters for each repeat
Instruction_m2.setAutoDraw(True)
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
InstructionComponents = [Instruction_m1, key_resp_4]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction_m1* updates
    if Instruction_m1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruction_m1.frameNStart = frameN  # exact frame index
        Instruction_m1.tStart = t  # local t and not account for scr refresh
        Instruction_m1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruction_m1, 'tStartRefresh')  # time at next scr refresh
        Instruction_m1.setAutoDraw(True)
    win1.flip()
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys = theseKeys.name  # just the last key pressed
            key_resp_4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruction_m1.started', Instruction_m1.tStartRefresh)
thisExp.addData('Instruction_m1.stopped', Instruction_m1.tStopRefresh)
Instruction_m2.setAutoDraw(False)
win1.flip()
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "webcam_check1"-------
# update component parameters for each repeat
video = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
webcam_check1Components = [Videomonitor1, key_resp_6, text_8]
for thisComponent in webcam_check1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
webcam_check1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "webcam_check1"-------
while continueRoutine:
    # get current time
    t = webcam_check1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=webcam_check1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Videomonitor1* updates
    if Videomonitor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Videomonitor1.frameNStart = frameN  # exact frame index
        Videomonitor1.tStart = t  # local t and not account for scr refresh
        Videomonitor1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Videomonitor1, 'tStartRefresh')  # time at next scr refresh
        Videomonitor1.setAutoDraw(True)
    returnVal, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)/255.0
    Videomonitor1.image = frame
    Videomonitor1.draw()
    win.flip()
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in webcam_check1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "webcam_check1"-------
for thisComponent in webcam_check1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Videomonitor1.started', Videomonitor1.tStartRefresh)
thisExp.addData('Videomonitor1.stopped', Videomonitor1.tStopRefresh)
video.release()


# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "webcam_check1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Pra_ins"-------
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
Pra_Instruction_m2.setAutoDraw(True)

# keep track of which components have finished
Pra_insComponents = [text_13, key_resp_10]
for thisComponent in Pra_insComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Pra_insClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Pra_ins"-------
while continueRoutine:
    # get current time
    t = Pra_insClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Pra_insClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_10.keys = theseKeys.name  # just the last key pressed
            key_resp_10.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    win1.flip()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Pra_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Pra_ins"-------
for thisComponent in Pra_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
Pra_Instruction_m2.setAutoDraw(False)
# the Routine "Pra_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pratice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_communicaitve_reduced.csv'),
    seed=None, name='pratice')
thisExp.addLoop(pratice)  # add the loop to the experiment
thisPratice = pratice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPratice.rgb)
if thisPratice != None:
    for paramName in thisPratice:
        exec('{} = thisPratice[paramName]'.format(paramName))

for thisPratice in pratice:
    currentLoop = pratice
    # abbreviate parameter names if possible (e.g. rgb = thisPratice.rgb)
    if thisPratice != None:
        for paramName in thisPratice:
            exec('{} = thisPratice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reminder"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_role_i_win1.setAutoDraw(True)
    # keep track of which components have finished
    reminderComponents = [text_11]
    for thisComponent in reminderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "reminder"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reminderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reminderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        win1.flip()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reminder"-------
    for thisComponent in reminderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('text_11.started', text_11.tStartRefresh)
    pratice.addData('text_11.stopped', text_11.tStopRefresh)
    text_role_i_win1.setAutoDraw(False)
    
    # ------Prepare to start Routine "pra_preview"-------
    # update component parameters for each repeat
    pra_img_pre_1.setImage(img_pre_1)
    key_resp_12.keys = []
    key_resp_12.rt = []
    text_16.setText('Please respond Yes if you believe you are having the same picture on both screens and No if you are having different pictures.')
    img_pre_1_m2.setImage(img_pre_11)
    img_pre_1_m2.setAutoDraw(True)
    ins_conf_2.setAutoDraw(True)
    # keep track of which components have finished
    pra_previewComponents = [pra_img_pre_1, key_resp_12, text_16]
    for thisComponent in pra_previewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra_previewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pra_preview"-------
    while continueRoutine:
        # get current time
        t = pra_previewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra_previewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pra_img_pre_1* updates
        if pra_img_pre_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_pre_1.frameNStart = frameN  # exact frame index
            pra_img_pre_1.tStart = t  # local t and not account for scr refresh
            pra_img_pre_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_pre_1, 'tStartRefresh')  # time at next scr refresh
            pra_img_pre_1.setAutoDraw(True)
        
        # *key_resp_12* updates
        waitOnFlip = False
        if key_resp_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.tStart = t  # local t and not account for scr refresh
            key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_12.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_12.getKeys(keyList=['y', 'n', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_12.keys = theseKeys.name  # just the last key pressed
                key_resp_12.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        win1.flip()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_previewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra_preview"-------
    for thisComponent in pra_previewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('pra_img_pre_1.started', pra_img_pre_1.tStartRefresh)
    pratice.addData('pra_img_pre_1.stopped', pra_img_pre_1.tStopRefresh)
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys = None
    pratice.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        pratice.addData('key_resp_12.rt', key_resp_12.rt)
    pratice.addData('key_resp_12.started', key_resp_12.tStartRefresh)
    pratice.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
    pratice.addData('text_16.started', text_16.tStartRefresh)
    pratice.addData('text_16.stopped', text_16.tStopRefresh)
    img_pre_1_m2.setAutoDraw(False)
    ins_conf_2.setAutoDraw(False)
    win1.flip()
    # the Routine "pra_preview" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pra_descri_1"-------
    # update component parameters for each repeat
    pra_im_pre_a1.setImage(img_pre_1)
    pra_img_tar_descri_1.setImage(img_tar_1)
    key_resp_7.keys = []
    key_resp_7.rt = []
    img_pre_2_m2.setImage(img_pre_11)
    img_ans_1_a_m2.setImage(img_ans_a_1)
    img_ans_1_b_m2.setImage(img_ans_b_1)
    img_ans_1_c_m2.setImage(img_ans_c_1)
    img_pre_2_m2.setAutoDraw(True)
    img_ans_1_a_m2.setAutoDraw(True)
    img_ans_1_b_m2.setAutoDraw(True)
    img_ans_1_c_m2.setAutoDraw(True)
    text_N.setAutoDraw(True)
    text_J.setAutoDraw(True)
    text_U.setAutoDraw(True)
    # keep track of which components have finished
    pra_descri_1Components = [pra_im_pre_a1, pra_img_tar_descri_1, key_resp_7, square]
    for thisComponent in pra_descri_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra_descri_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pra_descri_1"-------
    while continueRoutine:
        # get current time
        t = pra_descri_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra_descri_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pra_im_pre_a1* updates
        if pra_im_pre_a1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_im_pre_a1.frameNStart = frameN  # exact frame index
            pra_im_pre_a1.tStart = t  # local t and not account for scr refresh
            pra_im_pre_a1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_im_pre_a1, 'tStartRefresh')  # time at next scr refresh
            pra_im_pre_a1.setAutoDraw(True)
        
        # *pra_img_tar_descri_1* updates
        if pra_img_tar_descri_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_tar_descri_1.frameNStart = frameN  # exact frame index
            pra_img_tar_descri_1.tStart = t  # local t and not account for scr refresh
            pra_img_tar_descri_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_tar_descri_1, 'tStartRefresh')  # time at next scr refresh
            pra_img_tar_descri_1.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['u', 'j', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_7.keys = theseKeys.name  # just the last key pressed
                key_resp_7.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        win1.flip()
        
        # *square* updates
        if square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square.frameNStart = frameN  # exact frame index
            square.tStart = t  # local t and not account for scr refresh
            square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square, 'tStartRefresh')  # time at next scr refresh
            square.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_descri_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra_descri_1"-------
    for thisComponent in pra_descri_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('pra_im_pre_a1.started', pra_im_pre_a1.tStartRefresh)
    pratice.addData('pra_im_pre_a1.stopped', pra_im_pre_a1.tStopRefresh)
    pratice.addData('pra_img_tar_descri_1.started', pra_img_tar_descri_1.tStartRefresh)
    pratice.addData('pra_img_tar_descri_1.stopped', pra_img_tar_descri_1.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    pratice.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        pratice.addData('key_resp_7.rt', key_resp_7.rt)
    pratice.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    pratice.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    img_pre_2_m2.setAutoDraw(False)
    img_ans_1_a_m2.setAutoDraw(False)
    img_ans_1_b_m2.setAutoDraw(False)
    img_ans_1_c_m2.setAutoDraw(False)
    text_N.setAutoDraw(False)
    text_J.setAutoDraw(False)
    text_U.setAutoDraw(False)
    win1.flip()
    pratice.addData('square.started', square.tStartRefresh)
    pratice.addData('square.stopped', square.tStopRefresh)
    # the Routine "pra_descri_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [text_2]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('text_2.started', text_2.tStartRefresh)
    pratice.addData('text_2.stopped', text_2.tStopRefresh)
    
    # ------Prepare to start Routine "reminder_2"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_role_g_win1.setAutoDraw(True)
    # keep track of which components have finished
    reminder_2Components = [text_12]
    for thisComponent in reminder_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reminder_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "reminder_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = reminder_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reminder_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                text_12.setAutoDraw(False)
        win1.flip()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reminder_2"-------
    for thisComponent in reminder_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('text_12.started', text_12.tStartRefresh)
    pratice.addData('text_12.stopped', text_12.tStopRefresh)
    text_role_g_win1.setAutoDraw(False)
    
    # ------Prepare to start Routine "pra_preview_2"-------
    # update component parameters for each repeat
    pra_img_pre_2.setImage(img_pre_2)
    img_pre_3_m2.setImage(img_pre_22)
    img_pre_3_m2.setAutoDraw(True)
    ins_conf_22.setAutoDraw(True)
    key_resp_14.keys = []
    key_resp_14.rt = []
    # keep track of which components have finished
    pra_preview_2Components = [pra_img_pre_2, text_17, key_resp_14]
    for thisComponent in pra_preview_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra_preview_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pra_preview_2"-------
    while continueRoutine:
        # get current time
        t = pra_preview_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra_preview_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pra_img_pre_2* updates
        if pra_img_pre_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_pre_2.frameNStart = frameN  # exact frame index
            pra_img_pre_2.tStart = t  # local t and not account for scr refresh
            pra_img_pre_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_pre_2, 'tStartRefresh')  # time at next scr refresh
            pra_img_pre_2.setAutoDraw(True)
        win1.flip()
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        
        # *key_resp_14* updates
        waitOnFlip = False
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['y', 'n', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_14.keys = theseKeys.name  # just the last key pressed
                key_resp_14.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_preview_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra_preview_2"-------
    for thisComponent in pra_preview_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('pra_img_pre_2.started', pra_img_pre_2.tStartRefresh)
    pratice.addData('pra_img_pre_2.stopped', pra_img_pre_2.tStopRefresh)
    img_pre_3_m2.setAutoDraw(False)
    ins_conf_22.setAutoDraw(False)
    win1.flip()
    pratice.addData('text_17.started', text_17.tStartRefresh)
    pratice.addData('text_17.stopped', text_17.tStopRefresh)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    pratice.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        pratice.addData('key_resp_14.rt', key_resp_14.rt)
    pratice.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    pratice.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    # the Routine "pra_preview_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pra_compre_2"-------
    # update component parameters for each repeat
    pra_img_pre_a2.setImage(img_pre_2)
    pra_img_ans4.setImage(img_ans_a_2)
    pra_img_ans5.setImage(img_ans_b_2)
    pra_img_ans6.setImage(img_ans_c_2)
    img_pre_4_m2.setImage(img_pre_22)
    img_tar_compre_1.setImage(img_tar_2)
    img_pre_4_m2.setAutoDraw(True)
    img_tar_compre_1.setAutoDraw(True)
    square_win1.setAutoDraw(True)
    
    key_resp_8.keys = []
    key_resp_8.rt = []
    # keep track of which components have finished
    pra_compre_2Components = [pra_img_pre_a2, pra_img_ans4, pra_img_ans5, pra_img_ans6, key_resp_8, text, text_6, text_7]
    for thisComponent in pra_compre_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pra_compre_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pra_compre_2"-------
    while continueRoutine:
        # get current time
        t = pra_compre_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pra_compre_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pra_img_pre_a2* updates
        if pra_img_pre_a2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_pre_a2.frameNStart = frameN  # exact frame index
            pra_img_pre_a2.tStart = t  # local t and not account for scr refresh
            pra_img_pre_a2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_pre_a2, 'tStartRefresh')  # time at next scr refresh
            pra_img_pre_a2.setAutoDraw(True)
        
        # *pra_img_ans4* updates
        if pra_img_ans4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_ans4.frameNStart = frameN  # exact frame index
            pra_img_ans4.tStart = t  # local t and not account for scr refresh
            pra_img_ans4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_ans4, 'tStartRefresh')  # time at next scr refresh
            pra_img_ans4.setAutoDraw(True)
        
        # *pra_img_ans5* updates
        if pra_img_ans5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_ans5.frameNStart = frameN  # exact frame index
            pra_img_ans5.tStart = t  # local t and not account for scr refresh
            pra_img_ans5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_ans5, 'tStartRefresh')  # time at next scr refresh
            pra_img_ans5.setAutoDraw(True)
        
        # *pra_img_ans6* updates
        if pra_img_ans6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pra_img_ans6.frameNStart = frameN  # exact frame index
            pra_img_ans6.tStart = t  # local t and not account for scr refresh
            pra_img_ans6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pra_img_ans6, 'tStartRefresh')  # time at next scr refresh
            pra_img_ans6.setAutoDraw(True)
        win1.flip()
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['u', 'j', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_8.keys = theseKeys.name  # just the last key pressed
                key_resp_8.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pra_compre_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pra_compre_2"-------
    for thisComponent in pra_compre_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('pra_img_pre_a2.started', pra_img_pre_a2.tStartRefresh)
    pratice.addData('pra_img_pre_a2.stopped', pra_img_pre_a2.tStopRefresh)
    pratice.addData('pra_img_ans4.started', pra_img_ans4.tStartRefresh)
    pratice.addData('pra_img_ans4.stopped', pra_img_ans4.tStopRefresh)
    pratice.addData('pra_img_ans5.started', pra_img_ans5.tStartRefresh)
    pratice.addData('pra_img_ans5.stopped', pra_img_ans5.tStopRefresh)
    pratice.addData('pra_img_ans6.started', pra_img_ans6.tStartRefresh)
    pratice.addData('pra_img_ans6.stopped', pra_img_ans6.tStopRefresh)
    img_pre_4_m2.setAutoDraw(False)
    img_tar_compre_1.setAutoDraw(False)
    square_win1.setAutoDraw(False)
    win1.flip()
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    pratice.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        pratice.addData('key_resp_8.rt', key_resp_8.rt)
    pratice.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    pratice.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    pratice.addData('text.started', text.tStartRefresh)
    pratice.addData('text.stopped', text.tStopRefresh)
    pratice.addData('text_6.started', text_6.tStartRefresh)
    pratice.addData('text_6.stopped', text_6.tStopRefresh)
    pratice.addData('text_7.started', text_7.tStartRefresh)
    pratice.addData('text_7.stopped', text_7.tStopRefresh)
    # the Routine "pra_compre_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [text_2]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratice.addData('text_2.started', text_2.tStartRefresh)
    pratice.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'pratice'


# ------Prepare to start Routine "Real_trial_instruction"-------
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
real_trial.setAutoDraw(True)
# keep track of which components have finished
Real_trial_instructionComponents = [text_10, key_resp_9]
for thisComponent in Real_trial_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Real_trial_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Real_trial_instruction"-------
while continueRoutine:
    # get current time
    t = Real_trial_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Real_trial_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_9.keys = theseKeys.name  # just the last key pressed
            key_resp_9.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    win1.flip()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Real_trial_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Real_trial_instruction"-------
for thisComponent in Real_trial_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
real_trial.setAutoDraw(False)
win1.flip()
# the Routine "Real_trial_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "webcam_check1"-------
# update component parameters for each repeat
video = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
webcam_check1Components = [Videomonitor1, key_resp_6, text_8]
for thisComponent in webcam_check1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
webcam_check1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "webcam_check1"-------
while continueRoutine:
    # get current time
    t = webcam_check1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=webcam_check1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Videomonitor1* updates
    if Videomonitor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Videomonitor1.frameNStart = frameN  # exact frame index
        Videomonitor1.tStart = t  # local t and not account for scr refresh
        Videomonitor1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Videomonitor1, 'tStartRefresh')  # time at next scr refresh
        Videomonitor1.setAutoDraw(True)
    returnVal, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)/255.0
    Videomonitor1.image = frame
    Videomonitor1.draw()
    win.flip()
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in webcam_check1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "webcam_check1"-------
for thisComponent in webcam_check1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Videomonitor1.started', Videomonitor1.tStartRefresh)
thisExp.addData('Videomonitor1.stopped', Videomonitor1.tStopRefresh)
video.release()


# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "webcam_check1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Stimuli_total_" + expInfo["Stimuli1"] + "_revised.csv"),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "perivew"-------
    # update component parameters for each repeat
    img_pv_1.setImage(preview)
    img_pre_1_m2.setImage(preview_2)
    img_pre_1_m2.setAutoDraw(True)
    ins_conf_2.setAutoDraw(True)
    key_resp_13.keys = []
    key_resp_13.rt = []
    # keep track of which components have finished
    perivewComponents = [img_pv_1, key_resp_13, text_18]
    for thisComponent in perivewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    perivewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "perivew"-------
    while continueRoutine:
        # get current time
        t = perivewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=perivewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_pv_1* updates
        if img_pv_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_pv_1.frameNStart = frameN  # exact frame index
            img_pv_1.tStart = t  # local t and not account for scr refresh
            img_pv_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_pv_1, 'tStartRefresh')  # time at next scr refresh
            img_pv_1.setAutoDraw(True)
        win1.flip()
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['y', 'n', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_13.keys = theseKeys.name  # just the last key pressed
                key_resp_13.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_13.keys == str(congruency)) or (key_resp_13.keys == congruency):
                    key_resp_13.corr = 1
                else:
                    key_resp_13.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in perivewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "perivew"-------
    for thisComponent in perivewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('img_pv_1.started', img_pv_1.tStartRefresh)
    trials.addData('img_pv_1.stopped', img_pv_1.tStopRefresh)
    img_pre_1_m2.setAutoDraw(False)
    ins_conf_2.setAutoDraw(False)
    win1.flip()
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
        # was no response the correct answer?!
        if str(congruency).lower() == 'none':
           key_resp_13.corr = 1;  # correct non-response
        else:
           key_resp_13.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_13.keys',key_resp_13.keys)
    trials.addData('key_resp_13.corr', key_resp_13.corr)
    if key_resp_13.keys != None:  # we had a response
        trials.addData('key_resp_13.rt', key_resp_13.rt)
    trials.addData('key_resp_13.started', key_resp_13.tStartRefresh)
    trials.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
    trials.addData('text_18.started', text_18.tStartRefresh)
    trials.addData('text_18.stopped', text_18.tStopRefresh)
    # the Routine "perivew" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "descri_1"-------
    # update component parameters for each repeat
    im_pre_a1.setImage(preview)
    img_tar_descri_1.setImage(target_path)
    key_resp.keys = []
    key_resp.rt = []
    img_pre_2_m2.setImage(preview_2)
    img_ans_1_a_m2.setImage(ans1_path)
    img_ans_1_b_m2.setImage(ans2_path)
    img_ans_1_c_m2.setImage(ans3_path)
    img_pre_2_m2.setAutoDraw(True)
    img_ans_1_a_m2.setAutoDraw(True)
    img_ans_1_b_m2.setAutoDraw(True)
    img_ans_1_c_m2.setAutoDraw(True)
    text_N.setAutoDraw(True)
    text_J.setAutoDraw(True)
    text_U.setAutoDraw(True)
    
    
    cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    path_video = 'F:\\Experiment\\SGPV2_Interaction\\SGPV_Communicative\\data\\' + expInfo['participant'] + '\\' + expInfo['participant'] + '_' + str(trial_num) + '_' + str(thisTrial['Item_number']) + '.avi'
    trial_num = trial_num + 1
    
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path_video,fourcc, 30.0, (1280,720))
    square_trails.setImage('Materials/square.png')
    # keep track of which components have finished
    descri_1Components = [im_pre_a1, img_tar_descri_1, key_resp, square_trails]
    for thisComponent in descri_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    descri_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "descri_1"-------
    while continueRoutine:
        # get current time
        t = descri_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=descri_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *im_pre_a1* updates
        if im_pre_a1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im_pre_a1.frameNStart = frameN  # exact frame index
            im_pre_a1.tStart = t  # local t and not account for scr refresh
            im_pre_a1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im_pre_a1, 'tStartRefresh')  # time at next scr refresh
            im_pre_a1.setAutoDraw(True)
        
        # *img_tar_descri_1* updates
        if img_tar_descri_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_tar_descri_1.frameNStart = frameN  # exact frame index
            img_tar_descri_1.tStart = t  # local t and not account for scr refresh
            img_tar_descri_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_tar_descri_1, 'tStartRefresh')  # time at next scr refresh
            img_tar_descri_1.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['u', 'j', 'n', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp.keys == str(Correct_ans)) or (key_resp.keys == Correct_ans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        ret, frame1 = cap.read()
        out.write(frame1)
        win1.flip()
        
        # *square_trails* updates
        if square_trails.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square_trails.frameNStart = frameN  # exact frame index
            square_trails.tStart = t  # local t and not account for scr refresh
            square_trails.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square_trails, 'tStartRefresh')  # time at next scr refresh
            square_trails.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in descri_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "descri_1"-------
    for thisComponent in descri_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('im_pre_a1.started', im_pre_a1.tStartRefresh)
    trials.addData('im_pre_a1.stopped', im_pre_a1.tStopRefresh)
    trials.addData('img_tar_descri_1.started', img_tar_descri_1.tStartRefresh)
    trials.addData('img_tar_descri_1.stopped', img_tar_descri_1.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(Correct_ans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    img_pre_2_m2.setAutoDraw(False)
    img_ans_1_a_m2.setAutoDraw(False)
    img_ans_1_b_m2.setAutoDraw(False)
    img_ans_1_c_m2.setAutoDraw(False)
    text_N.setAutoDraw(False)
    text_J.setAutoDraw(False)
    text_U.setAutoDraw(False)
    cap.release()
    out.release()
    del cap
    del out
    cv2.destroyAllWindows()
    win1.flip()
    
    trials.addData('square_trails.started', square_trails.tStartRefresh)
    trials.addData('square_trails.stopped', square_trails.tStopRefresh)
    # the Routine "descri_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [text_2]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Real_trial_instruction"-------
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
real_trial.setAutoDraw(True)
# keep track of which components have finished
Real_trial_instructionComponents = [text_10, key_resp_9]
for thisComponent in Real_trial_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Real_trial_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Real_trial_instruction"-------
while continueRoutine:
    # get current time
    t = Real_trial_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Real_trial_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_9.keys = theseKeys.name  # just the last key pressed
            key_resp_9.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    win1.flip()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Real_trial_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Real_trial_instruction"-------
for thisComponent in Real_trial_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
real_trial.setAutoDraw(False)
win1.flip()
# the Routine "Real_trial_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "webcam_check1"-------
# update component parameters for each repeat
video = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
webcam_check1Components = [Videomonitor1, key_resp_6, text_8]
for thisComponent in webcam_check1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
webcam_check1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "webcam_check1"-------
while continueRoutine:
    # get current time
    t = webcam_check1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=webcam_check1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Videomonitor1* updates
    if Videomonitor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Videomonitor1.frameNStart = frameN  # exact frame index
        Videomonitor1.tStart = t  # local t and not account for scr refresh
        Videomonitor1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Videomonitor1, 'tStartRefresh')  # time at next scr refresh
        Videomonitor1.setAutoDraw(True)
    returnVal, frame = video.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)/255.0
    Videomonitor1.image = frame
    Videomonitor1.draw()
    win.flip()
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in webcam_check1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "webcam_check1"-------
for thisComponent in webcam_check1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Videomonitor1.started', Videomonitor1.tStartRefresh)
thisExp.addData('Videomonitor1.stopped', Videomonitor1.tStopRefresh)
video.release()


# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "webcam_check1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Stimuli_total_" + expInfo["Stimuli2"] + "_revised.csv"),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "perivew"-------
    # update component parameters for each repeat
    img_pv_1.setImage(preview)
    img_pre_1_m2.setImage(preview_2)
    img_pre_1_m2.setAutoDraw(True)
    ins_conf_2.setAutoDraw(True)
    key_resp_13.keys = []
    key_resp_13.rt = []
    # keep track of which components have finished
    perivewComponents = [img_pv_1, key_resp_13, text_18]
    for thisComponent in perivewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    perivewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "perivew"-------
    while continueRoutine:
        # get current time
        t = perivewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=perivewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_pv_1* updates
        if img_pv_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_pv_1.frameNStart = frameN  # exact frame index
            img_pv_1.tStart = t  # local t and not account for scr refresh
            img_pv_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_pv_1, 'tStartRefresh')  # time at next scr refresh
            img_pv_1.setAutoDraw(True)
        win1.flip()
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['y', 'n', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_13.keys = theseKeys.name  # just the last key pressed
                key_resp_13.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp_13.keys == str(congruency)) or (key_resp_13.keys == congruency):
                    key_resp_13.corr = 1
                else:
                    key_resp_13.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in perivewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "perivew"-------
    for thisComponent in perivewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('img_pv_1.started', img_pv_1.tStartRefresh)
    trials_2.addData('img_pv_1.stopped', img_pv_1.tStopRefresh)
    img_pre_1_m2.setAutoDraw(False)
    ins_conf_2.setAutoDraw(False)
    win1.flip()
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
        # was no response the correct answer?!
        if str(congruency).lower() == 'none':
           key_resp_13.corr = 1;  # correct non-response
        else:
           key_resp_13.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_13.keys',key_resp_13.keys)
    trials_2.addData('key_resp_13.corr', key_resp_13.corr)
    if key_resp_13.keys != None:  # we had a response
        trials_2.addData('key_resp_13.rt', key_resp_13.rt)
    trials_2.addData('key_resp_13.started', key_resp_13.tStartRefresh)
    trials_2.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
    trials_2.addData('text_18.started', text_18.tStartRefresh)
    trials_2.addData('text_18.stopped', text_18.tStopRefresh)
    # the Routine "perivew" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "descri_1"-------
    # update component parameters for each repeat
    im_pre_a1.setImage(preview)
    img_tar_descri_1.setImage(target_path)
    key_resp.keys = []
    key_resp.rt = []
    img_pre_2_m2.setImage(preview_2)
    img_ans_1_a_m2.setImage(ans1_path)
    img_ans_1_b_m2.setImage(ans2_path)
    img_ans_1_c_m2.setImage(ans3_path)
    img_pre_2_m2.setAutoDraw(True)
    img_ans_1_a_m2.setAutoDraw(True)
    img_ans_1_b_m2.setAutoDraw(True)
    img_ans_1_c_m2.setAutoDraw(True)
    text_N.setAutoDraw(True)
    text_J.setAutoDraw(True)
    text_U.setAutoDraw(True)
    
    
    cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    path_video = 'F:\\Experiment\\SGPV2_Interaction\\SGPV_Communicative\\data\\' + expInfo['participant'] + '\\' + expInfo['participant'] + '_' + str(trial_num) + '_' + str(thisTrial['Item_number']) + '.avi'
    trial_num = trial_num + 1
    
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path_video,fourcc, 30.0, (1280,720))
    square_trails.setImage('Materials/square.png')
    # keep track of which components have finished
    descri_1Components = [im_pre_a1, img_tar_descri_1, key_resp, square_trails]
    for thisComponent in descri_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    descri_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "descri_1"-------
    while continueRoutine:
        # get current time
        t = descri_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=descri_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *im_pre_a1* updates
        if im_pre_a1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im_pre_a1.frameNStart = frameN  # exact frame index
            im_pre_a1.tStart = t  # local t and not account for scr refresh
            im_pre_a1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im_pre_a1, 'tStartRefresh')  # time at next scr refresh
            im_pre_a1.setAutoDraw(True)
        
        # *img_tar_descri_1* updates
        if img_tar_descri_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_tar_descri_1.frameNStart = frameN  # exact frame index
            img_tar_descri_1.tStart = t  # local t and not account for scr refresh
            img_tar_descri_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_tar_descri_1, 'tStartRefresh')  # time at next scr refresh
            img_tar_descri_1.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['u', 'j', 'n', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp.keys == str(Correct_ans)) or (key_resp.keys == Correct_ans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        ret, frame1 = cap.read()
        out.write(frame1)
        win1.flip()
        
        # *square_trails* updates
        if square_trails.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            square_trails.frameNStart = frameN  # exact frame index
            square_trails.tStart = t  # local t and not account for scr refresh
            square_trails.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(square_trails, 'tStartRefresh')  # time at next scr refresh
            square_trails.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in descri_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "descri_1"-------
    for thisComponent in descri_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('im_pre_a1.started', im_pre_a1.tStartRefresh)
    trials_2.addData('im_pre_a1.stopped', im_pre_a1.tStopRefresh)
    trials_2.addData('img_tar_descri_1.started', img_tar_descri_1.tStartRefresh)
    trials_2.addData('img_tar_descri_1.stopped', img_tar_descri_1.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(Correct_ans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp.keys',key_resp.keys)
    trials_2.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials_2.addData('key_resp.rt', key_resp.rt)
    trials_2.addData('key_resp.started', key_resp.tStartRefresh)
    trials_2.addData('key_resp.stopped', key_resp.tStopRefresh)
    img_pre_2_m2.setAutoDraw(False)
    img_ans_1_a_m2.setAutoDraw(False)
    img_ans_1_b_m2.setAutoDraw(False)
    img_ans_1_c_m2.setAutoDraw(False)
    text_N.setAutoDraw(False)
    text_J.setAutoDraw(False)
    text_U.setAutoDraw(False)
    cap.release()
    out.release()
    del cap
    del out
    cv2.destroyAllWindows()
    win1.flip()
    
    trials_2.addData('square_trails.started', square_trails.tStartRefresh)
    trials_2.addData('square_trails.stopped', square_trails.tStopRefresh)
    # the Routine "descri_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauseComponents = [text_2]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_2.started', text_2.tStartRefresh)
    trials_2.addData('text_2.stopped', text_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "End"-------
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
end_text.setAutoDraw(True)
# keep track of which components have finished
EndComponents = [text_14, key_resp_11]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_11.keys = theseKeys.name  # just the last key pressed
            key_resp_11.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    win1.flip()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
end_text.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
