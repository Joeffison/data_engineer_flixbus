# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("""
    The approach I would apply is:
    <br />\n- Break down entry in pieces that the mentioned method rank_trips() supports (up to 5)
    <br />\n- Then Build a (heap-like) tree and rearrange the nodes and combine the subtrees with new calls to the original 
    rank_trips() method
    <br />\n
    <br />\nO(n log(n))
    """)
