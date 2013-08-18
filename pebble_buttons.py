#!/usr/bin/env python

import pebble as libpebble
import time

class PebbleButtons:

    def __init__(self, pebble_id, lightblue, pair):
        attempts = 0
        self.pebble = False
        while not self.pebble:
            if attempts == 4:
                print 'Could not connect to Pebble', e
                raise e
            try:
                self.pebble = libpebble.Pebble(pebble_id, lightblue, pair)
                print "Got Pebble."
            except Exception as e:
                print 'No pebble?'
                print 'error', e
                time.sleep(2)
                attempts += 1
        try:
            self.cmd_notification_email("Walk In The Park is ready.")
        except Exception as e:
            print 'error', e
            self.pebble.disconnect()
            time.sleep(2)
            raise e
            exit(2)
        print "Pebble OK"
        
    def update_screen(self, basket, score, name):
        artist = basket
        album = name
        title = str(score)
        try:
            self.pebble.set_nowplaying_metadata(title, album, artist)
        except Exception as e:
            print 'Udate screen error', e
            self.pebble.disconnect()
            time.sleep(2)
            raise e
            exit(2)

    def get_pebble(self):
        return self.pebble

    def cmd_notification_email(self, message):
        print str(message)
        self.pebble.notification_email("WalkInThePark", "", str(message))

