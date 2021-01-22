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
    brain.wanna_sleep = Brain.do_i_wanna_sleep(answer_logical)
    return brain.answer(answer_logical, input_text=input_text, sentence=sentence, kn=kn, brain=brain, ctx=ctx), \
           kn.lang_code


class Brain:
    threshold = 0.25

    def __init__(self, location="50,50"):
        self.location = location

        self.understood = False
        self.wanna_sleep = False

        self.last_else_cats = []

        self.contexts = []
        self.contexts.append(context.ContextExecutable(1, [_brain_main_context_handler, ]))

    def give_answer(self, input_text):
        return self.contexts[-1].execute_step(brain=self, input_text=input_text, kwargs={})

    @staticmethod
    def _lev(str1, str2):
        mts = [[i + j for j in range(len(str1) + 1)] for i in range(len(str2) + 1)]
        for r in range(1, len(str2) + 1):
            for c in range(1, len(str1) + 1):
                if not str1[c - 1] == str2[r - 1]:
                    mts[r][c] = min(mts[r - 1][c], mts[r - 1][c - 1], mts[r][c - 1]) + 1
                else:
                    mts[r][c] = mts[r - 1][c - 1]
        return mts[-1][-1]

    @staticmethod
    def _word_in_category(word, category, kn):
        for w in kn.words[category]:
            dst = Brain._lev(word, w)
            if dst / len(w) <= Brain.threshold:
                return True
        return False

    def analyze(self, input_text: str):
        kn = knowledge.lang_detector.detect(input_text)

        input_lower = input_text.lower()
        input_no_punctuation_marks = ""

        # clear all the punctuation marks
        for c in input_lower:
            if c not in knst.punct_marks:
                input_no_punctuation_marks += c

        sentence = input_no_punctuation_marks.split()

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
                if Brain._word_in_category(word, category, kn):
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

    @staticmethod
    def do_i_wanna_sleep(answer_logical):
        for sleep_category in knst.sleep_categories:
            if answer_logical[sleep_category]:
                return True
        return False


if __name__ == '__main__':
    b = Brain()
    while not b.wanna_sleep:
        reply = b.give_answer(input(">> "))
        print(reply)
