[Go back](../JavaCodingStandard.md)

## Nomenclature

On the whole, naming should follow Java standards.

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

### Classes & Interfaces

Written in __UpperCamelCase__. For example `RadialSlider`. 

### Methods

Written in __lowerCamelCase__. For example `setValue`.

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

### Variables & Parameters

Written in __lowerCamelCase__.

Single character values to be avoided except for temporary looping variables.

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
