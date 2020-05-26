<html>
    <head>
<!--include head.txt -->
        <title>
            Interface Cutover
        </title>
    </head>

 <body>
<!--include logo.txt -->
<!--include menu.txt -->


## Changing a Vital Interface in Your App... Without Breaking Everything

The situation: you have a vital and widely used interface in your
application: perhaps to a database, to an API, to a logging system, 
to a math library, etc. And now you find you need to replace it!

Why would this happen?

- Your company has changed databases.
- Your client or vendor has changed their API.
- You realize the old interface has problems you need to fix.
- You need to replace a third party library with a different one.

There are many more possible reasons!

The straightforward way to do this is:

1. Build the new interface.
2. Tear out the old interface.
3. Rewrite all uses of the interface to use the new one.
4. Test the system.

There are variations on this: we might do 2 - 1 - 3, or even 1 - 3 - 2.

But I want to suggest that all of these variations are asking for trouble: if
the interface is not utterly trivial, it is much better to apply our technique
of *incremental development* to the cutover. We *reduce batch sizes*, taking
the smallest steps we can in each "batch" of work.

(Question: Why would small batch size be good at a brewery?)

The process I will show you goes:

1. Build the new interface.
2. Test the new interface.
3. Re-write the old interface so that *it is a front for the new interface*.
4. Test the system with this "new-old" interface in place. (Note: we haven't
   yet touched any application code, just library code! Also, the application
   at this point is *actually using the new interface*... just *through* the
   old interface.)
5. Change *one module* of the application to directly use the new interface.
6. Test that module.
7. Repeat 5. and 6. until all modules are using the new interface.
8. Delete the old interface.

OK, now let's actually see how this works with some real code. The example I
will show you is pretty simple... but that's good! It let's us see the steps
very clearly. But the same steps apply to more complex interfaces.

</body>
</html>
