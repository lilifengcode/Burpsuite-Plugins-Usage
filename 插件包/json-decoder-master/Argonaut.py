# Burp Extension - Argonaut
# Copyright : Michal Melewski <michal.melewski@gmail.com>

# Process all request parameters
# and try to find if they are echoed back in response

# Version 0.4
# Transformations finally working

# Version 0.3
# Parsing moved to separate class

# Version 0.2
# Small fix due to NullPointerException


# Burp imports
from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from burp import IParameter

# Java imports
from javax.swing import JTable
from javax.swing import JScrollPane
from javax.swing.table import AbstractTableModel

# Python imports
from urllib import unquote

# Consts
MIN_PARAM_LEN = 3

## Transformations tables
TRANSFORMATIONS = [
    { "name": "plain", "table": []},
    { "name": "jinja", "table": [
      ('&', '&amp;'),
      ('<', '&lt;'),
      ('>', '&gt;'),
      ('"', '&#34;'),
      ('\'', '&#39;')]
    },
  ]


class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
  def registerExtenderCallbacks(self, callbacks):
    self._callbacks = callbacks
    self._helpers = callbacks.getHelpers()

    callbacks.setExtensionName('Argonaut')    
    callbacks.registerMessageEditorTabFactory(self)

    return

  def createNewInstance(self, controller, editable): 
    return ArgonautTab(self, controller, editable)


class ArgonautTab(IMessageEditorTab):
  def __init__(self, extender, controller, editable):
    self._extender = extender
    self._controller = controller
    self._helpers = extender._helpers

    # Data container
    self._dataContainer = ArgonautData()

    # Argonaut Parser
    self._argoParser = ArgonautParser(self._dataContainer)

    # Burp View (table)
    self._argoTable = ArgonautTable(self._dataContainer)
    self._tablePane = JScrollPane(self._argoTable)

    return

  def getTabCaption(self):
    return "Argonaut"

  def getUiComponent(self):
    return self._tablePane

  def isEnabled(self, content, isRequest):
    """Enable if parameters were present. Including cookies"""
    if isRequest:
      return False
    else:
      raw_req = self._controller.getRequest()

      if not raw_req:
        return False

    req = self._helpers.analyzeRequest(raw_req)
    params =  req.getParameters()

    if params.isEmpty():
      return False

    return True

  def setMessage(self, content, isRequest):
    if isRequest:
      return

    # Extract params from pair 
    req = self._helpers.analyzeRequest(self._controller.getRequest())
    params =  req.getParameters()

    # Grab response
    rsp = self._helpers.analyzeResponse(content)
    body = content[rsp.getBodyOffset():].tostring()

    # Parse
    self._dataContainer.reset()
    self._argoParser.parse(params, body)
    self._dataContainer.fireTableDataChanged()

    return

  def isModified(self):
    return False


## ArgonautParser
class ArgonautParser:
  def __init__(self, dataContainer):
    self.container = dataContainer

    # Transformers to the rescue
    self.prime = Optimus()
    self.prime.set_transformations(TRANSFORMATIONS)

  def parse(self, params, body):
    for param in params:
      # TODO: Add different extraction depending on param type
      paramValue = unquote(param.getValue())

      # Param testing
      if len(paramValue) < MIN_PARAM_LEN: continue

      # Search body
      for name, trns in self.prime.transform(paramValue):
        indexes = [x for x in list(self.find_all(trns, body))]

        # Extract snippet
        if indexes:
          for start, end in indexes:
            # TODO: more intelligent snippet
            snippet = body[max(0,start-30):min(end+30, len(body))]

            self.container.insertRow(paramValue, name, snippet)

          break

  @staticmethod
  def find_all(sub, string):
    l = len(sub)
    start = 0
    while True:
        start = string.find(sub, start)
        if start == -1: return
        yield (start, start+l)
        start += l


## Transformers class
class Optimus:
  def __init__(self):
    self.transformations = []

  def set_transformations(self, t):
    self.transformations = t

  def transform(self, target):
    if target:
      for t in self.transformations:
        yield t['name'], self._translate(target, t["table"])

  def _translate(self, string, transformation):
    return reduce(lambda a, kv: a.replace(*kv), transformation, string)


## Classes related to UITable
# TODO: need serious UI work
class ArgonautTable(JTable):
  def __init__(self, dataModel):
    self.setModel(dataModel)
    return


class ArgonautData(AbstractTableModel):
  _data = []

  def reset(self):
    self._data = []

  def insertRow(self, paramValue, transformation, snippet):
    entry = {
              'paramValue': paramValue,
              'transformation': transformation,
              'snippet': snippet
            }

    self._data.append(entry)

  def getRowCount(self):
    return len(self._data)

  def getColumnCount(self):
    return 3

  def getColumnName(self, columnIndex):
    if columnIndex == 0:
      return "Parameter Value"
    if columnIndex == 1:
      return "Transformation"
    if columnIndex == 2:
      return "Snippet"

    return ""

  def getValueAt(self, rowIndex, columnIndex):
    dataEntry = self._data[rowIndex]

    if columnIndex == 0:
      return dataEntry['paramValue']
    if columnIndex == 1:
      return dataEntry['transformation']
    if columnIndex == 2:
      return dataEntry['snippet']

    return ""
