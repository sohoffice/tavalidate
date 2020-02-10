tavalidate, utilities to help you validate [Tavern](https://tavern.readthedocs.io/en/latest/) response.

Installation
------------

Tavalidate can be installed through pip.

```
pip install tavalidate
```

XML
----

Tavern has great built-in Json support, but things are difficult when it comes to XML.
Use tavalidate.xmlv package to validate XML response.

XML validation example:

```
response:
  body:
    $ext:
      function: tavalidate.xmlv:assert_xml
      extra_kwargs:
        expected: |
          <foo attr="!anystr">
            <bar attr2="baz">!anyint</bar>
          </foo>
```

Simply put, pass the expected xml as an argument to the `tavalidate.xmlv.validate` function. The
function will validate the xml structure, node value and attribute value.

### extra_kwargs

Below are the supported extra kwargs of `tavalidate.xmlv.validate` function.

#### expected

This is the expected XML string.

You may use some (not all) of the tavern magic values to match data of your specified type:

- !anything: This matches value of any type.
- !anystr: Matches any string
- !anyint: Matches any integer
- !anyfloat: Matches any float
- !anybool: Matches any boolean

#### strict

Use `strict: True` if you want to make sure there's no extra tag in the response.