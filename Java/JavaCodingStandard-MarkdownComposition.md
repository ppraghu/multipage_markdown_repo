# The Official Java Coding Standards Document

**Version:** 1.0.2  
**Date Last Updated:** Sept 08,2020

---

**Original Author(s):** [Raghu Pushpakath](mailto:Raghu.Pushpakath@ust-global.com)  
**Maintainer(s):** [Raghu Pushpakath](mailto:Raghu.Pushpakath@ust-global.com), [Ram Krishnan](mailto:Ram.Krishnan@yahoo.com)  
**Contributer(s):** [Ram Krishnan](mailto:ramkrishnan@yahoo.com), [Gopal Shankar](mailto:g.shankar@gmail.com)  

---

(Courtesy: [Ray Wenderlich](https://github.com/raywenderlich/java-style-guide))

This style guide is different from other you may see, because the focus is
centered on readability for print and the web. We created this style guide to
keep the code in our tutorials consistent.

Our overarching goals are __conciseness__, __readability__ and __simplicity__.

## Inspiration

This style-guide is somewhat of a mash-up between the existing Java language
style guides, and a tutorial-readability focused Swift style-guide. The language
guidance is drawn from the
[Android contributors style guide](https://source.android.com/source/code-style.html)
and the
[Google Java Style Guide](https://google-styleguide.googlecode.com/svn/trunk/javaguide.html).

## Android Studio Coding Style

It is possible to get Android Studio to adhere to these style guidelines, via
a rather complex sequence of menus. To make it easier, we've provided a coding
style that can be imported into Android Studio.

First, clone this repository and run `install.sh`.

Then, open Android Studio. To set this codestyle as the default, select
__File > Other Settings > Default Settings...__:

![Default Settings](resources/default_settings.png)

In __Editor > Code Style__, choose the __Scheme__ to be __raywenderlich.com__:

![Setting the Scheme](resources/setting_scheme.png)

From now on, projects you create _should_ follow the correct style guidelines.


## Table of Contents

- [Nomenclature](#nomenclature)
- [Declarations](#declarations)
- [Spacing](#spacing)
- [Getters & Setters](#getters--setters)
- [Brace Style](#brace-style)
- [Switch Statements](#switch-statements)
- [Annotations](#annotations)
- [XML Guidance](#xml-guidance)
- [Language](#language)
- [Copyright Statement](#copyright-statement)
- [Credit](#credits)

{"gitdown": "include", "file": "sections/Nomenclature.md"}
{"gitdown": "include", "file": "sections/Declarations.md"}
{"gitdown": "include", "file": "sections/Spacing.md"}
{"gitdown": "include", "file": "sections/GettersSetters.md"}
{"gitdown": "include", "file": "sections/BraceStyle.md"}
{"gitdown": "include", "file": "sections/SwitchStatements.md"}
{"gitdown": "include", "file": "sections/Annotations.md"}
{"gitdown": "include", "file": "sections/XMLGuidance.md"}
{"gitdown": "include", "file": "sections/Language.md"}
{"gitdown": "include", "file": "sections/CopyrightStatement.md"}
{"gitdown": "include", "file": "sections/Credits.md"}
