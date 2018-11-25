from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

def create_widgets_in_budget_frame():

    def calculatebudget():

        class Application():
            def __init__(self):
                self.income = 0
                self.expenses = 0
                self.expense_list = []
                self.expense_name = []
                self.income_name = []
                self.income_list = []
                self.prompt_income()

            def income_ask(self):
                add_income = tkinter.messagebox.askquestion('Message', 'Would you like to add an income?')
                return add_income

            def income_sum(self):
                self.income = sum(self.income_list)

            def expense_ask(self):
                add_expense = tkinter.messagebox.askquestion('Message', 'Would you like to add an expense?')
                return add_expense

            def expense_sum(self):
                self.expenses = sum(self.expense_list)

            def income_check(self):
                if not self.income_list:
                    tkinter.messagebox.showinfo('Message', 'Please enter atleast one source of income')
                    self.prompt_income()
                else:
                    return

            def expense_check(self):
                if not self.expense_list:
                    tkinter.messagebox.showinfo('Message', 'Please enter atleast one expense')
                    self.prompt_expense()
                else:
                    return

            def prompt_income(self):
                x = False
                while not x:
                    result = self.income_ask()
                    if result == 'yes':
                        income_input = tkinter.simpledialog.askinteger('Message', 'Enter Income')
                        self.income_list.append(income_input)
                        income_name = tkinter.simpledialog.askstring('Message', 'Enter Income name')
                        self.income_name.append(income_name)
                    else:
                        self.income_check()
                        x = True
                self.income_sum()
                name = [name for name in self.income_name]
                income = [income for income in self.income_list]
                incomedict = dict(zip(name, income))
                message = ''
                for k in incomedict:
                    message = message + str(k + ': ' + '$' + str(incomedict[k])) + '\n'
                message = message + 'Total user income: $' + (str(self.income))
                tkinter.messagebox.showinfo('Message', message)
                self.prompt_expense()

            def prompt_expense(self):
                x = False
                while not x:
                    result = self.expense_ask()
                    if result == 'yes':
                        expense_input = tkinter.simpledialog.askinteger('Message', 'Enter Expense')
                        self.expense_list.append(expense_input)
                        expense_name = tkinter.simpledialog.askstring('Message', 'Enter Expense name')
                        self.expense_name.append(expense_name)
                    else:
                        self.expense_check()
                        x = True
                self.expense_sum()
                name = [name for name in self.expense_name]
                expense = [income for income in self.expense_list]
                expensedict = dict(zip(name, expense))
                message = ''
                for k in expensedict:
                    message = message + str(k + ': ' + '$' + str(expensedict[k]))
                message = message + 'Total user expenses: $' + (str(self.expenses))
                tkinter.messagebox.showinfo('Message', message)
                self.uservalue()

            def uservalue(self):
                valoutput = self.income - self.expenses
                if valoutput < 0:
                    message = ('You are in the negative, you have a deficit of ' + '$' + str(valoutput))
                    tkinter.messagebox.showinfo('Message', message)
                if valoutput == 0:
                    message = 'You have broken even, you are spending exactly as much as you make.'
                    tkinter.messagebox.showinfo('Message', message)
                if valoutput > 0:
                    message = ('You are in the positive, you have a surplus of ' + '$' + str(valoutput))
                    tkinter.messagebox.showinfo('Message', message)
                another = tkinter.messagebox.askquestion('Message', 'Would you like to run another analysis?')
                if another == 'yes':
                    self.reset_program()
                else:
                    self.close_program()

            def reset_program(self):
                self.income = 0
                self.expenses = 0
                del self.expense_list[0:]
                del self.expense_name[0:]
                del self.income_name[0:]
                del self.income_list[0:]
                self.prompt_income()

            def close_program(self):
                root.destroy()

        if __name__ == '__main__':
            Application()

    #incomesource_label = Label(budget_frame, text = 'Income Source').grid(row = 0, column = 0, padx = 10, pady = 10)
    #income_label = Label(budget_frame, text = 'Income').grid(row = 1, column = 0, padx = 10, pady = 10)
    #expensename_label = Label(budget_frame, text = 'Expense Name').grid(row = 3, column = 0, padx = 10, pady = 10)
    #expense_label = Label(budget_frame, text = 'Expense').grid(row = 4, column = 0, padx = 10, pady = 10)

    incomesource_entry = Entry(budget_frame)
    income_entry = Entry(budget_frame)
    expensename_entry = Entry(budget_frame)
    expense_entry = Entry(budget_frame)

    #incomesource_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
    #income_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
    #expensename_entry.grid(row = 3, column = 1, padx = 10, pady = 10)
    #expense_entry.grid(row = 4, column = 1, padx = 10, pady = 10)

    calculate_button = Button(budget_frame, text = 'Start', command = calculatebudget).grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10)

root=Tk()
budget_frame = Frame(root, width = 500, height = 500)
budget_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

create_widgets_in_budget_frame()

root.mainloop()