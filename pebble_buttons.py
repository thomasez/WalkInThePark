#!/usr/bin/env python

import pebble as libpebble
import time

def music_control_handler(endpoint, resp):
    print "Innom handler"
    if resp == "PLAYPAUSE":
        print 'PLAYPAUSE!'
    elif resp == "PREVIOUS":
        print 'PREVIOUS!'
    elif resp == "NEXT":
        print 'NEXT!'
    # self.update_screen("Basket 2", 7, resp)

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
            self.cmd_notification_email()
            # self.cmd_remote()
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

    def getPebble(self):
        return self.pebble

    def cmd_remote(self):
        self.pebble.register_endpoint("MUSIC_CONTROL", music_control_handler)
        print 'waiting for control events'
        try:
            while True:
                self.update_screen('Startup', 5, 'Done')
                if self.pebble._ser.is_alive():
                    print 'lever ja'
                    time.sleep(5)
                else:
                    break

        except KeyboardInterrupt:
            self.pebble.disconnect()
            time.sleep(2)
            exit(1)
        return

    def cmd_notification_email(self):
        print "Email"
        self.pebble.notification_email("makr.co", "relay board", "ready")

