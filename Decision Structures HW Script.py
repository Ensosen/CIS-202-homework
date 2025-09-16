# The assignment. I created a new line just to make it look a nicer.
print ('One cause for speeding is the desire to shorten the time spent traveling. Create a program that calculates the amount of time saved if you are traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit. As the user for the average speed in miles per hour, speed limit in miles per hour and distance travelled in miles. THE TIME SAVED SHOULD BE REPORTED IN MINUTES. Create a screenshot of output where your average speed is 80 mph, speed limit is 60 mph and distance travelled is 100 miles. Your answer should indicate that you saved 25 minutes.')
print ('\n')
# Constants
minutes = 60

# Asking for some constants to use.
speed_limit = int(input('What is the speed limit for the road? '))
average_speed = int(input('What speed ABOVE the speed limit were you traveling? '))
while average_speed <= speed_limit: average_speed = int(input('Answer was not above the speed limit please try again. '))
distance_traveled = int(input('How many miles did you travel? '))

# Now we calculate the time it took to travel and compare the times.
average_time = distance_traveled/speed_limit
average_time = int(average_time*minutes)
speeding_time = distance_traveled/average_speed
speeding_time = int(speeding_time*minutes)
time_saved = average_time-speeding_time

# rinting the final message.
print ('The total time in minutes while going the speed limit is',average_time,'minutes.')
print ('The time you took while going above the speed limit is',speeding_time,'minutes.')
print ('The time that you saved is',time_saved,'minutes.')
