#coding:utf-8

import hashlib

var ="mot de passe"
var = hashlib.sha256()

print(var.digest())

var.update(b"mot de passe")
var.digest()

print(var.digest())