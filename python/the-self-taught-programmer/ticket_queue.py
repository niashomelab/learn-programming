# TITLE: Ticket Queue 
# DESC: A queue can simulate people waiting in line to buy tickets for a movie


import time # epoch, in simulate_line() : time.time()
import random # in simulate_line() : random.randint()


class Queue:
    def __init__(self):
        # create an empty list for the queue
        self.items = []

    def is_empty(self):
        # check if the queue is empty
        return self.items == []

    def enqueue(self, item):
        # add items to the list i.e the queue
        self.items.insert(0, item)

    def dequeue(self):
        # remove the last item from the queue
        return self.items.pop()

    def size(self):
        # return the size of the queue
        return len(self.items)

    def simulate_line(self,
                      till_show,
                      max_time):
        # simulate selling tickets to a line of people
        # till_show = time selling ticket before the show starts; max_time = max delay between 2 person
        pq = Queue() # person queue
        tix_sold = [] # TIX = ticket

        for i in range(10):
            # set number of persons: 10 persons: person0, person1, person2, ..., person9
            pq.enqueue("person" + str(i)) # add (person1, person2, ... person9) to the queue "pq"

        t_end = time.time() + till_show # when the show begins, ticket no longer being sold
        now = time.time() # get the current time
        while now < t_end and not pq.is_empty(): # before running out of time, or no more persons, who want to buy a ticket
            now = time.time() # get the current time (2)
            r = random.randint(0, max_time) # random delay time
            time.sleep(r) # time delay between 2 person
            person = pq.dequeue() # get (person1) out of (person1, ...person9) = "pq" then move to "tix_sold"
            print(person) # print out the person who has bought the ticket
            tix_sold.append(person) # add moved person to "tix_sold"

        return tix_sold # the end value is "tix_sold", not "pq" 



queue = Queue()
sold = queue.simulate_line(1, 5)

print("\n")
print(sold)
# print("\n {}".format(sold))
