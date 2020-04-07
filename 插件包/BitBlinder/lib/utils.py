import json
import os

class URL(object):
    PARAM_URL = 0
    PARAM_BODY = 1
    PARAM_COOKIE = 2
    PARAM_XML = 3
    PARAM_XML_ATTR = 4
    PARAM_MULTIPART_ATTR = 5
    PARAM_JSON = 6

class Helpers(object):

    def get_payloads(self):

        return (self.payloads_list.getText().replace(" ","%20")).split("\n")

    def save_settings(self, evnt):

        config = {'isEnabled': 0, 'Randomize': 0, 'Payloads': []}
        config['isEnabled'] = self.enable.isSelected()
        config['Randomize'] = self.randomize.isSelected()

        for payload in self.get_payloads():
            config['Payloads'].append(payload)

        f = open("./config.json", "w") 
        f.write(json.dumps(config))
        f.close() # For some reason jython doesn't close the file without this line

        print("[~] Settings saved")
        return

    def load_settings(self):

        # Check if there's saved config if true then load it
        if os.path.isfile('./config.json'):

            f = open("./config.json", "r")
            config = json.loads(f.read())
            f.close() # For some reason jython doesn't close the file without this line

            self.enable.setSelected(config['isEnabled'])
            self.randomize.setSelected(config['Randomize'])
            self.payloads_list.setText('\n'.join(config['Payloads']))

            print("[~] Settings loaded")

        return
