#----------Functions to perform conversion/standardisation----------------------

def raw_acceleration(n_h,n_l):
    return n_l + n_h * 256

def twos_comp(val, bits):
    #compute the 2's complement of val
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val

#normalise the raw acceleration values
def normalise(l, h, divider):

    acc_l_ord = ord(l)
    acc_h_ord = ord(h)

    acceleration = raw_acceleration(acc_h_ord, acc_l_ord)
    acceleration_signed = twos_comp(acceleration, 16)

    normalised_acc  = acceleration_signed / divider

    return normalised_acc

#finds the minimum index in a list
def minimum(nLargestValues):
    minValueIndex = 0
    minValue = nLargestValues[0]
    for i in range (0, len(nLargestValues)):
        if(nLargestValues[i] < minValue):
            minValue = nLargestValues[i]
            minValueIndex = i
    return minValueIndex
