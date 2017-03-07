'''
Created on Mar 1, 2017

@author: jackwang
'''
import tobeimported
import logging
from logging.config import fileConfig

fileConfig('logging.ini')
logger = logging.getLogger(__name__)

def foo():
    logger.info('Logged from function foo')
    pass

logger.debug('Hello World!')

targetedString = """Two little kittens, one stormy night,
Began to quarrel, and then to fight;
One had a mouse, the other had none,
And that's the way the quarrel begun.

"I'll have that mouse," said the biggest cat;
"You'll have that mouse? We'll see about that!"
"I will have that mouse," said the eldest son;
"You shan't have the mouse," said the little one.

I told you before 'twas a stormy night
When these two little kittens began to fight;
The old woman seized her sweeping broom,
And swept the two kittens right out of the room.

The ground was covered with frost and snow,
And the two little kittens had nowhere to go;
So they laid them down on the mat at the door,
While the old woman finished sweeping the floor.

Then they crept in, as quiet as mice,
All wet with the snow, and cold as ice,
For they found it was better, that stormy night,
To lie down and sleep than to quarrel and fight."""

# week2l2bimported.print_first_and_last(targetedString)
tobeimported.print_first_and_last_sorted(targetedString)

logger.debug('I am back, now let\'s call the foo() function in my own module!')

foo()