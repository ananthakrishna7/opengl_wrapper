# Purpose
I had a small course project to finish (now in `main.py`), and didn't want to fight with OpenGL for every point I wanted to draw. You could call this a convenience script of sorts. 
My goal was to abstract away all the setup required in modern OpenGL, so that I could just get started with drawing things. I did NOT think about optimizations. The drawing in 
`main.py` uses about 358MB of RAM 💀.

You should be able to just clone this repo, and start implementing any CG algorithm (Bressenham's line drawing algo, Midpoint circle algo, etc.) with no setup (except for installing the dependencies in `requirements.txt`).

I was assisted by GitHub Copilot in this project.

# Structure
There's an example in `main.py`, and the rest of the files are named according to their functions. 
- The `Drawing` class takes primitives, computes their constituent points in NDC, populates vertex buffers and draws them.
- The `Window` class compiles the shaders and sets up a pygame window, in which it draws a `Drawing`. I haven't implemented dynamic resizing of the viewport, so resizing will squish your drawing.
- `primitives.py` has the `Point`, `Line`, `Circle`, and `Arc` classes, along with translation and y_reflection transforms.

# Usage
An example is present in `main.py`.

This is how you would draw a shape:
1. Define it using a primitive like `Line` (or use an algorithm to do it yourself using `Point` objects).
2. Create a `Drawing`.
3. Add the shape to the `Drawing`.
4. Pass the `Drawing` to a `Window`
5. Call the `Window`
