import csv

# Define the path of the input CSV file
csvpath = "c:/Users/jdilport/OneDrive - Prolink Staffing/Desktop/homework/dataviz-jdilport/Module_3_Python Challenge/PyBank/analysis/budget_data.csv"

# Define the path of the output text file
txtpath = "c:/Users/jdilport/OneDrive - Prolink Staffing/Desktop/homework/dataviz-jdilport/Module_3_Python Challenge/PyBank/analysis/budget_analysis.txt"

# Variables
total_months = 0
net_total_amount = 0
previous_profit_loss = 0
total_profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

# Open the CSV file and read the data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        
        # Update the total number of months
        total_months += 1
        
        # Calculate the net total amount of "Profit/Losses"
        current_profit_loss = int(row[1])
        net_total_amount += current_profit_loss
        
        # Calculate the change in "Profit/Losses"
        if total_months > 1:
            profit_loss_change = current_profit_loss - previous_profit_loss
            total_profit_loss_change += profit_loss_change
            
            # Check if the current change is the greatest increase or decrease
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change
        
        # Update the previous "Profit/Losses"
        previous_profit_loss = current_profit_loss

# Calculate the average change in "Profit/Losses"
average_profit_loss_change = round(total_profit_loss_change / (total_months - 1), 2)

# Generate the analysis report
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total_amount}\n"
    f"Average Change: ${average_profit_loss_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the analysis report to the terminal
print(analysis)

# Export the analysis report to a text file
with open(txtpath, "w") as txtfile:
    txtfile.write(analysis)
