import csv
import random
import yaml
from datetime import datetime

import itertools


class BillGenerator:
    def __init__(self, max_number, bill_slots, min_disjoint_slots, iterations=1000000):
        self._max_number = max_number
        self._bill_slots = bill_slots
        self._min_disjoint_slots = min_disjoint_slots
        self._iterations = iterations
        self._bills = []
        self._mapped_bills = []
        random.seed(datetime.now())

    def generate(self):
        i = 0
        while i < self._iterations:
            current_bill = self._generate_single_bill()
            if self._check_bill(current_bill):
                print('Bill {} generated on iteration {}'.format(len(self._bills), i))
                self._bills.append(current_bill)
                i = 0
            else:
                i += 1

        print('Iterations finished; generated {} bills'.format(len(self._bills)))
        print self._bills
        return self

    def map_symbols(self, yaml_file):
        with open(yaml_file, 'r') as stream:
            try:
                mappings = yaml.load(stream)
                print mappings
                for bill in self._bills:
                    mapped_bill = []
                    for number in bill:
                        mapped_bill.append(mappings[number])
                    self._mapped_bills.append(mapped_bill)
            except yaml.YAMLError as e:
                print('Error opening yaml file')

        print self._mapped_bills
        return self

    def to_csv(self, output_file, columns):
        with open(output_file, 'wb') as output_csv:
            wr = csv.writer(output_csv, quoting=csv.QUOTE_ALL)
            for bill in self._mapped_bills:
                grouped_bill = self._grouper(columns, bill, '')
                for row in grouped_bill:
                    wr.writerow(row)
                wr.writerow([])

    def _generate_single_bill(self):
        # To generate rows and columns proper distribution:
        # >>> N = 100
        # >>> K = 30 # K zeros, N-K ones
        # >>> arr = np.array([0] * K + [1] * (N-K))
        # >>> np.random.shuffle(arr) --> this is for the mask with 0s and 1s
        # Then use np.multiply by a matrix with random scaled values
        return random.sample(range(1, self._max_number), self._bill_slots)

    def _check_bill(self, bill_to_check):
        for bill in self._bills:
            overlap = len(set(bill) & set(bill_to_check))
            if self._bill_slots - overlap < self._min_disjoint_slots:
                return False

        return True

    def _grouper(self, n, iterable, fillvalue=None):
        "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return itertools.izip_longest(fillvalue=fillvalue, *args)
