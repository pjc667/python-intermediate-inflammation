#!/usr/bin/env python3
"""Software for managing and analysing patients inflammation data in our imaginary hospital."""

import argparse
import os

from inflammation import models, views
from inflammation.compute_data import analyse_data


def main(my_args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    In_Files = my_args.infiles
    if not isinstance(In_Files, list):
        In_Files = [my_args.infiles]

    if my_args.full_data_analysis:
        analyse_data(os.path.dirname(In_Files[0]))
        return

    for filename in In_Files:
        inflammation_data = models.load_csv(filename)

        view_data = {
            "average": models.daily_mean(inflammation_data),
            "max": models.daily_max(inflammation_data),
            "min": models.daily_min(inflammation_data),
        }

        views.visualize(view_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A basic patient inflammation data management system"
    )

    parser.add_argument(
        "infiles",
        nargs="+",
        help="Input CSV(s) containing inflammation series for each patient",
    )

    parser.add_argument(
        "--full-data-analysis", action="store_true", dest="full_data_analysis"
    )

    args = parser.parse_args()

    main(args)
