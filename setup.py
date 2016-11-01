#!/usr/bin/env python

from distutils.core import setup

setup(
    name='ife',
    version='1.0',
    description='Interactice fiction engine',
    author='nihlaeth',
    author_email='info@nihlaeth.nl',
    packages=[
        'ife',
        'living_the_dream',
        'living_the_dream.world',
        'living_the_dream.actors',
        'living_the_dream.transitions',
        'living_the_dream.events',],
    )
