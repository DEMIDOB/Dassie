import external_skills.external_skills_loader


class RequestContext:
    def __init__(self, input_text, brain, answer_logical: dict, sentence: list[str], kn, lang_code=""):
        self.input_text = input_text
        self.brain = brain
        self.answer_logical = answer_logical
        self.sentence = sentence
        self.kn = kn
        self.lang_code = lang_code

        self.silent_response = False
        self.response = ""
        self.understood = False
        self.esl = external_skills.external_skills_loader.ExternalSkillsLoader(ctx=self)

    def __str__(self):
        return self.response
