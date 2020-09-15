Title: Make a python object property behave like a classmethod
Date: 2013-07-11
Category: articles
Tags: python
Description: Using @property is nice and peachy when you use the instance of the class, but what if you need to get that property without instantiating the class.

Using `@property` is nice and peachy when you use the instance of the class, but what if you need to get that property without instantiating the class.

You can do that with `@classmethod` (you'd say), but I want to use it as an attribute not as a method.

Without further ado, the _hack_:

```python
class classproperty(property):
    def __get__(self, instance, cls):
        return classmethod(self.fget).__get__(instance, cls)()

class Foo(object):
    foobar = 'This ... is ... FOOBAR!!!'

    @classproperty
    def bar(self):
        return self.foobar

print Foo.bar
```
