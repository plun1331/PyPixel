# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2021 plun1331

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class Firework(object):
    r"""Represents a firework. Interesting, right?

    :param firework: The raw firework data.
    :type firework: dict"""

    def __init__(self, firework: dict):
        self.flight_duration = firework['flight_duaration'] if 'flight_duaration' in firework else None
        self.shape = firework['shape'] if 'shape' in firework else None
        self.trail_enabled = firework['trail'] if 'trail' in firework else None
        self.twinkles = firework['twinkle'] if 'twinkle' in firework else None
        self.colors = firework['colors'] if 'colors' in firework else None
        self.fading_colors = firework['fade_colors'] if 'fade_colors' in firework else None
        self.selected = firework['selected'] if 'selected' in firework else None
