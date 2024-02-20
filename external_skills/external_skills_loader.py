import os.path
import sys

# from knowledge.request_context import RequestContext


class ExternalSkillsLoader:
    def __init__(self, path="external_skills", ctx=None):
        if ctx is None:
            print("ctx not provided")
            return

        self.categories = []
        self.triggers = {}
        self.actions = {}

        if os.path.exists(path):
            for filename in os.listdir(path):
                if filename.endswith("skill.py"):
                    skill = __import__(path + "." + filename[:-3]).test_skill
                    if "triggers" in dir(skill) and "actions" in dir(skill) and "categories" in dir(skill):
                        for category in skill.categories:
                            if category not in skill.triggers or category not in skill.actions:
                                continue

                            if ctx.lang_code not in skill.triggers[category]:
                                continue

                            self.categories.append(category)
                            self.triggers[category] = skill.triggers[category][ctx.lang_code]
                            self.actions[category] = skill.actions[category]

                            ctx.kn.words[category] = skill.triggers[category][ctx.lang_code]
