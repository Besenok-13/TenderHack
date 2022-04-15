# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:08:23 2021
@author: artbo
"""

from .website import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
