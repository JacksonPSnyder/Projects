import time
from Queues import *


def how_many():
    done = False

    while not done:
        number = input("How many network requests would you like to simulate? Pick a number between 1 and 1,000,000:")
        if not number.isdigit() or int(number) > 1000000:
            print("Invalid entry. Try again.")
        else:
            done = True

    return int(number)


def simulate(queue, number):
    print("Simulating", number, "requests...")

    start = time.time()
    perc = 0.1
    print('Enqueuing progress:', end=' ')
    for i in range(number):
        queue.enqueue('Call' + str(i))
        if i+1 > number * perc:
            print("{:.0%}".format(perc), end=' ', flush=True)
            perc += 0.1
    enqueue_time = time.time() - start
    perc = 0.1
    start = time.time()
    count = 0
    print('\nDequeueing progress:', end=' ')
    while not queue.is_empty():
        queue.dequeue()
        count += 1
        if count > number * perc:
            print("{:.0%}".format(perc), end=' ', flush=True)
            perc += 0.1
    dequeue_time = time.time() - start

    print('\n# of requests: {}\nTime to enqueue: {:.10f}s\nTime to dequeue: {:.10f}s'
          .format(number, enqueue_time, dequeue_time))


def driver():
    done = False

    print("Welcome to the Network Queue simulator.")
    while not done:
        print("\nSelect an option:")
        print("1) Queue using a traditional Python array-based list")
        print("2) Queue using a LinkedList")
        print("3) Queue using a DoublyLinkedList")
        print("4) Quit")
        choice = input("Enter your choice [1-4]:")

        if choice == '1':
            simulate(QueuePythonList(), how_many())
        elif choice == '2':
            simulate(QueueLinkedList(), how_many())
        elif choice == '3':
            simulate(QueueDoublyLinkedList(), how_many())
        elif choice == '4':
            print("Exiting...")
            done = True
        else:
            print("Invalid choice. Pick again.")


if __name__ == "__main__":
    driver()
