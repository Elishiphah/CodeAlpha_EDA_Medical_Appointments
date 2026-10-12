import pandas as pd
import matplotlib.pyplot as plt

# Load the medical appointments dataset
df = pd.read_csv("KaggleV2-May-2016.csv")


# 1. Get an overview of the dataset

print("\n--- Dataset Overview ---")

# Display the first five records
print("\nFirst five records:")
print(df.head())

# Check the number of rows and columns
print("\nDataset size:")
print("Rows and columns:", df.shape)

# Display the column names
print("\nColumn names:")
print(df.columns.tolist())


# 2. Check the quality of the data

print("\n--- Data Quality Checks ---")

# Check for missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Check for completely duplicated rows
print("\nDuplicate rows:")
print(df.duplicated().sum())


# 3. Explore patient ages

print("\n--- Patient Age Analysis ---")

# Get basic statistics about patient ages
print("\nAge statistics:")
print(df["Age"].describe())

# Find records with negative ages
negative_ages = df[df["Age"] < 0]

print("\nNumber of records with negative ages:")
print(len(negative_ages))

# Display the records with negative ages
print("\nRecords with negative ages:")
print(negative_ages.to_string(index=True))

# Find records where the recorded age is above 100
older_patients = df[df["Age"] > 100]

print("\nNumber of patients aged over 100:")
print(len(older_patients))

# Display their ages
print("\nAges above 100:")
print(older_patients["Age"].to_list())


# 4. Summarize the initial findings

print("\n--- Initial Findings ---")

print("Total number of records:", len(df))
print("Records with negative ages:", len(negative_ages))
print("Records with ages above 100:", len(older_patients))

# Negative ages are invalid and need further investigation.
# Ages above 100 should be checked before deciding what to do.
# No records have been changed or deleted.

# Check how many patients attended or missed their appointments
print("\n--- Appointment Attendance ---")
print(df["No-show"].value_counts())

# Calculate the percentage of attended and missed appointments

print("\n--- Appointment Attendance Percentages ---")

attendance_percentage = df["No-show"].value_counts(normalize=True) * 100

print(attendance_percentage.round(2))


# Compare appointment attendance by gender

print("\n--- Appointment Attendance by Gender ---")

# Count appointments by gender and attendance status
gender_attendance = pd.crosstab(df["Gender"], df["No-show"])

print("\nAppointment counts by gender:")
print(gender_attendance)

# Calculate the percentage of appointments missed by gender
gender_percentage = pd.crosstab(
    df["Gender"],
    df["No-show"],
    normalize="index"
) * 100

print("\nAppointment percentages by gender:")
print(gender_percentage.round(2))

# Gender analysis findings:
# Female missed appointment rate: 20.31%
# Male missed appointment rate: 19.97%
# The difference between the rates is small.
# Further analysis is needed to investigate other factors.

# Group patients by age

print("\n--- Appointment Attendance by Age Group ---")

# Define age group boundaries and labels
age_bins = [0, 17, 35, 55, 75, float("inf")]
age_labels = [
    "0-17",
    "18-35",
    "36-55",
    "56-75",
    "76+"
]

# Create a new age group column
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels,
    include_lowest=True
)

# Count appointments in each age group
print("\nNumber of appointments by age group:")
print(df["AgeGroup"].value_counts().sort_index())


# Calculate appointment attendance by age group

print("\n--- Attendance by Age Group ---")

# Count attended and missed appointments in each age group
age_attendance = pd.crosstab(
    df["AgeGroup"],
    df["No-show"]
)

print("\nAppointment counts by age group:")
print(age_attendance)

# Calculate attendance percentages within each age group
age_percentages = pd.crosstab(
    df["AgeGroup"],
    df["No-show"],
    normalize="index"
) * 100

print("\nAppointment percentages by age group:")
print(age_percentages.round(2))

# Age-group analysis findings:
# Ages 18-35 have the highest missed appointment rate (23.82%).
# Ages 56-75 have the lowest missed appointment rate (15.53%).
# Missed appointment rates vary across age groups.
# These findings show associations, not causes.

# Visualize missed appointment rates by age group

print("\nCreating age-group attendance chart...")

# Get the missed appointment percentages
missed_rates = age_percentages["Yes"]

# Create the bar chart
plt.bar(missed_rates.index.astype(str), missed_rates.values)

# Add a title and axis labels
plt.title("Missed Appointment Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Missed Appointments (%)")

# Display the chart neatly
plt.tight_layout()

# Save the chart as an image
plt.savefig("missed_appointments_by_age.png")

# Display the chart
plt.show()


# Analyze appointment attendance by SMS reminders

print("\n--- Appointment Attendance by SMS Reminder ---")

# Count attended and missed appointments by SMS status
sms_attendance = pd.crosstab(
    df["SMS_received"],
    df["No-show"]
)

print("\nAppointment counts by SMS status:")
print(sms_attendance)

# Calculate percentages for each SMS group
sms_percentages = pd.crosstab(
    df["SMS_received"],
    df["No-show"],
    normalize="index"
) * 100

print("\nAppointment percentages by SMS status:")
print(sms_percentages.round(2))

# SMS analysis findings:
# Patients who received SMS reminders had a higher missed appointment rate.
# The rate was 27.57% for patients who received SMS and 16.70% for those who did not.
# This is an association, not proof that SMS reminders caused missed appointments.

