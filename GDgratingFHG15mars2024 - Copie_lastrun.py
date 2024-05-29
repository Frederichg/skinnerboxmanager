#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on mars 22, 2024, at 16:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
#To set up each box change the line 8 for the right path
#Also change the name of the Log file by editing line 10

import GPIO4

exp = data.ExperimentHandler(name="OUT", version='',
    extraInfo=None, runtimeInfo=None,
    originPath='C:\\Users\\pfh3221\\OneDrive - Université de Moncton\\Documents\\GitHub2\\skinnerboxmanager',
    savePickle=False, saveWideText=True,
    dataFileName="OUT1")


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\pfh3221\\OneDrive - Université de Moncton\\Documents\\GitHub2\\skinnerboxmanager\\GDgratingFHG15mars2024 - Copie_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='cover',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "delay_sart" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='WAIT',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "start" ---
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1), sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
aperture = visual.Aperture(
    win=win, name='aperture',
    units='norm', size=[1], pos=[0,0], ori=0.0,
    shape='circle', anchor='center'
    ,depth=-2
)
aperture.disable()  # disable until its actually used
# Set experiment start values for variable component nOmission
nOmission = 1
nOmissionContainer = []
# Set experiment start values for variable component mousePos
mousePos = ''
mousePosContainer = []
# Run 'Begin Experiment' code from code
clock = core.Clock()

def log(event:str):  #This is where the time stamps for each event is setted
    exp.addData('time', clock.getTime())
    exp.addData('event', event)
    exp.nextEntry()
    
log('START')

# --- Initialize components for Routine "Show_conditions" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Presentation" ---
Stim_presentation = visual.Aperture(
    win=win, name='Stim_presentation',
    units='norm', size=[0], pos=(0, 0), ori=0.0,
    shape='circle', anchor='center'
    ,depth=0
)
Stim_presentation.disable()  # disable until its actually used

