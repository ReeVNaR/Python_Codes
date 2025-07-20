def print_formatted(number):
    # your code goes here
    bw = number.bit_length()
    for i in range(1, number+1):
        print("{0}".format(i).rjust(bw), "{0:o}".format(i).rjust(bw), "{0:X}".format(i).rjust(bw), "{0:b}".format(i).rjust(bw))
        