# Visualize missed appointment rates by SMS reminder
print("\nCreating SMS reminder chart...")

sms_missed_rates = sms_percentages["Yes"]

plt.bar(
    ["No SMS", "Received SMS"],
    sms_missed_rates.values
)

plt.title("Missed Appointment Rate by SMS Reminder")
plt.xlabel("SMS Reminder Status")
plt.ylabel("Missed Appointments (%)")

plt.tight_layout()
plt.savefig("missed_appointments_by_sms.png")
plt.show()


# Calculate how many days patients wait for their appointments
print("\n--- Appointment Waiting Time Analysis ---")

# Convert appointment dates to datetime format
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"])
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"])

# Calculate the waiting time in days
df["WaitingDays"] = (
    df["AppointmentDay"].dt.normalize()
    - df["ScheduledDay"].dt.normalize()
).dt.days

# Display basic waiting-time statistics
print("\nWaiting-time statistics:")
print(df["WaitingDays"].describe())

# Check for appointments scheduled before the appointment date
negative_waiting = df[df["WaitingDays"] < 0]

print("\nRecords with negative waiting time:")
print(len(negative_waiting))

# Inspect records with negative waiting times
print("\n--- Investigating Negative Waiting Times ---")

print(
    negative_waiting[
        ["PatientId", "AppointmentID", "ScheduledDay",
         "AppointmentDay", "WaitingDays", "No-show"]
    ].to_string(index=False)
)

# Negative waiting-time findings:
# Five records have negative waiting times.
# Four records have a waiting time of -1 day.
# One record has a waiting time of -6 days.
# All five records are marked as missed appointments.
# These records are retained for investigation; none have been deleted.

# Group appointments by waiting time
print("\n--- Missed Appointments by Waiting Time ---")

# Use only non-negative waiting times for this comparison
valid_waiting = df[df["WaitingDays"] >= 0].copy()

# Create waiting-time categories
waiting_bins = [-1, 0, 7, 30, 90, float("inf")]
waiting_labels = [
    "Same day",
    "1-7 days",
    "8-30 days",
    "31-90 days",
    "Over 90 days"
]

valid_waiting["WaitingGroup"] = pd.cut(
    valid_waiting["WaitingDays"],
    bins=waiting_bins,
    labels=waiting_labels
)

# Count appointments in each waiting-time category
print("\nAppointments by waiting-time group:")
print(valid_waiting["WaitingGroup"].value_counts().sort_index())

# Calculate missed appointment rates for each waiting-time group
print("\n--- Missed Appointment Rates by Waiting Time ---")

waiting_attendance = pd.crosstab(
    valid_waiting["WaitingGroup"],
    valid_waiting["No-show"]
)

print("\nAppointment counts by waiting-time group:")
print(waiting_attendance)

waiting_percentages = pd.crosstab(
    valid_waiting["WaitingGroup"],
    valid_waiting["No-show"],
    normalize="index"
) * 100

print("\nAppointment percentages by waiting-time group:")
print(waiting_percentages.round(2))

# Waiting-time analysis findings:
# Same-day appointments had the lowest missed appointment rate (4.65%).
# The rate increased to 33.16% for appointments with 31-90 day waits.
# Appointments waiting over 90 days had a missed rate of 25.81%.
# This last group contained only 217 appointments.
# The results show an association, not proof of cause and effect.

# Visualize missed appointment rates by waiting time
print("\nCreating waiting-time chart...")

waiting_missed_rates = waiting_percentages["Yes"]

plt.bar(
    waiting_missed_rates.index.astype(str),
    waiting_missed_rates.values
)

plt.title("Missed Appointment Rate by Waiting Time")
plt.xlabel("Waiting Time")
plt.ylabel("Missed Appointments (%)")

plt.tight_layout()
plt.savefig("missed_appointments_by_waiting_time.png")
plt.show()

# Final Summary of Findings
print("\n" + "=" * 45)
print("FINAL SUMMARY OF FINDINGS")
print("=" * 45)

print("\n1. Dataset Overview")
print(f"Total appointments analyzed: {len(df):,}")
print(f"Number of columns in original dataset: 14")

print("\n2. Data Quality")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Records with negative ages: {len(negative_ages)}")
print(f"Records with ages above 100: {len(older_patients)}")
print(f"Records with negative waiting times: {len(negative_waiting)}")

print("\n3. Appointment Attendance")
print(f"Appointments attended: {(df['No-show'] == 'No').sum():,}")
print(f"Appointments missed: {(df['No-show'] == 'Yes').sum():,}")

print("\n4. Main Findings")
print("Age group 18-35 had the highest missed appointment rate: 23.82%.")
print("Patients who received SMS had a missed appointment rate of 27.57%.")
print("Same-day appointments had the lowest missed appointment rate: 4.65%.")
print("The 31-90 day waiting group had the highest missed appointment rate: 33.16%.")

print("\n5. Important Note")
print("These findings show associations, not proof of cause and effect.")
print("Unusual records were investigated without deleting the original data.")

print("\nCharts saved:")
print("- missed_appointments_by_age.png")
print("- missed_appointments_by_sms.png")
print("- missed_appointments_by_waiting_time.png")





