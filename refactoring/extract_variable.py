# From https://refactoring.guru/extract-variable
#
# Before refactoring
# An expression that’s hard to understand:
def render_banner(self):
    if (self.platform.toUpperCase().indexOf("MAC") > -1) and (
            self.browser.toUpperCase().indexOf("IE") > -1) and self.wasInitialized() and (self.resize > 0):
        # do something
        pass


# Highlight `self.platform.toUpperCase().indexOf("MAC") > -1`, and select Refactor | Extract/Introduce Variable.
# Name the new variable isMacOS
# Repeat for the other two conditions
def render_banner(self):
    if (self.platform.toUpperCase().indexOf("MAC") > -1) and (
            self.browser.toUpperCase().indexOf("IE") > -1) and self.wasInitialized() and (self.resize > 0):
        # do something
        pass

# After refactoring
# Place the result of the expression or its parts in separate variables that are self-explanatory.
def render_banner(self):
    isMacOs = self.platform.toUpperCase().indexOf("MAC") > -1
    isIE = self.browser.toUpperCase().indexOf("IE") > -1
    wasResized = self.resize > 0

    if isMacOs and isIE and self.wasInitialized() and wasResized:
        # do something
        pass
