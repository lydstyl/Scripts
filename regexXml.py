#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Regex pour réparer les 2 x double quote dans un xml du genre class=""ma-classe""
"""


# # 1/
# class=""(.*)""
# class="$1"

# # ou mieux

# \s.{1-100}

# # 2/
# ""([^ ])
# "$1

# # 3/
# ([^=])""
# $1"

# ou mieux à voir pour tout en un # [^=\s]+=""[^=\s]+""