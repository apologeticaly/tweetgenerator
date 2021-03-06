from random import randint
import random
class Dictogram:

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        self.word_list = word_list
       
        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())

        self.types = self.unique_words()

    def build_dictogram(self): 
        '''Creates a histogram dictionary using the word_list property and returns it'''
        dicto = {}
        for word in self.word_list:           
            if word in dicto: 
                dicto[word] += 1
            else: 
                dicto[word] = 1
        return dicto

    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary histogram'''
        if word in self.dictionary_histogram:
            return self.dictionary_histogram[word]

    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        used_words = []
        unique_words = 0

        for word in self.word_list:
            if word not in used_words:
                unique_words = unique_words + 1
                used_words.append(word)

        return unique_words

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''

        #TODO: use your sample function as a starting point to complete this method 

        total = self.tokens
        rand_val = random.randint(1, total)

        total = 0

        for key, value in self.dictionary_histogram.items():
            total += value
            if rand_val <= total:
                return key
        

# def print_dictogram(word_list):
#     '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

#     print()
#     print('Dictionary Histogram:')
#     print('word list: {}'.format(word_list))
#     # Create a dictogram and display its contents
#     dictogram = Dictogram(word_list)
#     print('dictogram: {}'.format(dictogram.dictionary_histogram))
#     print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
#     for word in word_list[-2:]:
#         freq = dictogram.frequency(word)
#         print('{!r} occurs {} times'.format(word, freq))
#     print()
#     print_dictogram_samples(dictogram)

# def print_dictogram_samples(dictogram):
#     '''Compares sampled frequency to observed frequency'''

#     print('Dictionary Histogram samples:')
#     # Sample the histogram 10,000 times and count frequency of results
#     samples_list = [dictogram.sample() for _ in range(10000)]
#     samples_hist = Dictogram(samples_list)
#     print('samples: {}'.format(samples_hist.dictionary_histogram))
#     print()
#     print('Sampled frequency and error from observed frequency:')
#     header = '| word type | observed freq | sampled freq  |  error  |'
#     divider = '-' * len(header)
#     print(divider)
#     print(header)
#     print(divider)
#     # Colors for error
#     green = '\033[32m'
#     yellow = '\033[33m'
#     red = '\033[31m'
#     reset = '\033[m'
#     # Check each word in original histogram
#     for key, value in dictogram.dictionary_histogram.items():
#         # Calculate word's observed frequency
#         observed_freq = value / dictogram.tokens
#         # Calculate word's sampled frequency
#         samples = samples_hist.frequency(key)
#         sampled_freq = samples / samples_hist.tokens
#         # Calculate error between word's sampled and observed frequency
#         error = (sampled_freq - observed_freq) / observed_freq
#         color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
#         print('| {!r:<9} '.format(key)
#             + '| {:>4} = {:>6.2%} '.format(value, observed_freq)
#             + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
#             + '| {}{:>+7.2%}{} |'.format(color, error, reset))
#     print(divider)
#     print()

# print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])