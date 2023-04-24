import matplotlib.pyplot as plt


# discrete time signal convolution
# Sajjad Rahmani

def conv(x_value, x_start, h_value, h_start):
    # calculate multiplication two signal (result in keeper)
    keeper = []
    for num in h_value:
        keeper.append([num * i for i in x_value])

    # insert zero in empty place
    for i in range(len(h_value)):
        keeper[i] = [0] * i + keeper[i] + [0] * (len(h_value) - 1 - i)

    # print keeper
    for i in keeper:
        print(*i)
    print("--" * (len(h_value) + 2))

    # calculate sum of each columns (result in conv_res)
    keeper = list(zip(*keeper))
    conv_res = []
    for i in keeper:
        conv_res.append(sum(i))

    # print convolution result
    print(*conv_res)

    # calculate n for first conv_res value
    conv_start = x_start + h_start

    # add some zeros to start and end of each signals
    x_value = [0] * 3 + x_value + [0] * 3
    h_value = [0] * 3 + h_value + [0] * 3
    conv_res = [0] * 3 + conv_res + [0] * 3

    plt.style.use('seaborn')
    fig, ax = plt.subplots(3, 1, sharex=True)

    ax[0].stem([i for i in range(x_start - 3, x_start + len(x_value) - 3)], x_value, use_line_collection=True,
               label='x[n]')
    ax[1].stem([i for i in range(h_start - 3, h_start + len(h_value) - 3)], h_value, use_line_collection=True,
               label='h[n]')
    ax[2].stem([i for i in range(conv_start - 3, conv_start + len(conv_res) - 3)], conv_res, use_line_collection=True,
               label='x[n] * h[n]')

    for axx in ax:
        axx.legend()
    plt.show()


# example 1 :
# sig1 = [1, 0, 2]
# sig1_start = 0  # start n for x[n]
#
# sig2 = [1, 1, 1]
# sig2_start = -1  # start n for h[n]
#
# conv(sig1, sig1_start, sig2, sig2_start)


# example 2 :
# sig1 = [2, 1, -1, -2, -3]
# sig1_start = -2  # start n for x[n]
#
# sig2 = [1, 2, 0, -3]
# sig2_start = -1  # start n for h[n]
#
# conv(sig1, sig1_start, sig2, sig2_start)


# example 3 :
# sig1 = [1, 2, 0, -3]
# sig1_start = -1  # start n for x[n]
#
# sig2 = [1]
# sig2_start = 0  # start n for h[n]
#
# conv(sig1, sig1_start, sig2, sig2_start)


# example 4 :
# sig1 = [3, 2, 1]
# sig1_start = 0  # start n for x[n]
#
# sig2_start = 0  # start n for h[n]
# sig2 = [pow(0.5, n) for n in range(sig2_start, 5)]
#
# conv(sig1, sig1_start, sig2, sig2_start)


# example 5 :
sig1 = [3, 2, 1]
sig1_start = 0  # start n for x[n]

sig2_start = 0  # start n for h[n]
sig2 = [pow(0.5, n) for n in range(sig2_start, 5)]

conv(sig1, sig1_start, sig2, sig2_start)
