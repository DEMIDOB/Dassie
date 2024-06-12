import random

import external_skills.external_skills_loader
import knowledge.lang_detector
import knowledge.static as knst
from builtin_skills import google_parse
from knowledge.request_context import RequestContext
from laugh.rec import is_laugh
import context


def _brain_main_context_handler(ctx, in_data):
    brain = in_data['brain']
    input_text = in_data['input_text']
    kwargs = in_data['kwargs']
    request_ctx = brain.analyze(input_text)
    brain.wanna_sleep = Brain.do_i_wanna_sleep(request_ctx)
    return brain.answer(request_ctx)


class Brain:
    threshold = 0.25

    def __init__(self, location="50,50"):
        self.location = location

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

    def analyze(self, input_text: str, reply_after_name=True):
        ctx = knowledge.lang_detector.create_language_request_context(input_text, self)

        input_lower = input_text.lower()
        input_no_punctuation_marks = ""

        # clear all the punctuation marks
        for c in input_lower:
            if c not in knst.punct_marks:
                input_no_punctuation_marks += c

        ctx.sentence = input_no_punctuation_marks.split()

        ctx.understood = False
        else_here = False

        for category in knst.categories + ctx.esl.categories:
            ctx.answer_logical[category] = False

        for else_word in ctx.kn.words["else_words"]:
            if else_word in ctx.sentence and len(self.last_else_cats) > 0:
                ctx.understood = True
                else_here = True

                for last_cat in self.last_else_cats:
                    ctx.answer_logical[last_cat] = True

                break

        if not else_here:
            self.last_else_cats = []

        if reply_after_name:
            while ctx.sentence and not Brain._word_in_category(ctx.sentence[0], "you_word", ctx.kn):
                ctx.sentence.pop(0)

            if ctx.sentence:
                ctx.sentence.pop(0)

            if not ctx.sentence:
                ctx.silent_response = True
                return ctx

        for category in knst.categories + ctx.esl.categories:
            for word in ctx.sentence:
                if Brain._word_in_category(word, category, ctx.kn):
                    ctx.answer_logical[category] = True

                    if category not in knst.service_cats:
                        ctx.understood = True

                    if category in knst.else_cates and category not in self.last_else_cats:
                        self.last_else_cats.append(category)
                elif is_laugh(word):
                    ctx.understood = True
                    ctx.answer_logical["laugh"] = True

        return ctx

    def answer(self, ctx: RequestContext) -> RequestContext:
        ret = ""
        print(ctx.understood, ctx.silent_response)

        if ctx.silent_response:
            return ctx

        if ctx.understood:
            for category in ctx.answer_logical:
                if ctx.answer_logical[category]:
                    if category in knst.actions:
                        ret += knst.actions[category](ctx)
                    elif category in ctx.esl.actions:
                        ret += ctx.esl.actions[category](ctx)
        # TODO:  google, and if this is not succeeded, tell user that i do not understand his request
        else:
            req = ""
            for word in ctx.sentence:
                if word not in ctx.kn.words["who_word"]:
                    req += f" {word}"

            ret = google_parse.parse(req)
            if len(ret) > 2:
                ctx.understood = True

        if not ctx.understood:
            ret = random.choice(ctx.kn.answers["dont_understand"])

        ctx.response = ret
        return ctx

    @staticmethod
    def do_i_wanna_sleep(ctx: RequestContext):
        for sleep_category in knst.sleep_categories:
            if ctx.answer_logical[sleep_category]:
                return True
        return False


if __name__ == '__main__':
    b = Brain()
    while not b.wanna_sleep:
        reply = b.give_answer(input(">> "))
        print(reply.response)
