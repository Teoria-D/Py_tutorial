# -*- coding: utf_8 -*-
"""抽象クラス・具象クラスについての落書き"""

from abc import ABC, abstractmethod

import maya.cmds as cmds


class Shape(ABC):
    """形状を題材に抽象クラスを定義してみる

    Args:
        ABC : 抽象基底クラス。これを継承したクラスを、抽象クラスという
    """

    def __init__(self, name):
        """Shapeクラスのコンストラクタ

        Args:
            name (str): cubeに対する命名
        """
        self.name = name

    @abstractmethod
    def create(self):
        print("createメソッドを必ず定義!")


class Cube(Shape):
    def __init__(self, depth, width, height):
        """Cubeクラスのコンストラクタ

        Args:
            depth (float): キューブの深さ
            width (float): キューブの幅
            height (float): キューブの高さ
        """
        super().__init__("cube")
        self.depth = depth
        self.width = width
        self.height = height

    def create(self):
        """抽象メソッドで規定されているため、必ず定義

        Note:
            定義しないとTypeErrorを返す
        """
        cmds.polyCube(d=self.depth, w=self.width, h=self.height)


mycube = Cube(1.0, 3.0, 6.0)
mycube.create()
# 深さ1、幅3、高さ6のキューブができる
