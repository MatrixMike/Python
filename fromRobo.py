class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        # put initialization code here
        pass

    def onUnload(self):
        # put clean-up code here
        pass

    def onInput_onStart(self):
        ttsProxy = ALProxy("ALTextToSpeech")
        ttsProxy.say("Hello, I am a Robot")
#       print("hello Mike 2")
#       x = self.getparameter("x")
#      y = self.getparameter("y")
#      amountToTurn = math.atan2(y,x)
#      amountToWalk = math.sqrt(x * x + y * y)
        # self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload()
    # it is recommended to reuse the clean-up as the box is stopped
        self.onStopped()  # activate the output of the box]]></content>
