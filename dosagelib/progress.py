from __future__ import division

import sys
import time

from . import util

class Guess(object):
    def __init__(self, weight):
        self.weight = weight
        self.guess = 0
        self.best = 0

    def feed(self, value):
        self.guess = self.weight * value + (1 - self.weight) * self.guess

    def distance(self, value):
        return (self.guess - value) ** 2

class FortuneTeller(object):
    weights = (0.2, 0.3, 0.4)

    def __init__(self):
        self.guesses = map(Guess, self.weights)

    def feed(self, value):
        best = min([(guess.distance(value), guess) for guess in self.guesses])[1]
        best.best += 1
        for guess in self.guesses:
            guess.feed(value)

    def predict(self):
        return max([(guess.best, guess) for guess in self.guesses])[1].guess

class OperationComplete(Exception): pass

def drawBar(fill, total, caption):
    screenWidth = util.getWindowSize()
    ratio = fill / total
    mask = '[%%s>%%s] (%.2f%%%%) %s' % (ratio * 100, caption)

    barWidth = screenWidth - len(mask) + 6
    fillWidth = int(barWidth * ratio) - 1
    emptyWidth = barWidth - fillWidth - 1

    sys.stdout.write('\r')
    sys.stdout.write(mask % ('=' * fillWidth, '-' * emptyWidth))
    sys.stdout.flush()

def drawBounceBar(pos, caption):
    screenWidth = util.getWindowSize()
    mask = '[%%s<=>%%s] %s' % (caption,)

    barWidth = screenWidth - len(mask) + 4
    leftWidth = pos % barWidth - 1
    rightWidth = barWidth - leftWidth - 1

    sys.stdout.write('\r')
    sys.stdout.write(mask % (' ' * leftWidth, ' ' * rightWidth))
    sys.stdout.flush()

def progressBar(fn):
    completed = bps = 0
    count = 0
    ft = FortuneTeller()
    currentTime = lastTime = time.time()
    try:
        while 1:
            inc = 0
            while currentTime - lastTime < 0.2:
                progress, total = fn()
                inc += progress
                currentTime = time.time()

            ft.feed(inc / (currentTime - lastTime))
            lastTime = currentTime

            completed += inc
            bps = ft.predict()

            if total == 0:
                drawBounceBar(count, '%s/sec' % util.saneDataSize(bps))
                count += 1
            else:
                drawBar(completed, max(total, completed), '%s/sec' % util.saneDataSize(bps))
    except OperationComplete:
        if count > 0:
            drawBounceBar(count, '%s/sec' % util.saneDataSize(bps))
        else:
            drawBar(max(total, completed), max(total, completed), '%s/sec' % util.saneDataSize(bps))
    print ''
