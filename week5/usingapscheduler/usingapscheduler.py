'''
Created on Mar 14, 2017

@author: jwang02
'''
# import sys
# from time import sleep
#  
# ##############################################################
#  
#
# 
from pytz import utc

# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

def main():
    
    sched = BlockingScheduler()
    
    @sched.scheduled_job('interval', minutes=3)
    def timed_job():
        print('This job is run every three minutes.')
    
    @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
    def scheduled_job():
        print('This job is run every weekday at 5pm.')

    sched.start()
    
if __name__ == "__main__":
    main()