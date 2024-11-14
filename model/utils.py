HM_PATH = "/data/frederick"   # change this line to your specified path to NoT repository.

def read_demonstration(demonstration_path):
    if demonstration_path is None:
        return None
    with open(demonstration_path, "r") as f:
        demonstration = f.read()
    return demonstration

def sample_demonstrations(demonstration, n_shot):
    demonstrations = [x.strip() for x in demonstration.split("# END")][:-1]
    return "\n# END\n\n".join(demonstrations[:n_shot])+ "\n# END\n\n"

def stagger_demonstrations(demonstration):
    demonstrations = [x.strip() for x in demonstration.split("# END")][:-1]
    staggered_demonstrations = []
    for x in demonstrations:
        user_input, assistant_input = x.split("def get_relations(self):")
        user_input = user_input.strip()+ "\n\n    def get_relations(self):\n        #TODO\n# END"
        assistant_input = "def get_relations(self):\n        " + assistant_input.strip() + "\n# END"
        staggered_demonstrations.append((user_input, assistant_input))
    return staggered_demonstrations

def stagger_demonstrations_NoT(demonstration):
    demonstrations = [x.strip() for x in demonstration.split("# END")][:-1]
    staggered_demonstrations = []
    for x in demonstrations:
        user_input, assistant_input = x.split("def get_narrative(self):")
        user_input = user_input.strip()+ "\n    def get_narrative(self):\n        #TODO\n\n    def get_relations(self):\n        #TODO\n# END"
        assistant_input = "    #Let's think of a narrative to link aforementioned events in the correct temporal order.\n    def get_narrative(self):\n        " + assistant_input.strip() + "\n# END"
        staggered_demonstrations.append((user_input, assistant_input))
    return staggered_demonstrations

def convert_data_to_program(scenario, events, camelCase=False):
    scenario_CamelCase= "".join([x.capitalize() for x in scenario.split()])
    title = scenario
    steps = len(events)
    return_obj = "class {scenario_CamelCase}:\n\n    title = \"{title}\"\n    steps = {steps}\n\n".format(scenario_CamelCase=scenario_CamelCase, title=title, steps=steps)
    for k, v in events.items():
        if camelCase:
            return_obj += "    def {i}(self):\n        return \"{event}\"\n\n".format(i=k, event=v)
        else:
            return_obj += "    def step{i}(self):\n        return \"{event}\"\n\n".format(i=k, event=v)
    return_obj += "    def get_relations(self):\n        #TODO\n# END"
    return return_obj

def convert_data_to_program_CoT(scenario, events, camelCase=False):
    scenario_CamelCase= "".join([x.capitalize() for x in scenario.split()])
    title = scenario
    steps = len(events)
    return_obj = "class {scenario_CamelCase}:\n\n    title = \"{title}\"\n    steps = {steps}\n\n".format(scenario_CamelCase=scenario_CamelCase, title=title, steps=steps)
    for k, v in events.items():
        if camelCase:
            return_obj += "    def {i}(self):\n        return \"{event}\"\n\n".format(i=k, event=v)
        else:
            return_obj += "    def step{i}(self):\n        return \"{event}\"\n\n".format(i=k, event=v)
    return_obj += "    #Let's think step by step.\n    def get_relations(self):\n        #TODO\n# END"
    return return_obj 

def convert_data_to_program_NoT(scenario, events, camelCase=False):
    scenario_CamelCase= "".join([x.capitalize() for x in scenario.split()])
    title = scenario
    steps = len(events)
    return_obj = "class {scenario_CamelCase}:\n\n    title = \"{title}\"\n    steps = {steps}\n\n".format(scenario_CamelCase=scenario_CamelCase, title=title, steps=steps)
    for k, v in events.items():
        if camelCase:
            return_obj += "    def {i}(self):\n        return \"{event}\"\n\n".format(i=k, event=v)
        else:
            return_obj += "    def step{i}(self):\n        return \"{event}\"\n\n".format(i=k, event=v)
    return_obj += "    #Let's think of a narrative to link aforementioned events in the correct temporal order.\n    def get_narrative(self):\n        #TODO\n\n    def get_relations(self):\n        #TODO\n# END"
    return return_obj


def parse_response(response):
    return [x.strip().replace("\"","") for x in response[response.find("get_relations(self):") + len("get_relations(self):") + response[response.find("get_relations(self):") + len("get_relations(self):"):].find("["):    
                                                         response.find("get_relations(self):") + len("get_relations(self):") + response[response.find("get_relations(self):") + len("get_relations(self):"):].find("]")]
                                                         .replace("return", "").replace("[","").strip().split(",") if x.strip() != ""]


