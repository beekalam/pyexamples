#!/usr/bin/env python

from os import system
import curses

def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def execute_cmd(cmd_string):
     system("clear")
     a = system(cmd_string)
     print ""
     if a == 0:
          print "Command executed correctly"
     else:
          print "Command terminated with error"
     raw_input("Press enter")
     print ""

x = 0

while x != ord('1'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     screen.addstr(2,  2, "Please enter a number...")
     screen.addstr(4,  4, "1 - Exit")
     screen.addstr(5,  4, "2 - Restart Apache")
     screen.addstr(6,  4, "3 - Show disk space")
     screen.addstr(7,  4, "4 - stop mongodb")
     screen.addstr(8,  4, "5 - start mongodb")
     screen.addstr(9,  4, "6 - stop postgres")
     screen.addstr(10, 4, "7 - start postgre")
     screen.addstr(11, 4, "8 - stop mysql")
     screen.addstr(12, 4, "9 - start mysql")
     screen.addstr(13, 4, "a - stop freeradius")
     screen.addstr(14, 4, "b - start freeradius")
     screen.addstr(15, 4, "c - stop teamviewer")
     screen.addstr(17, 4, "d - start teamviewer")

     screen.addstr(2, 30, "e - stop postfix")
     screen.addstr(3, 30, "f - start postfix")
     screen.addstr(4, 30, "g - stop hddtemp")
     screen.addstr(5, 30, "h - start hddtemp")
     screen.addstr(6, 30, "i - stop tor")
     screen.addstr(7, 30, "j - start tor")
     #screen.addstr(24, 4, "k - start teamviewer")

     screen.refresh()

     x = screen.getch()


     if x == ord('2'):
          curses.endwin()
          execute_cmd("apachectl restart")
     if x == ord('3'):
          curses.endwin()
          execute_cmd("df -h")
     if x ==  ord('4'):
          curses.endwin()
          execute_cmd("service mongodb stop")
     if x == ord('5'):
         curses.endwin()
         execute_cmd("service mongodb start")
     if x == ord('6'):
         curses.endwin()
         execute_cmd("service postgresql stop")
     if x == ord('7'):
         curses.endwin()
         execute_cmd('service postgresql start')
     if x == ord('8'):
         curses.endwin()
         execute_cmd('service mysql stop')
     if x == ord('9'):
          curses.endwin()
          execute_cmd('service mysql start')
     if x == ord('a'):
         curses.endwin()
         execute_cmd('service freeradius stop')
     if x == ord('b'):
         curses.endwin()
         execute_cmd('service freeradius start')
     if x == ord('c'):
         curses.endwin()
         execute_cmd('service teamviewerd stop')
     if x == ord('d'):
         curses.endwin()
         execute_cmd('service teamvierd start')
     if x == ord('e'):
         curses.endwin()
         execute_cmd('service postfix stop')
     if x == ord('f'):
         curses.endwin()
         execute_cmd('service postfix start')
     if x == ord('g'):
         curses.endwin()
         execute_cmd('service hddtemp stop')
     if x == ord('h'):
         curses.endwin()
         execute_cmd('service hddtemp start')
     if x == ord('i'):
         curses.endwin()
         execute_cmd('service tor stop')
     if x == ord('j'):
         curses.endwin()
         execute_cmd('service tor start')

curses.endwin()
