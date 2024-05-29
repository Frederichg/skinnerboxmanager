#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on mars 07, 2024, at 15:03
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
    originPath='C:\\Users\\pfh3221\\OneDrive - Université de Moncton\\Documents\\GitHub2\\skinnerboxmanager\\GDgratingFHG1mars2024.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
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

# --- Initialize components for Routine "start" ---
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
grating = visual.GratingStim(
    win=win, name='grating',
    tex='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1), sf=10.0, phase=0.0,
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
# Set experiment start values for variable component nOmition
nOmition = 1
nOmitionContainer = []
# Set experiment start values for variable component mousePos
mousePos = ''
mousePosContainer = []
# Run 'Begin Experiment' code from code
clock = core.Clock()

def log(event:str):
    exp.addData('time', clock.getTime())
    exp.addData('event', event)
    exp.nextEntry()
    
log('START')

# --- Initialize components for Routine "delay" ---
aperture_2 = visual.Aperture(
    win=win, name='aperture_2',
    units='norm', size=[0], pos=(0, 0), ori=0.0,
    shape='circle', anchor='center'
    ,depth=0
)
aperture_2.disable()  # disable until its actually used

# --- Initialize components for Routine "omition" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='omition',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
ITI = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('data.xlsx'),
    seed=None, name='ITI')
thisExp.addLoop(ITI)  # add the loop to the experiment
thisITI = ITI.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisITI.rgb)
if thisITI != None:
    for paramName in thisITI:
        exec('{} = thisITI[paramName]'.format(paramName))

for thisITI in ITI:
    currentLoop = ITI
    # abbreviate parameter names if possible (e.g. rgb = thisITI.rgb)
    if thisITI != None:
        for paramName in thisITI:
            exec('{} = thisITI[paramName]'.format(paramName))
    
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
    nOmition = 1
    
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
            pass
        
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
        #log('Response: ' + str(responses))
        if mouse.getPos()[0] != 0:
            log('Response: ' + str(responses))
            continueRoutine = False
            if (mouse.getPos()[0] > 0 and responses == 1) or (mouse.getPos()[0] < 0 and responses == 0):
                log('Good')
                GPIO4.send("FDR")
                log('FDR')
                
        #        IR = GPIO4.receive_data()
        #        if IR is not None:
        #             while GPIO4.send(IR, True) != "1" or GPIO4.send(IR, True) != 1: 
        #             #continue
        #                 log('IR')
                     
            elif mouse.getPos()[0] != 0:
                log('Bad')
            nOmition = 0
            log('Omition')
        
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
    # store data for ITI (TrialHandler)
    ITI.addData('mouse.x', mouse.x)
    ITI.addData('mouse.y', mouse.y)
    ITI.addData('mouse.leftButton', mouse.leftButton)
    ITI.addData('mouse.midButton', mouse.midButton)
    ITI.addData('mouse.rightButton', mouse.rightButton)
    ITI.addData('mouse.time', mouse.time)
    ITI.addData('mouse.clicked_name', mouse.clicked_name)
    aperture.enabled = False  # just in case it was left enabled
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "delay" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    delayComponents = [aperture_2]
    for thisComponent in delayComponents:
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
    
    # --- Run Routine "delay" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
# *aperture_2* updates
        
        # if aperture_2 is starting this frame...
        if aperture_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            aperture_2.frameNStart = frameN  # exact frame index
            aperture_2.tStart = t  # local t and not account for scr refresh
            aperture_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(aperture_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'aperture_2.started')
            # update status
            aperture_2.status = STARTED
            aperture_2.enabled = True
        
        # if aperture_2 is stopping this frame...
        if aperture_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > aperture_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                aperture_2.tStop = t  # not accounting for scr refresh
                aperture_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'aperture_2.stopped')
                # update status
                aperture_2.status = FINISHED
                aperture_2.enabled = False
        
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
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "delay" ---
    for thisComponent in delayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    aperture_2.enabled = False  # just in case it was left enabled
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=nOmition, method='random', 
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
        
        # --- Prepare to start Routine "omition" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        omitionComponents = [text_3]
        for thisComponent in omitionComponents:
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
        
        # --- Run Routine "omition" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 25.0:
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
                if tThisFlipGlobal > text_3.tStartRefresh + 25-frameTolerance:
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
            for thisComponent in omitionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "omition" ---
        for thisComponent in omitionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-25.000000)
        thisExp.nextEntry()
        
    # completed nOmition repeats of 'trials_3'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'ITI'

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