# --- Initialize components for Routine "omission" ---
text_omission = visual.TextStim(win=win, name='text_omission',
    text='\n\n\n\n\n\n\n\n\n\nomission',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ITI" ---
ITI_delay = visual.TextStim(win=win, name='ITI_delay',
    text='\n\n\n\n\n\n\n\nITI',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "delay_sart" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
delay_sartComponents = [text_4]
for thisComponent in delay_sartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "delay_sart" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # if text_4 is stopping this frame...
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            # update status
            text_4.status = FINISHED
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in delay_sartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "delay_sart" ---
for thisComponent in delay_sartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('data.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "start" ---
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code
    mouse.setPos((0,-1))
    nOmission = 1 #par défaut omission sauf si l'animal donne une réponse
    
    log('Response L/R: ' + str(responses))
    log('Spatial Freq: ' + str(SF))
    
    if responses:
        circlePos = 0.5
    else:
        circlePos = -0.5
    # keep track of which components have finished
    startComponents = [mouse, grating, aperture]
    for thisComponent in startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse is stopping this frame...
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse.stopped', t)
                # update status
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(grating, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # *grating* updates
        
        # if grating is starting this frame...
        if grating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grating.frameNStart = frameN  # exact frame index
            grating.tStart = t  # local t and not account for scr refresh
            grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grating, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grating.started')
            # update status
            grating.status = STARTED
            grating.setAutoDraw(True)
        
        # if grating is active this frame...
        if grating.status == STARTED:
            # update params
            grating.setSF(SF, log=False)
        
        # if grating is stopping this frame...
        if grating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > grating.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                grating.tStop = t  # not accounting for scr refresh
                grating.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'grating.stopped')
                # update status
                grating.status = FINISHED
                grating.setAutoDraw(False)
        
# *aperture* updates
        
        # if aperture is starting this frame...
        if aperture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            aperture.frameNStart = frameN  # exact frame index
            aperture.tStart = t  # local t and not account for scr refresh
            aperture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(aperture, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'aperture.started')
            # update status
            aperture.status = STARTED
            aperture.enabled = True
        
        # if aperture is stopping this frame...
        if aperture.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > aperture.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                aperture.tStop = t  # not accounting for scr refresh
                aperture.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'aperture.stopped')
                # update status
                aperture.status = FINISHED
                aperture.enabled = False
        if aperture.status == STARTED:  # only update if being  drawn
            aperture.setPos((responses - 0.5, 0), log=False)
        # Run 'Each Frame' code from code
        if mouse.getPos()[0] != 0:
            continueRoutine = False
            nOmission = 0
            if (mouse.getPos()[0] > 0 and responses == 1) or (mouse.getPos()[0] < 0 and responses == 0):
                log('Good')
                GPIO4.send("FDR") #Envoie la commande au arduino pour une récompense
                log('Reward')
                nOmission = 0
                
        #        IR = GPIO4.receive_data()
        #        if IR is not None:
        #             while GPIO4.send(IR, True) != "1" or GPIO4.send(IR, True) != 1: 
        #             #continue
        #                 log('IR')
                     
            elif mouse.getPos()[0] != 0:
                nOmission = 0
        else:
            nOmission = 1 #donc si l'animal ne répond pas = Omission
        
        
        
        
        
        
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start" ---
    for thisComponent in startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('mouse.x', mouse.x)
    trials_4.addData('mouse.y', mouse.y)
    trials_4.addData('mouse.leftButton', mouse.leftButton)
    trials_4.addData('mouse.midButton', mouse.midButton)
    trials_4.addData('mouse.rightButton', mouse.rightButton)
    trials_4.addData('mouse.time', mouse.time)
    trials_4.addData('mouse.clicked_name', mouse.clicked_name)
    aperture.enabled = False  # just in case it was left enabled
    # Run 'End Routine' code from code
    if mouse.getPos()[0] == 0:
        nOmission = 1 #pas 100% certain de la logique mais ça fonctionne
                       #si l'animal n'a pas bougé la souris la routine termine et
                       #on log une omission
        
        log('End Omission')
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Show_conditions" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_3.setText('\n\n\n\n\n\n$str(SF)')
    # keep track of which components have finished
    Show_conditionsComponents = [text_3]
    for thisComponent in Show_conditionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Show_conditions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Show_conditionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Show_conditions" ---
    for thisComponent in Show_conditionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Presentation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    PresentationComponents = [Stim_presentation]
    for thisComponent in PresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Presentation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
# *Stim_presentation* updates
        
        # if Stim_presentation is starting this frame...
        if Stim_presentation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stim_presentation.frameNStart = frameN  # exact frame index
            Stim_presentation.tStart = t  # local t and not account for scr refresh
            Stim_presentation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stim_presentation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Stim_presentation.started')
            # update status
            Stim_presentation.status = STARTED
            Stim_presentation.enabled = True
        
        # if Stim_presentation is stopping this frame...
        if Stim_presentation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stim_presentation.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Stim_presentation.tStop = t  # not accounting for scr refresh
                Stim_presentation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_presentation.stopped')
                # update status
                Stim_presentation.status = FINISHED
                Stim_presentation.enabled = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Presentation" ---
    for thisComponent in PresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Stim_presentation.enabled = False  # just in case it was left enabled
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=nOmission, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "omission" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        omissionComponents = [text_omission]
        for thisComponent in omissionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "omission" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_omission* updates
            
            # if text_omission is starting this frame...
            if text_omission.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_omission.frameNStart = frameN  # exact frame index
                text_omission.tStart = t  # local t and not account for scr refresh
                text_omission.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_omission, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_omission.started')
                # update status
                text_omission.status = STARTED
                text_omission.setAutoDraw(True)
            
            # if text_omission is active this frame...
            if text_omission.status == STARTED:
                # update params
                pass
            
            # if text_omission is stopping this frame...
            if text_omission.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_omission.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_omission.tStop = t  # not accounting for scr refresh
                    text_omission.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_omission.stopped')
                    # update status
                    text_omission.status = FINISHED
                    text_omission.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in omissionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "omission" ---
        for thisComponent in omissionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed nOmission repeats of 'trials_3'
    
    # get names of stimulus parameters
    if trials_3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_3.trialList[0].keys()
    # save data for this loop
    trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_delay]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_delay* updates
        
        # if ITI_delay is starting this frame...
        if ITI_delay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_delay.frameNStart = frameN  # exact frame index
            ITI_delay.tStart = t  # local t and not account for scr refresh
            ITI_delay.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_delay, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_delay.started')
            # update status
            ITI_delay.status = STARTED
            ITI_delay.setAutoDraw(True)
        
        # if ITI_delay is active this frame...
        if ITI_delay.status == STARTED:
            # update params
            pass
        
        # if ITI_delay is stopping this frame...
        if ITI_delay.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_delay.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ITI_delay.tStop = t  # not accounting for scr refresh
                ITI_delay.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_delay.stopped')
                # update status
                ITI_delay.status = FINISHED
                ITI_delay.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'

# get names of stimulus parameters
if trials_4.trialList in ([], [None], None):
    params = []
else:
    params = trials_4.trialList[0].keys()
# save data for this loop
trials_4.saveAsExcel(filename + '.xlsx', sheetName='trials_4',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
# Run 'End Experiment' code from code
log('END')

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
