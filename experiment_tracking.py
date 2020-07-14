import gspread
import sys


class ExperimentTracker():
    def __init__(self, client_secret: str, spreadsheet: str,
                 worksheet: str):
        self.gc = gspread.service_account(client_secret)
        self.spreadsheet = spreadsheet
        self.worksheet = worksheet

    def get_params(self):
        return self.experiment_params

    def record_experiment(self, param_lst):
        sheet = self.gc.open(self.spreadsheet).worksheet(self.worksheet)
        sheet.append_row(param_lst)


