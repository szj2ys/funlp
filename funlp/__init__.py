#-*- encoding:utf-8 -*-
from __future__ import absolute_import, print_function
import warnings
from .TextRank4Sentence import TextRank4Sentence
from .TextRank4Word import TextRank4Words
from . import utils

from .__version__ import version, __version__

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')