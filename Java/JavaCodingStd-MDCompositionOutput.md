<a name="the-official-java-coding-standards-document"></a>
# The Official Java Coding Standards Document

**Version:** 1.0.2  
**Date Last Updated:** Sept 08,2020

---

**Original Author(s):** [Raghu Pushpakath](mailto:Raghu.Pushpakath@ust-global.com)  
**Maintainer(s):** [Raghu Pushpakath](mailto:Raghu.Pushpakath@ust-global.com), [Ram Krishnan](Ram.Krishnan@yahoo.com)  
**Contributer(s):** [Ram Krishnan](ramkrishnan@yahoo.com), [Gopal Shankar](g.shankar@gmail.com)  

---

(Courtesy: [Ray Wenderlich](https://github.com/raywenderlich/java-style-guide))

This style guide is different from other you may see, because the focus is
centered on readability for print and the web. We created this style guide to
keep the code in our tutorials consistent.

Our overarching goals are __conciseness__, __readability__ and __simplicity__.

<a name="the-official-java-coding-standards-document-inspiration"></a>
## Inspiration

This style-guide is somewhat of a mash-up between the existing Java language
style guides, and a tutorial-readability focused Swift style-guide. The language
guidance is drawn from the
[Android contributors style guide](https://source.android.com/source/code-style.html)
and the
[Google Java Style Guide](https://google-styleguide.googlecode.com/svn/trunk/javaguide.html).

<a name="the-official-java-coding-standards-document-android-studio-coding-style"></a>
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


<a name="the-official-java-coding-standards-document-table-of-contents"></a>
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

[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-nomenclature"></a>
## Nomenclature

On the whole, naming should follow Java standards.

<a name="the-official-java-coding-standards-document-nomenclature-packages"></a>
### Packages

Package names are all __lower-case__, multiple words concatenated together,
without
hypens or underscores:

__BAD__:

```java
com.RayWenderlich.funky_widget
```

__GOOD__:

```java
com.raywenderlich.funkywidget
```

<a name="the-official-java-coding-standards-document-nomenclature-classes-interfaces"></a>
### Classes &amp; Interfaces

Written in __UpperCamelCase__. For example `RadialSlider`. 

<a name="the-official-java-coding-standards-document-nomenclature-methods"></a>
### Methods

Written in __lowerCamelCase__. For example `setValue`.

<a name="the-official-java-coding-standards-document-nomenclature-fields"></a>
### Fields

Written in __lowerCamelCase__.

Static fields should be written in __uppercase__, with an underscore separating
words:

```java
public static final int THE_ANSWER = 42;
```

As distasteful as it is, field naming should follow the Android source code
naming conventions:

- Non-public, non-static field names start with an `m`.
- Static field names start with an `s`.

For example:

```java
public class MyClass {
  public static final int SOME_CONSTANT = 42;
  public int publicField;
  private static MyClass sSingleton;
  int mPackagePrivate;
  private int mPrivate;
  protected int mProtected;
}
```

> __Note:__ You can set Android Studio to follow this convention. See this SO
> link for details http://stackoverflow.com/questions/22732722/intellij-android-studio-member-variable-prefix

<a name="the-official-java-coding-standards-document-nomenclature-variables-parameters"></a>
### Variables &amp; Parameters

Written in __lowerCamelCase__.

Single character values to be avoided except for temporary looping variables.

<a name="the-official-java-coding-standards-document-nomenclature-misc"></a>
### Misc

In code, acronyms should be treated as words. For example:

__BAD:__

```java
XMLHTTPRequest
String URL
findPostByID
```
__GOOD:__

```java
XmlHttpRequest
String url
findPostById
```

[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-declarations"></a>
## Declarations

<a name="the-official-java-coding-standards-document-declarations-access-level-modifiers"></a>
### Access Level Modifiers

Access level modifiers should be explicitly defined for classes, methods and
member variables.

<a name="the-official-java-coding-standards-document-declarations-fields-variables"></a>
### Fields &amp; Variables

Prefer single declaration per line.

__BAD:__

```java
String username, twitterHandle;
```

__GOOD:__

```java
String username;
String twitterHandle;
```

<a name="the-official-java-coding-standards-document-declarations-classes"></a>
### Classes

Exactly one class per source file, although inner classes are encouraged where
scoping appropriate.


<a name="the-official-java-coding-standards-document-declarations-enum-classes"></a>
### Enum Classes

Enum classes should be avoided where possible, due to a large memory overhead.
Static constants are preferred. See http://developer.android.com/training/articles/memory.html#Overhead
for further details.

Enum classes without methods may be formatted without line-breaks, as follows:

```java
private enum CompassDirection { EAST, NORTH, WEST, SOUTH }
```


[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-spacing"></a>
## Spacing

Spacing is especially important in raywenderlich.com code, as code needs to be
easily readable as part of the tutorial. Java does not lend itself well to this.

<a name="the-official-java-coding-standards-document-spacing-indentation"></a>
### Indentation

Indentation is using spaces - never tabs.

<a name="the-official-java-coding-standards-document-spacing-indentation-blocks"></a>
#### Blocks

Indentation for blocks uses 2 spaces (not the default 4):

__BAD:__

```java
for (int i = 0; i < 10; i++) {
    Log.i(TAG, "index=" + i);
}
```

__GOOD:__

```java
for (int i = 0; i < 10; i++) {
  Log.i(TAG, "index=" + i);
}
```

<a name="the-official-java-coding-standards-document-spacing-indentation-line-wraps"></a>
#### Line Wraps

Indentation for line wraps should use 4 spaces (not the default 8):

__BAD:__

```java
CoolUiWidget widget =
        someIncrediblyLongExpression(that, reallyWouldNotFit, on, aSingle, line);
```

__GOOD:__

```java
CoolUiWidget widget =
    someIncrediblyLongExpression(that, reallyWouldNotFit, on, aSingle, line);
```

<a name="the-official-java-coding-standards-document-spacing-line-length"></a>
### Line Length

Lines should be no longer than 100 characters long.


<a name="the-official-java-coding-standards-document-spacing-vertical-spacing"></a>
### Vertical Spacing

There should be exactly one blank line between methods to aid in visual clarity 
and organization. Whitespace within methods should separate functionality, but 
having too many sections in a method often means you should refactor into
several methods.


[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-getters-setters"></a>
## Getters &amp; Setters

For external access to fields in classes, getters and setters are preferred to
direct access of the fields. Fields should rarely be `public`.

However, it is encouraged to use the field directly when accessing internally
(i.e. from inside the class). This is a performance optimization recommended
by Google: http://developer.android.com/training/articles/perf-tips.html#GettersSetters


[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-brace-style"></a>
## Brace Style

Only trailing closing-braces are awarded their own line. All others appear the
same line as preceding code:

__BAD:__

```java
class MyClass
{
  void doSomething()
  {
    if (someTest)
    {
      // ...
    }
    else
    {
      // ...
    }
  }
}
```

__GOOD:__

```java
class MyClass {
  void doSomething() {
    if (someTest) {
      // ...
    } else {
      // ...
    }
  }
}
```

Conditional statements are always required to be enclosed with braces,
irrespective of the number of lines required.

__BAD:__

```java
if (someTest)
  doSomething();
if (someTest) doSomethingElse();
```

__GOOD:__

```java
if (someTest) {
  doSomething();
}
if (someTest) { doSomethingElse(); }
```



[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-switch-statements"></a>
## Switch Statements

Switch statements fall-through by default, but this can be unintuitive. If you
require this behavior, comment it.

Alway include the `default` case.

__BAD:__

```java
switch (anInput) {
  case 1:
    doSomethingForCaseOne();
  case 2:
    doSomethingForCaseOneOrTwo();
    break;
  case 3:
    doSomethingForCaseOneOrThree();
    break;
}
```

__GOOD:__

```java
switch (anInput) {
  case 1:
    doSomethingForCaseOne();
    // fall through
  case 2:
    doSomethingForCaseOneOrTwo();
    break;
  case 3:
    doSomethingForCaseOneOrThree();
    break;
  default:
    break;
}
```

[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-annotations"></a>
## Annotations

Standard annotations should be used - in particular `@Override`. This should
appear the line before the function declaration.

__BAD:__

```java
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
}
```

__GOOD:__

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
}
```


[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-xml-guidance"></a>
## XML Guidance

Since Android uses XML extensively in addition to Java, we have some rules
specific to XML.

<a name="the-official-java-coding-standards-document-xml-guidance-xml-file-names"></a>
### XML File Names

View-based XML files should be prefixed with the type of view that they
represent.

__BAD:__

- `login.xml`
- `main_screen.xml`
- `rounded_edges_button.xml`

__GOOD:__

- `activity_login.xml`
- `fragment_main_screen.xml`
- `button_rounded_edges.xml`

<a name="the-official-java-coding-standards-document-xml-guidance-indentation-1"></a>
### Indentation

Similarly to Java, indentation should be __two characters__.

<a name="the-official-java-coding-standards-document-xml-guidance-use-context-specific-xml-files"></a>
### Use Context-Specific XML Files

Wherever possible XML resource files should be used:

- Strings => `res/values/strings.xml`
- Styles => `res/values/styles.xml`
- Colors => `res/color/colors.xml`
- Animations => `res/anim/`
- Drawable => `res/drawable`


<a name="the-official-java-coding-standards-document-xml-guidance-xml-attribute-ordering"></a>
### XML Attribute Ordering

Where appropriate, XML attributes should appear in the following order:

- `id` attribute
- `layout_*` attributes
- style attributes such as `gravity` or `textColor`
- value attributes such as `text` or `src`

Within each of these groups, the attributes should be ordered alphabetically.



[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-language"></a>
## Language

Use US English spelling.

__BAD:__

```java
String colour = "red";
```

__GOOD:__

```java
String color = "red";
```

[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-copyright-statement"></a>
## Copyright Statement

The following copyright statement should be included at the top of every source
file:

    /*
     * Copyright (c) 2017 Razeware LLC
     * 
     * Permission is hereby granted, free of charge, to any person obtaining a copy
     * of this software and associated documentation files (the "Software"), to deal
     * in the Software without restriction, including without limitation the rights
     * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
     * copies of the Software, and to permit persons to whom the Software is
     * furnished to do so, subject to the following conditions:
     * 
     * The above copyright notice and this permission notice shall be included in
     * all copies or substantial portions of the Software.
     * 
     * Notwithstanding the foregoing, you may not use, copy, modify, merge, publish, 
     * distribute, sublicense, create a derivative work, and/or sell copies of the 
     * Software in any work that is designed, intended, or marketed for pedagogical or 
     * instructional purposes related to programming, coding, application development, 
     * or information technology.  Permission for such use, copying, modification,
     * merger, publication, distribution, sublicensing, creation of derivative works, 
     * or sale is expressly withheld.
     *
     * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
     * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
     * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
     * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
     * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
     * THE SOFTWARE.
     */

[Go back](../JavaCodingStandard.md)

<a name="the-official-java-coding-standards-document-credits"></a>
## Credits

This style guide is a collaborative effort from the most stylish
raywenderlich.com team members:

- [Darryl Bayliss](https://github.com/DarrylBayliss)
- [Sam Davies](https://github.com/sammyd)
- [Mic Pringle](https://github.com/micpringle)
- [Ray Wenderlich](https://github.com/rwenderlich)

