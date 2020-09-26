class ContextExecutable:
    def __init__(self, stepsNum, executors=[], initStep=0):
        self.stepsNum = stepsNum
        self._ready = False
        self._executors = executors
        if len(executors) == stepsNum:
            self._ready = True
        self.step = initStep
        self.hasFinished = False


    def addExecutor(self, executor):
        if not self.isReady():
            self._executors.append(executor)
            if len(self._executors) == self.stepsNum:
                self._ready = True


    def isReady(self):
        return self._ready and len(self._executors) == self.stepsNum


    def allowNextStep(self):
        if self.step < self.stepsNum and self.isReady():
            self.step += 1
            return True
        return False


    def executeStep(self, **kwargs):
        '''

        Executes a handler for the current status.
        Handler is a function provided by the class user, recieves the context object and inputData.
        If the context is not _ready, returns None

        :param inputData: any data sent by the class user, preferably: a tuple
        :return:          any data returned by the executor function, preferably: a tuple

        '''
        if not self.isReady():
            raise Exception(f"The executors are not ready yet!\nYou have {len(self._executors)} executors of required {self.stepsNum}")

        if self.step >= self.stepsNum:
            self.hasFinished = True
            return "Context has finished executing"

        return self._executors[self.step](self, kwargs)


if __name__ == "__main__":
    def s0(ctx: ContextExecutable, arg):
        print(arg)
        ctx.allowNextStep()
        return "I'm done"

    def s1(ctx: ContextExecutable, arg):
        print(arg)
        ctx.allowNextStep()

    c = ContextExecutable(2)
    c.addExecutor(s0)
    c.addExecutor(s1)

    print(c.executeStep(someString='тут строка кароч', two=2))
    print(c.executeStep())
    print(c.executeStep())

