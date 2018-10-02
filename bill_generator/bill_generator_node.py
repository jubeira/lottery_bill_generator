#!/usr/bin/env python

import argparse
import os

from bill_generator import BillGenerator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--max-number',
        dest='max_number',
        type=int,
        default=90,
        help='Max number allowed in bills (min is always 1).')
    parser.add_argument(
        '--bill-slots',
        dest='bill_slots',
        type=int,
        default=15,
        help='Number of slots required to win a game.')
    parser.add_argument(
        '--min-disjoint-slots',
        dest='min_disjoint_slots',
        type=int,
        default=10,
        help='Minimum amount of unique slots per bill.')
    parser.add_argument(
        '--input-mappings',
        dest='input_mappings',
        type=str,
        default='../data/mappings.yaml',
        help='Input mappings.')
    parser.add_argument(
        '--output-file',
        dest='output_file',
        type=str,
        default='../output/bills.csv',
        help='Output CSV file.')
    parser.add_argument(
        '--columns',
        dest='bill_columns',
        type=int,
        default=4,
        help='Columns in each bill')

    script_path = os.path.dirname(os.path.realpath(__file__))
    args = parser.parse_args()
    bill_gen = BillGenerator(args.max_number, args.bill_slots, args.min_disjoint_slots)
    bill_gen.generate()
    bill_gen.map_symbols(os.path.join(script_path, args.input_mappings))
    bill_gen.to_csv(os.path.join(script_path, args.output_file), args.bill_columns)
