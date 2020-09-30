import random

import knowledge.lang_detector
import knowledge.static as knst
from laugh.rec import isLaugh
import context


def _brain_main_context_handler(ctx, in_data):
    brain = in_data['brain']
    input_text = in_data['input_text']
    kwargs = in_data['kwargs']
    answer_logical, sentence, kn = brain.analyze(input_text)
    brain.wanna_sleep = brain.do_i_wanna_sleep(answer_logical)
    return brain.answer(answer_logical, input_text=input_text, sentence=sentence, kn=kn, brain=brain)


class Brain:
    def __init__(self, location="50,50"):
        self.location = location

        self.understood = False
        self.wanna_sleep = False

        self.last_else_cats = []

        self.contexts = []
        self.contexts.append(context.ContextExecutable(1, [_brain_main_context_handler, ]))

    def give_answer(self, input_text):
        return self.contexts[-1].executeStep(brain=self, input_text=input_text, kwargs={})

    def analyze(self, input_text: str):
        kn = knowledge.lang_detector.detect(input_text)

        input_lower = input_text.lower()
        input_no_punct_marks = ""

        # clear all the punctuation marks
        for c in input_lower:
            if c not in knst.punct_marks:
                input_no_punct_marks += c

        sentence = input_no_punct_marks.split()

        answer = ""
        self.understood = False
        else_here = False

        answer_logical = {}

        for category in knst.categories:
            answer_logical[category] = False

        for else_word in kn.words["else_words"]:
            if else_word in sentence and len(self.last_else_cats) > 0:
                self.understood = True
                else_here = True

                for last_cat in self.last_else_cats:
                    answer_logical[last_cat] = True

                break

        if not else_here:
            self.last_else_cats = []

        for category in knst.categories:
            for word in sentence:
                if word in kn.words[category]:
                    answer_logical[category] = True

                    if category not in knst.service_cates:
                        self.understood = True

                    if category in knst.else_cates and category not in self.last_else_cats:
                        self.last_else_cats.append(category)
                elif isLaugh(word):
                    self.understood = True
                    answer_logical["laugh"] = True

        return answer_logical, sentence, kn


    def answer(self, answer_logical, **kwargs):
        ret = ""

        kn = kwargs['kn']

        if self.understood:
            for category in answer_logical:
                if answer_logical[category]:
                    ret += knst.actions[category](answer_logical, kwargs)
        # TODO:  google, and if this is not succeeded, tell user that i do not understand his request
        elif not self.understood:
            ret = random.choice(kn.answers["dont_understand"])

        return ret

    def do_i_wanna_sleep(self, answer_logical):
        for sleep_category in knst.sleep_categories:
            if answer_logical[sleep_category]:
                return True
        return False


if __name__ == '__main__':
    b = Brain()
    while not b.wanna_sleep:
        reply = b.give_answer(input(">> "))
        print(reply)
