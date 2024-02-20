class ContextExecutable:
    def __init__(self, steps_num, executors=None, init_step=0):
        if executors is None:
            executors = []

        self.steps_num = steps_num
        self._ready = False
        self._executors = executors
        if len(executors) == steps_num:
            self._ready = True
        self.step = init_step
        self.has_finished = False

    def add_executor(self, executor):
        if not self.is_ready():
            self._executors.append(executor)
            if len(self._executors) == self.steps_num:
                self._ready = True

    def is_ready(self):
        return self._ready and len(self._executors) == self.steps_num

    def allow_next_step(self):
        if self.step < self.steps_num and self.is_ready():
            self.step += 1
            return True
        return False

    def execute_step(self, **kwargs):
        """

        Executes a handler for the current status.
        Handler is a function provided by the class user, recieves the context object and inputData.
        If the context is not _ready, returns None

        :param inputData: any data sent by the class user, preferably: a tuple
        :return:          any data returned by the executor function, preferably: a tuple

        """
        if not self.is_ready():
            raise Exception(
                f"The executors are not ready yet!\nYou have {len(self._executors)} executors of required {self.steps_num}")

        if self.step >= self.steps_num:
            self.has_finished = True
            return "Context has finished executing"

        return self._executors[self.step](self, kwargs)


if __name__ == "__main__":
    def s0(ctx: ContextExecutable, arg):
        print(arg)
        ctx.allow_next_step()
        return "I'm done"


    def s1(ctx: ContextExecutable, arg):
        print(arg)
        ctx.allow_next_step()


    c = ContextExecutable(2)
    c.add_executor(s0)
    c.add_executor(s1)

    print(c.execute_step(someString='тут строка кароч', two=2))
    print(c.execute_step())
    print(c.execute_step())
