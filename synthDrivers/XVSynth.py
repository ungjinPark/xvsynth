﻿# coding: utf-8
# ver 0.2.1

import math
import speech
import synthDriverHandler, os, config, re, logging
from logHandler import log
from synthDriverHandler import SynthDriver, VoiceInfo, BooleanSynthSetting
import languageHandler
from collections import OrderedDict
from _XVSynth import xvEngine
from comtypes.client import CreateObject




class SynthDriver(synthDriverHandler.SynthDriver):
 supportedSettings = [SynthDriver.PitchSetting(), SynthDriver.RateSetting(), SynthDriver.VolumeSetting()]

# supportedSettings=(SynthDriver.VoiceSetting(),SynthDriver.VariantSetting(),SynthDriver.RateSetting(), SynthDriver.PitchSetting(), SynthDriver.InflectionSetting(), SynthDriver.VolumeSetting())
 description = 'SenseReader Synth'
 name = 'XVSynth'
 speakingLanguage=""
 @classmethod
 def check(cls):
  try:
   obj = CreateObject('SenseReader.Application')
   return True
  except:
   return False

 def __init__(self):
  self.xv = xvEngine()
  lang = languageHandler.getLanguage()
  self.speakingLanguage=lang

 def speak(self,speechSequence):
  try:
   for item in speechSequence:
    if isinstance(item, basestring):
     self.xv.ctrl.Speak(item, self.xv.si)
  except:
   pass

 def speakText(self, test, index=None):
  try:
   if isinstance(text, basestring):
    self.xv.ctrl.Speak(text, self.xv.si)
  except:
   pass

 def pause(self,switch):
  try:
   if not self.xv.ctrl.Speaking: return
   self.xv.ctrl.Stop()
  except:
   pass
 def cancel(self):
  try:
   if not self.xv.ctrl.Speaking: return
   self.xv.ctrl.Stop()
  except:
   pass

 def _get_rate(self):
  try:
   return self.xv.si.Speed * 5
  except:
   pass


 def _set_rate(self, vl):
  try:
   self.xv.si.Speed = int(math.ceil(vl * 0.2))
  except:
   pass
 


 def _get_volume(self):
  try:
   return self.xv.si.Volume * 5
  except:
   pass


 def _set_volume(self, vl):
  try:
   self.xv.si.Volume = int(math.ceil(vl * 0.2))
  except:
   pass



 def _get_pitch(self):
  try:
   return self.xv.si.Pitch * 5
  except:
   pass


 def _set_pitch(self, vl):
  try:
   self.xv.si.Pitch = int(math.ceil(vl * 0.2))
  except:
   pass
